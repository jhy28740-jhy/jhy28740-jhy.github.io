"""Numerical diagnostic for the orbit-aligned polarization bridge.

This file is deliberately non-certifying.  It generates finite isotropic atomic
measures from Stiefel matrices, maximizes the cross-energy over O(3), and
reports 2 D_orb - Q(nu - R# mu_*).  A negative value is only a numerical
candidate until the rotation optimum and all arithmetic are certified.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize
from scipy.spatial.transform import Rotation


C_STAR = (9.0 + math.sqrt(5.0) + 2.0 * math.sqrt(35.0)) / 18.0


def polar_retract(a: np.ndarray) -> np.ndarray:
    u, _, vt = np.linalg.svd(a, full_matrices=False)
    return u @ vt


def candidate() -> tuple[np.ndarray, np.ndarray]:
    alpha = (91.0 - 25.0 * math.sqrt(7.0)) / 126.0
    beta = (1.0 - alpha) / 5.0
    m = np.array([[alpha, math.sqrt(5.0 * alpha * beta)],
                  [math.sqrt(5.0 * alpha * beta), 3.0 * beta]])
    values, vectors = np.linalg.eigh(m)
    uv = vectors[:, -1]
    if np.any(uv < 0):
        uv = -uv
    u, v = uv
    angles = 2.0 * math.pi * np.arange(5) / 5.0
    x = np.zeros((6, 3))
    x[0] = [u / math.sqrt(alpha), 0.0, 0.0]
    x[1:, 0] = v / math.sqrt(5.0 * beta)
    x[1:, 1] = math.sqrt(2.0 / (5.0 * beta)) * np.cos(angles)
    x[1:, 2] = math.sqrt(2.0 / (5.0 * beta)) * np.sin(angles)
    return x, np.array([alpha] + [beta] * 5)


def from_q(q: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    gram = q @ q.T
    h = np.maximum(gram, 0.0)
    values, vectors = np.linalg.eigh(h)
    s = vectors[:, -1]
    if np.sum(s) < 0:
        s = -s
    s = np.abs(s)
    s /= np.linalg.norm(s)
    weights = s * s
    keep = weights > 1e-10
    return q[keep] / s[keep, None], weights[keep]


def energy(x: np.ndarray, w: np.ndarray, y: np.ndarray, v: np.ndarray,
           r: np.ndarray | None = None) -> float:
    if r is not None:
        y = y @ r.T
    return float(np.sum(w[:, None] * v[None, :] * np.maximum(x @ y.T, 0.0)))


def so3_matrix(z: np.ndarray) -> np.ndarray:
    return Rotation.from_rotvec(z).as_matrix()


@dataclass
class OrbitFit:
    value: float
    matrix: np.ndarray


def maximize_orbit(x: np.ndarray, w: np.ndarray, y: np.ndarray,
                   v: np.ndarray, starts: int, rng: np.random.Generator) -> OrbitFit:
    best = OrbitFit(-math.inf, np.eye(3))
    reflections = (np.eye(3), np.diag([-1.0, 1.0, 1.0]))
    initial = [np.zeros(3)] + [rng.normal(scale=1.0, size=3) for _ in range(starts)]
    for reflection in reflections:
        for z0 in initial:
            def objective(z: np.ndarray) -> float:
                r = reflection @ so3_matrix(z)
                return -energy(x, w, y, v, r)
            result = minimize(objective, z0, method="BFGS",
                              options={"gtol": 1e-10, "maxiter": 500})
            r = reflection @ so3_matrix(result.x)
            value = -float(result.fun)
            if value > best.value:
                best = OrbitFit(value, r)
    return best


def bridge_sample(x: np.ndarray, w: np.ndarray, y: np.ndarray, v: np.ndarray,
                  starts: int, rng: np.random.Generator) -> tuple[float, float, float, OrbitFit]:
    fit = maximize_orbit(x, w, y, v, starts, rng)
    self_energy = energy(x, w, x, w)
    cross = fit.value
    qdiff = self_energy + C_STAR - 2.0 * cross
    return self_energy, C_STAR - cross, 2.0 * (C_STAR - cross) - qdiff, fit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=100)
    parser.add_argument("--starts", type=int, default=12)
    parser.add_argument("--atoms", type=int, default=6)
    parser.add_argument("--scale", type=float, default=0.08)
    parser.add_argument("--seed", type=int, default=20260907)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    y, v = candidate()
    q_star = np.sqrt(v)[:, None] * y
    measures: list[tuple[str, np.ndarray, np.ndarray]] = [("candidate", y, v)]
    for index in range(args.samples):
        if index < args.samples // 2 and args.atoms == 6:
            q = polar_retract(q_star + args.scale * rng.normal(size=q_star.shape))
            x, w = from_q(q)
            measures.append(("near", x, w))
        else:
            q = polar_retract(rng.normal(size=(args.atoms, 3)))
            x, w = from_q(q)
            measures.append(("random", x, w))

    axis_atoms = math.sqrt(3.0) * np.vstack((np.eye(3), -np.eye(3)))
    measures.append(("axes", axis_atoms, np.full(6, 1.0 / 6.0)))
    for _ in range(max(2, args.samples // 10)):
        r = Rotation.random(random_state=rng).as_matrix()
        t = rng.uniform(0.05, 0.95)
        mixture_atoms = np.vstack((y, y @ r.T))
        mixture_weights = np.concatenate((t * v, (1.0 - t) * v))
        measures.append(("mix-orbit", mixture_atoms, mixture_weights))

    worst = (math.inf, None)
    max_identity_residual = 0.0
    for label, x, w in measures:
        self_energy, d_orb, gap, fit = bridge_sample(x, w, y, v, args.starts, rng)
        identity_residual = abs(gap - (C_STAR - self_energy))
        max_identity_residual = max(max_identity_residual, identity_residual)
        print(f"{label:9s} support={len(w):2d} self={self_energy:.12f} "
              f"Dorb={d_orb:.3e} bridge_gap={gap:+.3e} "
              f"identity_res={identity_residual:.1e} "
              f"rot_det={np.linalg.det(fit.matrix):+.0f}")
        if gap < worst[0]:
            worst = (gap, (label, self_energy, d_orb, fit.value, len(w)))
    print("worst numerical bridge gap:", worst)
    print(f"maximum polarization-identity residual = {max_identity_residual:.3e}")
    print("WARNING: local optimizer output is not a proof or a global rotation certificate.")


if __name__ == "__main__":
    main()
