import './Footer.css'
import {HomeOutlined, UserOutlined, SwapOutlined} from '@ant-design/icons';
import { useLocation, useNavigate } from 'react-router-dom';

function Footer(props) {

  const navigate = useNavigate();
  const location = useLocation();

  return (
    <div className="footer-container">
      <SwapOutlined className={props.name ==="alter"? 'btn2 click':'btn2'} onClick={() => {
        navigate('/alter')
      }}/>
      <HomeOutlined className={props.name ==="main"? 'btn2 click':'btn2'} onClick={() => {
        navigate('/')
      }}/>
      <UserOutlined className={props.name ==="mypage"? 'btn2 click':'btn2'} onClick={() => {
        navigate('/mypage')
      }}/>
    </div>
  )
}
export default Footer;