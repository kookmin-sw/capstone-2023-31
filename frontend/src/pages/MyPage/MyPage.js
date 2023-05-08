import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import Record from "../../components/Record/Record";
import ModalComponent from "../../components/Modal/ModalComponent";
import "./MyPage.css"
import "../../components/Modal/Modal.css"
import { useState } from "react";
import { Button, Row, Col} from 'antd';

import EditProfile from "../../components/EditProfile";
import { useNavigate, Link } from "react-router-dom";


function MyPage(){
  const navigate = useNavigate();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const showModal = () => {
    setIsModalOpen(true);
  };
  const handleOk = () => {
    setIsModalOpen(false);
  };
  const handleCancel = () => {
    setIsModalOpen(false);
  };

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

  return (
    <div className="container">
      <Header/>
      <div className="mypage-container">
        <div className="user">
          <div style={{fontSize: "25px", fontWeight:"bold"}}>마이페이지</div>
          <div className="profile-edit">
            <div style={{margin:"20px"}}>OOO님의 얼굴형: OOO형</div>
            <div>
              <Button style={{margin:"10px", width:"200px"}} onClick={()=>navigate('/camera')}>얼굴형 재분석</Button>
              <Button style={{margin:"10px", width:"200px"}} onClick={showModal}>프로필 편집</Button>
            </div>
          </div>
        </div>

        <ModalComponent 
          title="프로필 편집" isOpen={isModalOpen} onCancel={handleCancel}>
          <div style={{display:"flex", justifyContent:"space-between", marginBottom:"20px"}}>
            <div>프로필 편집</div>
            <Button className="modal-close-btn" onClick={handleCancel}>X</Button>
          </div>
          
          <EditProfile/>
          <Button onClick={handleCancel} style={{ float:"right"}}>변경하기</Button>
        </ModalComponent>

        <div className="dibs">
          <div style={{fontSize:"20px", margin: "0 30px"}}>찜한 안경</div>
          <div className="list-glasses" style={{marginBottom:"0"}}>
          <Row gutter={[8,8]}>
              {gridData.map((item, index) => (
                  <Col key={index} lg={6} md={8} sm={12} xs={24}
                    style={{display:"flex", flexDirection:"column", alignItems:"center", marginBottom:"3rem"}}
                    >
                    <Link 
                      className="link" 
                      to={`/detail`}
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
      </div>
      <Footer name="mypage"/>
    </div>

    
  )
}

export default MyPage;