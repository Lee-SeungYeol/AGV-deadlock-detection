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
&nbsp;&nbsp;&nbsp;&nbsp;AGV 연구소에서 카메라를 설치한뒤 2대의 AGV를 주행. 교차로 상태를 가정하여 데드락 상황과 정상 주행 상황을 제현

![image](https://github.com/user-attachments/assets/5fb13937-5c66-40ad-9d69-c9ccb6b12972)
