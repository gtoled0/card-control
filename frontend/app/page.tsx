"use client"
import { useState } from "react"
import api from "../lib/api"

export default function Home(){
  const [u,setU]=useState("")
  const [p,setP]=useState("")
  const [alerts,setAlerts]=useState([])

  const login=async()=>{
    const res=await api.post("/auth/login",{username:u,password:p})
    localStorage.setItem("token",res.data.access_token)
  }

  const loadAlerts=async()=>{
    const res=await api.get("/alerts/")
    setAlerts(res.data)
  }

  return(
    <div style={{padding:40}}>
      <h1>Fintech Enterprise</h1>
      <input placeholder="user" onChange={e=>setU(e.target.value)}/><br/>
      <input type="password" placeholder="pass" onChange={e=>setP(e.target.value)}/><br/>
      <button onClick={login}>Login</button>
      <button onClick={loadAlerts}>Load Alerts</button>
      <ul>
        {alerts.map((a:any)=><li key={a.id}>{a.message} - {a.level}</li>)}
      </ul>
    </div>
  )
}