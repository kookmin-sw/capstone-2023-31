import { useLocation, useNavigate } from "react-router-dom";
import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import "./Detail.css"
import { Button } from "antd";
import { useDispatch } from 'react-redux';
import { addWishList } from "../../_actions";

function Detail(){
  const navigate = useNavigate();
  const location = useLocation();
  const data = location.state
  console.log(data);

  const dispatch = useDispatch();

  function handleAddToWishlist() {
    dispatch(addWishList(data));
    console.log("상품 찜")
  }

  return(
    <div className="container">
      <Header/>
      <div className="detail-container">
        <div style={{display: "flex", flexDirection:"column"}}>
          <img 
            style={{ width:'800px', height: "auto"}}
            src={data.image}
            >
          </img>
          <div style={{marginTop: "20px"}}>
            <div>{data.brandName}브랜드</div>
            <div style={{fontSize:"30px"}}>{data.name} 안경</div>
            <div style={{fontSize:"30px", float:"right"}}>{data.price}원</div>
          </div>
          <div style={{display:"flex", marginTop: "20px"}}>
            <Button size="large" onClick={handleAddToWishlist}>♥</Button>
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