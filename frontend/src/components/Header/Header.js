import './Header.css'
import { useEffect, useState } from 'react';
import { Link, useNavigate} from 'react-router-dom';
import axios from 'axios';

function Header() {
  const navigate = useNavigate();
  
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const checkLoginStatus = async () => { //실시간으로 로그인했는지 확인
    try {
      const response = await axios.get('/user/check-login/');
      setIsLoggedIn(response.data.isLoggedIn);
    } catch (error) {
      console.error(error);
    }
  };
  useEffect(() => {
    checkLoginStatus();
  }, []);


  const onLogoutHandler = async (event) => {
    event.preventDefault();

    try {
      const logoutResponse = await axios.get('/user/logout/');

      if (logoutResponse.data.success) {
        alert(logoutResponse.data.message);
        setIsLoggedIn(false); // 로그인 상태 업데이트
        navigate('/');
      } else {
        alert(logoutResponse.data.message);
      }
    } catch (error) {
      console.error(error);
    }
  };


  return (
  <div className="header-container">
    <div className="app-name">
      <Link className="link" to="/">
        <img 
          src='https://github.com/kookmin-sw/capstone-2023-31/assets/63188042/26054fe7-1531-4741-9b5b-ab5d14e372ec' 
          style={{ height: "50px"}}>
        </img>
      </Link>
    </div>
    <div className="profile">
      <ul>
          {isLoggedIn ? (
            <>
              <li><Link className="link" to="/mypage">마이페이지</Link></li>
              <li><Link className="link" to="/user/logout" onClick={onLogoutHandler}>로그아웃</Link></li>
            </>
          ) : (
            <>  
              <li><Link className="link" to="/user/login">로그인</Link></li>
              <li><Link className="link" to="/user/signup">회원가입</Link></li>
            </>
          )}
      </ul>
    </div>
  </div>

  )
}
export default Header;