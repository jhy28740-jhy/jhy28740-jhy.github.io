# 图的前三大邻接特征值和

这是《图的前三大邻接特征值和的变分结构及谱极值》的公开发布目录。

| 文件 | 用途 |
| --- | --- |
| [thesis.pdf](./thesis.pdf) | 最新增强版论文 PDF |
| [论文思维导图.md](./论文思维导图.md) | GitHub 可直接渲染的 Mermaid 思维导图源码 |
| [mindmap.html](./mindmap.html) | 可在浏览器打开的思维导图网页 |
| [thesis-source.zip](./thesis-source.zip) | LaTeX 正文、参考文献、图表与计算脚本 |

## 更新约定

论文后续修改时，保持 `thesis.pdf`、`论文思维导图.md` 和 `mindmap.html` 的文件名不变，网页地址就不会变化。每次更新应同步提交 PDF、源文件压缩包和版本日期，并在 Git 提交信息中注明修改内容。

当前版本：2026-09-02（新增有限原子 Stiefel--Perron 约化、光滑不可约有限驻点
的矩阵 KKT 方程、至多四原子的精确
上界与等号刻画、任意全局极值分布的自支撑椭球和二阶必要条件，以及候组六原子
zonotope 的严格区间椭球证书。候选交叉能量的等号分布唯一，并具有平方耦合距离
$O(\!\sqrt D)$ 的定量近等号刚性；第五章 Hessian 闭式另有精确符号证书；
新增自能量缺口的精确极化恒等式，并用显式六点轴向各向同性分布排除“全局条件
负性”这一直接捷径；
全局自能量匹配上界与自能量等号唯一性仍为猜想。二者若成立，定性 cut 稳定性
由 graphon 紧致性推出；显式速率仍未解决。）

## 后续更新

1. 在论文工程中重新编译 `main.tex`，确认 `build/main.pdf` 为最新版本。
2. 将最新 PDF 覆盖为本目录的 `thesis.pdf`。
3. 重新打包 LaTeX 源码为 `thesis-source.zip`，并按需要更新本文件和思维导图。
4. 在 `jhy28740-jhy.github.io` 仓库中执行：

   ```powershell
   git add thesis-spectral-extremal
   git commit -m "Update spectral extremal thesis"
   git push origin main
   ```

固定地址不会改变：
`https://jhy28740-jhy.github.io/thesis-spectral-extremal/`
