import React, { Fragment, useEffect, useState } from "react";
import { useLocation, useParams, Link } from "react-router-dom";
import Header from "../../components/Header/Header"
import "./ListPage.css"
import Footer from "../../components/Footer/Footer";
import {Row, Col, Pagination} from "antd";
import Paginator from "../../components/Paginator/Paginator";
import SearchBar from "../../components/Search/SearchBar";
import axios from "axios";
function ListPage() {

  useEffect(()=>{ // 페이지 이동 시 스크롤 위치 초기화
    window.scrollTo(0, 0);
  }, [])

  // const { style } = useParams();
  const location = useLocation();
  const { name , shape} = location.state;
  const [glassesData, setGlassesData] = useState([]);

  useEffect(()=>{
      axios.get(`/product/${shape}?shape=${shape}`)
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error);
        })
      // setGlassesData(glasses.data);
    
    // fetchGlassesData();
  }, [shape]);

  // console.log(glassesData);

  const gridData = [
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

  const [currentPage, setCurrentPage] = useState(1);
  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  return(
    <div className="container">
      <Header/>
      <div className="list-container">
        <div className="style-name">{name}</div>
        <SearchBar/>
        <div className="list-glasses">
            <Row gutter={[8,8]}>
              {gridData.map((item, index) => (
                  <Col key={index} lg={6} md={8} sm={12} xs={24}
                    style={{display:"flex", flexDirection:"column", alignItems:"center", marginBottom:"3rem"}}
                    >
                    <Link 
                      className="link" 
                      to={`/product/${item.id}`}
                      state={item}
                      >
                    <div style={{display: "flex", flexDirection:"column"}}>
                        <img 
                          style={{ width:'250px', height:"160px"}}
                          src={item.image}
                          >
                        </img>
                        <div>
                          <div>{item.brandName}</div>
                          <div>{item.name}</div>
                          <div>{item.price}원</div>
                        </div>
                    </div>
                    </Link>
                    
                  </Col>

            ))}
            </Row>
            
      
        </div>
      </div>
      {/* <Paginator/> */}
      <div style={{display:"flex", justifyContent:"center"}}>
      <Pagination current={currentPage} total={50} onChange={handlePageChange}/>
      </div>
      <Footer/>
    </div>
    
  )
}

export default ListPage;