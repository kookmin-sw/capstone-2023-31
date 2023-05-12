
import { Button } from "antd";
import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import './FaceAnalyze.css'
import { ResponsiveContainer, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';
import { Link, useLocation, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import ModalComponent from "../../components/Modal/ModalComponent";

function FaceAnalyze() {
  const navigate = useNavigate();
  const location = useLocation();
  const predictedShape = location.state; // backend에서 전달받음

  const [showAlert, setShowAlert] = useState(false);
  const data = [    
    { category: 'heart', categoryName: "하트형", value: 25 },    //하트형
    { category: 'oblong', categoryName: "긴얼굴형", value: 25 }, //긴얼굴형
    { category: 'oval', categoryName: "타원형", value: 25 },     //타원형
    { category: 'round', categoryName: "둥근형", value: 25 },    //둥근형
    { category: 'square', categoryName: "사각형", value: 25 },   //사각형
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
  
  const [isModalOpen, setIsModalOpen] = useState(false)
  
  
  const showModal = () => {
    setIsModalOpen(true);
  };
  const handleOk = () => {
    setIsModalOpen(false);
  };
  const handleCancel = () => {
    setIsModalOpen(false);
  };


  


  const maxCategory = data.reduce((prev, current) => {
    return (prev.value > current.value) ? prev : current;
  }).category;

  return(
    <>
    { predictedShape == null  ? (
      null
    ) : (
      <div className="container">
      <Header/>
      <div className="face-analyze-container">
        <div style={{ fontSize: "20px",fontWeight: "bold", marginTop: "20px"}}>{updatedData.find((obj) => obj.category === predictedShape)?.categoryName} 얼굴</div>
        <div className="chart-wrapper">
          <RadarChart cx={200} cy={200} outerRadius={120} width={400} height={400} data={updatedData}>
            <PolarGrid />
            <PolarAngleAxis dataKey="categoryName"/>
            <Radar dataKey="value" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
          </RadarChart>
        </div>
      </div>
      <div style={{ fontSize: "20px",fontWeight: "bold", margin: "0 30px"}}>얼굴형 분석 결과</div>
      <div className="face-text">
        얼굴 비율이 OO한 편이에요.
      </div>
      <div style={{ fontSize: "20px",fontWeight: "bold", margin: "0 30px"}}>추천 프레임</div>
      <div className="face-text">
        OOO 프레임 추천!
      </div>
      <Button style={{ margin: "15px 30px" }} type="primary" onClick={() => navigate(`/list/round`)}>추천 안경테 적용해보기</Button>
      <Footer />
    </div>
    )}
    </>
  )
}

export default FaceAnalyze;