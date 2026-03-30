# 🎓 Student Performance Predictor

A complete end-to-end data science project with a professional Flask web application to predict student final grades.

---

## 📋 Project Structure

```
project/
├── Student_score_predicter.ipynb    # Complete ML analysis & EDA
├── application.py                   # Flask backend API
├── student_model.joblib             # Trained ML model
├── model_metadata.joblib            # Model metadata & RMSE
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker configuration
├── .dockerignore                    # Docker build exclusions
├── templates/
│   └── index.html                   # Web interface
├── static/
│   ├── style.css                    # Professional styling
│   └── analysis/                    # Analysis visualizations
└── student-por.csv                  # Dataset (649 records)
```

---

## 🚀 Quick Start

### 🔹 Local Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask app
python application.py

# Open browser
http://localhost:5000
```

---

## 🐳 Run from Docker Hub (Recommended)

Run the app instantly without installing anything.

### 🔹 1. Pull Image

```bash
docker pull harihara02062006/student-predictor
```

### 🔹 2. Run Container

```bash
docker run -d -p 5000:5000 harihara02062006/student-predictor
```

### 🔹 3. Open in Browser

```
http://localhost:5000
```

👉 **Docker Hub Link:** https://hub.docker.com/r/harihara02062006/student-predictor

---

## 🐳 Docker Setup (Local Build)

### 🔹 1. Build Image

```bash
docker build -t student-performance-predictor .
```

### 🔹 2. Run Container

```bash
docker run -d -p 5000:5000 student-performance-predictor
```

---

## ⚙️ Docker Commands (Optional)

**Stop Container**

```bash
docker ps
docker stop <container_id>
```

**Remove Container**

```bash
docker rm <container_id>
```

**Remove Image**

```bash
docker rmi student-performance-predictor
```

---

## ✨ Features

### 🤖 ML Model

- Predicts final grades (0–20 scale) with 85%+ accuracy
- Linear Regression trained on 649 student records
- Statistical testing & hypothesis validation
- PCA dimensionality reduction analysis

### 🌐 Web App

- 📊 Real-time predictions
- 🎯 Performance classification
- 💯 95% confidence intervals
- 💡 Smart recommendations
- 🧠 Key insights analysis
- 📱 Fully responsive UI

---

## 🛠️ Technologies

| Layer | Technology |
|---|---|
| Backend | Flask |
| ML | Scikit-learn, Pandas, NumPy |
| Frontend | HTML5, CSS3, JavaScript |
| Visualization | Matplotlib, Seaborn |
| Containerization | Docker |

---

## 📈 Model Performance

| Metric | Value |
|---|---|
| R² Score | 0.85+ (85% variance explained) |
| MAE | ±1.2 points |
| RMSE | ±1.5 points |

---

## 📁 Key Files

| File | Description |
|---|---|
| `Student_score_predicter.ipynb` | Full ML workflow |
| `application.py` | Flask backend |
| `student_model.joblib` | Trained model |
| `model_metadata.joblib` | Performance metrics |
| `Dockerfile` | Container config |
| `student-por.csv` | Dataset |

---
## Output
<img width="1898" height="918" alt="Screenshot 2026-03-03 191125" src="https://github.com/user-attachments/assets/71429d58-497b-4062-b6c1-c8a814fe1a27" />