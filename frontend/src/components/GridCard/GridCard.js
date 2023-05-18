import React from "react";
import { Col } from "antd";
import { Link } from "react-router-dom";

function GridCard(props){
  return(
      <Col lg={8} md={12} xs={24} 
        style={{display:"flex", flexDirection:"column", alignItems:"center"}}>
        <Link 
          className="link" 
          to={`/product/${props.shape}`}
          state={{ name: props.name, shape: props.shape}}
          >
        <div style={{display: "flex", alignItems:"center", borderRadius: "50%", width: "200px", height: "200px", justifyContent: "center", margin: "2rem", border: "1px solid gray"}}>
            <img 
              style={{borderRadius: "50%", maxWidth:'200px'}}
              src={props.image}
              >
            </img>
        </div>
        </Link>
        <div style={{fontSize:"20px"}}>{props.name}</div>
      </Col>
  )
}

export default GridCard;