"use client"

import { useRouter } from "next/navigation"
import BackgroundPaths from "./components/BackgroundPaths"
import Header from "./components/Header"
import AboutSection from "./components/AboutSection"
import ContactSection from "./components/ContactSection"
import Footer from "./components/Footer"

export default function Home() {
  const router = useRouter()

  const handleStartChat = () => {
    router.push("/signup")
  }

  return (
    <div className="min-h-screen text-white relative">
      <Header />
      <BackgroundPaths
        title="DiagnAI"
        subtitle="AI That Understands, Diagnoses, and Empowers"
        buttonText="Start Chat"
        onButtonClick={handleStartChat}
      />
      <main className="relative z-10">
        <AboutSection />
        <ContactSection />
      </main>
      <Footer />
    </div>
  )
}

