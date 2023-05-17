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
          label="닉네임"
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
          label="이전 비밀번호"
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
          label="새로운 비밀번호"
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
            변경하기
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}

export default EditProfile;
