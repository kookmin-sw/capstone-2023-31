import { Button, Calendar, Badge } from "antd";
import { useState } from "react";
import ModalComponent from '../Modal/ModalComponent';
import dayjs from 'dayjs';
import RecordAllergy from "./RecordAllergy";
import "./Record.css"
import "../Modal/Modal.css"

function Record(){

  const [selectedValue, setSelectedValue] = useState(() => dayjs());

  const onPanelChange = (value, mode) => {
    console.log(value);
    console.log(mode);
    console.log(value.format('YYYY-MM-DD'), mode);
  };

  const onSelect = (newValue) => {
    setSelectedValue(newValue);
    setIsModalOpen(true);

  }

  const [isModalOpen, setIsModalOpen] = useState(false);
  
  const showModal = () => {
    setIsModalOpen(true);
    
  };
  const handleOk = () => {
    setIsModalOpen(false);
  };
  const handleCancel = () => {
    setIsModalOpen(false);
  };





  const getListData = (value) => {
    let listData;
    switch (value.date()) {
      case 8:
        listData = [
          {
            type: 'warning',
            content: 'This is warning event.',
          },
          {
            type: 'success',
            content: 'This is usual event.',
          },
        ];
        break;
      
      default:
        break;
    }
    return listData || [];
  };
  

  const DateCellRender = (value) => {
    const listData = getListData(value);
    const [count, setCount] = useState(0);
    const [s, setData] = useState();

    // useEffect(() => {
    //   listData.map((item) => (
    //     console.log(item.type)
    //   ))
    // }, [])

    return (
      <div>
        {listData.map((item) => (
          <Badge key={item.content} size="small" status={item.content} />
          
        ))}
      
      </div>
    );
  }




  return(
    <div className="record-container">
      <div className="record-name">
        알러지 일기
      </div>
      <div className="record">
        {/* <Calendar className="calendar" fullscreen={false}
          dateCellRender={DateCellRender}
          onPanelChange={onPanelChange} onSelect={onSelect}/> */}
        {/* <Modal title={`알러지 일기 목록 (${selectedValue.format("YYYY-MM-DD")})`}
          open={isModalOpen} onOk={handleOk} onCancel={handleCancel}>
          리스트
        </Modal> */}
        
        <Button className="btn3" type="primary" onClick={showModal}>추가하기</Button>
        <ModalComponent title={`알러지 일기 (${selectedValue.format("YYYY-MM-DD")})`}
          isOpen={isModalOpen} onCancel={handleCancel}>
          <div style={{ marginBottom: "20px", display: "inline-block"}}>알러지 일기</div>
          <button className="modal-close-btn" onClick={handleCancel}>X</button>
          <RecordAllergy/>
          <Button onClick={handleCancel} style={{ float:"right"}}>추가하기</Button>
        </ModalComponent>
      </div>
    </div>
  )
}

export default Record;


// import { Badge, Calendar } from 'antd';
// const getListData = (value) => {
//   let listData;
//   switch (value.date()) {
//     case 8:
//       listData = [
//         {
//           type: 'warning',
//           content: 'This is warning event.',
//         },
//         {
//           type: 'success',
//           content: 'This is usual event.',
//         },
//       ];
//       break;
//     case 10:
//       listData = [
//         {
//           type: 'warning',
//           content: 'This is warning event.',
//         },
//         {
//           type: 'success',
//           content: 'This is usual event.',
//         },
//         {
//           type: 'error',
//           content: 'This is error event.',
//         },
//       ];
//       break;
//     case 15:
//       listData = [
//         {
//           type: 'warning',
//           content: 'This is warning event',
//         },
//         {
//           type: 'success',
//           content: 'This is very long usual event。。....',
//         },
//         {
//           type: 'error',
//           content: 'This is error event 1.',
//         },
//         {
//           type: 'error',
//           content: 'This is error event 2.',
//         },
//         {
//           type: 'error',
//           content: 'This is error event 3.',
//         },
//         {
//           type: 'error',
//           content: 'This is error event 4.',
//         },
//       ];
//       break;
//     default:
//   }
//   return listData || [];
// };
// const getMonthData = (value) => {
//   if (value.month() === 8) {
//     return 1394;
//   }
// };
// const Record = () => {
//   const monthCellRender = (value) => {
//     const num = getMonthData(value);
//     return num ? (
//       <div className="notes-month">
//         <section>{num}</section>
//         <span>Backlog number</span>
//       </div>
//     ) : null;
//   };
//   const dateCellRender = (value) => {
//     const listData = getListData(value);
//     return (
//       <ul className="events">
//         {listData.map((item) => (
//           <li key={item.content}>
//             <Badge status={item.type} text={item.content} />
//           </li>
//         ))}
//       </ul>
//     );
//   };
//   return <Calendar dateCellRender={dateCellRender} monthCellRender={monthCellRender} />;
// };
// export default Record;