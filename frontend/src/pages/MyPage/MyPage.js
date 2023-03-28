import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import Record from "../../components/Record/Record";
import ModalComponent from "../../components/Modal/ModalComponent";
import "./MyPage.css"
import "../../components/Modal/Modal.css"
import { useState } from "react";
import { Button} from 'antd';

import EditProfile from "../../components/EditProfile";


function MyPage(){

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

  return (
    <div className="mypage-container">
      <Header/>
      <div className="profile-edit">
      <Button className="btn" onClick={showModal}
      style={{
          marginBottom: "20px"
        }}>프로필 편집하기
      </Button>

      <ModalComponent 
        title="프로필 편집" isOpen={isModalOpen} onCancel={handleCancel}>
        <span style={{ marginBottom: "30px"}}>프로필 편집</span>
        <button className="modal-close-btn" onClick={handleCancel}>X</button>
        <EditProfile/>
        <Button onClick={handleCancel} style={{ float:"right"}}>변경하기</Button>
        
      </ModalComponent>
      
 
    

      
        
        
        
      </div>
      <Record/>
      
      <Footer name="mypage"/>
    </div>

    
  )
}

export default MyPage;