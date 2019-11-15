from keras.utils.data_utils import get_file
import zipfile
import os

class GANsDataset():
    def downloadFile(self, filename):
        self.filename = filename
        self.zipPath = os.getcwd()
        url = 'http://106.13.194.145/datasets/' + self.filename + '.zip'
        path = get_file(self.zipPath + self.filename + '.zip', origin=url)
        return path

if __name__ == '__main__':
    #支持的数据集：ae_photos  apple2orange  cityscapes  facades  summer2winter_yosemite
    download = GANsDataset()
    path = download.downloadFile('summer2winter_yosemite')

    #解压下载文件
    dataPath = os.path.join(os.getcwd(), 'datasets')
    isExist = os.path.exists(dataPath)
    if not isExist:
        os.makedirs(dataPath)
    zipFile = zipfile.ZipFile(path)
    zipFile.extractall(dataPath)
    zipFile.close()