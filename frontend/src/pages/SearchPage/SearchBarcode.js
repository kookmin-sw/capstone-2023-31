import React, { useEffect, useRef, useState } from "react";
import { useNavigate} from "react-router-dom";
import Quagga from "quagga";
import Webcam from "react-webcam";
import './SearchBarcode.css'

function SearchBarcode(){

  const navigate = useNavigate()
  const [data2, setdata2] = useState("")

  useEffect(() => {
    Quagga.init({
      inputStream: {
        name: "Live",
        type: "LiveStream",
        target: document.querySelector("#camera"),
        constranits: {
          facingMode: "environment"
        }
    },
    decoder: {
      readers: ["ean_reader"],
    },
  }, function(err) {
      if (err) {
          console.log(err);
          return
      }
      console.log("Initialization finished. Ready to start");
      Quagga.start();
  });

  Quagga.onDetected((data) => {
    console.log(data.codeResult.code)
    Quagga.stop();
    navigate('/detail', {state: {value: data.codeResult.code}})
  })
}, []);

const videoConstraints = {
   facingMode: "environment",
};

const webcamRef = useRef(null)

const onUserMedia = (e) => {
   console.log(e);
}
  return(
    <div>
      {/* <video id="camera" /> */}
      <Webcam
        id="camera"
        className="barcode"
        ref={webcamRef}
        screenshotFormat="image/png"
        videoConstraints={videoConstraints}
        onUserMedia={onUserMedia}
        screenshotQuality={1}
       />
    </div>
  )
}


export default SearchBarcode;