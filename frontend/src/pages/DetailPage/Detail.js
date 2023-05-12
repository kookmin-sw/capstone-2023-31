import { useLocation, useNavigate } from "react-router-dom";
import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import "./Detail.css"
import { Button } from "antd";
function Detail(){
  const navigate = useNavigate();
  const data = useLocation();
  console.log(data.state);

  return(
    <div className="container">
      <Header/>
      <div className="detail-container">
        <div style={{display: "flex", flexDirection:"column"}}>
          <img 
            style={{ width:'800px', height: "auto"}}
            src={data.state.image}
            >
          </img>
          <div style={{marginTop: "20px"}}>
            <div>{data.state.brandName}브랜드</div>
            <div style={{fontSize:"30px"}}>{data.state.name} 안경</div>
            <div style={{fontSize:"30px", float:"right"}}>{data.state.price}원</div>
          </div>
          <div style={{display:"flex", marginTop: "20px"}}>
            <Button size="large">❤</Button>
            <Button style={{flex:1}} size="large" onClick={()=>navigate('/product/camera')}>가상 피팅하러 가기</Button>
          </div>
          <Button type="primary" size="large" style={{marginTop: "10px"}}>구매하기</Button>
      </div>
        </div>
      <Footer/>
    </div>
  );
}
export default Detail;