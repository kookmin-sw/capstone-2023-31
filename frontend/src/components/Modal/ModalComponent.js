import Modal from "react-modal";

function ModalComponent({isOpen, title, children}){

  const customStyles = {
    content: {
      maxHeight: '50vh',
      minWidth: '60vw',
      top: '50%',
      left: '50%',
      right: 'auto',
      bottom: 'auto',
      marginRight: '-50%',
      transform: 'translate(-50%, -50%)',
    },
  };

  return (
    <div>
      <Modal
        ariaHideApp={false} 
        isOpen={isOpen}
        contentLabel={title}
        style={customStyles}
      >
        {children}
      </Modal>
      
    </div>
  )
}

export default ModalComponent;