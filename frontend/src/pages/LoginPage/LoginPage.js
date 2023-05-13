import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [isFormValid, setIsFormValid] = useState(true); // 입력값 유효성 상태를 관리하는 상태 변수

    const onEmailHandler = (event) => {
        setEmail(event.target.value);
    };

    const onPasswordHandler = (event) => {
        setPassword(event.target.value);
    };

    const onSubmitHandler = (event) => {
        event.preventDefault();

        // 입력값 유효성 검사
        if (!email || !password) {
            setIsFormValid(false);
            return;
        }

        axios.get('/user/get-csrf-token/') // Get CSRF token from the server
            .then(response => {
                const csrfToken = response.data.csrfToken;

                // Send registration data to the backend
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
                {!isFormValid && <p>모든 값을 입력해주세요</p>} {/* 입력값 유효성 에러 메시지 표시 */}
                <br />
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default Login;
