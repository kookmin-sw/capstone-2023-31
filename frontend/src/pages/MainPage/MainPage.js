  import React, { Fragment, useEffect, useState } from "react";
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
  import axios from "axios";
  function MainPage() {

    const navigate = useNavigate();

    const [randomImages, setRandomImages] = useState([]);

    useEffect(()=>{ 
      const fetchData = async () => {
        try {
          axios.get('/ /')
          .then(response => {
            setRandomImages(response.data.results);
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
      { style: "round", stylename: "둥근형", image: '/images/glasses2.jpg'},
      { style: "square", stylename: "사각형", image: '/images/glasses3.jpg'},
      { style: "oval", stylename: "타원형", image: '/images/glasses4.jpg'},
      { style: "half", stylename: "하금테", image: '/images/glasses4.jpg'},
      { style: "wellington", stylename: "웰링턴", image: '/images/glasses4.jpg'},
    ]

    const settings = {
      dots: true,
      infinite: false,
      speed: 500,
      slidesPerRow: 4,
      slidesToScroll: 1,
      rows: 2,
      arrows: true,
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
          <SearchBar/>

          <div className="random-glasses">
            <Slider {...settings}>
              {randomImages.map((item, index) => (
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