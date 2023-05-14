import React, { useEffect, useRef, useState, useCallback } from "react";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import { Button, Spin } from "antd";
import "./Camera.css";
import Webcam from 'react-webcam';
import { useNavigate } from "react-router-dom";
import { Audio } from "react-loader-spinner";
import { SketchOutlined } from "@ant-design/icons";

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
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const capture = useCallback(
    () => {
      const capturedImageSrc = webcamRef.current.getScreenshot();
      setImageSrc(capturedImageSrc);
    },
    [webcamRef]
  );

  const analyzeFace = async () => {
    if (!imageSrc) {
      console.error("No image to analyze");
      return;
    }

    setIsAnalyzing(true);

    const formData = new FormData();
    formData.set('image', dataURItoBlob(imageSrc));

    try {
      const csrfResponse = await fetch('/analyze/get-csrf-token/');
      const csrfData = await csrfResponse.json();
      const csrfToken = csrfData.csrfToken;
  
      const analyzeResponse = await fetch('/analyze/analyze-face/', {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': csrfToken
        }
      });
  
      const analyzeData = await analyzeResponse.json();
      setIsAnalyzing(false);
      navigate('/analyze/result', { state: analyzeData.predicted_shape });
    } catch (error) {
      console.error(error);
      setIsAnalyzing(false);
    }
  }

  
  const txt = "분석 중 입니다...";
  const [text, setText] = useState('');
  const [count, setCount] = useState(0);

  useEffect(()=>{
    const interval = setInterval(() => {
      setText((prevText) => {
        let resultText = prevText ? prevText + txt[count] : txt[0];
        if(count >= txt.length){
          setCount(0);
          setText('');
        } else{
          setCount(count+1);
        }
        return resultText;
      });
    }, 150);
    return () => clearInterval(interval);
  })


  return (
    <div className="container">
      <Header />
      {isAnalyzing ? (
        <div className="loading-container">
          <Audio color="gray" heigth={500} width={500} duration={3}/>
          <h2>{text}</h2>
        </div>
      ):(
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
                width={1000}
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
      )}
      
      <Footer />
    </div>
  );
}

export default AnalyzeCamera;
