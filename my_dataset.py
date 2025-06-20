from PIL import Image
import torch
from torch.utils.data import Dataset

class MyDataSet(Dataset):
    """自定义数据集"""

    def __init__(self, images_path: list, images_class: list, transform=None):
        self.images_path = images_path
        self.images_class = images_class
        self.transform = transform

    def __len__(self):
        return len(self.images_path)

    def __getitem__(self, item):
        # 加载图像并强制转换为RGB模式
        img = Image.open(self.images_path[item]).convert('RGB')  # 关键修改
        # 定义标签
        label = self.images_class[item]  # 必须正确定义label

        if self.transform is not None:
            img = self.transform(img)

        return img, label  # 确保返回img和label

    @staticmethod
    def collate_fn(batch):
        images, labels = tuple(zip(*batch))
        images = torch.stack(images, dim=0)
        labels = torch.as_tensor(labels)
        return images, labels