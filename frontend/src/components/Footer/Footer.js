import './Footer.css'
import {HomeOutlined, UserOutlined, ChromeFilled} from '@ant-design/icons';
import { useLocation, useNavigate } from 'react-router-dom';
import { Button } from 'antd';
function Footer(props) {

  const navigate = useNavigate();
  const location = useLocation();

  return (
    <div className="footer-container">
      <HomeOutlined className={props.name ==="main"? 'btn2 click':'btn2'} onClick={(e) => {
        e.preventDefault();
        navigate('/')
      }}/>
      <ChromeFilled style={{fontSize: "60px"}}className={props.name ==="camera"? 'btn2 click':'btn2'} onClick={(e) => {
        e.preventDefault();
        navigate('/camera')
      }}/>
      <UserOutlined className={props.name ==="mypage"? 'btn2 click':'btn2'} onClick={(e) => {
        e.preventDefault();
        navigate('/mypage')
      }}/>
    </div>
  )
}
export default Footer;