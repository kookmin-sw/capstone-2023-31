import React, { Fragment } from "react";
import { useNavigate, Link} from "react-router-dom";
import { Input, Row, Col, Button } from 'antd';
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import GridCard from "../../components/GridCard/GridCard";
import "./MainPage.css"
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import SearchBar from "../../components/Search/SearchBar";
function MainPage() {

  const navigate = useNavigate();
  const { Search } = Input;
  const onSearch = (e) => {
    if (e == ''){
      alert("입력 필수")
    }else {
    navigate('/product', {state: {value: e}});
    }
  }

  const slideData = [
    { id: 1, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 2, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 3, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 4, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 5, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 6, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 7, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 8, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 9, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 10, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 11, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 12, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 13, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
    { id: 14, image: '/images/image1.png', brandName: "AAA", name: "BBB", price: "30,000"},
  ];

  const gridData = [
    { style: "round", stylename: "둥근형", image: '/images/image1.png'},
    { style: "square", stylename: "사각형", image: '/images/image1.png'},
    { style: "etc", stylename: "기타", image: '/images/image1.png'},
  ]

  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesPerRow: 4,
    // slidesToScroll: 4,
    slidesToShow: 1,
    rows: 2,
    arrows: false,
    
  };

  return (
    <div className="container">
      <Header/>
      <div className="content-container">
        <div className="content-info">
          <div className="info-text">
            가상 안경 피팅 서비스 !<br/><br/>
            얼굴형 분석으로 안경 추천까지<br/><br/>
            <Button type="primary" onClick={()=>navigate('/analyze/camera')}>얼굴형 분석하러 가기</Button>
          </div>
          <img className="wear-glass-image" alt="wear-glass" src="/images/frame1.png" />
        </div>
        <SearchBar/>
    

        <div className="random-glasses">
          <Slider {...settings}>
            {slideData.map((item) => (
              <div key={item.id}>
                <Link className="link" to="/product" state={item}>
                  <img style={{ width: "210px", height: "150px"}}src={item.image}></img>
                </Link>
              </div>
            )) }
          </Slider>
        </div>

        <div className="style-glasses">
          <div style={{fontSize:"20px", fontWeight:"bold"}}>스타일별 안경</div>
          <div>
            <Row gutter={[8, 8]} style={{ borderRadius: '50%'}}>
              {gridData.map((item, index) => (
                <GridCard key={index} image={item.image} name={item.stylename} st={item.style}></GridCard>
               ))}
            </Row>
            
          </div>
        </div>
      </div>
      <Footer/>
      
    </div>
  )
}

export default MainPage;