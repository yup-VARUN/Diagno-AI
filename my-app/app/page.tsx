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
    <div className="min-h-screen text-white relative overflow-hidden">
      <div className="glow-effect" />
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
      <div className="fixed bottom-0 left-0 right-0 h-64 pointer-events-none">
        <div
          className="absolute inset-0 bg-gradient-to-t from-purple-900 via-purple-600 to-transparent"
          style={{
            filter: "blur(100px)",
          }}
        />
      </div>
    </div>
  )
}
