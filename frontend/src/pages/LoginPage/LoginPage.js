import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

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

    const onSubmitHandler = async (event) => {
        event.preventDefault();

        try {
            const csrfResponse = await axios.get('/user/get-csrf-token/');
            const csrfToken = csrfResponse.data.csrfToken;

            await axios.post('/user/login/', {
                email: email,
                password: password,
            }, {
                headers: {
                    'X-CSRFToken': csrfToken
                }
            });

            checkLoginStatus();
            navigate('/');
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            {isLoggedIn ? (
                <>
                    <p>이미 로그인되어 있습니다.</p>
                    <button onClick={() => navigate('/')}>메인 페이지로 이동</button>
                </>
            ) : (
                    <div>
                        <h2>Login</h2>
                        <form
                            style={{ display: 'flex', flexDirection: 'column' }}
                            onSubmit={onSubmitHandler}
                        >
                            <label>Email</label>
                            <input type="email" value={email} onChange={onEmailHandler} />
                            <label>Password</label>
                            <input type="password" value={password} onChange={onPasswordHandler} />
                            <br />
                            <button type="submit">Login</button>
                        </form>
                    </div>
                )}
        </div>
    );
}

export default Login;