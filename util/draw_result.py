import pygal
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator


def draw_radar(data, output_path, class_name):
    '''雷达图'''
    name = data.columns.tolist()
    radar_chart = pygal.Radar(fill=False, range=(0, 1.0))
    # 添加雷达图的标题
    radar_chart.title = class_name
    # 添加雷达图各顶点的含义
    radar_chart.x_labels = ['ACC', 'SN', 'SP', 'MCC', 'AUC']
    for n in name:
        radar_chart.add(n, data[n].values)
    # 保存图像
    radar_chart.render_to_file(output_path+'.svg')


def draw_bar_chart(data, output_path, labels, width, rot, y_up, y_down):
    '''成组bar图'''
    AB = data.iloc[:, 0]
    ABT = data.iloc[:, 1]
    SOTA = data.iloc[:, 2]

    # x轴是由[1,2,3,4,5]组成
    x = np.arange(len(labels))
    x *= 2
    colours = ['lightskyblue', '#4fc4aa', '#7199cf', 'moccasin', 'lightseagreen', 'lightsalmon', 'pink']
    fig, ax = plt.subplots()
    # 先画第一个男性矩形

    rects1 = ax.bar(x - width, AB, width, label='iDNA-AB', color=colours[0])
    rects4 = ax.bar(x, SOTA, width, label='iDNA-MS', color=colours[3])
    rects3 = ax.bar(x+ width, ABT, width, label='iDNA-ABT', color=colours[2])
    # 设置图像的一些参数
    ax.set_ylabel("MCC", fontsize=18)
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=rot)
    ax.legend(loc='upper center', ncol=4)

    # 为图像加上标签
    # rect.get_height()是获取当前的高度，比如蓝色的第一条高度就是20 rect.get_x()获取当前矩形的起始x轴的位置
    plt.xticks(fontsize=10)
    plt.ylim([y_down, y_up])
    fig.tight_layout()  # 自动调整子图充满整个屏幕
    fig.show()


def draw_feature_bar_chart(data, output_path, labels, width, rot, y_up, y_down):
    '''成组bar图'''
    ABT = data.iloc[:, 1]
    DNC = data.iloc[:, 4]
    NAC = data.iloc[:, 5]
    EIIP = data.iloc[:, 6]
    BINARY = data.iloc[:, 7]
    ANF = data.iloc[:, 8]
    NCP = data.iloc[:, 9]
    # x轴是由[1,2,3,4,5]组成
    x = np.arange(len(labels))
    x *= 2
    colours = ['steelblue', '#4fc4aa', 'powderblue', '#7199cf', 'lightskyblue', 'lightgreen', 'aquamarine', 'pink']
    fig, ax = plt.subplots()
    # 先画第一个男性矩形

    rects3 = ax.bar(x-3*width, ABT, width, label='iDNA-ABT', color=colours[0])
    rects5 = ax.bar(x-2 * width, DNC, width, label='DNC', color=colours[1])
    rects6 = ax.bar(x-width, NAC, width, label='NAC', color=colours[2])
    rects7 = ax.bar(x, EIIP, width, label='EIIP', color=colours[3])
    rects8 = ax.bar(x + width, BINARY, width, label='BINARY', color=colours[4])
    rects9 = ax.bar(x + 2*width, ANF, width, label='ANF', color=colours[5])
    rects10 = ax.bar(x + 3*width, NCP, width, label='NCP', color=colours[6])
    # 设置图像的一些参数
    ax.set_ylabel("MCC", fontsize=18)
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=rot)
    ax.legend(loc='upper center', ncol=4)

    # 为图像加上标签
    plt.xticks(fontsize=14)
    plt.ylim([y_down, y_up])
    fig.tight_layout()  # 自动调整子图充满整个屏幕
    fig.show()


def draw_lines(data, output, labels, y_up, y_down, rot):
    AB = data.iloc[:, 0]
    ABT = data.iloc[:, 1]
    SOTA = data.iloc[:, 3]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = np.arange(len(labels))
    plt.ylim([y_down, y_up])
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=rot, fontsize='small')
    colours = ['steelblue', '#4fc4aa', 'powderblue', '#7199cf', 'lightskyblue', 'lightgreen', 'aquamarine', 'pink']

    ax.plot(x, ABT, c=colours[0], label='ABT_iDNA')
    ax.plot(x, AB, c=colours[1], ls='-.', label='AB_iDNA')
    ax.plot(x, SOTA, c=colours[2],  ls='-', label='iDNA_MS')

    ax.grid()
    ax.legend(loc='upper center', ncol=4)
    plt.show()


if __name__ == '__main__':
    '''雷达图'''
    # file = pd.read_excel('main_result.xlsx')
    # draw_radar(file.iloc[:, 0:2], '5hmC', '5hmC')
    # draw_radar(file.iloc[:, 2:6], '4mC', '4mC')
    # draw_radar(file.iloc[:, 6:19], '6mA', '6mA')
    '''柱状图'''
    cols = [1,  2, 3, 4]  # 4mc
    # cols = [5, 6]
    # cols = [7, 8, 9,x 10, 11, 12, 13, 14, 15, 16, 17, 18]
    AB = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='AB').iloc[6, :]
    HAND = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='hand').iloc[6, :]
    ABT = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='ABT').iloc[6, :]
    SOTA = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='SOTA').iloc[6, :]
    DNC = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='DNC').iloc[6, :]
    NAC = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='NAC').iloc[6, :]
    EIIP = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='EIIP').iloc[6, :]
    BINARY = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='BINARY').iloc[6, :]
    ANF = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='ANF').iloc[6, :]
    NCP = pd.read_excel('compare_result.xlsx', usecols=cols, sheet_name='NCP').iloc[6, :]
    file = pd.concat([AB, ABT, HAND, SOTA, DNC, NAC, EIIP, BINARY, ANF, NCP], axis=1)
    name = ['A.thaliana', 'C.elegans', 'C.equisetifolia', 'D.melanogaster','F.vesca', 'H.sapiens','R.chinensis','S.cerevisiae','T.thermophile','Tolypocladium','Xoc BLS256']

    draw_feature_bar_chart(file, 'compare', file.index.values, 0.2, 0, 0.8, 0.2)
    # draw_feature_bar_chart(file, 'compare', file.index.values, 0.2, 0, 0.98, 0.85)
    # draw_feature_bar_chart(file, 'compare', name, 0.2, 35, 0.95, 0.3)

    # file = pd.concat([AB, ABT, SOTA], axis=1)
    # draw_bar_chart(file, 'compare', name, 0.4, 35, 0.95, 0.3)
    # draw_bar_chart(file, 'compare', file.index.values, 0.2, 0, 1, 0.8)
    # draw_bar_chart(file, 'compare', file.index.values, 0.3, 0, 0.8, 0.2)
    # draw_lines(file, '6mA', name, 0.95, 0.4, 20)
    # draw_lines(file, '4mC', file.index.values, 0.8, 0.2)

    # draw_lines(file, '5hmC', file.index.values, 1.1, 0.2, 10)



