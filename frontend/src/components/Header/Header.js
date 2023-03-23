import './Header.css'
import { ArrowLeftOutlined, UserOutlined } from '@ant-design/icons';
import { Avatar } from 'antd';
import { useEffect, useState } from 'react';
import { useLocation, useNavigate} from 'react-router-dom';

function Header() {
  
  const navigate = useNavigate()
  const location = useLocation();
  const [headerLogo, setHeaderLogo] = useState("Allergy Pang")

  useEffect(()=>{
    if(location.pathname == '/'){
      setHeaderLogo("Allergy Pang")
    }else if(location.pathname == '/danger') {
      setHeaderLogo("위험 음식 페이지")
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
        <div className='allergy'>
          <div style={{
            flex: 1,
          }}>
            나의 알레르기 정보:
          </div>
          <div className='allergy-data'>
            토마토
          </div>
        </div>
        <div className='profile'>
            <Avatar size={64} icon={<UserOutlined />} />
        </div>
      </div>
      {/* <div style={{
        backgroundColor: "whitesmoke",
        height: "2vh",
      }}>
      </div> */}
    </div>
  )
}
export default Header;