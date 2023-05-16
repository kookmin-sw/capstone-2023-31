import { useLocation, useNavigate, useParams } from "react-router-dom";
import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import "./Detail.css"
import { Button } from "antd";
import { HeartOutlined, HeartFilled } from '@ant-design/icons';
import { useDispatch, useSelector } from 'react-redux';
import { addWishList, deleteWishList } from "../../_actions";
import { useEffect, useState } from "react";

function Detail(){
  // let { id } = useParams();
  const navigate = useNavigate();
  const location = useLocation();
  const data = location.state;

  // console.log(data);

  const dispatch = useDispatch();
  const wishList = useSelector(state => state.wishReducer || []);
  // console.log(wishList)
  const [isWish, setIsWish] = useState(false);

  useEffect(() => {
    const isProductInWishList = wishList.some(
      (product) => product.id === data.id
    );

    // console.log(isProductInWishList)
    setIsWish(isProductInWishList);
  }, [data.id]);


  const handleAddToWishlist = () => {
    setIsWish(true);
    dispatch(addWishList(data));
    // console.log("상품 찜")
  }

  const handleDeleteToWishlist = () => {
    setIsWish(false);
    dispatch(deleteWishList(data));
    // console.log("상품 삭제");
  }


  return(
    <div className="container">
      <Header/>
      <div className="detail-container">
        <div style={{display: "flex", flexDirection:"column"}}>
          <img 
            style={{ width:'800px', height: "auto"}}
            src={`/images/input/${data.image}`}
            >
          </img>
          <div style={{marginTop: "20px"}}>
            <div>{data.brand}브랜드</div>
            <div style={{fontSize:"30px"}}>{data.name} 안경</div>
            { data.cost == "문의" ? (
                <div style={{fontSize:"30px", float:"right"}}>{data.cost}</div>
              ) : (
                <div style={{fontSize:"30px", float:"right"}}>{data.cost}원</div>
              )}
          </div>
          <div style={{display:"flex", marginTop: "20px"}}>
            {isWish ? (
              <Button size="large" style={{ color: "red"}} onClick={handleDeleteToWishlist}><HeartFilled /></Button>
            ): (
              <Button size="large" style={{ color: "red"}} onClick={handleAddToWishlist}><HeartOutlined /></Button>
            )}
            <Button style={{flex:1}} size="large" onClick={()=>navigate(`/fitting/camera/${data.id}`, {state: data})}>가상 피팅하러 가기</Button>
          </div>
          <Button type="primary" size="large" style={{marginTop: "10px"}}>구매하기</Button>
      </div>
        </div>
      <Footer/>
    </div>
  );
}
export default Detail;