import './App.css';
import React, { useState, useEffect } from "react";
import 
{ BrowserRouter as Router,
   Routes, 
   Route,
} from "react-router-dom";
import MainPage from './pages/MainPage/MainPage';
import SearchName from './pages/CameraPage/SearchName';
import Camera from './pages/CameraPage/Camera';
import ListPage from './pages/ListPage/ListPage';
import FaceAnalyze from './pages/Analyzepage/FaceAnalyze';
import MyPage from './pages/MyPage/MyPage';
import Detail from './pages/DetailPage/Detail'

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
          <Route path="/camera" element={<Camera />}></Route>
          <Route path="/list/:style" element={<ListPage />}></Route>
          <Route path="/mypage" element={<MyPage />}></Route>
          <Route path="/analyze" element={<FaceAnalyze/>}></Route>
          <Route path="/detail" element={<Detail/>}></Route>

        </Routes>
      </Router>
  )
}

export default App;