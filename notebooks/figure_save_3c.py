
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes


data = pd.read_csv("figure_3.csv")
dataC = data.copy()
energy_cutoff = 0.5

filtered_dataC = dataC[(dataC['energyC'] > energy_cutoff) | (dataC['energyC'] < -energy_cutoff)]
filtered_dataC.reset_index(drop=True, inplace=True)
plt.rcParams['font.size'] = 10

fig, (ax2, ax1) = plt.subplots(2, 1, sharex=True, figsize=(1.5, 1.5))
fig.subplots_adjust(hspace=0.3)  

sns.barplot(data=filtered_dataC, x='residueC', y='energyC', color='k', ax=ax2)
sns.barplot(data=filtered_dataC, x='residueC', y='energyC', color='k', ax=ax1)

ax1.set_ylim(-9, -7)  
ax2.set_ylim(-1, filtered_dataC['energyC'].max() + 1) 

ax1.set_xlim(filtered_dataC.index.min()-1, filtered_dataC.index.max()+1)  
ax2.set_xlim(filtered_dataC.index.min()-1, filtered_dataC.index.max()+1)  

ax2.spines.bottom.set_visible(False)
ax1.spines.top.set_visible(False)


ax2.tick_params(labelbottom=False, bottom=False)

ax1.set_xticks([0, 1, 2, 4, 5, 7, 8])
ax1.set_xticklabels(['745', '', '', '', '805', '', '906'], rotation=45)
ax2.set_yticks([-1, 0, 2])
ax1.set_yticks([-7, -8, -9])

d = .5  
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax2.plot([0, 1], [0, 0], transform=ax2.transAxes, **kwargs)
ax1.plot([0, 1], [1, 1], transform=ax1.transAxes, **kwargs)
fig = plt.figure(figsize=(1.5, 1.5))
ax1.set_xlabel('')
ax1.set_ylabel('')
ax2.set_xlabel('')
ax2.set_ylabel('')
fig1 = plt.gcf()
fig1.savefig('figure_3_c.png',bbox_inches='tight', pad_inches=0, transparent=False)
