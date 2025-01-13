import torch
from torch.utils.data import Dataset
import numpy as np
import torchvision
import torchvision.transforms as T
import torchvision.transforms.functional as F
import random
seed = 2024
deterministic = True
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)


class RandHorizontalFlip(object):
    def __call__(self, image, labels):
        # 50% 확률로 수평반전
        number=random.random()
        if number > 0.5:
            
            for t in range(image.shape[0]):
                image[t,:,:,:] = F.hflip(image[t,:,:,:])
        return image, labels

# 수직반전 클래스
class RandVerticalFlip(object):
    def __call__(self, image, labels):
        # 50% 확률로 수직반전
        if random.random() > 0.5:

            for t in range(image.shape[0]):
                image[t,:,:,:] = F.vflip(image[t,:,:,:])
        return image, labels
    
class RandRotate90(object):
    def __call__(self, image, labels):
        # 90도 단위로 회전 (0도, 90도, 180도, 270도 중 하나 선택)
        angles = [0, 90, 180, 270]
        angle = random.choice(angles)
        
        # 이미지 회전 적용
        for t in range(image.shape[0]):
            image[t,:,:,:] = F.rotate(image[t,:,:,:], angle)

        return image, labels



class RandCutout(object):
    def __init__(self, num_holes=6, max_h_size=32, max_w_size=32, p=0.5):
       
        self.num_holes = num_holes
        self.max_h_size = max_h_size
        self.max_w_size = max_w_size
        self.p = p

    def __call__(self, image, labels):
        if random.random() > self.p:
            return image, labels  # p 확률에 따라 적용 안함
        

        for _ in range(self.num_holes):
            # 랜덤 위치 및 크기 설정
            hole_x = random.randint(0, 416-self.max_h_size)
            hole_y = random.randint(0, 416-self.max_h_size)
            #print(hole_x)
            # # 이미지의 해당 위치에 구멍을 넣음 (0으로 설정)
            image[:,:,hole_x:hole_x+self.max_h_size, hole_y:hole_y+self.max_h_size] = 0  # 구멍에 해당하는 부분을 0으로 설정
        
        return image, labels

class RandBrightness(object):
    def __call__(self, image, labels):
        # 60채널(60개의 프레임)에 동일한 밝기 조정을 적용
        
        # 각 채널에 대해 밝기 조정 적용
        for t in range(image.shape[0]):  # image.shape[2]는 채널 수(60)
            brightness_factor = 1 + np.random.uniform(-0.5, 0.5)
            image[t,:, :,:] = torchvision.transforms.functional.adjust_brightness(image[t,:,:,:], brightness_factor)
        
        return image, labels

class RandRotateView(object):
    def __call__(self, image,labels):
        rotate = random.uniform(-30, 30)
        if random.randint(0, 3) == 1 :

            for t in range(image.shape[0]):

                image[t,:,:,:] = torchvision.transforms.functional.rotate(image[t,:,:,:], rotate)  # ndimage.rotate 대신 torchvision의 rotate 사용

        return image, labels


class RandomTranslate(object):
    def __call__(self, image, labels, range_x=80, range_y=20):
        trans_x = range_x * (np.random.rand() - 0.5)
        trans_y = range_y * (np.random.rand() - 0.5)
        
        for t in range(image.shape[0]): 
            image[t,:, :,:] = T.functional.affine(image[t,:, :,:], angle=0, translate=(trans_x, trans_y), scale=1.0, shear=[0, 0])
        return image, labels

class CustomDataset(Dataset):
    def __init__(self, image_arrays, labels,mode='Valid'):

        self.image_arrays = image_arrays
        self.labels = labels
        self.mode=mode
        self.RandomTranslate=RandomTranslate()
        self.RandRotateView=RandRotateView()
        self.RandBrightness=RandBrightness()
        self.RandCutout=RandCutout()
        self.RandRotate90=RandRotate90()
        self.RandHorizontalFlip=RandHorizontalFlip()
        self.RandVerticalFlip=RandVerticalFlip()


    def __len__(self):
        return len(self.image_arrays)

    def __getitem__(self, idx):
     
        image_sequence = self.image_arrays[idx]
       
        image_sequence_tensor = torch.from_numpy(image_sequence).float() / 255.0
        image_sequence_tensor = image_sequence_tensor.permute(0,3, 1, 2)
        #print(image_sequence.shape)

        label = self.labels[idx]

        if self.mode=='Train':
            image_sequence_tensor,label=self.RandHorizontalFlip(image_sequence_tensor,label)
            image_sequence_tensor,label=self.RandRotateView(image_sequence_tensor,label)
            
            #image_sequence_tensor,label=self.RandomTranslate(image_sequence_tensor,label)
            
            #image_sequence_tensor,label=self.RandBrightness(image_sequence_tensor,label)
            #image_sequence_tensor,label=self.RandCutout(image_sequence_tensor,label)
            
            #image_sequence_tensor,label=self.RandRotate90(image_sequence_tensor,label)
            #image_sequence_tensor,label=self.RandVerticalFlip(image_sequence_tensor,label)

            



        return image_sequence_tensor, torch.tensor(label, dtype=torch.float32)
