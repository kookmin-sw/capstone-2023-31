import { useLocation } from "react-router-dom";
import Header from "../../components/Header/Header"
import "./DetailPage.css"

function DetailPage() {

  const {state} = useLocation();

  return(
    <div className="detail-container"> 
      <Header/>
      
      <div className="food-name">{state.value}</div>
      <div className="detail-content">
        <div className="contents" >제품 성분</div>
        <div className="contents">{`알러지 성분`}</div>
        <div className="contents">{`위험`}</div>
      </div>
      
    </div>
  )
}

export default DetailPage;