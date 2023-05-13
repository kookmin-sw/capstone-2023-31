import React, { useState } from 'react';
import axios from 'axios';
import { useLocation, useNavigate } from "react-router-dom";
import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";

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
    const onSubmitHandler = (event) => {
        event.preventDefault();

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
        
        <div style={{
            display: 'flex', justifyContent: 'center', alignItems: 'center',
            width: '100%', height: '100vh'
        }}>
            <form style={{ display: 'flex', flexDirection: 'column' }}
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
            </form>
        </div>
        //ㅎㅔ더 푸터 추가해야행!!
    )
}

export default RegisterPage;
