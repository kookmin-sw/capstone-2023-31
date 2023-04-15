import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import './AlterFoodPage.css'

function AlterFoodPage(){
  return(

    <div className="alterfoodpage-container">
      <Header/>
      <div className="contents">대체음식 페이지입니다.</div>
      <Footer name="alter"/>
    </div>
    
  )
}

export default AlterFoodPage;