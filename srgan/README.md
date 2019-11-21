# SRGAN
SRGACN目的是使用低分辨率图片生成自然的高分辨率图片。SRGAN的生成器使用了深层VGG网络，能更好的提取图片的感知特征。相对于其他超高分辨率方法，SRGAN主要创新点在损失函数的设计：<br>
1 第一部分是感知损失。使用了不同于基于像素的计算方法，用VGG网络提取的特征，和真实图片的特征对比，得到全新的感知损失函数；<br>
2 第二部分是对抗损失。这部分损失函数以欺骗判别器为目的，最终使生成的细节符合人类的视觉习惯。<br>
生成对抗网络（包括其他深度学习算法）最关键的是损失函数的设计，它能指导整个网络如何工作。
<br>
<br>
论文：[Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial](https://arxiv.org/abs/1609.04802)
<br>
## 示例
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/srgan/0.png" width="640"\>
    <br>
    输入的噪声图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/srgan/500.png" width="640"\>
    <br>
    200个epoch后生成的图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/srgan/5000.png" width="640"\>
    <br>
    1000个epoch后生成的图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/srgan/10000.png" width="640"\>
    <br>
    5000个epoch后生成的图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/srgan/20000.png" width="640"\>
    <br>
    14000个epoch后生成的图片
</p>
<br>

## 数据集
示例中采用的是coco数据集，可以直接从cocodataset官网上下载：
[COCO data test2017](http://images.cocodataset.org/zips/test2017.zip)

数据集大小为6G，国内可以直接运行dataset_downloader.py下载数据并解压。

```sh
python dataset_downloader.py
```

## 训练SRGAN

```sh
python sr_train.py
```

## 测试SRGN

测试模型

```sh
python sr_test.py test_model
```

测试生成效果

```sh
python sr_test test_lr_images
```
