# ---encoding:utf-8---
# @Time : 2021.03.03
# @Author : yuying0711
# @Email : 2539449171@qq.com
# @IDE : PyCharm
# @File : test.py

import torch

a = torch.tensor([0.8, 0.4, 0.3])
b = torch.tensor([0.7, 0.3, 0.3])
c = torch.tensor([0.6, 0.5, 0.3])

a = a.view(1, -1)
b = b.view(1, -1)
c = c.view(1, -1)

tensor_list = [a, b, c]
res = torch.cat(tensor_list, dim=0)
# print(res)

res = torch.mean(res, dim=0)
# print(res)

print('-' * 50)
