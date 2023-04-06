import { Button, Badge, Select } from "antd";
import { forwardRef, useEffect, useRef, useState } from "react";
import ModalComponent from '../Modal/ModalComponent';
import dayjs from 'dayjs';
import AddRecord from "./AddRecord";
import "./Record.css"
import "../Modal/Modal.css"
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import ListRecord from "./ListRecord";
import { useNavigate } from "react-router-dom";
import DetailRecord from "./DetailRecord";


function Record(){

  const navigate = useNavigate();
  
  const [selectedValue, setSelectedValue] = useState(() => dayjs());
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [type, setType] = useState('list');
  const [date, setDate] = useState(new Date());
  const [selectedItemName, setSelectedItemName] = useState(null);

  const showModal = () => {
    setIsModalOpen(true);
  };

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  const tileClassName = ({ date, view }) => {
    if (view === 'month' && date.getDay() === 0) {
      return 'sunday';
    }
  };

  const [dataList, setDataList] = useState([
    { name: "1", sympton: "Item 1" },
    { name: "2", sympton: "Item 2" },
    { name: "3", sympton: "Item 3" },
  ]);

  const handleAdd = (item) => {
    setDataList([...dataList, item]);
  };

  const selectItem = (itemName) => {
    setSelectedItemName(itemName);
  }
  const changeType = (newType) => {
    setType(newType);
  }
  const select = (itemName, type2) => {
    selectItem(itemName);
    changeType(type2);
  }

  return(
    <div className="record-container">
      <div className="record-name">
        알러지 일기
      </div>
      <div className="record">
        {/* <Calendar 
          className="calendar" 
          headerRender={""}
          fullscreen={false}
          dateCellRender={DateCellRender}
          onPanelChange={OnPanelChange} 
          onSelect={calendarMode == 'year' ? null : onSelect}
          onChange={(value)=> onChange(value)}>
        </Calendar> */}

        <Calendar 
          onChange={setDate} 
          value={date}
          onClickDay={showModal}
          tileClassName={tileClassName}
          calendarType={'US'}
          formatDay={(locale, date) => dayjs(date).format('D')}
         />
        
        <ModalComponent 
          title={`알러지 일기 (${selectedValue.format("YYYY-MM-DD")})`}
          isOpen={isModalOpen} 
          onCancel={handleCancel}
        >
          <>
          {type == "list" ? 
            <> 
            <ListRecord data={dataList} onClick={handleCancel} onSelect={(itemName, newType)=>select(itemName, newType)}/>
            <Button onClick={()=> {setType("add")}} style={{ float:"right"}}>추가하기</Button>
            </>
          : type == "add" ? 
            <>
            <AddRecord onSubmit={handleAdd} onClick={()=>{setType("list")}}/>
           
            </>
          : type == "detail" ? 
            <>
            <DetailRecord item={dataList.find((item) => item.name === selectedItemName)} changeType={changeType} onClick={()=>{setType("list")}}/>
            </>
          : null }
          </>
        </ModalComponent>
      </div>
    </div>
  )
}

export default Record;