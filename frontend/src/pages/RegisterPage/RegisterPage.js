import React, { useState } from 'react';
import axios from 'axios';
import { useLocation, useNavigate } from "react-router-dom";
import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import './RegisterPage.css'
import { UserOutlined, LockOutlined} from '@ant-design/icons';
import { Button, Form, Input, Checkbox } from 'antd';

function RegisterPage(props) {
    const navigate = useNavigate();
    const [Email, setEmail] = useState("");
    const [Nickname, setNickname] = useState("");
    const [Password, setPassword] = useState("");
    const [ConfirmPassword, setConfirmPassword] = useState("");

    const onEmailHandler = (event) => {
        setEmail(event.currentTarget.value);
    }
    const onNicknameHandler = (event) => {
        setNickname(event.currentTarget.value);
    }
    const onPasswordHandler = (event) => {
        setPassword(event.currentTarget.value);
    }
    const onConfirmPasswordHandler = (event) => {
        setConfirmPassword(event.currentTarget.value);
    }
    const onSubmitHandler = () => {
        // event.preventDefault();

        if (Password !== ConfirmPassword) {
            return alert('비밀번호가 일치하지 않습니다.')
        }

        axios.get('/user/get-csrf-token/') // Get CSRF token from the server
            .then(response => {
                const csrfToken = response.data.csrfToken;

                // Send registration data to the backend
                axios.post('/user/register/', {
                    email: Email,
                    nickname: Nickname,
                    password: Password,
                }, {
                    headers: {
                        'X-CSRFToken': csrfToken
                    }
                })
                    .then(response => {
                        if (response.data.success) {
                            alert(response.data.message);
                            navigate('/user/login');
                        } else {
                            alert('Error');
                        }
                    })
                    .catch(error => {
                        console.error(error);
                    });
            })
            .catch(error => {
                console.error(error);
            });
    }

    return (
        <div className='container'>
            <Header/>
            <div className='register-container'>
            {/* <form style={{ display: 'flex', flexDirection: 'column' }}
                onSubmit={onSubmitHandler}
            >
                <label>Email</label>
                <input type='email' value={Email} onChange={onEmailHandler} />
                <label>Nickname</label>
                <input type='text' value={Nickname} onChange={onNicknameHandler} />
                <label>Password</label>
                <input type='password' value={Password} onChange={onPasswordHandler} />
                <label>Confirm Password</label>
                <input type='password' value={ConfirmPassword} onChange={onConfirmPasswordHandler} />
                <br />
                <button type='submit'>
                    회원가입
                </button>
            </form> */}
                <h2>회원가입</h2>
                <Form
                    name="normal_register"
                    className="register-form"
                    onFinish={onSubmitHandler}
                    >
                    <Form.Item
                        name="email"
                        label="이메일"
                        rules={[
                            {
                                type: 'email',
                                message: '잘못된 형식의 이메일입니다.',
                            },
                            {
                                required: true,
                                message: '이메일을 입력해주세요.',
                            },
                        ]}
                    >
                        <Input prefix={<UserOutlined className="site-form-item-icon" />} 
                            placeholder="Email" 
                            value={Email}
                            onChange={onEmailHandler}
                         />
                    </Form.Item>
                    <Form.Item
                        name="nickname"
                        label="닉네임"
                        rules={[
                        {
                            required: true,
                            message: '닉네임을 입력해주세요.',
                            whitespace: true,
                        },
                        ]}
                    >
                        <Input prefix={<UserOutlined className="site-form-item-icon" />}
                            placeholder="Nickname" 
                            value={Nickname}
                            onChange={onNicknameHandler}
                        />
                    </Form.Item>
                    <Form.Item
                        name="password"
                        label="비밀번호"
                        rules={[
                        {
                            required: true,
                            message: '비밀번호를 입력해주세요.',
                        },
                        ]}
                    >
                        <Input
                        prefix={<LockOutlined className="site-form-item-icon" />}
                        type="password"
                        placeholder="Password"
                        value={Password}
                        onChange={onPasswordHandler}
                        />
                    </Form.Item>
                    <Form.Item
                        name="passwordConfirm"
                        label="비밀번호 확인"
                        rules={[
                        {
                            required: true,
                            message: '비밀번호를 다시 확인해주세요.',
                        },
                        ]}
                    >
                        <Input
                        prefix={<LockOutlined className="site-form-item-icon" />}
                        type="password"
                        placeholder="Password Confirm"
                        value={ConfirmPassword}
                        onChange={onConfirmPasswordHandler}
                        dependencies={['password']}
                        />
                    </Form.Item>

                    <Form.Item>
                        <Button type="primary" htmlType="submit" className="register-form-button">
                            회원가입
                        </Button>
                    </Form.Item>
                </Form>
            </div>
            <Footer/>
        </div>
       
    )
}

export default RegisterPage;
