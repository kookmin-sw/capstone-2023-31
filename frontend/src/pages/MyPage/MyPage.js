import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import ModalComponent from "../../components/Modal/ModalComponent";
import "./MyPage.css";
import "../../components/Modal/Modal.css";
import { useState, useEffect } from "react";
import { Button, Row, Col } from "antd";
import EditProfile from "../../components/EditProfile";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import { Provider, useSelector } from "react-redux";



function MyPage() {
  const navigate = useNavigate();
  const [nickname, setNickname] = useState("");
  const [updatedpassword, setUpdatePassword] = useState("");
  const [faceShape, setFaceShape] = useState("");
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

  const sendSetProfileRequest = async () => {
    try {
      const csrfResponse = await axios.get('/user/get-csrf-token/');
      const csrfToken = csrfResponse.data.csrfToken;

      const response = await axios.post('/setprofile/', null, {
        headers: {
          'X-CSRFToken': csrfToken
        }
      });

      if (response.data.success) {
        const data = response.data;
        setNickname(data.nickname);
        setFaceShape(data.face_shape);
        handleCancel();
        
      }
      
    } catch (error) {
      console.error(error);
    }

  };

  const handleProfileUpdate = async (updatedNickname, lastPassword, updatedPassword) => {
    try {
      const response = await axios.get('/user/get-csrf-token/');
      const csrfToken = response.data.csrfToken;

      const updateResponse = await axios.post('/user/edit-profile/', {
        nickname: updatedNickname,
        lastpassword: lastPassword,
        updatedpassword: updatedPassword
      }, {
        headers: {
          'X-CSRFToken': csrfToken
        }
      });

      if (updateResponse.data.success) {
        const data = updateResponse.data;
        alert(data.message);
        if (data.nickname) {
          setNickname(data.nickname);
        }
        if (data.updatedpassword) {
          setUpdatePassword(data.updatedpassword);
        }
        handleCancel();
        window.location.reload();
      } else {
        alert(updateResponse.data.message);
      }
    } catch (error) {
      console.error(error);
    }
  };


  useEffect(() => {
    sendSetProfileRequest();
  }, []);
 
  const wishlist = useSelector(store => store.wishReducer || []);

  return (
    <div className="container">
      <Header />
      <div className="mypage-container">
        <div className="user">
          <div style={{ fontSize: "25px", fontWeight: "bold" }}>마이페이지</div>
          <div className="profile-edit">
            <div style={{ margin: "20px" }}>
              {`${nickname}님의 얼굴형: ${faceShape}`}
            </div>
            <div>
              <Button
                style={{ margin: "10px", width: "200px" }}
                onClick={() => navigate("/analyze/camera")}
              >
                얼굴형 재분석
              </Button>
              <Button
                style={{ margin: "10px", width: "200px" }}
                onClick={showModal}
              >
                프로필 편집
              </Button>
            </div>
          </div>
        </div>
        
        <ModalComponent
          title="프로필 편집"
          isOpen={isModalOpen}
        >
          <div style={{display:"flex", justifyContent:"space-between", marginBottom:"20px"}}>
            <div style={{fontWeight:"bold", fontSize:"20px"}}>프로필 편집</div>
            <Button onClick={() => handleCancel(true)}>X</Button>
          </div>
          <EditProfile onUpdate={handleProfileUpdate} />
        </ModalComponent>

          <div className="dibs">
            <div style={{fontSize:"20px", margin: "0 30px", fontWeight:"bold"}}>찜한 안경</div>
            {wishlist.length == 0 ? (
              <p style={{margin:"20px auto"}}>찜한 상품이 없습니다.</p>
            ):(
              <div className="list-glasses" style={{marginBottom:"0"}}>
              <Row gutter={[8,8]}>
                  {wishlist.map((item, index) => (
                      <Col key={index} lg={6} md={8} sm={12} xs={24}
                        style={{display:"flex", flexDirection:"column", alignItems:"center", marginBottom:"3rem"}}
                        >
                        <Link 
                          className="link" 
                          to={`/product/${item.style}/${item.id}`}
                          state={item}
                          >
                        <div style={{display: "flex", flexDirection:"column"}}>
                            <img 
                              style={{ width:'250px'}}
                              src={`/images/input/${item.image}`}
                              >
                            </img>
                            <div>
                              <div style={{fontSize:"15px"}}>{item.brand}</div>
                              <div style={{fontSize: "20px", fontWeight:"bold"}}>{item.name}</div>
                              { item.cost == "문의" ? (
                              <div style={{fontSize:"20px"}}>{item.cost}</div>
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
            )}
          </div>

      </div>
      <Footer name="mypage" />
    </div>


  )
}

export default MyPage; 