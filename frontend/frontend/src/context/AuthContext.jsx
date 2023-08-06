import { createContext, useState, useEffect } from "react";
import jwtDecode from "jwt-decode";
import {useNavigate} from 'react-router-dom'



const  AuthContext = createContext();
export default AuthContext;



export const AuthProvider = ({children}) => {
    
    const [authTokens, setAuthTokens] = useState(() => localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
    const [user, setUser] = useState(() => localStorage.getItem('authTokens') ? jwtDecode(localStorage.getItem('authTokens')) : null)
    const navigate = useNavigate()
    const loginUser = async(e ) => {
        e.preventDefault()
        const response = await fetch('http://127.0.0.1:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'email':e.target.email.value, 'password': e.target.password.value})
        })
        const data = await response.json()
        if (response.status === 200) {
            setAuthTokens(data)
            setUser(jwtDecode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
            navigate('/')
        } else {
            alert('something went wrong!')
        }

        }
    
        let logOutUser = () => {
            setAuthTokens(null)
            setUser(null)
            localStorage.removeItem('authtokens')
            navigate('/login')

        }
    
    const contextData = {
        user: user,
        loginUser:loginUser,
        logOutUser: logOutUser,
    }  
    return (
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}
