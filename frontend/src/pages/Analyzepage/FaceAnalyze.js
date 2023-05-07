import { Button } from "antd";
import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import './FaceAnalyze.css'
import { ResponsiveContainer, Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';
import { useNavigate } from "react-router-dom";

function FaceAnalyze(){
  const navigate = useNavigate('');
  const data = [
    { category: '하트형', value: 100 },
    { category: '직사각형', value: 25 },
    { category: '타원형', value: 25 },
    { category: '둥근형', value: 25 },
    { category: '사각형', value: 25 },
  ];

  const maxCategory = data.reduce((prev, current) => {
    return (prev.value > current.value) ? prev : current;
  }).category;

  return(
    <div className="container">
      <Header/>
      <div className="face-analyze-container">
        <div style={{ fontSize: "20px",fontWeight: "bold", marginTop: "20px"}}>{maxCategory} 얼굴</div>
        <div className="chart-wrapper">
          <RadarChart cx={200} cy={200} outerRadius={120} width={400} height={400} data={data}>
            <PolarGrid />
            <PolarAngleAxis dataKey="category"/>
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
      {/* <div style={{ display:"flex", flexDirection:"column", marginLeft: "30px", marginRight: "30px"}}> */}
      <Button style={{margin: "15px 30px"}} type="primary" onClick={()=>navigate('/camera')}>추천 안경테 적용해보기</Button>
      {/* </div> */}
      <Footer/>
    </div>
    
  )
}

export default FaceAnalyze;