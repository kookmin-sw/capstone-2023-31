import React, { useEffect, useState } from "react";
import { useLocation, Link } from "react-router-dom";
import Header from "../../components/Header/Header"
import "./ListPage.css"
import Footer from "../../components/Footer/Footer";
import {Row, Col, Pagination} from "antd";
import axios from "axios";
import SelectComponent from "../../components/Select/Select";

function ListPage() {
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


  const [sortedImages, setSortedImages] = useState(glassesData);
  const [sortOption, setSortOption] = useState('');
  const options = [
    { value: '', label: "기본 순"},
    { value: 'name', label: "이름 순"},
    { value: 'highCost', label: "높은 가격 순"},
    { value: 'lowCost', label: "낮은 가격 순"}
  ]

  const handleSortChange = (value) => {
    setSortOption(value);
  };

  useEffect(()=>{
    // 정렬 옵션에 따라 이미지 배열을 정렬
    let sortedData = [...glassesData];
    if (sortOption === 'name') {
      sortedData.sort((a, b) => a.name.localeCompare(b.name));
    } else if (sortOption === 'highCost') {
      sortedData.sort((a, b) => compareCost(a.cost, b.cost, 'high'));
    } else if (sortOption === 'lowCost'){
      sortedData.sort((a, b) => compareCost(a.cost, b.cost, 'low'));
    }
    setSortedImages(sortedData);
  }, [glassesData, sortOption])

  const compareCost = (a, b, order) => {
    if (a === "문의") return order === 'high' ? 1 : -1;
    if (b === "문의") return order === 'high' ? -1 : 1;

    return order === 'high' ? b - a : a - b;
  };

  const [page, setPage] = useState(1);

  useEffect(()=>{ // 페이지 이동 시 스크롤 위치 초기화
    window.scrollTo(0, 0);
  }, [page])

  const handlePageChange = (page) => {
    setPage(page);
  };

  return(
    <div className="container">
      <Header/>
      <div className="list-container">
        <div className="style-name">{name}</div>
        <div style={{marginTop: "2rem", marginLeft: "5rem"}}>
          <SelectComponent onSortChange={handleSortChange} options={options} defaultValue={sortOption}/>
        </div>
        <div className="list-glasses">
            <Row gutter={[8,8]}>
              {sortedImages.slice((page - 1) * pageSize, page * pageSize).map((item, index) => (
                  <Col key={index} lg={6} md={8} sm={12} xs={24}
                    style={{display:"flex", flexDirection:"column", alignItems:"center", marginBottom:"3rem"}}
                    >
                    <Link 
                      className="link" 
                      to={`/product/${shape}/${item.id}`}
                      state={item}
                      >
                      <div style={{display: "flex", flexDirection:"column", width: '250px'}}>
                        <img src={`/images/input/${item.image}`}></img>
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
      <div style={{display:"flex", justifyContent:"center"}}>
      <Pagination current={page} total={glassesData.length} pageSize={pageSize} onChange={handlePageChange}/>
      </div>
      <Footer/>
    </div>
    
  )
}

export default ListPage;