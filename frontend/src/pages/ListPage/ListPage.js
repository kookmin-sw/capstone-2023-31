import React, { Fragment, useEffect, useState } from "react";
import { useLocation, useParams, Link } from "react-router-dom";
import Header from "../../components/Header/Header"
import "./ListPage.css"
import Footer from "../../components/Footer/Footer";
import {Row, Col, Pagination} from "antd";
import Paginator from "../../components/Paginator/Paginator";
import SearchBar from "../../components/Search/SearchBar";
import axios from "axios";
// import myImage from "../../../../crawling/image/input";
function ListPage() {

  // const { shape } = useParams();

  const location = useLocation();
  const { name , shape } = location.state;
  const [ glassesData, setGlassesData] = useState([]);
  const pageSize = 20;
  useEffect(()=>{ 
    const fetchData = async () => {
      try {
        const response = await axios.get(`/product/${shape}?shape=${shape}`);
        const data = response.data.glasses_shape;
        setGlassesData(data);
        }
        catch(error) {
          console.log(error);
        }
      };
      fetchData();
    }, [shape]);

  useEffect(()=>{ // 페이지 이동 시 스크롤 위치 초기화
    window.scrollTo(0, 0);
  }, [])

  const [page, setPage] = useState(1);

  const handlePageChange = (page) => {
    setPage(page);
  };

  return(
    <div className="container">
      <Header/>
      <div className="list-container">
        <div className="style-name">{name}</div>
        <SearchBar/>
        <div className="list-glasses">
            <Row gutter={[8,8]}>
              {glassesData.slice((page - 1) * pageSize, page * pageSize).map((item, index) => (
                  <Col key={index} lg={6} md={8} sm={12} xs={24}
                    style={{display:"flex", flexDirection:"column", alignItems:"center", marginBottom:"3rem"}}
                    >
                    <Link 
                      className="link" 
                      to={`/product/${shape}/${item.id}`}
                      state={item}
                      >
                    <div style={{display: "flex", flexDirection:"column"}}>
                        <img 
                          style={{ width:'250px', height:"160px"}}
                          src={`/images/input/${item.image}`}
                          >
                        </img>
                        <div>
                          <div style={{fontSize: "15px"}}>{item.brand}</div>
                          <div style={{fontSize:"20px", fontWeight:"bold"}}>{item.name}</div>
                          { item.cost == "문의" ? (
                            <div style={{fontSize:"15px", fontWeight:"bold"}}>{item.cost}</div>
                          ) : (
                            <div style={{fontSize:"20px"}}>{item.cost}원</div>
                          )}
                          
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
      <Pagination current={page} total={glassesData.length} pageSize={pageSize} onChange={handlePageChange}/>
      </div>
      <Footer/>
    </div>
    
  )
}

export default ListPage;