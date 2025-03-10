# CNN-LSTM 기반 자동 운반 차량의 운행 데드락 탐지 시스템
## 1. 프로젝트의 개요
### 1-1. 프로젝트 개발 배경

&nbsp;&nbsp;&nbsp;&nbsp;최근 스마트 팩토리의 생산성을 향상과 자동화 생산 라인을 구성하기 위해 특정 물건을 자동으로 운반하는 자동화의 핵심 기술인 AGV(Automated Guided Vehicle)을 도입하고 있음.그러나 여러 대의 AGV가 자율적으로 동작하면서 두 대 이상의 AGV가 다양한 원인으로 서로 주행하지 못하는 데드락(deadlock)이 발생하여 생산성 감소는 물론 물리적인 안전성을 침해할 수 있
다. 

&nbsp;&nbsp;&nbsp;&nbsp;따라서 본 프로젝트에서는 스마트 팩토리에서 발생할 수 있는 AGV 데드락을 탐지하기 위해 CNN-LSTM기반 AGV 데드락 탐지 시스템을 구현하였다. 실제 스마트팩토리 환경에서 AGV 주행 과정에서 이미지 시퀀스 데이터를 추출하여 CNN-LSTM을 학습한 뒤 AGV의 데드락 여부를 판단하였으며 안전한 운행을 보장하는 AI모델을 구성하였다.

### 1-2. 프로젝트 목표 및 주요 기능
### 최종 목표 : 데드락이 발생한 AGV를 탐지하는 AI 모델 개발

|  | tools |
|-------------|-------|
| 개발 언어   |![Python](https://img.shields.io/badge/Python-3.8.4-3776AB?logo=python&logoColor=white)|
| 사용 프레임워크| ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| 환경      | AGV 연구소|
| 개발 환경      |Windows 11  |

## 3. 시스템 구조도
&nbsp;&nbsp;&nbsp;&nbsp;AGV 연구소에서 카메라를 설치한뒤 2대의 AGV를 주행. 교차로 상태를 가정하여 데드락 상황과 정상 주행 상황 아래의 그림과 같이 CNN-LSTM 기반 자동 운반 차량의 운행 데드락 탐지 시스템
## 1. 프로젝트의 개요
### 1-1. 프로젝트 개발 배경

&nbsp;&nbsp;&nbsp;&nbsp;최근 스마트 팩토리의 생산성을 향상과 자동화 생산 라인을 구성하기 위해 특정 물건을 자동으로 운반하는 자동화의 핵심 기술인 AGV(Automated Guided Vehicle)을 도입하고 있음.그러나 여러 대의 AGV가 자율적으로 동작하면서 두 대 이상의 AGV가 다양한 원인으로 서로 주행하지 못하는 데드락(deadlock)이 발생하여 생산성 감소는 물론 물리적인 안전성을 침해할 수 있
다. 

&nbsp;&nbsp;&nbsp;&nbsp;따라서 본 프로젝트에서는 스마트 팩토리에서 발생할 수 있는 AGV 데드락을 탐지하기 위해 CNN-LSTM기반 AGV 데드락 탐지 시스템을 구현하였다. 실제 스마트팩토리 환경에서 AGV 주행 과정에서 이미지 시퀀스 데이터를 추출하여 CNN-LSTM을 학습한 뒤 AGV의 데드락 여부를 판단하였으며 안전한 운행을 보장하는 AI모델을 구성하였다.

### 1-2. 프로젝트 목표 및 주요 기능
### 최종 목표 : 데드락이 발생한 AGV를 탐지하는 AI 모델 개발

|  | tools |
|-------------|-------|
| 개발 언어   |![Python](https://img.shields.io/badge/Python-3.8.4-3776AB?logo=python&logoColor=white)|
| 사용 프레임워크| ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| 환경      | AGV 연구소|
| 개발 환경      |Windows 11  |

## 3. 시스템 구조도
&nbsp;&nbsp;&nbsp;&nbsp;AGV 연구소에서 카메라를 설치한뒤 2대의 AGV를 주행. 교차로 상태를 가정하여 데드락 상황과 정상 주행 상황 아래의 그림과 같이 재현

![image](https://github.com/user-attachments/assets/5fb13937-5c66-40ad-9d69-c9ccb6b12972)

&nbsp;&nbsp;&nbsp;&nbsp;정상 주행 상황과 데드락 상황을 촬영하여 동영상 데이터를 획득. 그 후 동영상 데이터를 1초 단위로 분할하여 이미지 시퀀스 데이터를 구성한뒤 AI 모델의 입력데이토로 활용. 각 이미지 데이터는 현재 시점으로부터 t시간 이후의 이미지를 포함하며
 n초동안 여러대의 AGV가 정지 상태일경우 데드락상태라고 지정하였음. 본 프로젝트에서는 60초동안 정지해 있을경우 데드락이라고 판단.
 ![image](https://github.com/user-attachments/assets/b32ebec4-728a-4832-9906-9a8fdc06556f)
![image](https://github.com/user-attachments/assets/27a429b3-006b-492a-bf0f-0d09900fae3e)

## 3-1. 모델 구조도
 본 프로젝트에서는 데드락을 탐지하기위해 CNN과 LSTM을 결합하여 모델을 구성하였음
 
 ![image](https://github.com/user-attachments/assets/ae007ef3-630a-491b-83b9-2e8db62d73c1)
 
비디오 데이터로부터 추출한 이미지 시퀀스 데이터는 현재 시간 t로부터 n초 뒤의 이미지로 구성되어 있으며 이 이미지 시퀀스 데이터를 CNN 네트워크를 통해 비디오 프레임에서 특징 벡터 시퀀스를 추출한다. 특징 벡터 시퀀스를 추출한 뒤 LSTM에 입력하여 시간에 따른 AGV의 동선을 분석한 뒤 데드락을 탐지.

![image](https://github.com/user-attachments/assets/12edf3f9-6d82-41cf-af18-a2763cd708b8)

## 4. 데드락 탐지 여부 확인
CNN-LSTM과 CNN-RNN 두가지 모델을 평가.
구현한 모델을 AGV연구소 AI서버에 탑재하여 성능을 평
![image](https://github.com/user-attachments/assets/ed75a9d7-eaae-437a-bac9-b71070805595)

![image](https://github.com/user-attachments/assets/9aa0d917-a14e-4bcd-a09a-c3b137c44e27) ![image](https://github.com/user-attachments/assets/6261ca3f-f22e-49eb-acfa-f6edb78c3399) ![image](https://github.com/user-attachments/assets/228b7d68-fc59-4f16-bf03-8f0b47c97d39)




