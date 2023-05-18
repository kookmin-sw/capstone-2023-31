  import React, { useEffect, useState } from "react";
  import { useNavigate, Link} from "react-router-dom";
  import { Row, Button } from 'antd';
  import Header from "../../components/Header/Header";
  import Footer from "../../components/Footer/Footer";
  import GridCard from "../../components/GridCard/GridCard";
  import "./MainPage.css"
  import Slider from "react-slick";
  import "slick-carousel/slick/slick.css";
  import "slick-carousel/slick/slick-theme.css";
  import axios from "axios";

  function MainPage() {
    const navigate = useNavigate();
    const [images, setImages] = useState([]);

    useEffect(()=>{ 
      const fetchData = async () => {
        try {
          axios.get('/ /')
          .then(response => {
      setImages(response.data.results);
      })
      .catch(error => {
        console.log(error);
      });
          }
          catch(error) {
            console.log(error);
          }
        };
        fetchData();
      }, []);

    const gridData = [
      { style: "round", stylename: "둥근형", image: '/images/round.jpg'},
      { style: "square", stylename: "사각형", image: '/images/square.jpg'},
      { style: "oval", stylename: "타원형", image: '/images/oval.jpg'},
      { style: "half", stylename: "하금테", image: '/images/half.jpg'},
      { style: "wellington", stylename: "웰링턴", image: '/images/wellington.jpg'},
    ]

    const settings = {
      dots: true,
      infinite: false,
      speed: 500,
      slidesPerRow: 4,
      slidesToScroll: 1,
      rows: 2,
      arrows: true,
      responsive: [
        {
          breakpoint: 1280,
          settings: {
            slidesToScroll: 1,
            slidesPerRow: 3,
          }
        },
        {
          breakpoint: 980,
          settings: {
            slidesToScroll: 1,
            slidesPerRow: 2,
          }
        },
        {
          breakpoint: 650,
          settings: {
            slidesToScroll: 1,
            slidesPerRow: 1,
          }
        },
      ]
    };

    return (
      <div className="container">
        <Header/>
        <div className="content-container">
          <div className="content-info">
            <div className="info-text">
              가상 안경 피팅 서비스 !<br/><br/>
              얼굴형 분석으로 안경 추천까지<br/><br/>
              <Button type="primary" size="large" onClick={()=>navigate('/analyze/camera')}>얼굴형 분석하러 가기</Button>
            </div>
            <img className="wear-glass-image" alt="wear-glass" src="/images/frame1.png" />
          </div>
          <div className="random-glasses">
            <div className="style-glasses">
            <div style={{ fontSize: "20px", fontWeight: "bold" }}>이런 안경도 있어요!</div>
            </div>
            <Slider {...settings}>
              {images.map((item, index) => (
                <div key={index}>
                  <Link className="link" to={`/product/${item.shape}/${item.id}`} state={item}>
                    <img style={{ width: "250px", height: "250px"}} src={`/images/input/${item.image}`}></img>
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
                  <GridCard key={index} image={item.image} name={item.stylename} shape={item.style}></GridCard>
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