import './Footer.css'
import {HomeOutlined, UserOutlined, SwapOutlined} from '@ant-design/icons';
import { useLocation, useNavigate } from 'react-router-dom';

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
        navigate('/alter')
      }}/>
      <UserOutlined className={props.name ==="mypage"? 'btn2 click':'btn2'} onClick={() => {
        navigate('/mypage')
      }}/>
    </div>
  )
}
export default Footer;