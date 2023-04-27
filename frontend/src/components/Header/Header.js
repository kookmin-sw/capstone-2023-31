import './Header.css'
import { ArrowLeftOutlined, UserOutlined } from '@ant-design/icons';
import { Avatar } from 'antd';
import { useEffect, useState } from 'react';
import { useLocation, useNavigate} from 'react-router-dom';

function Header() {
  
  const navigate = useNavigate()
  const location = useLocation();
  const [headerLogo, setHeaderLogo] = useState("")

  useEffect(()=>{
    if(location.pathname == '/'){
      setHeaderLogo("가상 안경")
    }else if(location.pathname == '/alter') {
      setHeaderLogo("분석 페이지")
    }else if(location.pathname == '/mypage'){
      setHeaderLogo("마이 페이지")
    }else{
      setHeaderLogo(<ArrowLeftOutlined onClick={() => {
        navigate(-1);
      }}/>);
    }
   }, [location])

  return (
    <div className="header-container">
      <div className="app-name">{headerLogo}</div>
      <div className='info'>
        
      </div>
    </div>
  )
}
export default Header;