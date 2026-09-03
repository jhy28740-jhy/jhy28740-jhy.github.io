# 图的前三大邻接特征值和

这是《图的前三大邻接特征值和的变分结构及谱极值》的公开发布目录。

| 文件 | 用途 |
| --- | --- |
| [thesis.pdf](./thesis.pdf) | 最新增强版论文 PDF |
| [论文思维导图.md](./论文思维导图.md) | GitHub 可直接渲染的 Mermaid 思维导图源码 |
| [mindmap.html](./mindmap.html) | 可在浏览器打开的思维导图网页 |
| [thesis-source.zip](./thesis-source.zip) | LaTeX 正文、参考文献、图表与计算脚本 |
| [kkt_audit_results.txt](./kkt_audit_results.txt) | 十三类剩余模板固定种子 KKT 审计摘要 |
| [文本原创性与AI风格自检报告.md](./文本原创性与AI风格自检报告.md) | 本地表层重合与模板化表达自检，不等同于正式检测率 |

## 更新约定

论文后续修改时，保持 `thesis.pdf`、`论文思维导图.md` 和 `mindmap.html` 的文件名不变，网页地址就不会变化。每次更新应同步提交 PDF、源文件压缩包和版本日期，并在 Git 提交信息中注明修改内容。

当前版本：2026-09-03，共 115 页（新增至多 $48$ 原子的全局达到性与单个紧
Stiefel--Perron 问题约化、光滑不可约有限驻点的矩阵 KKT 方程、至多四原子的精确
上界与等号刻画、全部五原子的统一上界 $(4+\sqrt6)/5$ 和正惯性筛选、
$K_1\vee C_4$ 五类模板的严格排除、任意全局极值分布的自支撑椭球和二阶必要条件，以及候组六原子
zonotope 的严格区间椭球证书。候选交叉能量的等号分布唯一，并具有平方耦合距离
$O(\!\sqrt D)$ 的定量近等号刚性；第五章 Hessian 闭式另有精确符号证书；
候选六条接触正射线上的全部各向同性分布已得到类内自能量上界、唯一等号和
定量耦合稳定性；候选六原子投影在完整九维 Grassmann 图表中的非退化严格局部
极大性已有有向舍入区间证书；一般粗上界严格不可达，并给出高能量对象的重心定位；
新增自能量缺口的精确极化恒等式，并用显式六点轴向各向同性分布排除“全局条件
负性”这一直接捷径；新增真孪生合并引理及剩余模板的孪生对精确核验，明确
假孪生不能直接降为五分块；
新增一般六模板的 Ky Fan 内点 KKT 必要条件（活动最大化矩阵集合覆盖第三特征值重根），
并严格说明十三个剩余模板的边界值均退化到至多五块、从而不超过 $c_4$；固定种子
KKT 审计结果仅作为后续区间覆盖的数值线索；
第五章进一步证明：只要任意支撑数的各向同性分布能够按候选 clique-$C_5$ 正负
内积关系分成六类，就能得到匹配上界、正交意义下的唯一等号和定量 cut 稳定性；
全局自能量匹配上界与自能量等号唯一性仍为猜想。五原子统一上界仍高于
$c_*$，因此不能据此宣称五阶问题或全局问题已闭合。前两项核心猜想若成立，定性 cut 稳定性
由 graphon 紧致性推出；显式速率仍未解决。）

正文的“开放问题 8.3”明确列出三个仍未闭合的全局层次：全体三维各向同性分布
的匹配上界、等号分布在正交变换下的唯一性，以及由近等号无条件推出六分块
cut 距离结构稳定性。现有定理只在候选六类符号模板内解决了这三层问题；尚未
证明任意极值或充分近极值分布都能作出这样的六类符号分拆。

## 证书哈希与剩余掩码

为使下载包与正文版本可核对，三份逐模板 JSON 证书的 SHA256 为：

| 文件 | SHA256 |
| --- | --- |
| `five_block_dual_certificates.json` | `8F3A93B0E3DA4A4A932ED05B0FCDCF11361DA413709418569F83572334E6E98C` |
| `six_block_low_inertia_dual_certificates.json` | `5EA61DEF3E9DBFE2FDB5773396C38113ECF6238994393B1AE5AE81F4A6575539` |
| `six_block_shifted_dual_certificates.json` | `2ED71CC3CF6147EA50AE1C26BF90086C62751F0BF9BAEC759BBC46F7044CA5E5` |

六原子 156 类中已有 143 类严格闭合；仍未排除的 13 个完整惯性 $(4,2,0)$ 掩码为
`03bc, 03bd, 03be, 06df, 077c, 077d, 07de, 07fe, 0fdf, 1bbc, 1bbd, 1bfe, 3dfe`。

本次发布的 `thesis.pdf`（115 页）SHA256 为
`D30A0A9D15E7B9A13894FCB1DEABA1A728A740A2177230ED327B2B6DFA55BB92`。

本次发布的 `thesis-source.zip` SHA256 为
`6076A6078F856AA81A4BEAA0B9B17CEA9D2E962A699B72EB5F12E9E00990B3E9`。

文本原创性与 AI 风格自检报告已基于 115 页 PDF 重新生成；其结果仍只是本地表层
筛查，不等同于学校正式查重率或 AI 检测率。

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
