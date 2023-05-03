import { React } from "react";
import { useNavigate } from 'react-router-dom';
import { Input } from 'antd';
import './SearchName.css'
import Header from "../../components/Header/Header";


function SearchName() {

  const navigate = useNavigate();

  const { Search } = Input;
  const onSearch = (e) => {
    if (e == ''){
      alert("입력 필수")
    }else {
    navigate('/detail', {state: {value: e}});
    }
  }
  
  return (
    <div className="search-name-container">
      <Header />
      <div className="search-bar">
        <Search className="bar" placeholder="음식 또는 식품명을 입력해주세요." onSearch={onSearch} enterButton />
      </div>
    </div>
    
  )
}

export default SearchName;