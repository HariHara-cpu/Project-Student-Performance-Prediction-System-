# Student Performance Prediction System

## Overview
A machine learning project that predicts student final grades in Portuguese language courses using data science and statistical analysis. The project implements the complete data science lifecycle including data preparation, exploratory data analysis, model development, and evaluation.

## Features
- **Data Analysis**: In-depth exploration of 649 student records with 30+ features
- **Predictive Modeling**: Linear regression model to predict final grades (G3) with multiple performance metrics
- **Statistical Testing**: Correlation analysis, outlier detection, and feature importance evaluation
- **Dimensionality Reduction**: PCA implementation for improved model performance
- **Data Visualization**: 30+ visualizations for insights (distributions, correlations, performance metrics)

## Dataset
- **Source**: Kaggle(https://www.kaggle.com/datasets/larsen0966/student-performance-data-set)
- **Samples**: 649 students
- **Features**: 30+ attributes including demographics, family background, study habits, and academic performance

## Methodology
1. **Business Understanding**: Define prediction goals and success criteria
2. **Data Understanding**: Exploratory analysis and statistical summary
3. **Data Preparation**: Encoding categorical variables and outlier detection
4. **EDA**: Distribution analysis and correlation studies
5. **Modeling**: Linear regression with feature standardization
6. **Evaluation**: R² score, MAE, MSE metrics
7. **Deployment**: Model saved for production use

## Technologies
- Python, Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn (visualization)
- Joblib (model persistence)

## Model Performance
- Achieves robust predictions with multiple evaluation metrics
- Identifies key factors influencing student academic performance
- Ready for deployment in educational analytics applications

## Files
- `Untitled.ipynb` - Complete analysis notebook
- `student_model.joblib` - Trained ML model
- `model_metadata.joblib` - Model metadata and configuration
- `student-por.csv` - Dataset
