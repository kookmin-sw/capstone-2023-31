import { Select } from "antd";
const { Option } = Select;

function SelectComponent({onSortChange, options, defaultValue}){
  const handleSortChange = (value) => {
    onSortChange(value);
  };

  return (
    <>    
      <Select defaultValue={defaultValue} style={{ width: 200, marginBottom: 16 }} onChange={handleSortChange}>
        {options.map((item, index)=>(
          <Option key={index} value={item.value}>{item.label}</Option>
        ))}
      </Select>

  </>
  );
}

export default SelectComponent;