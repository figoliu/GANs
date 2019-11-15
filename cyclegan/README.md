# CYCLEGAN
针对两张完全不同的图片，CYCLEGAN设计了一个网络结构，能够相互生成。简单的讲，就是有两个生成器和两个判别器，训练过程中循环使用，最后得到两个生成器和两个判别器。<br>
[cyclegan](https://)

<br>
<br>
论文：[Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593)
<br>
## 示例
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/0.png"\>
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/200.png"\>
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/1000.png"\>
    <br>
    输入的噪声图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/200.png" width="640"\>
    <br>
    50个epoch后生成的图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/1000.png" width="640"\>
    <br>
    100个epoch后生成的图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/5000.png" width="640"\>
    <br>
    200个epoch后生成的图片
</p>
<br>
<br>

## 数据集

可以从IMAGENET直接下载相关数据集。数据集需要放到datasets文件夹下。更方便的方法是，示例中直接运行datasetsdownloader.py, 可以从国内服务器下载数据集并解压。

```sh
cd Gans/cyclegan
python datasetsdownloader.py
```
目前支持下载的数据集：ae_photos  apple2orange  cityscapes  facades  summer2winter_yosemite<br>
如果要下载facades数据集，到datasetsdownloader.py文件中修改即可。

```python
#支持的数据集：ae_photos  apple2orange  cityscapes  facades  summer2winter_yosemite
download = GANsDataset()
path = download.downloadFile('summer2winter_yosemite')
```
改成：<br>
```python
#支持的数据集：ae_photos  apple2orange  cityscapes  facades  summer2winter_yosemite
download = GANsDataset()
path = download.downloadFile('facades')
```

## 运行CYCLEGAN
将数据集改成已下载到本地的数据集：
```python
if __name__ == '__main__':
    #支持的数据集：ae_photos  apple2orange  cityscapes  facades  summer2winter_yosemite
    gan = CycleGAN(dataset='facades')
    gan.train(epochs=200, batch_size=1)
```
<br>
运行：

```sh
python cyclegan.py
```