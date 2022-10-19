import torch
import torch.nn as nn
import torch.nn.functional as F


class TextCNN(nn.Module):
    def __init__(self, config):
        super(TextCNN, self).__init__()
        self.config = config
        self.kmer = config.k_mer

        self.filter_sizes = [1, 2, 4, 8, 16, 32]
        self.embedding_dim = 128
        dim_cnn_out = config.num_embedding
        filter_num = 128

        # self.filter_sizes = [int(fsz) for fsz in self.filter_sizes.split(',')]
        self.embedding = nn.Embedding(4101, self.embedding_dim, padding_idx=0)

        self.convs = nn.ModuleList(
            [nn.Conv2d(1, filter_num, (fsz, self.embedding_dim)) for fsz in self.filter_sizes])
        self.linear = nn.Linear(len(self.filter_sizes) * filter_num, dim_cnn_out)

    def forward(self, seqs):
        x = self.embedding(seqs)  # 经过embedding,x的维度为(batch_size, max_len, embedding_dim)

        # 经过view函数x的维度变为(batch_size, input_chanel=1, w=max_len, h=embedding_dim)
        x = x.view(x.size(0), 1, x.size(1), self.embedding_dim)

        # 经过卷积运算,x中每个运算结果维度为(batch_size, out_chanel, w, h=1)
        x = [F.relu(conv(x)) for conv in self.convs]
        # print('conv x', len(x), [x_item.size() for x_item in x])

        # 经过最大池化层,维度变为(batch_size, out_chanel, w=1, h=1)
        x = [F.max_pool2d(input=x_item, kernel_size=(x_item.size(2), x_item.size(3))) for x_item in x]
        # print('max_pool2d x', len(x), [x_item.size() for x_item in x])

        # 将不同卷积核运算结果维度（batch，out_chanel,w,h=1）展平为（batch, outchanel*w*h）
        x = [x_item.view(x_item.size(0), -1) for x_item in x]
        # print('flatten x', len(x), [x_item.size() for x_item in x])

        # 将不同卷积核提取的特征组合起来,维度变为(batch, sum:outchanel*w*h)
        representation = torch.cat(x, 1)
        logits_clsf = representation
        print(representation.shape)
        return logits_clsf, representation
