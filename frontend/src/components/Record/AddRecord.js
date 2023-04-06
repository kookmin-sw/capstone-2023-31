import { Form, Input, Button } from 'antd';

function AddRecord({onSubmit, onClick}){
  const [form] = Form.useForm();

  const handleClose = () => {
    onClick();
  }

  const handleSubmit = (item) => {
    onSubmit(item);
    // form.resetFields();
    onClick();
  }
  return(
    <div>
      <button style={{ marginTop: "4px", marginLeft: "20px", display: "inline-block"}} className="modal-close-btn" onClick={handleClose}>X</button>
      <Form form={form} onFinish={handleSubmit}>
        <Form.Item
          label="음식명"
          name="name"
          rules={[
            {
              required: true,
              message: '음식명을 입력해주세요.',
            },
          ]}
        >
          <Input />
        </Form.Item>

      <Form.Item
        label="재료"
        name="ingredient"
        rules={[
          {
            required: true,
            message: '재료를 입력해주세요.',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="증상"
        name="sympton"
        rules={[
          {
            required: true,
            message: '증상을 입력해주세요',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit">추가</Button>
      </Form.Item>
    </Form>

    {/* <Button onClick={addItem} style={{ float:"right"}}>완료</Button> */}
    </div>
  )
}

export default AddRecord;