import './Footer.css'
import {HomeOutlined, UserOutlined, ChromeFilled} from '@ant-design/icons';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Button } from 'antd';
function Footer() {

  const navigate = useNavigate();
  const location = useLocation();

  return (
    <div className="footer-container">
      <div className="footer-info">
        Virtual Glasses
      </div>
      <div>
        <Link className="link" to="https://github.com/kookmin-sw/capstone-2023-31">github.com</Link>
      </div>



      {/* <HomeOutlined className={props.name ==="main"? 'btn2 click':'btn2'} onClick={(e) => {
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
      }}/> */}
    </div>
  )
}
export default Footer;