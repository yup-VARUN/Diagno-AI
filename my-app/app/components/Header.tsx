"use client"

import { useState, useEffect } from "react"
import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Menu, LogIn } from "lucide-react"

export default function Header() {
  const [isScrolled, setIsScrolled] = useState(false)
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 0)
    }
    window.addEventListener("scroll", handleScroll)
    return () => window.removeEventListener("scroll", handleScroll)
  }, [])

  const handleNavClick = (e: React.MouseEvent<HTMLAnchorElement>, id: string) => {
    e.preventDefault()
    setIsMenuOpen(false)
    
    // Find the element
    const element = document.getElementById(id)
    if (!element) return

    // Get header height (for offset)
    const header = document.querySelector('header')
    const headerHeight = header ? header.getBoundingClientRect().height : 0

    // Calculate the final position
    const elementPosition = element.getBoundingClientRect().top
    const offsetPosition = elementPosition + window.pageYOffset - headerHeight

    // Smooth scroll to element
    window.scrollTo({
      top: offsetPosition,
      behavior: "smooth"
    })
  }

  return (
    <header className={`fixed w-full z-50 transition-all duration-300 ${isScrolled ? "bg-black/90 backdrop-blur-sm" : "bg-transparent"}`}>
      <div className="container mx-auto px-4 py-4 flex justify-between items-center">
        <Link href="/" className="text-3xl font-bold tracking-tighter">
          DiagnAI
        </Link>
        <div className="md:hidden">
          <Button variant="ghost" size="icon" onClick={() => setIsMenuOpen(!isMenuOpen)}>
            <Menu />
          </Button>
        </div>
        <nav
          className={`${
            isMenuOpen ? "block" : "hidden"
          } md:block absolute md:relative top-full left-0 w-full md:w-auto bg-black/90 backdrop-blur-sm md:bg-transparent`}
        >
          <ul className="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-8 p-4 md:p-0">
            <li>
              <Link 
                href="/" 
                className="hover:text-blue-400 transition-colors" 
                onClick={() => setIsMenuOpen(false)}
              >
                Home
              </Link>
            </li>
            <li>
              <a
                href="#about"
                className="hover:text-blue-400 transition-colors"
                onClick={(e) => handleNavClick(e, "about")}
              >
                About
              </a>
            </li>
            <li>
              <a
                href="#contact"
                className="hover:text-blue-400 transition-colors"
                onClick={(e) => handleNavClick(e, "contact")}
              >
                Contact
              </a>
            </li>
          </ul>
        </nav>
        <Button asChild variant="outline" className="hidden md:flex items-center gap-2">
          <Link href="/login">
            <LogIn className="w-4 h-4" />
            Login
          </Link>
        </Button>
      </div>
    </header>
  )
}
