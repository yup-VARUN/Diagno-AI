"use client"

import { useRef } from "react"
import Image from "next/image"
import { motion, useScroll, useTransform } from "framer-motion"
import { Brain, Stethoscope, ClipboardCheck, Activity } from "lucide-react"

const achievements = [
  { icon: <Brain className="w-6 h-6" />, label: "AI Powered", value: "24/7" },
    { icon: <Stethoscope className="w-6 h-6" />, label: "Health Insights", value: "100+" },
    { icon: <ClipboardCheck className="w-6 h-6" />, label: "Symptoms Analyzed", value: "1000+" },
    { icon: <Activity className="w-6 h-6" />, label: "Active Users", value: "10K+" },
]

export default function AboutSection() {
  const ref = useRef(null)
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  })

  const y = useTransform(scrollYProgress, [0, 1], [100, -100])
  const opacity = useTransform(scrollYProgress, [0, 0.3, 0.6, 1], [0, 1, 1, 0])

  return (
    <section ref={ref} id="about" className="py-20 relative overflow-hidden">
      <div className="container mx-auto px-4">
        <motion.div className="grid md:grid-cols-2 gap-12 items-center" style={{ y, opacity }}>
          <div className="relative">
            <div className="absolute inset-0 bg-gradient-to-br from-white/10 to-white/0 rounded-3xl transform -rotate-6"></div>
            <Image
              src="/placeholder.svg?height=600&width=600"
              alt="drannel"
              width={600}
              height={600}
              className="rounded-3xl relative z-10"
            />
          </div>
          <div>
            <h2 className="text-4xl md:text-5xl font-bold mb-6">About DiagnAI</h2>
            <p className="text-lg mb-6 text-zinc-300">
            Understanding your health shouldn’t be complicated. Our AI-driven platform analyzes your past conversations to generate detailed and personalized diagnosis reports, giving you clarity and actionable insights. 
          Whether you're tracking symptoms, monitoring health patterns, or seeking guidance, our intelligent system ensures accuracy, privacy, and ease of use.
            </p>
            <p className="text-lg mb-8 text-zinc-300">
            With a seamless and intuitive experience, our AI continuously learns from your interactions to provide smarter, data-driven health assessments. Whether you need a quick overview or an in-depth analysis, our technology translates your conversations into meaningful reports, helping you stay informed and proactive about your well-being. Your health, your data—analyzed with precision and care.
            </p>
            <div className="grid grid-cols-2 gap-6">
              {achievements.map((achievement, index) => (
                <motion.div
                  key={achievement.label}
                  className="bg-zinc-900/50 rounded-lg p-4 border border-white/10"
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  viewport={{ once: true }}
                >
                  <div className="flex items-center mb-2">
                    <div className="mr-2 text-white">{achievement.icon}</div>
                    <div className="text-2xl font-bold">{achievement.value}</div>
                  </div>
                  <div className="text-sm text-zinc-400">{achievement.label}</div>
                </motion.div>
              ))}
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  )
}

