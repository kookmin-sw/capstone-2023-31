import { Form, Input } from 'antd';

function EditProfile(){
  return(
    <div className="edit-profile-container">
      <Form>
        <Form.Item
          label="Username"
          name="username"
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
        label="Password"
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your password!',
          },
        ]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item
        label="Password Confirm"
        name="passwordconfirm"
        rules={[
          {
            required: true,
            message: 'Please input your password confirm!',
          },
        ]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item
        label="Allergy"
        name="allergy"
        rules={[
          {
            required: true,
            message: 'Please input your allergy!',
          },
        ]}
      >
        <Input />
      </Form.Item>
    </Form>
    </div>
  )
}

export default EditProfile;