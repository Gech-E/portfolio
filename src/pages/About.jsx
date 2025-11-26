import React from 'react'
import { motion } from 'framer-motion'
import { Code, Database, Brain, TrendingUp, FlaskConical, Globe, GitBranch } from 'lucide-react'

const About = () => {
  const techStack = [
    { category: 'Backend', icon: FlaskConical, items: ['Flask', 'FastAPI', 'Python', 'PostgreSQL', 'SQLAlchemy', 'REST APIs'] },
    { category: 'Frontend', icon: Globe, items: ['React', 'JavaScript', 'HTML/CSS', 'Typescript', 'next.js' 'Tailwind CSS', 'Vite'] },
    { category: 'AI/ML/DL', icon: Brain, items: ['TensorFlow', 'PyTorch', 'Opencv', 'Scikit-learn', 'Keras', 'Neural Networks'] },
    { category: 'Data Science', icon: TrendingUp, items: ['Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Jupyter'] },
    { category: 'Tools', icon: GitBranch, items: ['Git', 'Docker', 'Postman', 'VS Code', 'Linux'] },
  ]

  return (
    <div className="pt-16">
      <section className="section-container">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="max-w-4xl mx-auto"
        >
          <h1 className="text-5xl font-bold text-center mb-8 text-gray-900">
            About Me
          </h1>
          <div className="card mb-12">
            <p className="text-lg text-gray-700 mb-4 leading-relaxed">
              I'm a passionate full-stack developer with expertise in Python-based backend development
              and modern React & next.js frontend applications. My journey in software development has led me to
              specialize in building robust, scalable web applications while also diving deep into the
              world of artificial intelligence, machine learning, and data science.
            </p>
            <p className="text-lg text-gray-700 mb-4 leading-relaxed">
              With a strong foundation in Flask and FastAPI for backend development, I create efficient
              RESTful APIs that power modern web applications. I'm proficient in PostgreSQL database
              design and optimization, ensuring data integrity and performance.
            </p>
            <p className="text-lg text-gray-700 leading-relaxed">
              On the frontend, I leverage React & next.js to build interactive, responsive user interfaces that
              provide exceptional user experiences. My AI/ML expertise allows me to integrate intelligent
              features into applications, while my data science skills help me derive insights and make
              data-driven decisions.
            </p>
          </div>

          <h2 className="text-3xl font-bold text-center mb-8 text-gray-900">
            Technical Skills
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {techStack.map((tech, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="card"
              >
                <div className="flex items-center gap-3 mb-4">
                  <tech.icon className="text-primary-600" size={24} />
                  <h3 className="text-xl font-semibold text-gray-900">{tech.category}</h3>
                </div>
                <div className="flex flex-wrap gap-2">
                  {tech.items.map((item, itemIndex) => (
                    <span
                      key={itemIndex}
                      className="px-3 py-1 bg-primary-100 text-primary-700 rounded-full text-sm font-medium"
                    >
                      {item}
                    </span>
                  ))}
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>
    </div>
  )
}

export default About



