import React, { useState } from 'react'
import { motion } from 'framer-motion'
import { Mail, Github, Linkedin, Send, MapPin, Phone } from 'lucide-react'

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  })

  const handleSubmit = (e) => {
    e.preventDefault()
    // Handle form submission
    console.log('Form submitted:', formData)
    alert('Thank you for your message! I will get back to you soon.')
    setFormData({ name: '', email: '', message: '' })
  }

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    })
  }

  return (
    <div className="pt-16">
      <section className="section-container">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="max-w-4xl mx-auto"
        >
          <h1 className="text-5xl font-bold text-center mb-4 text-gray-900">
            Get In Touch
          </h1>
          <p className="text-xl text-center text-gray-600 mb-12">
            I'm open to new opportunities and collaborations
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Contact Info */}
            <div className="space-y-6">
              <motion.div
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.2 }}
                className="card"
              >
                <h3 className="text-2xl font-bold mb-6 text-gray-900">Contact Information</h3>
                <div className="space-y-4">
                  <div className="flex items-center gap-3">
                    <Mail className="text-primary-600" size={20} />
                    <a href="mailto:getachewekubay8@gmail.com" className="text-gray-700 hover:text-primary-600">
                      getachewekubay8@gmail.com
                    </a>
                  </div>
                  <div className="flex items-center gap-3">
                    <MapPin className="text-primary-600" size={20} />
                    <span className="text-gray-700">Available for Remote Work</span>
                  </div>
                </div>
                <div className="mt-6 pt-6 border-t border-gray-200">
                  <h4 className="font-semibold mb-4 text-gray-900">Connect with me</h4>
                  <div className="flex gap-4">
                    <a
                      href="https://github.com/Gech-E"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="p-2 bg-gray-100 rounded-lg hover:bg-primary-100 transition-colors"
                      title="GitHub"
                    >
                      <Github className="text-gray-700" size={24} />
                    </a>
                    <a
                      href="https://www.linkedin.com/in/getachew99"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="p-2 bg-gray-100 rounded-lg hover:bg-primary-100 transition-colors"
                      title="LinkedIn"
                    >
                      <Linkedin className="text-gray-700" size={24} />
                    </a>
                    <a
                      href="mailto:getachewekubay8@gmail.com"
                      className="p-2 bg-gray-100 rounded-lg hover:bg-primary-100 transition-colors"
                      title="Email"
                    >
                      <Mail className="text-gray-700" size={24} />
                    </a>
                  </div>
                </div>
              </motion.div>
            </div>

            {/* Contact Form */}
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.3 }}
              className="card"
            >
              <h3 className="text-2xl font-bold mb-6 text-gray-900">Send a Message</h3>
              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-2">
                    Name
                  </label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  />
                </div>
                <div>
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
                    Email
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  />
                </div>
                <div>
                  <label htmlFor="message" className="block text-sm font-medium text-gray-700 mb-2">
                    Message
                  </label>
                  <textarea
                    id="message"
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    required
                    rows={5}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  />
                </div>
                <button
                  type="submit"
                  className="btn-primary w-full flex items-center justify-center gap-2"
                >
                  Send Message <Send size={20} />
                </button>
              </form>
            </motion.div>
          </div>
        </motion.div>
      </section>
    </div>
  )
}

export default Contact



