# Purpose - predict bird class from image
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

import os

birds = pd.read_csv('../docs/birds.csv')
birds_label_grouped = birds[birds['data set'] == 'train'] \
    .groupby('labels', as_index=False).agg({'class index': 'count'})
birds_label_grouped = birds_label_grouped[['class index', 'labels']]

# for i in range(400):
#     print(birds_label_grouped.iloc[[i], :2], sep='\n')

bp = sns.barplot(x='class index', y='labels',
                 data=birds_label_grouped.sort_values(by='class index'))
bp.set(yticklabels=[])
plt.show()
# sns.barplot(x='class index', y='labels', data=birds_label_grouped[50:100])
#
# sns.barplot(x='class index', y='labels', data=birds_label_grouped[100:150])
#
# sns.barplot(x='class index', y='labels', data=birds_label_grouped[150:200])
#
# sns.barplot(x='class index', y='labels', data=birds_label_grouped[200:250])
#
# sns.barplot(x='class index', y='labels', data=birds_label_grouped[250:300])
#
# sns.barplot(x='class index', y='labels', data=birds_label_grouped[350:400])
# bp.xaxis.set_tick_params(rotation=90)

