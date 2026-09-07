# 图的前三大邻接特征值和

这是《图的前三大邻接特征值和的变分结构及谱极值》的公开发布目录。

| 文件 | 用途 |
| --- | --- |
| [thesis.pdf](./thesis.pdf) | 最新增强版论文 PDF |
| [论文思维导图.md](./论文思维导图.md) | GitHub 可直接渲染的 Mermaid 思维导图源码 |
| [mindmap.html](./mindmap.html) | 可在浏览器打开的思维导图网页 |
| [thesis-source.zip](./thesis-source.zip) | LaTeX 正文、参考文献、图表与计算脚本 |
| [kkt_audit_results.txt](./kkt_audit_results.txt) | 统一证书残余十三类的固定种子 KKT 审计摘要（其中 `3dfe` 已另有专用证书） |
| [remaining_stationary_search.txt](./remaining_stationary_search.txt) | 十二个未决模板的光滑内点 KKT 轨道侦察（非完备性证明） |
| [six_block_boundary_dual_collar_certificates.json](./six_block_boundary_dual_collar_certificates.json) | 68 个模板--坐标宽边界领的直接 shifted-dual 有理证书 |
| [six_block_exception_boundary_collar_certificates.json](./six_block_exception_boundary_collar_certificates.json) | 四个原例外面：20 份 1/60 辅助领与 4 份总正谱证书 |
| [orbit_bridge_review.md](./orbit_bridge_review.md) | 轨道桥接等价、谱椭球、二次重构与 40 块条件分支的独立审查记录 |
| [orbit_bridge_diagnostic_20260907.txt](./orbit_bridge_diagnostic_20260907.txt) | 固定样本数值诊断输出，仅作恒等式实现核对 |
| [diagnose_orbit_bridge.py](./diagnose_orbit_bridge.py) | 上述诊断的可复现脚本 |
| [毕业论文下一阶段规划.md](./毕业论文下一阶段规划.md) | 退化分支、谱椭球/40 块二分与十二模板 KKT 的后续路线 |
| [文本原创性与AI风格自检报告.md](./文本原创性与AI风格自检报告.md) | 本地表层重合与模板化表达自检，不等同于正式检测率 |

## 更新约定

论文后续修改时，保持 `thesis.pdf`、`论文思维导图.md` 和 `mindmap.html` 的文件名不变，网页地址就不会变化。每次更新应同步提交 PDF、源文件压缩包和版本日期，并在 Git 提交信息中注明修改内容。

当前版本：2026-09-07，共 137 页（新增至多 $48$ 原子的全局达到性与单个紧
Stiefel--Perron 问题约化、光滑不可约有限驻点的矩阵 KKT 方程、至多四原子的精确
上界与等号刻画、全部五原子的粗统一上界 $(4+\sqrt6)/5$、正惯性筛选和
精确最大值 $c_4=(9+4\sqrt6)/15$ 的完整有理分类、任意全局极值分布的自支撑椭球和二阶必要条件，以及候组六原子
zonotope 的严格区间椭球证书。候选交叉能量的等号分布唯一，并具有平方耦合距离
$O(\!\sqrt D)$ 的定量近等号刚性；第五章 Hessian 闭式另有精确符号证书；
候选六条接触正射线上的全部各向同性分布已得到类内自能量上界、唯一等号和
定量耦合稳定性；候选六原子投影在完整九维 Grassmann 图表中的非退化严格局部
极大性已有有向舍入区间证书；一般粗上界严格不可达，并给出高能量对象的重心定位；
新增自能量缺口的精确极化恒等式，并用显式六点轴向各向同性分布排除“全局条件
负性”这一直接捷径；新增真孪生合并引理及剩余模板的孪生对精确核验，明确
假孪生不能直接降为五分块；
新增一般六模板的 Ky Fan 内点 KKT 必要条件（活动最大化矩阵集合覆盖第三特征值重根），
并严格说明十三个统一证书残余模板的边界值均退化到至多五块、从而不超过 $c_4$；
再以秩一交错、Perron 根质量转移和精确三角 Bernstein 正性证书证明
`3dfe` 在全部六维权重上严格小于 $32/25<c_*$。固定种子 KKT 审计结果仅作为
其余模板后续区间覆盖的数值线索；对实际未解十二模板的 $72$ 个模板--坐标边界
领，统一箭头扰动论证先严格给出 $d_k\leq1/1300$ 的排除，再由 68 份逐面有理
shifted-dual 证书和四个例外面的二分证书完整加强为全部
$d_k\leq1/100$。四个例外面 `(03be,4), (07de,3), (07fe,3), (0fdf,1)` 删除对应
坐标后均诱导五阶模板 `07e=I+A(K_{2,3})`；当另一坐标不超过 $1/60$ 时使用
20 份辅助证书，否则用第四正特征值扣除总正谱证书。这不是对十二个模板内点的
全局排除；
第五章进一步证明：只要任意支撑数的各向同性分布能够按候选 clique-$C_5$ 正负
内积关系分成六类，就能得到匹配上界、正交意义下的唯一等号和定量 cut 稳定性；
全局自能量匹配上界与自能量等号唯一性仍为猜想。五原子的粗统一矩估计仍高于
$c_*$，但后续逐模板有理对偶分类已把五阶问题精确闭合在 $c_4<c_*$；这仍不能
闭合六原子以上或全局问题。前两项核心猜想若成立，定性 cut 稳定性由 graphon
紧致性推出；显式速率仍未解决。

本轮进一步证明：极值 graphon 的前三个特征函数坐标满足精确谱椭球等式；正内积
胞腔内存在二次重构，从而同一正射线上至多有一个支撑半径。若相应二次固定点
系统是零维的，Bézout 计数给出每个胞腔至多七个非零复解；连续支撑只能来自
尚未分类的正维退化分支。另有严格条件二分：自支撑矩阵等于谱矩阵时，谱矩阵
给出全局交叉支撑证书；二者不同时，该分支存在至多 40 块的极大 graphon。
这不是无条件 40 原子约化。轨道桥接余量已被证明恰等于自能量缺口，因此轨道
桥接不等式与全局匹配上界精确等价，不能视为较弱的中间命题。

正文的“开放问题 8.3”明确列出三个仍未闭合的全局层次：全体三维各向同性分布
的匹配上界、等号分布在正交变换下的唯一性，以及由近等号无条件推出六分块
cut 距离结构稳定性。现有定理只在候选六类符号模板内解决了这三层问题；尚未
证明任意极值或充分近极值分布都能作出这样的六类符号分拆。

## 证书哈希与剩余掩码

为使下载包与正文版本可核对，五份逐模板 JSON 证书的 SHA256 为：

| 文件 | SHA256 |
| --- | --- |
| `five_block_dual_certificates.json` | `8F3A93B0E3DA4A4A932ED05B0FCDCF11361DA413709418569F83572334E6E98C` |
| `six_block_low_inertia_dual_certificates.json` | `5EA61DEF3E9DBFE2FDB5773396C38113ECF6238994393B1AE5AE81F4A6575539` |
| `six_block_shifted_dual_certificates.json` | `2ED71CC3CF6147EA50AE1C26BF90086C62751F0BF9BAEC759BBC46F7044CA5E5` |
| `six_block_boundary_dual_collar_certificates.json` | `2D9577E2908974208FED54C2F35CEBC76B4BD940D5DAFB76B53FEEFC26BC873C` |
| `six_block_exception_boundary_collar_certificates.json` | `F8C75D4106E3A32CC6B460EBE2B17D054CEF937B369C2F1D40D7714178659400` |

六原子 156 类中，统一证书闭合 143 类，`3dfe` 的专用证书再闭合 1 类，合计
已有 144 类严格闭合。当前仍未排除的 12 个完整惯性 $(4,2,0)$ 掩码为
`03bc, 03bd, 03be, 06df, 077c, 077d, 07de, 07fe, 0fdf, 1bbc, 1bbd, 1bfe`。

本次发布的 `thesis.pdf`（137 页）SHA256 为
`1ECAA5806F3EEF720C557981AE2D9875B31798F0D240FF2606AB2B849B793814`。

本次发布的 `thesis-source.zip` SHA256 为
`6C060243748A4B1CAE256787E3904E0BEAAC54AED88E97FFE225F306DED5703E`。

文本原创性与 AI 风格自检报告已基于 137 页 PDF 重新生成；其结果仍只是本地表层
筛查，不等同于学校正式查重率或 AI 检测率。

本版新增十三个统一证书残余模板的补图边集与自同构轨道精确数据，并对 `3dfe`
给出秩一--三匹配分块和六变量 secular 方程；对应核验脚本已包含在源码包中。
进一步的 Perron--Bernstein 证书已在全测度单纯形上严格排除 `3dfe`，所以实际
未完成全局分类的六原子模板降为十二类。另新增
1bbc 等匹配对、三元测度对称切片的分段谱公式和严格低于 $c_4$ 的受限切片证书；
该证书同样不涉及一般 1bbc 权重或全局匹配上界。对 3dfe 还新增双平衡对--单
分裂对的全局 $c_4$ 上界，以及平方根不平衡量不超过 $1/2500$ 时的严格局部领
排除；这些受限结论是一般六维证书之前的中间结果，不应与最终全局排除相混淆。
本轮又增加统一 $1/1300$ 边界领、全部 $72/72$ 个逐面 $1/100$ 宽领证书和十二模板
光滑 KKT 驻点轨道侦察。所有数值驻点均出现正 Hessian 方向，但轨道枚举尚无
严格完备性，也未覆盖第三、第四特征值碰撞分支，因此正文仍把十二模板内点问题
和三个全局层次保留为开放问题。

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
