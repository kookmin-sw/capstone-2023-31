function DetailRecord({ item, onClick }) {
  const handleClose = () => {
    onClick();
  }
  return (
    <div>
      <button style={{ marginTop: "4px", marginLeft: "20px", display: "inline-block"}} className="modal-close-btn" onClick={handleClose}>X</button>
      <div style={{display: "inline-block", fontSize: "25px", fontWeight: "bold"}}>{item.name}</div>
      <div>{item.sympton}</div>
    </div>
  );
}

export default DetailRecord;