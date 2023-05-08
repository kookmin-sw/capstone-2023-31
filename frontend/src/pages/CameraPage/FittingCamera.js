import React, { useEffect, useRef, useState, useCallback } from "react";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import { Button } from "antd";
import "./Camera.css"
import Webcam from 'react-webcam';
import { useNavigate } from "react-router-dom";

const videoConstraints = {
  width: 1280,
  height: 720,
  facingMode: "user"
};

function FittingCamera(){
  const navigate = useNavigate('');

  const webcamRef = useRef(null);
  const [imageSrc, setImageSrc] = useState(null);

  const capture = useCallback(
    () => {
      const capturedImageSrc = webcamRef.current.getScreenshot();
      setImageSrc(capturedImageSrc);
    },
    [webcamRef]
  );

  return(
    
    <div className="container">
        <Header/>
        {/* <WebCam
          audio={false}
          // video={true}
          mirrored={true}
          // style={{ width: '80%', height: '50%' }}
        /> */}
        {/* <div className="camera-container"> */}
            
        <div className="webcam-container">
          <Webcam
            className="webcam"
            audio={false}
            // height={600}
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
          {imageSrc && (
          <div>
            <h2>Captured Image:</h2>
            <img src={imageSrc} alt="Captured" />
          </div>
          )}
        </div>
        <Footer/>
    </div>

  )
}


export default FittingCamera;