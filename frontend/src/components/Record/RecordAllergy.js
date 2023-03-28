import { Form, Input } from 'antd';

function RecordAllergy({}){
  return(
    <div>
      <Form>
        <Form.Item
          label="먹은 음식"
          name="food"
          rules={[
            {
              required: true,
              message: 'Please input your username!',
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
            message: 'Please input your password!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="증상"
        name="passwordconfirm"
        rules={[
          {
            required: true,
            message: 'Please input your password confirm!',
          },
        ]}
      >
        <Input />
      </Form.Item>
    </Form>

    
    </div>
  )
}

export default RecordAllergy;