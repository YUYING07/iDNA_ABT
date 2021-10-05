# ---encoding:utf-8---
# @Author : yuying0711
# @Email : 2539449171@qq.com
# @IDE : PyCharm
# @File : visualization.py

from util import util_dim_reduction

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import pandas as pd

NUM_CLASS = 2  # 一起设置类别
PATH = '../image_results/'


def dimension_reduction(repres_list, label_list, epoch, config):
    print('t-SNE')
    title = 'Samples Embedding t-SNE Visualisation, Epoch[{}]'.format(epoch)
    util_dim_reduction.t_sne(title, repres_list, label_list, None, NUM_CLASS, config)
    print('PCA')
    title = 'Samples Embedding PCA Visualisation, Epoch[{}]'.format(epoch)
    util_dim_reduction.pca(title, repres_list, label_list, None, NUM_CLASS, config)


def penultimate_feature_visulization(repres_list, label_list, epoch, config):
    X = np.array(repres_list)  # [num_samples, n_components]
    data_index = label_list
    data_label = None
    class_num = NUM_CLASS  # 4
    # draw
    title = 'Learned Feature Visualization, Epoch[{}]'.format(epoch)
    font = {"color": "darkred", "size": 13, "family": "serif"}
    plt.style.use("default")

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=data_index, alpha=0.6, cmap=plt.cm.get_cmap('Set1', class_num))  # tab20c

    if data_label:
        for i in range(len(X)):
            plt.annotate(data_label[i], xy=(X[:, 0][i], X[:, 1][i]),
                         xytext=(X[:, 0][i] + 1, X[:, 1][i] + 1))
            # X, Y is the coordinate to be marked, and 'xytext' is the corresponding label coordinate
    plt.title(title, fontdict=font)

    if data_label is None:
        cbar = plt.colorbar(ticks=range(class_num))
        cbar.set_label(label='digit value', fontdict=font)
        plt.clim(0 - 0.5, class_num - 0.5)
    final_path = PATH+str(re.sub('/', '_', config.train_data))+title+'.png'
    plt.savefig(final_path)
    plt.show()


def xlsx_heatmap(input_file, sheet_num):
    for i in range(sheet_num):
        df = pd.read_excel(input_file, sheet_name=i, index_col=0)
        if i != sheet_num-1:
            ax = sns.heatmap(df*100, annot=True, cmap="summer", fmt='.2f',)
            plt.xticks(fontsize=10, rotation=30)
            plt.yticks(fontsize=10, rotation=30)
        else:
            ax = sns.heatmap(df*100, annot=True, cmap="summer",)
            plt.xticks(fontsize=6, rotation=30)
            plt.yticks(fontsize=6, rotation=30)
        # 设置colorbar的刻度字体大小
        cax = plt.gcf().axes[-1]
        cax.tick_params(labelsize=15)
        plt.savefig("../compare_results/Cross_Species_Validation/"+str(i)+".png", dpi=600)
        plt.show()     # show


if __name__ == '__main__':
    xlsx_heatmap("../compare_results/Cross_Species_Validation/Cross-Species_Validation.xlsx", 3)