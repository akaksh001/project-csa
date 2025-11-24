# Loan Approval Prediction System

> AI-powered loan approval prediction using Machine Learning with 87% accuracy

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![ML](https://img.shields.io/badge/ML-Random%20Forest-orange.svg)]()
[![Accuracy](https://img.shields.io/badge/Accuracy-87%25-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [About]
- [Features]
- [Installation]
- [Usage]
- [Project-Structure]
- [How-It-Works]
- [Model-Performance]
- [Screenshots]
- [Technologies]
- [Author]
- [License]

---

## 🎯 About

This project uses **Machine Learning** to predict whether a loan application will be **approved** or **rejected**.

### Problem Statement
Banks process thousands of loan applications daily. Manual review is:
- ⏰ Time-consuming
- 🎯 Inconsistent
- 💰 Expensive

### Solution
An AI system that:
- ⚡ Gives instant predictions (< 1 second)
- 📊 96% accuracy
- 💡 Explains every decision
- 🌐 Easy-to-use web interface

---

## ✨ Features

- ✅ **Instant Predictions** - Results in under 1 second
- ✅ **High Accuracy** - 96% success rate
- ✅ **Transparent AI** - Explains why approved/rejected
- ✅ **User-Friendly** - No coding needed
- ✅ **Real-time Analysis** - 5 financial parameters
- ✅ **Confidence Score** - Shows AI certainty
- ✅ **Example Cases** - Pre-loaded test scenarios

---

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Setup (3 Steps)

**1. Clone or Download**

**2. Install Dependencies**

**3. Verify Installation**

You should see:
-pandas==2.3.3
-numpy==2.3.5
-scikit-learn==1.7.2
-gradio==6.0.0
-joblib==1.5.2
---

## 🚀 Usage

### Step 1: Generate Training Data

**Output:**
Making fake loan applications...
✅ Created 500 fake people
✅ 287 people approved
✅ 213 people rejected
✅ Saved to: loan_data.csv


### Step 2: Train the Model

**Output:**
🎓 Teaching AI to predict loans...
-- Loaded 500 people
-- Training AI model...
-- AI trained!
-- AI Accuracy: 96.0%
-- AI saved to: loan_model.pkl

### Step 3: Launch Web App

**Output:**

Starting website...
-- URL: http://localhost:7860
-- Press Ctrl+C to stop


**Then open in browser:** http://localhost:7860

### Using the Web Interface

1. **Enter applicant details** using sliders:
   -  Monthly Salary
   -  Credit Score
   -  Loan Amount
   -  Job Experience
   -  Existing Debt

2. **Click "Submit"**

3. **View Results:**
   - ✅/❌ Approved or Rejected
   -  Confidence percentage
   -  Detailed reasons
   -  Improvement tips

---

## 📁 Project Structure

loan-approval-prediction/
│
├── 1_datasets.py # Generate synthetic data
├── 2_train_model.py # Train ML model
├── 3_prediction.py # Prediction logic
├── 4_interface.py # Web interface
│
├── loan_data.csv # Generated dataset (500 records)
├── loan_model.pkl # Trained model
├── loan_scaler.pkl # Feature scaler
│
├── requirements.txt # Python dependencies
├── README.md # This file
└── screenshots/ # Project images
├── homepage.png
├── approved.png
├── rejected.png
└── terminal.png


### File Descriptions

| File | Purpose |
|------|---------|
| `1_create_data.py` | Generates 500 synthetic loan applications |
| `2_train_model.py` | Trains Random Forest ML model (87% accuracy) |
| `3_predictor.py` | Contains prediction logic and test cases |
| `4_app.py` | Creates interactive web interface (Gradio) |
| `requirements.txt` | Python package dependencies |
| `README.md` | Project documentation (this file) |

---

## 🧠 How It Works

### Data Generation
Creates 500 fake loan applicants
↓
Each with 5 features: salary, credit score, loan amount, job years, debt
↓
Applies realistic approval rules


### Model Training
Splits data: 80% training (400), 20% testing (100)
↓
Trains Random Forest Classifier (100 decision trees)
↓
Each tree votes: approve or reject
↓
Majority wins → Final decision


### Prediction
User enters 5 details
↓
Normalize values (same scale as training)
↓
Pass through 100 trees
↓
Trees vote (e.g., 87 approve, 13 reject)
↓
Result: Approved with 87% confidence
↓
Display reasons why


### Why Random Forest?

Think of it as **100 smart experts voting**:

- **Expert 1:** "Is credit score > 700?"
- **Expert 2:** "Is salary > ₹80,000?"
- **Expert 3:** "Is loan < ₹30,00,000?"
- ... (97 more experts)

**Final Decision:** Majority vote = Result

**Why this works:** 100 experts rarely all wrong!

---

## 📊 Model Performance

### Accuracy
- **Overall Accuracy:** 96.0%
- **Meaning:** Out of 100 predictions, 96 are correct

### Feature Importance

Which factors matter most for approval?

| Factor | Importance |
|--------|-----------|
|  Credit Score | 35% (Most important!) |
|  Monthly Salary | 28% |
|  Loan Amount | 20% |
|  Job Years | 12% |
|  Existing Debt | 5% (Least important) |

**Insight:** Credit score + salary = 63% of decision

---

## 📸 Screenshots

### Homepage with Input Sliders
![Homepage](screenshots/homepage.png)
*Clean interface on web* 

### Approved Case
![Approved](screenshots/approved.png)
*applicant gets instant approval*

### Rejected Case
![Rejected](screenshots/rejected.png)
*applicatn gets rejected with reasons and improvement tips*

### Terminal Output
![Terminal](screenshots/terminal.png)
*Model training showing 96% accuracy*

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.8+ | Programming language |
| **pandas** | 2.3.3 | Data manipulation |
| **numpy** | 2.3.5 | Numerical computing |
| **scikit-learn** | 1.7.2 | Machine Learning library |
| **Gradio** | 6.0.0 | Web interface framework |
| **joblib** | 1.5.2 | Model serialization |

---

## 🔮 Future Enhancements

### Planned Features
- [ ] Add more input features (age, education, property value)
- [ ] Increase training data to 5000+ samples
- [ ] Try advanced algorithms (XGBoost, Neural Networks)
- [ ] Add data visualization (charts and graphs)
- [ ] Generate PDF reports
- [ ] Email notifications
- [ ] Mobile app version
- [ ] Cloud deployment

---

## 👨‍💻 Author

**Your Full Name** Akaksh Samdani

🎓 **Academic Information:**
- **Registration Number:** 25BCG10033
- **College:** VIT Bhopal University
- **Course:** B.Tech Computer Science & Engineering In Gaming Technology
- **Year:** First Year (2025-26)
- **Semester:** 1st Semester

📧 **Contact:**
- **Email:** [akisamdani@gmail.com]
- **GitHub:** [@akaksh001](https://github.com/akaksh001)

📅 **Project Date:** November 2025

---

## 📄 License

This project is licensed under the **MIT License** for educational purposes.

**Educational Use:**
- ✅ Free to use for learning
- ✅ Free to modify for educational projects
- ✅ Share with attribution
- ❌ NOT for commercial use
- ❌ NOT for real banking decisions

**Disclaimer:**
This is a demonstration system. Real loan decisions require:
- Comprehensive financial data
- Regulatory compliance
- Legal oversight
- Security measures

---

## 🙏 Acknowledgments

- **scikit-learn Team** - For excellent ML library
- **Gradio Team** - For amazing UI framework
- **Python Community** - For great documentation
- **My Professor** - For guidance

---


**Have questions?**
-  Read this README thoroughly
-  Email: [akisamdani@gmail.com]

**Found a bug?**
- Describe the problem
- Include error message
- Steps to reproduce

---

## ⭐ Show Your Support

If you found this helpful:
-  **Star this repository**
-  **Fork it**
-  **Share with classmates**
-  **Provide feedback**

---

**Thank you for checking out this project!** 🎉

---

*Last Updated: November 24, 2025*  
*Version: 1.0.0*  
*Status: ✅ Complete and Working*

---

**Made with by Akaksh**
