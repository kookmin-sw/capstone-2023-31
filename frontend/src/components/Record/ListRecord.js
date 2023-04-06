import { List } from 'antd';
import { useState } from 'react';
import Pagination from 'react-js-pagination';

function ListItem({ item, onClick }) {
  return (
    <List.Item key={item.name} onClick={() => onClick(item.name)}>
      {item.name}
    </List.Item>
  );
}


function ListRecord({data, onClick, onSelect}){

  const [selectedItemName, setSelectedItemName] = useState(null);
  const [type, setType] = useState('list');
  
  const handleClick = (itemName) => {
    onSelect(itemName , 'detail');
  };

  function handleClose() {
    onClick();
  }

  const [activePage, setActivePage] = useState(1);
  const handlePageChange = (pageNumber) => {
    setActivePage(pageNumber);
  };

  return(
    <div className="list-allergy-container">
      <div style={{ marginBottom: "20px", display: "inline-block"}}>알러지 일기 리스트</div>
      <button style={{ marginTop: "4px", marginLeft: "20px", display: "inline-block"}} className="modal-close-btn" onClick={handleClose}>X</button>
      <List
        size='large'>
        {data.map((item, index) => (
          <ListItem key={index} item={item} onClick={()=>{handleClick(item.name)}} />
        ))}
      </List>
    </div>
  )
}


export default ListRecord