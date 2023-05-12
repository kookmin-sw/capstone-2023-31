import React from "react";
import { Input } from "antd";
import { useNavigate } from "react-router-dom";
import "./SearchBar.css"
function SearchBar(){
  const navigate = useNavigate();
  const { Search } = Input;
  const onSearch = (e) => {
    if (e == ''){
      alert("입력 필수")
    }else {
    navigate('/detail', {state: {value: e}});
    }
  }
  return(
    <div className="search">
      <Search className="s-bar" placeholder="안경 검색하기" onSearch={onSearch} size="large"/>
    </div>
  )
}
export default SearchBar