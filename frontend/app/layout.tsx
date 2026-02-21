"use client"
import { useState } from "react"

export default function RootLayout({children}:{children:React.ReactNode}){
  const [dark,setDark]=useState(true)
  return(
    <html>
      <body style={{background:dark?"#111":"#fff",color:dark?"#fff":"#000"}}>
        <button onClick={()=>setDark(!dark)} style={{margin:20}}>Toggle Theme</button>
        {children}
      </body>
    </html>
  )
}