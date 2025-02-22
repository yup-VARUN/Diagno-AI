"use client"

import type React from "react"

import { useState, useRef, useEffect, useCallback } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent } from "@/components/ui/card"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Send, User, Mic, Plus } from "lucide-react"
import { ScrollArea } from "@/components/ui/scroll-area"

interface Message {
  id: string
  content: string
  role: "user" | "assistant"
  timestamp: Date
}

interface Chat {
  id: string
  name: string
  messages: Message[]
}

export default function ChatPage() {
  const [chats, setChats] = useState<Chat[]>([
    {
      id: "1",
      name: "Initial Chat",
      messages: [
        {
          id: "1",
          content: "Hello! I'm DiagnAI, your personal health assistant. How can I help you today?",
          role: "assistant",
          timestamp: new Date(),
        },
      ],
    },
  ])
  const [currentChatId, setCurrentChatId] = useState("1")
  const [input, setInput] = useState("")
  const [isListening, setIsListening] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const currentChat = chats.find((chat) => chat.id === currentChatId) || chats[0]

  const scrollToBottom = useCallback(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [])

  useEffect(() => {
    scrollToBottom()
  }, [scrollToBottom])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim()) return

    const newMessage: Message = {
      id: Date.now().toString(),
      content: input,
      role: "user",
      timestamp: new Date(),
    }

    setChats((prevChats) =>
      prevChats.map((chat) =>
        chat.id === currentChatId ? { ...chat, messages: [...chat.messages, newMessage] } : chat,
      ),
    )
    setInput("")

    // Simulate AI response
    setTimeout(() => {
      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: "I understand your concern. Could you please provide more details about your symptoms?",
        role: "assistant",
        timestamp: new Date(),
      }
      setChats((prevChats) =>
        prevChats.map((chat) =>
          chat.id === currentChatId ? { ...chat, messages: [...chat.messages, aiMessage] } : chat,
        ),
      )
    }, 1000)
  }

  const handleMicClick = () => {
    if (!isListening) {
      setIsListening(true)
      const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)()
      recognition.lang = "en-US"
      recognition.start()

      recognition.onresult = (event: SpeechRecognitionEvent) => {
        const transcript = event.results[0][0].transcript
        setInput(transcript)
      }

      recognition.onend = () => {
        setIsListening(false)
      }
    } else {
      setIsListening(false)
    }
  }

  const createNewChat = () => {
    const newChat: Chat = {
      id: Date.now().toString(),
      name: `Chat ${chats.length + 1}`,
      messages: [],
    }
    setChats((prevChats) => [...prevChats, newChat])
    setCurrentChatId(newChat.id)
  }

  const handleDiagnoseNow = () => {
    // Functionality to be implemented
    console.log("Diagnose Now button clicked")
  }

  return (
    <div className="flex h-screen bg-zinc-950">
      {/* Sidebar */}
      <div className="w-64 bg-zinc-900 p-4 flex flex-col">
        <Button onClick={createNewChat} className="w-full mb-4">
          <Plus className="w-4 h-4 mr-2" /> New Chat
        </Button>
        <ScrollArea className="flex-grow">
          {chats.map((chat) => (
            <Button
              key={chat.id}
              variant="ghost"
              className={`w-full justify-start mb-2 ${currentChatId === chat.id ? "bg-zinc-800" : ""}`}
              onClick={() => setCurrentChatId(chat.id)}
            >
              {chat.name}
            </Button>
          ))}
        </ScrollArea>
        <Button onClick={handleDiagnoseNow} className="w-full mt-4 bg-green-600 hover:bg-green-700">
          Diagnose Now
        </Button>
      </div>

      {/* Chat Interface */}
      <div className="flex-1 flex flex-col">
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {currentChat.messages.map((message) => (
            <div
              key={message.id}
              className={`flex items-start gap-3 ${message.role === "assistant" ? "justify-start" : "justify-end"}`}
            >
              {message.role === "assistant" && (
                <Avatar>
                  <AvatarFallback>AI</AvatarFallback>
                  <AvatarImage src="/ai-avatar.png" />
                </Avatar>
              )}
              <Card className={`max-w-[80%] ${message.role === "user" ? "bg-blue-600" : "bg-zinc-800"}`}>
                <CardContent className="p-3">
                  <p className="text-sm text-white">{message.content}</p>
                </CardContent>
              </Card>
              {message.role === "user" && (
                <Avatar>
                  <AvatarFallback>
                    <User className="w-4 h-4" />
                  </AvatarFallback>
                </Avatar>
              )}
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>
        <div className="p-4 border-t border-zinc-800">
          <form onSubmit={handleSubmit} className="flex gap-2">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your message..."
              className="flex-1"
            />
            <Button
              type="button"
              size="icon"
              onClick={handleMicClick}
              variant={isListening ? "destructive" : "default"}
            >
              <Mic className="w-4 h-4" />
            </Button>
            <Button type="submit" size="icon">
              <Send className="w-4 h-4" />
            </Button>
          </form>
        </div>
      </div>
    </div>
  )
}
