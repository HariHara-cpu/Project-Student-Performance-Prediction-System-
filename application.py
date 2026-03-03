"""
Student Performance Predictor - Flask Application
A web application to predict student final grades based on various factors
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import joblib
from datetime import datetime

# Initialize Flask app
application = Flask(__name__)
app = application  # for gunicorn compatibility

# Load the trained model and scaler
try:
    model = joblib.load('student_model.joblib')
    metadata = joblib.load('model_metadata.joblib')
    
    # The joblib scaler is the one correctly fit on the 7 model features
    # We recreate predictions using the model directly (it was trained without scaling)
    scaler = None  # will handle below
    
    print("✓ Model loaded successfully via joblib!")
except FileNotFoundError as e:
    print(f"✗ Error loading model files: {e}")
    model = None
    metadata = None

# Feature names as used in the model training
FEATURES = ['studytime', 'absences', 'G1', 'G2', 'Medu', 'Fedu', 'failures']
FEATURE_RANGES = {
    'studytime': (1, 4),
    'absences': (0, 93),
    'G1': (0, 20),
    'G2': (0, 20),
    'Medu': (0, 4),
    'Fedu': (0, 4),
    'failures': (0, 4)
}


@app.route('/')
def index():
    """Render the main prediction page"""
    return render_template('index.html')


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    API endpoint to make predictions
    Expects JSON payload with student data
    """
    try:
        data = request.get_json()
        
        # Validate input data
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        # Extract features and validate ranges
        student_data = {}
        for feature in FEATURES:
            if feature not in data:
                return jsonify({'success': False, 'error': f'Missing feature: {feature}'}), 400
            
            try:
                value = float(data[feature])
                min_val, max_val = FEATURE_RANGES[feature]
                
                if not (min_val <= value <= max_val):
                    return jsonify({
                        'success': False,
                        'error': f'{feature} must be between {min_val} and {max_val}'
                    }), 400
                
                student_data[feature] = value
            except ValueError:
                return jsonify({
                    'success': False,
                    'error': f'{feature} must be a valid number'
                }), 400
        
        # Prepare input for model — NO scaling needed (model was trained on raw features)
        X = pd.DataFrame([student_data])[FEATURES]
        
        # Make prediction
        prediction = model.predict(X)[0]
        prediction = max(0, min(20, prediction))  # Clamp between 0-20
        
        # Use actual RMSE from training metadata for accurate confidence interval
        rmse = metadata['rmse']
        confidence_lower = max(0, prediction - 1.96 * rmse)
        confidence_upper = min(20, prediction + 1.96 * rmse)
        
        # Determine performance level and risk assessment
        if prediction >= 16:
            performance = "Excellent"
            risk_level = "VERY LOW RISK"
            recommendation = "Exceptional performance! Maintain this trajectory."
            color = "#27ae60"  # Green
        elif prediction >= 14:
            performance = "Very Good"
            risk_level = "LOW RISK"
            recommendation = "Strong performance! Continue with current efforts."
            color = "#2ecc71"  # Light Green
        elif prediction >= 12:
            performance = "Good"
            risk_level = "LOW RISK"
            recommendation = "Good progress! Stay consistent with your efforts."
            color = "#f39c12"  # Orange
        elif prediction >= 10:
            performance = "Satisfactory"
            risk_level = "MEDIUM RISK"
            recommendation = "Adequate performance. Consider improving study habits."
            color = "#e67e22"  # Dark Orange
        else:
            performance = "Needs Improvement"
            risk_level = "HIGH RISK"
            recommendation = "Urgent: Seek additional help and tutoring support."
            color = "#e74c3c"  # Red
        
        # Generate insights
        insights = []
        
        if student_data['G1'] < 10 or student_data['G2'] < 10:
            insights.append("⚠️ Previous grades show academic struggle")
        elif student_data['G1'] >= 14 and student_data['G2'] >= 14:
            insights.append("✓ Consistent high performance in previous periods")
        
        if student_data['absences'] > 10:
            insights.append(f"⚠️ High absences ({int(student_data['absences'])}) may impact performance")
        elif student_data['absences'] <= 3:
            insights.append("✓ Excellent attendance record")
        
        if student_data['studytime'] <= 2:
            insights.append("⚠️ Consider increasing study time for better results")
        else:
            insights.append("✓ Good study habits observed")
        
        if student_data['failures'] > 0:
            insights.append(f"⚠️ Past failures ({int(student_data['failures'])}) require attention")
        else:
            insights.append("✓ No previous class failures")
        
        avg_parent_edu = (student_data['Medu'] + student_data['Fedu']) / 2
        if avg_parent_edu >= 3:
            insights.append("✓ Strong parental education background")
        
        return jsonify({
            'success': True,
            'prediction': round(prediction, 2),
            'confidence_lower': round(confidence_lower, 2),
            'confidence_upper': round(confidence_upper, 2),
            'performance': performance,
            'risk_level': risk_level,
            'recommendation': recommendation,
            'color': color,
            'insights': insights,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Prediction error: {str(e)}'
        }), 500


@app.route('/api/info')
def info():
    """API endpoint to get application information"""
    return jsonify({
        'app_name': 'Student Performance Predictor',
        'version': '1.0.0',
        'description': 'Predict student final grades based on study habits and academic history',
        'features': FEATURES,
        'feature_ranges': FEATURE_RANGES
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'success': False, 'error': 'Page not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'success': False, 'error': 'Internal server error'}), 500


if __name__ == '__main__':
    if model is None or metadata is None:
        print("\n✗ ERROR: Model files not found!")
        print("  Make sure 'student_model.joblib' and 'model_metadata.joblib' are in the project directory")
    else:
        print("\n" + "="*60)
        print("🚀 Student Performance Predictor - Flask App")
        print("="*60)
        print("Starting Flask server...")
        print("Visit: http://localhost:5000")
        print("="*60 + "\n")
        app.run()