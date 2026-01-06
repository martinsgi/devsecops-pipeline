# DevSecOps CI/CD Pipeline

A production-ready CI/CD pipeline demonstrating automated security scanning and cloud deployment.

## 🎯 Project Overview

This project implements a complete DevSecOps pipeline that:
- Automatically tests code on every push
- Scans for security vulnerabilities
- Builds and scans Docker containers
- Deploys to AWS using Infrastructure as Code

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Application | Python Flask |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud | AWS (EC2, VPC) |
| IaC | Terraform |
| Monitoring | Prometheus + Grafana |

## 🔒 Security Tools

- **Bandit** - Python static code analysis
- **Safety** - Dependency vulnerability scanning
- **Trivy** - Container image scanning
- **TruffleHog** - Secrets detection

## 📁 Project Structure

```
devsecops-pipeline/
├── app/                    # Flask application
│   ├── app.py
│   └── requirements.txt
├── tests/                  # Unit tests
│   └── test_app.py
├── docker/                 # Docker configuration
│   └── Dockerfile
├── infrastructure/         # Terraform IaC
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── .github/workflows/      # CI/CD pipeline
│   └── cicd.yml
├── monitoring/             # Prometheus & Grafana
└── docs/                   # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker Desktop
- Git

### Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/devsecops-pipeline.git
cd devsecops-pipeline

# Install dependencies
pip install -r app/requirements.txt

# Run the application
python app/app.py

# Visit http://localhost:5000
```

### Run Tests

```bash
pip install pytest
pytest tests/ -v
```

## 📊 Pipeline Stages

1. **Test** - Run unit tests
2. **SAST Scan** - Static security analysis
3. **Build** - Create Docker image
4. **Container Scan** - Scan for vulnerabilities
5. **Deploy** - Push to AWS

## 🏗️ Project Status

- [x] Phase 1: Flask Application
- [x] Phase 2: Docker Containerization
- [x] Phase 3: CI/CD Pipeline
- [ ] Phase 4: Infrastructure as Code
- [ ] Phase 5: Monitoring
- [ ] Phase 6: Documentation

## 📝 License

MIT License

## 👤 Author

Martin Garcia

---

*Built as a DevSecOps learning project*
