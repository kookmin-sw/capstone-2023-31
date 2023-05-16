import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './LoginPage.css'
import { UserOutlined, LockOutlined} from '@ant-design/icons';
import { Button, Form, Input, Checkbox } from 'antd';
import Header from '../../components/Header/Header';
import Footer from '../../components/Footer/Footer';


function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    const checkLoginStatus = async () => { //실시간으로 로그인했는지 확인
        try {
            const response = await axios.get('/user/check-login/');
            setIsLoggedIn(response.data.isLoggedIn);
        } catch (error) {
            console.error(error);
        }
    };

    useEffect(() => {
        checkLoginStatus();
    }, []);

    const onEmailHandler = (event) => {
        setEmail(event.target.value);
    };

    const onPasswordHandler = (event) => {
        setPassword(event.target.value);
    };

    const onSubmitHandler = async () => {

        try {
            const csrfResponse = await axios.get('/user/get-csrf-token/');
            const csrfToken = csrfResponse.data.csrfToken;

            const response=await axios.post('/user/login/', {
                email: email,
                password: password,
            }, {
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });
            if (response.data.success) {
                const data = response.data;
                alert(data.message);
                
                checkLoginStatus();
                navigate('/');

            }
            else {
                alert(response.data.message)
            }
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className='container'>
            <Header/>
            {isLoggedIn ? (
                <>
                    <p>이미 로그인되어 있습니다.</p>
                    <button onClick={() => navigate('/')}>메인 페이지로 이동</button>
                </>
            ) : (
                    <div className='login-container'>
                        <h2>로그인</h2>
                        <Form
                            name="normal_login"
                            className="login-form"
                            initialValues={{
                                remember: true,
                            }}
                            onFinish={onSubmitHandler}
                            >
                            <Form.Item
                                name="email"
                                rules={[
                                {
                                    required: true,
                                    message: '이메일을 입력해주세요.',
                                },
                                ]}
                            >
                                <Input prefix={<UserOutlined className="site-form-item-icon" />} 
                                    placeholder="email" 
                                    value={email}
                                    onChange={onEmailHandler} />
                            </Form.Item>
                            <Form.Item
                                name="password"
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
                                value={password}
                                onChange={onPasswordHandler}
                                />
                            </Form.Item>
                            <Form.Item>
                                <Form.Item name="remember" valuePropName="checked" noStyle>
                                    <Checkbox>정보 기억하기</Checkbox>
                                </Form.Item>
                            </Form.Item>

                            <Form.Item>
                                <Button type="primary" htmlType="submit" className="login-form-button">
                                    로그인
                                </Button>
                            </Form.Item>
                        </Form>
                    </div>
                )}
            <Footer/>
        </div>
    );
}

export default Login;