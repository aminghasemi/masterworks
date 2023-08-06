import React from 'react'
import { Link } from 'react-router-dom'
import { useContext } from 'react'
import AuthContext from '../context/AuthContext'
export const Header = () => {
  let {user, logOutUser} = useContext(AuthContext)
  return (
    <div>
        <Link to='/'>Home Page</Link>
        <span> | </span>
        {user ? (
          <button onClick={logOutUser}>Log out</button>
        ): (
        <Link to='/login'>Login</Link>
        )}
        {user && <p>Hello {user.user_id}</p>}
        
    </div>
  )
}
