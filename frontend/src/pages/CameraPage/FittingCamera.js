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

  const alertHandler = () => {
    alert("다시 찍어주세요");
  }

  const dataURItoBlob = (dataURI) => {
    const byteString = atob(dataURI.split(',')[1]);
    const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], { type: mimeString });
  }

  const capture = async () => {
    const capturedImageSrc = webcamRef.current.getScreenshot();

    const formData = new FormData();
    formData.set('image', dataURItoBlob(capturedImageSrc));

    try {
      const csrfResponse = await fetch('/fitting/get-csrf-token/');
      const csrfData = await csrfResponse.json();
      const csrfToken = csrfData.csrfToken;

      const fittingResponse = await axios.post(`/fitting/camera/${glassesId}/?id=${glassesId}`, formData, {
        headers: {
          'X-CSRFToken': csrfToken
        }
      });

      console.log(fittingResponse);
      const base64Data = fittingResponse.data;
      setImageSrc(`data:image/jpeg;base64,${base64Data}`);
    } catch (error) {
      console.log(error);
    }
  };

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
          {imageSrc ? (
            <div className="captured-image">
              <img src={imageSrc} alt="Captured" />
            </div>
          ) : (
              <div className="captured-image">
                <div onChange={alertHandler}></div>
              </div>
            )}
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default FittingCamera;
