#!/usr/bin/env python3
# _*_coding:utf-8 _*_
# author: Mr.He
# datetime:2019/10/31 14:49
# software: PyCharm


from torchvision import models
from torchsummary import summary

net = models.resnet18(pretrained=False)
print(net)