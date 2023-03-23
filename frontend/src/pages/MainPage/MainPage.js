import React from "react";
import { useNavigate} from "react-router-dom";
import { Button} from 'antd';
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import "./MainPage.css"

function MainPage() {

  const navigate = useNavigate()

  return (
    <div className="container">
      <Header/>
      <div className="middle">
        <Button id="name" className="btn" type="primary" onClick={() => {
          navigate("/searchname")
        }}>
          음식 또는 상품명으로 검색하기
        </Button>
        <Button id="barcode" className="btn" onClick={() => {
          navigate("/searchbarcode")
        }}>
          바코드로 검색하기
        </Button>
      </div>

      <Footer name="main"/>
      
    </div>
  )
}

export default MainPage;