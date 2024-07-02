import React from 'react'
import { BrowserRouter, Routes, Navigate, Route } from 'react-router-dom'
import Home from "./pages/Home"
import Register from "./pages/Register"
import Login from "./pages/Login"
import ProtectedRoute from "./components/protectedRoute"
import NotFound from './pages/NotFound'


function Logout(){
  localStorage.clear()
  return <Navigate to="/Login" />
}

function RegisterAndLogout(){
  localStorage.clear()
  return <Register />

}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path = "/" element= {<ProtectedRoute>
          <Home />
          </ProtectedRoute>} />
      
      <Route path= "/Login" element={<Login/>}/>
      <Route path= "/register" element={<RegisterAndLogout/>}/>
      <Route path= "*" element={<NotFound/>}/>
      </Routes>


    </BrowserRouter>
  )
}

export default App
