import './Footer.css'
import Icon, {HomeOutlined, UserOutlined, SwapOutlined} from '@ant-design/icons';
import { useLocation, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';

function Footer(props) {

  const navigate = useNavigate();
  const location = useLocation();

  return (
    <div className="footer-container">
      {/* <Icon className="btn2"component={HomeOutlined} style={{color: setClick ? "blue" : "black"}}/> */}
      <HomeOutlined className={props.name ==="main"? 'btn2 click':'btn2'} onClick={() => {
        navigate('/')
      }}/>
      <SwapOutlined className={props.name ==="alter"? 'btn2 click':'btn2'} onClick={() => {
        navigate('/danger')
      }}/>
      <UserOutlined className={props.name ==="mypage"? 'btn2 click':'btn2'} onClick={() => {
        navigate('/mypage')
      }}/>
    </div>
  )
}
export default Footer;