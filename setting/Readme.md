# 환경 설정과 관련된 폴더입니다. 

## dlib설치방법
1.http://dlib.net/ 링크로 접속합니다.
<br/><br/>
2. <img width="139" alt="스크린샷 2023-05-24 오전 1 34 26" src="https://github.com/kookmin-sw/capstone-2023-31/assets/66404477/e1df570e-b541-46ff-af9f-3b4b8dedcca8"><br>
파일을 다운 받습니다.<br/><br/>
3. 압축을 해제하고, build 폴더와 source 폴더를 생성하고
모든 파일을 source 폴더로 이동시킵니다. <br>
<img width="357" alt="스크린샷 2023-05-24 오전 1 41 16" src="https://github.com/kookmin-sw/capstone-2023-31/assets/66404477/213075dc-9310-483a-a895-942b1cc7250d"> <br> -> <br>
<img width="770" alt="스크린샷 2023-05-24 오전 1 36 22" src="https://github.com/kookmin-sw/capstone-2023-31/assets/66404477/f1a1bb36-90b6-488e-b8e8-cd48319138f8">
<br><br/>
4. cd source<br/><br/>
5. python setup.py build<br/><br/>
6. python setup.py install<br/><br/>
<확인 방법><br>
1. python 접속<br/>
2. import dlib<br/>
print(dlib.__version__)  -> 잘 나오면 설치 완료


## tensorflow

  pip install tensorflow
  
  
