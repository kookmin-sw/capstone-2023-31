import { Button } from "antd";
import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import './FaceAnalyze.css'
import { ResponsiveContainer, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';
import { Link, useLocation, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import ModalComponent from "../../components/Modal/ModalComponent";
import { useLocation, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";

function FaceAnalyze() {
  const navigate = useNavigate();
  const location = useLocation();
  const predictedShape = location.state; // backend에서 전달받음

  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const checkLoginStatus = async () => { //실시간으로 로그인했는지 확인
    try {
      const response = await axios.get('/user/check-login/');
      setIsLoggedIn(response.data.isLoggedIn);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    checkLoginStatus();
  }, []);

  const updateFaceShape = (shape) => {
    // 로그인된 사용자의 경우에만 예측된 얼굴 형태를 저장
    if (isLoggedIn) {
      axios.get('/user/get-csrf-token/') // Get CSRF token from the server
        .then(response => {
          const csrfToken = response.data.csrfToken;

          axios.post('/analyze/save-face-shape/', 
            { face_shape:predictedShape, 
            }, {
            headers: {
              'X-CSRFToken': csrfToken
            }
          })
            .then(response => {
              if (response.data.success) {
                alert(response.data.message);
              } else {
                alert('Error');
              }
            })
            .catch(error => {
              console.error(error);
            });
        })
        .catch(error => {
          console.error(error);
        });
      
    } else {
      alert('로그인이 필요합니다.');
      navigate('/user/login');
    }
  };

  const [updatedData, setUpdatedData] = useState(data);

  useEffect(() => {
    if (predictedShape) {
      const updatedDataCopy = [...updatedData];
      const targetIndex = updatedDataCopy.findIndex((obj) => obj.category === predictedShape);
      if (targetIndex !== -1) {
        updatedDataCopy[targetIndex].value = 100;
        setUpdatedData(updatedDataCopy);
      }
    } else {
      alert("얼굴형을 분석할 수 없습니다. 다시 사진을 찍어주세요.")
      navigate('/analyze/camera');
    }
  }, [predictedShape]);

  return (
    <>
    { predictedShape == null  ? (
      null
    ) : (
      <div className="container">
      <Header />
      <div className="face-analyze-container">
        <div style={{ fontSize: "20px", fontWeight: "bold", marginTop: "20px" }}>{updatedData.find((obj) => obj.category === predictedShape)?.categoryName} 얼굴</div>
        <div className="chart-wrapper">
          <RadarChart cx={200} cy={200} outerRadius={120} width={400} height={400} data={updatedData}>
            <PolarGrid />
            <PolarAngleAxis dataKey="categoryName" />
            <Radar dataKey="value" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
          </RadarChart>
        </div>
      </div>
      <div style={{ fontSize: "20px", fontWeight: "bold", margin: "0 300px" }}>얼굴형 분석 결과</div>
      <div className="face-text">
        얼굴 비율이 OO한 편이에요.
      </div>
      {isLoggedIn ? (
        <button
          style={{ margin: "15px 300px" }}
          type="primary"
          onClick={() => updateFaceShape(predictedShape)}
        >
          얼굴형 정보 업데이트하기
        </button>
      ) : (
          <div>로그인 후 얼굴형 정보를 저장할 수 있습니다.</div>
        )}
      <div style={{ fontSize: "20px", fontWeight: "bold", margin: "0 300px" }}>추천 프레임</div>
      <div className="face-text">
        OOO 프레임 추천!
      </div>
      <Button style={{ margin: "15px 300px" }} size="large" type="primary" onClick={() => navigate(`/list/round`)}>추천 안경테 적용해보기</Button>
      <Footer />
    </div>
    )}
    </>
  )
}

export default FaceAnalyze;