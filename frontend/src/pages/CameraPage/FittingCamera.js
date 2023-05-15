import React, { useEffect, useRef, useState, useCallback } from "react";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import { Button } from "antd";
import "./Camera.css"
import Webcam from 'react-webcam';
import { useLocation, useNavigate } from "react-router-dom";
import axios from 'axios'

const videoConstraints = {
  width: 1280,
  height: 720,
  facingMode: "user"
};

function FittingCamera(){
  const navigate = useNavigate('');
  const location = useLocation();
  const glassesImg = location.state.image;

  useEffect(()=>{
    console.log(glassesImg)
  }, [])
  
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

  const capture = async () => {
      const capturedImageSrc = webcamRef.current.getScreenshot();
      setImageSrc(capturedImageSrc);


      // 통신하는 코드 !!! 잠깐 주석 처리

      // const formData = new FormData();
      // const blob = dataURItoBlob(capturedImageSrc);
      // formData.append('image', blob, 'captured_image.jpg');
      // formData.append('glassesImg', glassesImg)

      // try {
      //   const csrfResponse = await fetch('/fitting/get-csrf-token/');
      //   const csrfData = await csrfResponse.json();
      //   const csrfToken = csrfData.csrfToken;
    
      //   const fittingResponse = await axios.post('/fitting/fitting-face/', formData, {
      //     headers: {
      //       'X-CSRFToken': csrfToken,
      //       // 'Content-Type': 'multipart/form-data'
      //     }
      //   });
        
      //   const { data } = fittingResponse;
      //   const imageUrl = URL.createObjectURL(data);
      //   setImageSrc(imageUrl);
  
      // } catch (error) {
      //   console.log(error)
      // }
    };
  
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