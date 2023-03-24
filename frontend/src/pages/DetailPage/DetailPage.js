import { useLocation } from "react-router-dom";

function DetailPage() {

  const {state} = useLocation();

  return(
    <div style={{
      backgroundColor: "skyblue",
      
    }}> 
      상세페이지 - 전달받은 값: "{state.value}"
    </div>
  )
}

export default DetailPage;