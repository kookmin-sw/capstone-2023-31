import './App.css';
import React, { useState, useEffect } from "react";
import 
{ BrowserRouter as Router,
   Routes, 
   Route,
} from "react-router-dom";
import MainPage from './pages/MainPage/MainPage';
import SearchName from './pages/CameraPage/SearchName';
import Webcam from './pages/CameraPage/Webcam';
import DetailPage from './pages/DetailPage/DetailPage';
import AlterFoodPage from './pages/AlterFoodPage/AlterFoodPage';
import MyPage from './pages/MyPage/MyPage';

// function App() {
//   const [msg, setMsg] = useState([]);
//   useEffect(() => {
//     fetch("/api/hello")
//       .then((res) => { return res.json(); })
//       .then((data) => { setMsg(data); })
//   }, []);
//   return (
//     <div className="App">
//       <header className="App-header">
//         <ul>
//           {msg.map((content, idx) => <li key={`${idx} - ${content}`}>{content}</li>)}
//         </ul>
//       </header>
//     </div>
//   );
// }

function App() {
  return (
      <Router>
        <Routes>
          <Route path="/" element={<MainPage />}></Route>
          <Route path="/searchname" element={<SearchName />}></Route>
          <Route path="/camera" element={<Webcam />}></Route>
          <Route path="/detail" element={<DetailPage />}></Route>
          <Route path="/mypage" element={<MyPage />}></Route>
          <Route path="/alter" element={<AlterFoodPage/>}></Route>

        </Routes>
      </Router>
  )
}

export default App;