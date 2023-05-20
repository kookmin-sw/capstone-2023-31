import React, { useEffect, useRef, useState } from "react";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import { Button } from "antd";
import "./Camera.css";
import Webcam from 'react-webcam';
import { useLocation, useNavigate } from "react-router-dom";
import axios from 'axios';

const videoConstraints = {
  width: 1280,
  height: 720,
  facingMode: "user"
};

function FittingCamera() {
  const navigate = useNavigate();
  const location = useLocation();
  const glassesImg = location.state.image;
  const glassesId = location.state.id;

  useEffect(() => {
    console.log(glassesImg);
    console.log(typeof glassesId);
  }, []);

  const webcamRef = useRef(null);
  const [imageSrc, setImageSrc] = useState(null);
  const [mirror, setMirror] = useState(false);
  const [isCapturing, setIsCapturing] = useState(false);

  const alertHandler = () => {
    alert("다시 찍어주세요");
  }

  const dataURItoBlob = (dataURI) => {
    const byteString = atob(dataURI.split(',')[1]);
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    const blob = new Blob([ab], { type: 'image/jpeg' });
    return blob;
  }

  const capture = async () => {

    setIsCapturing(true);

    const capturedImageSrc = webcamRef.current.getScreenshot();

    const formData = new FormData();
    const blob = dataURItoBlob(capturedImageSrc);
    formData.append('image', blob, 'captured_image.jpg');

    try {
      const csrfResponse = await fetch('/fitting/get-csrf-token/');
      const csrfData = await csrfResponse.json();
      const csrfToken = csrfData.csrfToken;

      const fittingResponse = await axios.post(`/fitting/camera/${glassesId}/?id=${glassesId}`, formData, {
        headers: {
          'X-CSRFToken': csrfToken
        }
      });

      if(fittingResponse.data.fitted_face == "Not detected"){
        alert("얼굴을 인식할 수 없습니다. 사진을 다시 찍어주세요.")
      }else{
        const base64Data = fittingResponse.data;
        setImageSrc(`data:image/jpeg;base64,${base64Data}`);
        setIsCapturing(false);
      }

    } catch (error) {
      console.log(error);
    }
  };

  const txt = "가상 피팅 중 입니다...";
  const [text, setText] = useState('');
  const [count, setCount] = useState(0);

  useEffect(()=>{
    const interval = setInterval(() => {
      setText((prevText) => {
        let resultText = prevText ? prevText + txt[count] : txt[0];
        if(count >= txt.length-1){
          setCount(0);
          setText('');
        } else{
          setCount((prvcount) => prvcount + 1);
        }
        return resultText;
      });
    }, 150);
    return () => clearInterval(interval);
  })

  return (
    <div className="container">
      <Header />
      <div className="webcam-container">
        <Webcam
          className="webcam"
          audio={false}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={1000}
          videoConstraints={videoConstraints}
          mirrored={mirror}
        />
        <div style={{ marginTop: "20px" }}>
          <Button
            size="large"
            shape="round"
            onClick={() => setMirror(!mirror)}
            style={{
              margin: "0 10px"
            }}
          >
            좌우 반전
          </Button>
          {imageSrc ? (
            <Button
              size="large"
              shape="round"
              onClick={() => setImageSrc(null)}
              style={{
                margin: "0 10px"
              }}
            >
              다시 찍기
            </Button>
          ) : (
              <Button
                size="large"
                shape="round"
                onClick={capture}
                style={{
                  margin: "0 10px"
                }}
              >
                사진 찍기
              </Button>
            )}
        </div>
        <div className="captured-image-container">
          {isCapturing ? (
            <>
            <h3 style={{color: "black", textShadow: "-1px 0px rgb(172, 174, 174), 0px 1px rgb(172, 174, 174), 1px 0px rgb(172, 174, 174), 0px -1px rgb(172, 174, 174)"}}>{text}</h3>
            </>
          ):(
            <>
            {imageSrc ? (
              <div className="captured-image">
                <img src={imageSrc} alt="Captured" />
              </div>
            ) : (
              <div className="captured-image">
                <div onChange={alertHandler}></div>
              </div>
            )}
            </>
          )}
          
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default FittingCamera;
