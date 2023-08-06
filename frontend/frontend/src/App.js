import './App.css';
import AuthContext, { AuthProvider } from './context/AuthContext';
import HomePage from './pages/homePage';
import LoginPage from './pages/loginPage';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import { Header } from './components/Header';
import { useContext } from 'react';

function App() {
  let {user} = useContext(AuthContext)
  console.log('user:', user)
  return (
    <div className="App">
      <BrowserRouter>
          <AuthProvider>
          <Header />
          <Routes>
            <Route path='/' element={!user ? <Navigate replace to='/login'/> : <HomePage/>}/>
            <Route path='/login' element={<LoginPage/>}/>
          </Routes>
          </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
