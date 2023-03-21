import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar



def scan_test_main(request):
    return render(request, 'main.html')


def get_barcode_img(request):
    return render(request, 'scan_main.html')


def barcode_scan(request):
    cap = cv2.VideoCapture(0)  # 비디오 캡처 객체 생성
    cap.set(3, 640)
    cap.set(4, 480)

    detected = True
    while detected:
        # 비디오에서 프레임 읽기
        ret, frame = cap.read()

        # 프레임에서 바코드 인식
        decodedObjects = pyzbar.decode(frame)

        # 바코드가 인식된 경우
        if len(decodedObjects) > 0:
            for obj in decodedObjects:
                # 바코드 텍스트 가져오기
                barcode_text = obj.data.decode("utf-8")

                detected = False

        # 프레임 표시
        cv2.imshow("Barcode Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 종료
    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'scan_complete.html', {'barcode_text': barcode_text})


def barcode_to_food(request):
    test_barcode = '8801047284482'


def get_food_api(request):  # 제품 db 가져오기
    url = 'http://openapi.foodsafetykorea.go.kr/api/aee1cfc463594b10a12b/C002/xml/1/1/MAKER_NAME=오뚜기'

    response = requests.get(url)
    contents = response.text

    pp = pprint.PrettyPrinter(indent=4)
    print(pp.pprint(contents))
