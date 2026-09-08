# 图的前三大邻接特征值和：图极限方法与有限维约化

本目录发布毕业论文独立重写版。论文以图极限为主线，研究简单图邻接矩阵前三大特征值之和
\[
S_3(G)=\lambda_1(G)+\lambda_2(G)+\lambda_3(G).
\]

固定发布页：<https://jhy28740-jhy.github.io/thesis-spectral-extremal/>

## 下载

| 文件 | 内容 |
| --- | --- |
| [thesis.pdf](./thesis.pdf) | 最新论文 PDF，当前 52 页 |
| [thesis-source.zip](./thesis-source.zip) | 可编译的 LaTeX 源码 |
| [mindmap.html](./mindmap.html) | 七章结构思维导图 |
| [论文思维导图.md](./论文思维导图.md) | Mermaid 导图源码 |
| [毕业论文下一阶段规划.md](./毕业论文下一阶段规划.md) | 全局匹配上界的研究计划 |
| [文本原创性与AI风格自检报告.md](./文本原创性与AI风格自检报告.md) | 本地表层文本审计 |

## 当前严格结论

1. 证明有限图极值比值的极限存在，并等于 graphon 极值常数
   \(\mathfrak c_3\)。
2. 把全局问题等价改写为三维各向同性随机向量的正内积矩问题：
   \[
   \mathfrak c_3=\sup_{\mathbb E(XX^{\mathsf T})=I_3}
   \mathbb E(X^{\mathsf T}Y)_+.
   \]
3. 证明存在至多 48 步的全局极值 graphon，并得到极值元的符号条件、
   自支撑椭球、谱椭球等式、二阶必要条件和胞腔内二次重构。
4. 在固定 clique-\(C_5\) 六块模板中允许全部块测度变化，证明平衡测度是
   唯一全局最大点，并得到模板内二次稳定性。
5. 应用 Deregowska--Lewandowska 已证明的三维实投影常数定理，得到对所有
   \(n\) 阶简单图成立的上界
   \[
   S_3(G)\leq \frac{3+\sqrt5}{4}n-3.
   \]

因此当前无条件区间为
\[
\frac{9+\sqrt5+2\sqrt{35}}{18}
\leq \mathfrak c_3
\leq \frac{3+\sqrt5}{4}.
\]

## 结论边界

本文没有证明候选匹配等式
\[
\mathfrak c_3=\frac{9+\sqrt5+2\sqrt{35}}{18}.
\]
下列问题仍作为猜想或开放问题保留：

1. 全体三维各向同性分布上的匹配上界；
2. 全局等号分布在正交变换下的唯一性；
3. 任意全局极值 graphon 必须约化为候选六块模板；
4. 由近等号推出无条件 cut 距离稳定性。

固定六块模板内的唯一性不能外推为全体 graphon 的唯一性。数值搜索也不作为
驻点完备性或全局上界的证明。

## 来源与原创范围

- `2604.00512v1.pdf` 提供前两大特征值和问题的最新图极限证明框架；
- `Proof of a conjecture of V. Nikiforov.pdf` 提供图极限谱极值方法的理论基础；
- `Top Three Eigenvalues of graphs.pdf` 是作者已有的三特征值小论文；
- Deregowska--Lewandowska 的三维实投影常数精确值是外部定理，本文只给出其在
  图谱和问题中的推论。

正文将“外部定理”“本文推论”“固定模板内定理”和“全局猜想”分层标注。

## 版本约定

后续更新继续使用 `thesis.pdf`、`thesis-source.zip` 和 `mindmap.html` 这些固定
文件名，故发布页和下载链接保持不变。目录内旧版的 KKT、区间盒和轨道桥接证书
保留为历史研究记录，不属于当前 52 页论文的论证链。

当前版本日期：2026-09-08。

## 文件校验

```text
thesis.pdf         SHA256 22799AB2FBBD11E58C1FC245C70F53FDF1FB416CE0E23F868A4CB52D11505550
thesis-source.zip  SHA256 B10F42F7ED4C63F7C73B0B7CA8631DFE4567F1DB576C84C5FDC8640926935813
```
