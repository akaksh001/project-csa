"""
TEACH AI TO PREDICT LOANS
Shows AI examples so it learns the pattern
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib

print("🎓 Teaching AI to predict loans ")

# Load the fake data we created
data = pd.read_csv('loan_data.csv')
print(f"✅ Loaded {len(data)} people")

# Separate: What we KNOW about people (X) vs What we want to PREDICT (y)
X = data[['monthly_salary', 'credit_score', 'loan_amount', 'job_years', 'existing_debt']]
y = data['approved']

print("\n📊 What AI will learn from:")
print(f"  - Monthly salary")
print(f"   - Credit score")
print(f"  - Loan amount wanted")
print(f"   - Job experience (years)")
print(f"   - Existing debt")

# Split into two groups:
# - 80% to TEACH the AI (training data)
# - 20% to TEST the AI (testing data)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\n✅ Teaching group: {len(X_train)} people")
print(f"✅ Testing group: {len(X_test)} people")

# Make numbers similar scale (helps AI learn better)
# Example: Salary (50,000) and Credit Score (700) become similar
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\n🧠 Training AI model...")

# Creating an AI model (Random Forest = Asks 100 smart questions)
model = RandomForestClassifier(
    n_estimators=100,  # Ask 100 questions
    random_state=42
)

# TEACH: Show AI the training data
model.fit(X_train, y_train)

print("✅ AI is trained!")

# TEST: Can AI predict correctly on people it never saw?
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"\n📊 AI Accuracy: {accuracy*100:.1f}%")
print(f"   (Out of 100 predictions, {int(accuracy*100)} are correct)")

# If accuracy is good, save the AI
if accuracy > 0.80:
    print("\n✅ Good accuracy! Saving AI brain...")
    joblib.dump(model, 'loan_model.pkl')
    joblib.dump(scaler, 'loan_scaler.pkl')
    print("✅ AI saved to: loan_model.pkl")
else:
    print("\n⚠️ Accuracy too low. Try generating more data.")

print("\n" + "="*50)
print("🎉 TRAINING COMPLETE!")
print("="*50)
