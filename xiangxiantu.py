"""
绘制箱线图。
参考原图来自论文MicorScopiQ (ISCA 2025)的Figure 2.
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 20, 'font.family': 'Times New Roman'})  # 统一设置字体

# 模拟数据
models = ['OPT-6.7B', 'LLaMA2-13B', 'LLaMA2-7B', 'MPT-7B', 'VILA-7B']
n_models = len(models)
n_samples = 10

np.random.seed(42)
outliers = [np.random.uniform(1, 5, n_samples) for _ in range(n_models)]
adj_outliers = [np.random.uniform(0.0, 2.5, n_samples) for _ in range(n_models)]

# 箱线图的位置
x = np.arange(n_models)
width = 0.3

fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

# 绘制箱线图（左轴：Outliers）
bp1 = ax1.boxplot(outliers, positions=x - width/2-0.05, widths=width,
                  patch_artist=True, boxprops=dict(facecolor='orange', alpha=0.6),
                  medianprops=dict(color='black'))

# 绘制箱线图（右轴：Adjacent Outliers）
bp2 = ax2.boxplot(adj_outliers, positions=x + width/2+0.05, widths=width,
                  patch_artist=True, boxprops=dict(facecolor='mediumseagreen', alpha=0.6),
                  medianprops=dict(color='black'))

# 设置坐标轴
ax1.set_xticks(x)
ax1.set_xticklabels(models, rotation=45, ha='right')
ax1.set_ylabel("Outlier Percentage", color='orange')
ax2.set_ylabel("Adjacent Outlier Percentage", color='mediumseagreen')

# 图例
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='orange', edgecolor='black', label='Outliers'),
    Patch(facecolor='mediumseagreen', edgecolor='black', label='Adjacent Outliers')
]
ax1.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=2, frameon=False)

plt.tight_layout()
plt.show()
