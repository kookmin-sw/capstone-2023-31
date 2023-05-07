import './Header.css'
import { ArrowLeftOutlined, UserOutlined } from '@ant-design/icons';
import { Avatar } from 'antd';
import { useEffect, useState } from 'react';
import { Link, useLocation, useNavigate} from 'react-router-dom';

function Header() {
  
  const navigate = useNavigate()
  const location = useLocation();
  // const [headerLogo, setHeaderLogo] = useState("")

  // useEffect(()=>{
  //   if(location.pathname == '/'){
  //     setHeaderLogo("가상 안경")
  //   }else if(location.pathname == '/alter') {
  //     setHeaderLogo("분석 페이지")
  //   }else if(location.pathname == '/mypage'){
  //     setHeaderLogo("마이 페이지")
  //   }else{
  //     setHeaderLogo(<ArrowLeftOutlined onClick={() => {
  //       navigate(-1);
  //     }}/>);
  //   }
  //  }, [location])

  return (

  <div className="header-container">
    <div className="app-name">
      <Link className="link" to="/">가상 안경</Link>  
    </div>
    <div className="profile">
      <ul>
        <li><Link className="link" to="/">로그인</Link></li>
        <li><Link className="link" to="/">회원가입</Link></li>
      </ul>
    </div>
  </div>

  )
}
export default Header;