# 轨道化桥接不等式独立审查记录

本记录只用于诊断，不是论文正文，也不把数值实验当作定理。

## 1. 精确化简

令

\[
D_{\mathrm{orb}}(\nu)=c_*-\mathcal B(\nu,R_{\nu\#}\mu_*),
\qquad
\eta=\nu-R_{\nu\#}\mu_*,
\]

其中 `R_nu` 是任一达到轨道交叉能量最大值的正交矩阵。由双线性展开以及
`B(R#mu_*,R#mu_*)=c_*`，有

\[
\begin{aligned}
2D_{\mathrm{orb}}(\nu)-\mathcal Q(\eta)
&=2c_*-2\mathcal B(\nu,R_{\nu\#}\mu_*)\\
&\quad-\bigl(\mathcal B(\nu,\nu)+c_*
       -2\mathcal B(\nu,R_{\nu\#}\mu_*)\bigr)\\
&=c_*-\mathcal B(\nu,\nu).
\end{aligned}
\]

所以

\[
\mathcal Q(\nu-R_{\nu\#}\mu_*)\leq2D_{\mathrm{orb}}(\nu)
\]

对全部各向同性分布成立，当且仅当全局匹配上界
`B(nu,nu) <= c_*` 成立。旋转最大化器的选择不影响桥接余量，也不能把该问题
化成一个比全局猜想更弱的问题。

同理，加强式

\[
\mathcal Q(\nu-R_{\nu\#}\mu_*)\leq(2-\kappa)D_{\mathrm{orb}}(\nu)
\]

精确等价于

\[
c_*-\mathcal B(\nu,\nu)\geq\kappa D_{\mathrm{orb}}(\nu).
\]

因此若要证明严格余量，真正需要的是自能量缺口与最优交叉亏损的局部可比性。

## 2. 已可严格得到的局部版本

第五章的 `thm:six-cell-sign-rigidity` 已证明：若各向同性分布具有候选
clique-C5 六类内积符号分拆，则

\[
\mathcal B(\nu,\nu)\leq c_*,
\]

且等号仅发生在候选正交轨道。其
`cor:candidate-support-neighborhood-rigidity` 进一步给出一个 `r_*>0`：只要
`supp(nu)` 落在某个旋转后的六个候选原子 `r_*` 邻域之并内，上述结论就成立，
而且不限制原子数并允许连续部分。

于是可严格陈述以下推论。

**候选支撑邻域内的轨道桥接与等号刚性。** 存在 `r_*>0`，使得对任意
`O in O(3)`，若三维各向同性分布 `nu` 满足

\[
\operatorname{supp}\nu\subseteq\bigcup_{i=0}^5B(Ox_i,r_*),
\]

则对任一轨道交叉能量最大化器 `R_nu`，

\[
\mathcal Q\bigl(\nu-(R_\nu)_\#\mu_*\bigr)
\leq2D_{\mathrm{orb}}(\nu).
\]

等号成立当且仅当 `nu=O'#mu_*` 对某个 `O' in O(3)` 成立。此外，若
`Delta=c_*-B(nu,nu)`，则该桥接不等式的余量精确等于 `Delta`，并且现有
六类符号定理已经给出

\[
\|d-d_*\|_2\leq\sqrt{\Delta/\gamma_6},
\qquad
\delta_\square(W_\nu,W_{d_*})
\leq\sqrt{6\Delta/\gamma_6}.
\]

**证明。** 支撑邻域推论保证六类内积符号条件，因此
`thm:six-cell-sign-rigidity` 给出自能量上界、等号分类及两个稳定性估计。
将第一节的精确恒等式代入即可得到桥接不等式；桥接取等恰好等价于
`B(nu,nu)=c_*`，故等号分类也直接继承。证毕。

这不是新的独立核心定理，而是现有严格结果与轨道极化恒等式的直接推论。

## 3. 六原子 Grassmann 局部版本

若只考虑六个带标签的正权原子，令

\[
Q_i=\sqrt{w_i}x_i^{\mathsf T},\qquad s_i=\sqrt{w_i}.
\]

各向同性条件给出 `Q^T Q=I_3`，且

\[
\mathcal B(\nu,\nu)
=s^{\mathsf T}[QQ^{\mathsf T}]_+s
\leq\lambda_{\max}([QQ^{\mathsf T}]_+).
\]

第四章的 `thm:candidate-grassmann-local-max` 证明右端在 `[Q_*]` 附近不超过
`c_*`，故也单独推出六原子近邻内的桥接不等式。若需要定量形式，负定 Hessian
和候选 Perron 谱隙还给出局部常数 `a,b>0`，使

\[
c_*-\mathcal B(\nu,\nu)
\geq a\,\operatorname{dist}_{\mathrm{Gr}}([Q],[Q_*])^2
 +b\,\|s-p(Q)\|_2^2,
\]

其中 `p(Q)` 是 `[QQ^T]_+` 的正单位 Perron 向量。证明分别使用局部 Hessian
二次下降和 Rayleigh 商相对于简单 Perron 特征向量的谱隙。此定量式若进入正文，
应另行把邻域、Grassmann 距离和统一谱隙常数写清楚；现稿无需依赖它。

## 4. 数值诊断

脚本 `computation/diagnose_orbit_bridge.py`：

- 从 Stiefel 矩阵构造严格各向同性有限原子分布；
- 在 `O(3)` 的两个行列式分支上多起点优化交叉能量；
- 测试候选附近、随机六原子、轴向六原子和两个旋转候选的混合；
- 同时核对桥接余量与 `c_*-B(nu,nu)` 的恒等式残差。

一次固定种子运行的最大恒等式残差为 `2.22e-16`，未观察到负桥接余量。这些结果
只是浮点诊断；局部旋转优化既不是全局证书，也不能证明全局猜想。

## 5. 建议插入位置

若正文需要显式串联逻辑，建议在第四章
`prop:orbit-aligned-cross-deficit` 之后只加入第一节的单行恒等式说明；再在第五章
`cor:candidate-support-neighborhood-rigidity` 后加入第二节的短推论。不要把它写成
“证明了全局桥接”，也不要声称数值搜索排除了反例。

## 6. 审查结论

现稿没有把桥接猜想误写成定理。真正尚未闭合的仍是候选六类符号结构之外的全局
自能量上界；轨道化本身不会缩小这一缺口。候选支撑邻域内的桥接、等号刚性与
cut 稳定性已经严格具备，只需要在叙述上把它们的推论关系写得更透明。
