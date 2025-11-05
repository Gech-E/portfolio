import React from 'react'
import { motion } from 'framer-motion'
import { Github, ExternalLink, FlaskConical, Zap, Brain, BarChart3 } from 'lucide-react'

const Projects = () => {
  const projects = [
    {
      id: 1,
      title: 'Task Management API',
      description: 'A robust RESTful API built with Flask and PostgreSQL for managing tasks, users, and projects. Features include authentication, role-based access control, and real-time updates.',
      tech: ['Flask', 'PostgreSQL', 'SQLAlchemy', 'JWT', 'REST API'],
      icon: FlaskConical,
      color: 'bg-blue-500',
      folder: 'flask-task-api',
    },
    {
      id: 2,
      title: 'E-commerce API',
      description: 'High-performance e-commerce backend built with FastAPI. Includes product management, shopping cart, payment processing, and order tracking with comprehensive documentation.',
      tech: ['FastAPI', 'PostgreSQL', 'Pydantic', 'OpenAPI', 'AsyncIO'],
      icon: Zap,
      color: 'bg-green-500',
      folder: 'fastapi-ecommerce',
    },
    {
      id: 3,
      title: 'Image Classification ML Model',
      description: 'Deep learning model for image classification using Convolutional Neural Networks. Trained on CIFAR-10 dataset with data augmentation and transfer learning techniques.',
      tech: ['TensorFlow', 'Keras', 'CNN', 'Python', 'NumPy'],
      icon: Brain,
      color: 'bg-purple-500',
      folder: 'ml-image-classification',
    },
    {
      id: 4,
      title: 'Sales Analytics Dashboard',
      description: 'Comprehensive data science project analyzing sales data with interactive visualizations, predictive models, and business insights. Includes ETL pipeline and automated reporting.',
      tech: ['Pandas', 'Matplotlib', 'Seaborn', 'Jupyter', 'Scikit-learn'],
      icon: BarChart3,
      color: 'bg-orange-500',
      folder: 'data-science-sales',
    },
  ]

  return (
    <div className="pt-16">
      <section className="section-container">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <h1 className="text-5xl font-bold text-center mb-4 text-gray-900">
            My Projects
          </h1>
          <p className="text-xl text-center text-gray-600 mb-12 max-w-2xl mx-auto">
            A collection of projects showcasing my skills in full-stack development, AI/ML, and data science
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {projects.map((project, index) => (
              <motion.div
                key={project.id}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="card group hover:scale-105 transition-transform duration-300"
              >
                <div className={`${project.color} p-4 rounded-lg mb-4 inline-flex`}>
                  <project.icon className="text-white" size={32} />
                </div>
                <h3 className="text-2xl font-bold mb-3 text-gray-900">{project.title}</h3>
                <p className="text-gray-600 mb-4 leading-relaxed">{project.description}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {project.tech.map((tech, techIndex) => (
                    <span
                      key={techIndex}
                      className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm"
                    >
                      {tech}
                    </span>
                  ))}
                </div>
                <div className="flex gap-4">
                  <a
                    href={`#${project.folder}`}
                    className="flex items-center gap-2 text-primary-600 hover:text-primary-700 font-medium"
                  >
                    <Github size={20} />
                    View Code
                  </a>
                  <a
                    href={`#${project.folder}`}
                    className="flex items-center gap-2 text-primary-600 hover:text-primary-700 font-medium"
                  >
                    <ExternalLink size={20} />
                    View Project
                  </a>
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>
    </div>
  )
}

export default Projects



