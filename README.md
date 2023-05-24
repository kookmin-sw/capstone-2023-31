# GLASSFIT

> **팀페이지 (2023-31) :** [https://kookmin-sw.github.io/capstone-2023-31/](https://kookmin-sw.github.io/capstone-2023-31/)

### 🗣️ 안경 사야 하는데 너무 귀찮아 !
### 👀 집에서 편하게 써보고 구매하고 싶은데 !! 
### 🦊 내 얼굴형에 맞는 안경을 구매하고 싶어 !!! 

<p align="center"><img src="https://github.com/kookmin-sw/capstone-2023-31/assets/63188042/7829dec5-8297-4236-96d2-4495ba0f6722" width="700"/></p>

<br>

## 목차
- [1. 프로젝트 소개 😎](#1-프로젝트-소개-😎) 
- [2. 주요 기능 🌟](#2-주요-기능-🌟)
- [3. 팀원 소개 👩](#3-팀원-소개-👩)
- [4. 소개 영상 🎥](#4-소개-영상-🎥)
- [5. 프로젝트 구조 🗂️](#5-프로젝트-구조-🗂️)
- [6. 기술 스택 📊](#6-기술-스택-📊)
- [7. 사용법 🕹️](#7-사용법-🕹️)
- [8. Document 📑](#8-document-📑)


## 1. 프로젝트 소개 😎
<code>“GLASSFIT”</code>은 사용자의 얼굴형을 분석하여 어울리는 안경테를 추천하고, 웹캠을 통해 가상으로 해당 안경을 착용해 볼 수 있는 웹 서비스입니다.

안경은 오랜 기간 사용되는 상품인 만큼 많은 사람들이 자신과 어울리는 안경을 구매하고자 합니다. 그러나 옷 쇼핑과는 달리 안경원에서는 다양한 안경테를 직접 착용해 보는 것이 어렵고 번거로운 일입니다. 이러한 불편함을 해소하기 위해 저희는 집에서 편하게 안경을 착용해 보고, 자신의 얼굴형에 맞는 안경테를 추천받을 수 있는 서비스를 제공하고자 합니다.

본 프로젝트의 목표는 사용자에게 편리하고 직관적인 안경 선택 과정을 제공하는 것입니다. 이를 통해 사용자는 자신에게 어울리는 안경을 찾는 과정에서의 불필요한 시간과 비용을 절약할 수 있습니다.

<br><br>


## 2. 주요 기능 🌟
<code>[얼굴형 분석 기능]</code>

메인 페이지의 ‘얼굴형 분석하기’ 버튼을 누르면 실시간 Web-Cam 화면이 나타납니다. 사용자는 정면을 응시한 뒤 사진 찍기 버튼을 눌러 얼굴형 분석 기능을 사용할 수 있습니다. 업로드된 얼굴 이미지는 Tensorflow 툴을 통해 학습된 모델을 사용해서 사용자의 얼굴 형태, 윤곽, 비율 등을 신속하게 분석하고 해석합니다. 분석된 얼굴형은 마이페이지에 저장할 수 있으며, 사용자에게 안경테 종류를 추천해줍니다. 
<br><br>

<code>[안경 가상 피팅]</code>

사용자는 추천된 안경테를 가상으로 착용할 수 있습니다. Web-cam을 통해 자신의 얼굴에 추천된 안경테를 씌워볼 수 있으며, 실제로 착용하지 않고도 어떻게 보일지 미리 확인할 수 있습니다. 이를 통해 사용자는 자신과 잘 어울리는 안경테를 선택하는데 도움을 받을 수 있습니다. 
<br><br>

#### 페이지별 기능
<p align="center"><img src="https://github.com/kookmin-sw/capstone-2023-31/assets/63188042/5e2a6d34-0f8b-40d7-b980-a2aa27abd75c" width="800"/></p>
<p align="center"><img src="https://github.com/kookmin-sw/capstone-2023-31/assets/63188042/87d357fd-7f51-483b-ae63-a03946bcde07" width="800"/></p>
<p align="center"><img src="https://github.com/kookmin-sw/capstone-2023-31/assets/63188042/5d9b799f-641c-4380-881f-2fae27d20884" width="800"/></p>

<br><br>


## 3. 팀원 소개 👩
#### 김수빈 
<img src="https://user-images.githubusercontent.com/66404477/229358314-5537125b-0a28-4ba3-9f79-64f01f4c65a5.png" width="100"/>

[subeen's Github](https://github.com/soosbk)
~~~
👩‍🎓 Student ID : ****2218
📧 E-mail: sb121300@naver.com
📌 Role: 팀장, ML(얼굴형 분석 모델 생성), Backend(얼굴형 분석 페이지, user, 마이페이지, 회원가입/로그인), Release(배포)
~~~
<br>

#### 김시은
<img src="https://user-images.githubusercontent.com/66404477/229358307-fa2fce06-7696-4495-bca7-0397fa9d6c29.png" width="100"/>

[sieun's Github](https://github.com/se0983)

~~~
👩‍🎓 Student ID : ****2219
📧 E-mail: se098300@gmail.com
📌 Role: Data(데이터 수집, 이미지 전처리 및 DB 구축), Backend (안경 가상 피팅, 상품 리스트 및 상세 페이지)
~~~
<br>

#### 김소은
<img src="https://user-images.githubusercontent.com/66404477/229358312-ac729795-7298-42e7-a7bc-81581f9ed242.png" width="100"/>

[soeun's Github](https://github.com/silver0108)

~~~
👩‍🎓 Student ID : ****2217
📧 E-mail: kimsoeun0108@gmail.com
📌 Role: Frontend(클라이언트 개발, 레이아웃 설계, UI/UX 디자인)
~~~

<br><br>



## 4. 소개 영상 🎥

[소개 영상](https://youtu.be/aLYHJLLP1NU) <br>
[시연 영상](https://youtu.be/NodPse4up2s)

<br><br>



## 5. 프로젝트 구조 🗂️
<img src="https://github.com/kookmin-sw/capstone-2023-31/assets/63188042/1b8d42c6-7b4e-45b4-a408-def9f915b8e0" width="800"/>

<br><br>



## 6. 기술 스택 📊

#### ML
* <p float="left">
  <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
  <img src="https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white">
  <img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white">
  <img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
</p>

#### Data
* <p float="left">
  <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/dlib-008000?style=for-the-badge&logo=dlib&logoColor=white"/>
  <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"/>
</p>

#### Frontend
* <p float="left">
  <img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB">
  <img src="https://img.shields.io/badge/reactrouter-CA4245?style=for-the-badge&logo=reactrouter&logoColor=%2361DAFB">
  <img src="https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white">
  <img src="https://img.shields.io/badge/axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white" />
  <img src="https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white" />
</p>

#### Backend
* <p float="left">
  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</p>

#### Collaboration

* <p float="left">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/>
  <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white" /> 
  <img src="https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white" /> 
  <img src="https://img.shields.io/badge/vscode_liveshare-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" /> 
</p>



<br/><br/>



## 7. 사용법 🕹️
추가 예정.

<br/><br/>



## 8. Document 📑
[최종 포스터](https://github.com/kookmin-sw/capstone-2023-31/files/11550511/31_._.pdf) <br>
최종발표자료 <br>
수행결과보고서

