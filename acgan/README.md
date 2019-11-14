# ACGAN
ACGACN在训练生成器的时候，同时训练了一个辅助分类器。比如ImageNet的1000张图片，可以训练100个GAN模型出来。相当于训练生成器的同时也训练了一个分类器。这样做的目的是提高GAN的稳定性，有了分类器的帮助，生成图片的准确性也应该可以得到提升。
<br>
<br>
论文：[Conditional Image Synthesis With Auxiliary Classifier GANs](https://arxiv.org/abs/1610.09585)
<br>
## 示例
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/0.png" width="640"\>
    <br>
    输入的噪声图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/200.png" width="640"\>
    <br>
    200个epoch后生成的图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/1000.png" width="640"\>
    <br>
    1000个epoch后生成的图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/5000.png" width="640"\>
    <br>
    5000个epoch后生成的图片
</p>
<br>
<p align="center">
    <img src="https://github.com/figoliu/GANs/blob/master/resources/acgan/14000.png" width="640"\>
    <br>
    14000个epoch后生成的图片
</p>
<br>

## 数据集
示例中采用的是Mnist数据集，已经集成到Keras中，可以直接调用Keras API进行下载。如果数据集下载太慢，可以通过修改Keras代码，使用国内服务器下载：

找到文件 keras\datasets\mnist.py

```python
path = get_file(path, origin='https://s3.amazonaws.com/img-datasets/mnist.npz', file_hash='8a61469f7ea1b51cbae51d4f78837e45')
```
改为

```python
path = get_file(path, origin='http://106.13.194.145/mnist.npz')
```

## 运行ACGAN

```sh
python acgan.py
```