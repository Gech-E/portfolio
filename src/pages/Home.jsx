import React from 'react'
import { motion } from 'framer-motion'
import { ArrowRight, Code, Database, Brain, TrendingUp, Github, Linkedin, Mail } from 'lucide-react'
import { Link } from 'react-router-dom'

const Home = () => {
  const skills = [
    { icon: Code, title: 'Full Stack', description: 'Flask, FastAPI, React, Typescript, next.js' },
    { icon: Database, title: 'Backend', description: 'PostgreSQL, REST APIs' },
    { icon: Brain, title: 'AI/ML/DL', description: 'TensorFlow, PyTorch, scikit-learn, opencv' },
    { icon: TrendingUp, title: 'Data Science', description: 'Pandas, NumPy, Visualization' },
  ]

  return (
    <div>
      {/* Hero Section */}
      <section className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-50 via-white to-primary-50 pt-16">
        <div className="section-container text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <h1 className="text-5xl md:text-7xl font-bold text-gray-900 mb-6">
              Hi, I'm a{' '}
              <span className="text-primary-600">Full Stack Developer</span>
            </h1>
            <p className="text-xl md:text-2xl text-gray-600 mb-8 max-w-3xl mx-auto">
              Specializing in Python, React, next.js AI/ML, and Data Science
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
              <Link to="/projects" className="btn-primary inline-flex items-center gap-2">
                View Projects <ArrowRight size={20} />
              </Link>
              <Link to="/contact" className="btn-secondary">
                Get In Touch
              </Link>
            </div>
            <div className="flex justify-center gap-6">
              <a href="https://github.com/Gech-E" target="_blank" rel="noopener noreferrer" className="text-gray-600 hover:text-primary-600 transition-colors" title="GitHub">
                <Github size={24} />
              </a>
              <a href="https://www.linkedin.com/in/getachew99" target="_blank" rel="noopener noreferrer" className="text-gray-600 hover:text-primary-600 transition-colors" title="LinkedIn">
                <Linkedin size={24} />
              </a>
              <a href="mailto:getachewekubay8@gmail.com" className="text-gray-600 hover:text-primary-600 transition-colors" title="Email">
                <Mail size={24} />
              </a>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Skills Section */}
      <section className="section-container bg-white">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <h2 className="text-4xl font-bold text-center mb-12 text-gray-900">
            My Expertise
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {skills.map((skill, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="card text-center"
              >
                <div className="flex justify-center mb-4">
                  <div className="p-3 bg-primary-100 rounded-full">
                    <skill.icon className="text-primary-600" size={32} />
                  </div>
                </div>
                <h3 className="text-xl font-semibold mb-2 text-gray-900">{skill.title}</h3>
                <p className="text-gray-600">{skill.description}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* Quick Stats */}
      <section className="section-container bg-gray-100">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            className="card"
          >
            <h3 className="text-4xl font-bold text-primary-600 mb-2">5+</h3>
            <p className="text-gray-600">Projects Completed</p>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
            className="card"
          >
            <h3 className="text-4xl font-bold text-primary-600 mb-2">4</h3>
            <p className="text-gray-600">Technologies Mastered</p>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2 }}
            className="card"
          >
            <h3 className="text-4xl font-bold text-primary-600 mb-2">100%</h3>
            <p className="text-gray-600">Code Quality</p>
          </motion.div>
        </div>
      </section>
    </div>
  )
}

export default Home



