import { Form, Input, Button } from 'antd';

function EditProfile({ nickname, onUpdate }) {
  const onFinish = (values) => {
    const { nickname, lastpassword, updatedpassword } = values;
    onUpdate(nickname, lastpassword, updatedpassword);
  };

  return (
    <div className="edit-profile-container">
      <Form onFinish={onFinish}>
        <Form.Item
          label="Nickname"
          name="nickname"
          initialValue={nickname}
          rules={[
            {
              required: true,
              message: 'Please input your nickname!',
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Last Password"
          name="lastpassword"
          rules={[
            {
              required: true,
              message: 'Please input your last password!',
            },
          ]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item
          label="Updated Password"
          name="updatedpassword"
          rules={[
            {
              required: true,
              message: 'Please input your new password!',
            },
          ]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item>
          <Button type="primary" htmlType="submit">
            Update Profile
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}

export default EditProfile;
