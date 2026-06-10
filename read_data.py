from torch.utils.data import Dataset
import cv2
from PIL import Image
# class MyData(Dataset):

#     def __init__(self):

#     def getitem__(self, idx):
img_path = "./hymenoptera_data/train/ants/0013035.jpg"

img = Image.open(img_path)