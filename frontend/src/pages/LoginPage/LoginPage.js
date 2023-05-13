import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    
    const onEmailHandler = (event) => {
        setEmail(event.target.value);
    };

    const onPasswordHandler = (event) => {
        setPassword(event.target.value);
    };

    const onSubmitHandler = (event) => {
        event.preventDefault();

        //header , footer x , 유효성 검사(빈칸)는 백엔드에서 처리하는 것으로 변경

        axios.get('/user/get-csrf-token/') // CSRF token 서버로 부터 불러옴
            .then(response => {
                const csrfToken = response.data.csrfToken;

                // login url 설정
                axios.post('/user/login/', {
                    email: email,
                    password: password,
                },
                {
                    headers: {
                        'X-CSRFToken': csrfToken
                    }
                })

                    .then((response) => {
                        if (response.data.success) {
                            alert(response.data.message);
                            navigate('/');
                        } else {
                            alert(response.data.message);
                        }
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            })
            .catch((error) => {
                console.error(error);
            });
    };

    return (
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
    );
}

export default Login;
