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
  const [mirror, setMirror] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      capture();
    }, 100);

    return () => clearInterval(interval);
  }, []);

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

      const formData = new FormData();
      const blob = dataURItoBlob(capturedImageSrc);
      formData.append('image', blob, 'captured_image.jpg');

      console.log(blob);
      console.log(formData);


    },
    [webcamRef]
  );


  
  
  
  
    return(
    <div className="container">
        <Header/>
        <div className="webcam-container">
          <Webcam
            className="webcam"
            audio={false}
            // height={600}
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            width={1000}
            videoConstraints={videoConstraints}
            mirrored={mirror}
          />
          <Button 
            size="large"
            shape="round" 
            onClick={()=>setMirror(!mirror)}
            style={{
               marginTop: "20px"
            }}
          >좌우 반전</Button>
         <div className="captured-image-container">
          {imageSrc && (
          <div className="captured-image">
            <img src={imageSrc} alt="Captured" />
            <div>사진 찍히고 있는 중</div>
          </div>
          )}
          </div>
        </div>
        <Footer/>
    </div>

  )
}


export default FittingCamera;