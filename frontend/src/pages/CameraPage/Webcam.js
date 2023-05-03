import React, { useEffect, useRef, useState } from "react";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import { Button } from "antd";
import "./Webcam.css"
import WebCam from 'react-webcam';
import { useNavigate } from "react-router-dom";
function Webcam(){
  // const navigate = useNavigate('');
  // const videoRef = useRef(null);

  // const [error, setError] = useState(null);

  // useEffect(() => {
  //   navigator.mediaDevices.getUserMedia({ video: true })
  //     .then(stream => {
  //       videoRef.current.srcObject = stream;
  //     })
  //     .catch(error => {
  //       setError(error);
  //     });
  // }, []);

  // if (error) {
  //   return <div>{error.message}</div>;
  // }

  // return (
  //   <>
  //     <div className="webcam-container">
  //       <video
  //         style={{
  //           position: 'absolute',
  //           top: 0,
  //           left: 0,
  //           width: '100%',
  //           height: '100%',
  //           objectFit: 'cover',
  //           transform: 'scaleX(-1)' // 좌우반전 설정
  //         }}
  //         ref={videoRef}
  //         autoPlay
  //         playsInline
  //         muted
  //       />
  //     </div>
  //     <div className="camera-container">
  //       <Header/>
  //       <Button className="face-btn" shape="round" onClick={()=> navigate('/analyze')}>얼굴형 분석</Button>
  //     </div>
    
    
  //   {/* <Footer name="camera"/> */}
  // </>
  // );

  // const webcamRef = useRef(null);

  // const videoConstraints = {
  //   width: 390,
  //   height: 640,
  //   aspectRatio: 9/22,
  // };

  // return (
  //   <div style={{
  //     display: "flex",
  //     height: "100%"
  //   }}>
  //     <WebCam
  //       audio={false}
  //       height={videoConstraints.height}
  //       width={videoConstraints.width}
  //       videoConstraints={videoConstraints}
  //       ref={webcamRef}
  //     />
  //   </div>
  // );






  const navigate = useNavigate('');
  return(
    
    <div >
        {/* <Header/> */}
        <WebCam
          audio={false}
          // video={true}
          style={{ width: '50%', height: '50%' }}
        />
        <div className="camera-container">
            
            <Button className="face-btn" shape="round" onClick={()=> navigate('/analyze')}>얼굴형 분석</Button>
        </div>
    </div>

  )
}


export default Webcam;