import { Button } from "antd";
import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import './FaceAnalyze.css'
import { ResponsiveContainer, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';
import { Link, useLocation, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import ModalComponent from "../../components/Modal/ModalComponent";
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
  const data = [
    { category: 'Heart', categoryName: "하트형", value: 25, shape: 'wellington', shapeName: "웰링턴" },    //하트형
    { category: 'Oblong', categoryName: "긴얼굴형", value: 25, shape: 'oval', shapeName: "타원형" }, //긴얼굴형
    { category: 'Oval', categoryName: "타원형", value: 25, shape: 'half', shapeName: "하금테"  },     //타원형
    { category: 'Round', categoryName: "둥근형", value: 25, shape: 'square', shapeName: "사각형"  },    //둥근형
    { category: 'Square', categoryName: "사각형", value: 25, shape: 'round', shapeName: "둥근형"  },   //사각형
  ];

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

  const matchingItem = data.find(item => item.category === predictedShape);

  return (
    <>
    { predictedShape == null  ? (
      null
    ) : (
      <div className="container">
      <Header />
      <div className="face-analyze-container">
        <div style={{ fontSize: "20px", fontWeight: "bold", marginTop: "20px", textAlign: "center" }}>{matchingItem.categoryName} 얼굴</div>
        <div className="chart-wrapper">
          <RadarChart cx={200} cy={200} outerRadius={120} width={400} height={400} data={updatedData}>
            <PolarGrid />
            <PolarAngleAxis dataKey="categoryName" />
            <Radar dataKey="value" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
          </RadarChart>
        </div>
        {isLoggedIn ? (
        <Button
          style={{ margin: "15px 300px" }}
          type="primary"
          onClick={() => updateFaceShape(predictedShape)}
        >
          얼굴형 정보 업데이트하기
        </Button>
      ) : (
          <p style={{ fontSize: "18px", fontWeight: "bold" , textAlign:"center"}}>로그인 후 얼굴형 정보를 저장할 수 있습니다.</p>
        )}
      <div style={{ marginTop: "10px", fontSize: "20px", fontWeight: "bold"}}>추천 프레임</div>
      <div className="face-text">{matchingItem.shapeName} 프레임 추천!
      </div>
      <Button 
        style={{margin: "10px 0"}} size="large" type="primary" 
        onClick={() => navigate(`/product/${matchingItem.shape}`, {state:{name: `${matchingItem.shapeName}`, shape: `${matchingItem.shape}`}})}>추천 안경테 적용해보기</Button>
      </div>
      <Footer />
    </div>
    )}
    </>
  )
}

export default FaceAnalyze;