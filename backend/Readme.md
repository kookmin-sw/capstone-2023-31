# 환경 설정과 관련된 폴더입니다. 
## 깃 원격저장소
1. 가상환경을 생성합니다.
2. 원격 저장소를 clone 받습니다.

## Docker file 실행
1. docker-compose up <br>
동시에 터미널을 한개 더 켜서 frontend 폴더로 이동합니다. 
2. npm install 
3. npm start
frontend를 실행시키면 docker에서 신호를 잡아, 실행됩니다. 첫 실행 시, 큰 시간이 걸립니다. 


#### 도커 파일이 실행되지 않은 경우 다음과 같은 과정을 따라주세요:)
## requirements.txt (capstone-2023-31 에 존재)
1. pip install --upgrade pip
2. pip install -r requirements.txt
  <br> 실행
  
## dlib설치방법
1.http://dlib.net/ 링크로 접속합니다.
<br/><br/>
2. <img width="139" alt="스크린샷 2023-05-24 오전 1 34 26" src="https://github.com/kookmin-sw/capstone-2023-31/assets/66404477/e1df570e-b541-46ff-af9f-3b4b8dedcca8"><br>
파일을 다운 받습니다.<br/><br/>
3. 압축을 해제하고, 레포지토리로 dlib 폴더를 이동합니다.<br>
4. build 폴더와 source 폴더를 생성하고
모든 파일을 source 폴더로 이동시킵니다. <br>
<img width="357" alt="스크린샷 2023-05-24 오전 1 41 16" src="https://github.com/kookmin-sw/capstone-2023-31/assets/66404477/213075dc-9310-483a-a895-942b1cc7250d"> <br> -> <br>
<img width="770" alt="스크린샷 2023-05-24 오전 1 36 22" src="https://github.com/kookmin-sw/capstone-2023-31/assets/66404477/f1a1bb36-90b6-488e-b8e8-cd48319138f8">
<br><br/>
5. cd source<br/><br/>
6. python setup.py build<br/><br/>
7. python setup.py install<br/><br/>
<확인 방법><br>
1. python 접속<br/>
2. import dlib<br/>
print(dlib.__version__)  -> 잘 나오면 설치 완료


## tensorflow

  pip install tensorflow

### front-end
1. frontend 폴더로 이동한다.  <br>
2. npm install <br>
3. npm start <br>

### back-end
1. cd backend/eyeglassy <br>
2. python csv_to_db.py (실행) <br>
3. python manage.py migrate <br>
4. python manage.py runserver
  
