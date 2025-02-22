import "./globals.css"
import type { Metadata } from "next"
import { Space_Grotesk } from "next/font/google"
import type React from "react"

const spaceGrotesk = Space_Grotesk({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "DiagnAI - AI-Powered Health Assistant",
  description: "Get personalized health insights and diagnosis assistance with DiagnAI",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className={`${spaceGrotesk.className} bg-white dark:bg-black text-black dark:text-white`}>{children}</body>
    </html>
  )
}

