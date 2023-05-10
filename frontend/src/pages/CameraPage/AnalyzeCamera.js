import React, { useEffect, useRef, useState, useCallback } from "react";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import { Button } from "antd";
import "./Camera.css";
import Webcam from 'react-webcam';
import { useNavigate } from "react-router-dom";

const videoConstraints = {
  width: 1280,
  height: 720,
  facingMode: "user"
};

function dataURItoBlob(dataURI) { // 이미지 처리
  const byteString = atob(dataURI.split(',')[1]);
  const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
  const ab = new ArrayBuffer(byteString.length);
  const ia = new Uint8Array(ab);
  for (let i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }
  return new Blob([ab], { type: mimeString });
}


function AnalyzeCamera() { //카메라
  const navigate = useNavigate();
  const webcamRef = useRef(null);
  const [imageSrc, setImageSrc] = useState(null);

  const capture = useCallback(
    () => {
      const capturedImageSrc = webcamRef.current.getScreenshot();
      setImageSrc(capturedImageSrc);
    },
    [webcamRef]
  );

  const analyzeFace = () => {
    if (!imageSrc) {
      console.error("No image to analyze");
      return;
    }

    const formData = new FormData();
    formData.set('image', dataURItoBlob(imageSrc));

    fetch('/analyze/get-csrf-token/') //django와 통신하기 위해 csrf-token 을 미리 교환한다. 
      .then(response => response.json())
      .then(data => {
        const csrfToken = data.csrfToken;
        // fetch 요청에 csrfToken 헤더 추가
        fetch('/analyze/analyze-face/', { //장고의 urls.py 와 일치하게 set
          method: 'POST',
          body: formData,
          headers: {
            'X-CSRFToken': csrfToken
          }
        })
          .then(response => response.json())
          .then(data => {
            navigate('/analyze/result', { state: data.predicted_shape });
          })
          .catch(error => {
            console.error(error);
          });
      })
      .catch(error => {
        console.error(error);
      });
  }


  return (
    <div className="container">
      <Header />
      <div className="webcam-container">
        {imageSrc ? (
          <div className="display-container">
            <img src={imageSrc} alt="Captured" style={{ marginTop: "20px" }} />
            <div style={{ marginTop: "20px" }}>
              <Button
                className="capture-btn"
                shape="round"
                onClick={() => setImageSrc(null)}
                style={{
                  margin: "0 10px"
                }}
              >다시 찍기</Button>
              <Button
                className="face-btn"
                shape="round"
                style={{ margin: "0 10px" }}
                onClick={analyzeFace}>얼굴형 분석</Button>
            </div>
          </div>
        ) : (
            <div className="webcam-container">
              <Webcam
                className="webcam"
                audio={false}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                width={750}
                videoConstraints={videoConstraints}
              />
              <Button
                className="capture-btn"
                shape="round"
                onClick={capture}
                style={{
                  marginTop: "20px"
                }}
              >사진 찍기</Button>
            </div>
          )}
      </div>
      <Footer />
    </div>
  );
}

export default AnalyzeCamera;
