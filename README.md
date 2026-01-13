# Machine Learning Deployment Workshop

This workshop demonstrates an **end-to-end machine learning deployment pipeline**, starting from a simple ML model and ending with a **Kubernetes-deployed API** that is consumed by a lightweight user interface.

The focus is not model accuracy, but **how to turn a model into a reliable product**.

---

## 🎯 What You Will Learn

- How to package an ML model as an API
- How Docker enables reproducible environments
- How Kubernetes manages deployment, scaling, and recovery
- Why UI should communicate with APIs, not directly with models
- How local Kubernetes (Minikube) mirrors real production setups

---

## 🧱 Project Structure
```text
tech_talk_model_deployment/
├── data/                 # Training data
├── models/               # Trained model artifacts
├── src/
│   ├── train.py          # Model training script
│   └── app.py            # FastAPI application
├── ui/
│   └── app.py            # Streamlit UI (local)
├── k8s/
│   ├── deployment.yaml   # Kubernetes Deployment
│   └── service.yaml      # Kubernetes Service
├── requirements.txt
└── README.md
```

---

## 📋 Prerequisites

### **VSCode**
- Download: [https://code.visualstudio.com/](https://code.visualstudio.com/)

### **Python**
- Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### **Docker Desktop**
- Download: [https://www.docker.com/](https://www.docker.com/)
- **Setup Check:** 
```bash
  docker --version
```
- ⚠️ Make sure Docker Desktop is running.

### **For Mac** (these commands will be run in the terminal)

#### **Homebrew**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- **Setup Check:** 
```bash
  brew --version
```

#### **Minikube**
```bash
brew install minikube
```
- **Setup Check:** 
```bash
  minikube version
```

#### **Kubectl**
```bash
brew install kubectl
```
- **Setup Check:** 
```bash
  kubectl version --client
```

---

## 🐍 Environment Setup

### Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

---