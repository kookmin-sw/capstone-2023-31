import React, { useEffect, useRef, useState, useCallback } from "react";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import { Button } from "antd";
import "./Camera.css"
import Webcam from 'react-webcam';
import { useNavigate } from "react-router-dom";
import axios from 'axios'

const videoConstraints = {
  width: 1280,
  height: 720,
  facingMode: "user"
};

function FittingCamera(){
  const navigate = useNavigate('');
  
  const webcamRef = useRef(null);
  const [imageSrc, setImageSrc] = useState(null);
  const [sfile, setFile] = useState(null);
  // useEffect(() => {
  //   const interval = setInterval(() => {
  //     capture();
  //   }, 100);

  //   return () => clearInterval(interval);
  // }, []);

  const capture = useCallback(
    () => {
      const capturedImageSrc = webcamRef.current.getScreenshot();
      // const byteString = atob(capturedImageSrc.split(',')[1]);
      // const ab = new ArrayBuffer(byteString.length);
      // const ia = new Uint8Array(ab);
      // for (let i = 0; i < byteString.length; i++) {
      //   ia[i] = byteString.charCodeAt(i);
      // }
      // const blob = new Blob([ab], { type: 'image/jpeg' });
      // const file = new File([blob], 'captured_image.jpg', { type: 'image/jpeg' });
      // const imageUrl = URL.createObjectURL(blob);
      // console.log(`ㅎㅇㅎㅇㅎㅇㅎ${file.name}`);
      // console.log(imageUrl);
      // setImageSrc(imageUrl);
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
          {imageSrc && (
          <div>
            <h2>Captured Image:</h2>
            <img src={imageSrc} alt="Captured" />
            <div>{sfile}</div>
          </div>
          )}
        </div>
        <Footer/>
    </div>

  )
}


export default FittingCamera;