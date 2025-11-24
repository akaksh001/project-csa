"""
USING AI TO PREDICT
Takes someone's details and predicts if they get loan
"""

import joblib
import numpy as np

class LoanPredictor:
    """
    Simple loan predictor
    """
    
    def __init__(self):
        """Load the saved AI brain"""
        print("📦 Loading AI brain...")
        self.model = joblib.load('loan_model.pkl')
        self.scaler = joblib.load('loan_scaler.pkl')
        print("✅ AI ready!")
    
    def predict(self, salary, credit_score, loan_amount, job_years, debt):
        """
        Predict if person gets loan
        
        Give me:
        - salary: How much they earn per month ?
        - credit_score: Their credit score (300-850)?
        - loan_amount: How much they want ?
        - job_years: How long they've worked ?
        - debt: How much debt they have ?
        
        I'll tell you:
        - approved: Yes or No 
        - confidence: How sure I am (0-100%)
        - reasons: Why I decided this
        """
        
        # Put all details in order
        details = np.array([[salary, credit_score, loan_amount, job_years, debt]])
        
        # Scale it (same way we did during training)
        details_scaled = self.scaler.transform(details)
        
        # Ask AI: Should we approve?
        prediction = self.model.predict(details_scaled)[0]
        
        # Ask AI: How confident are you?
        confidence = self.model.predict_proba(details_scaled)[0]
        confidence_percent = confidence[prediction] * 100
        
        # Convert 1/0 to Yes/No
        approved = (prediction == 1)
        
        # EXPLAIN WHY (Simple logic)
        reasons = []
        
        # Credit Score check
        if credit_score >= 750:
            reasons.append("✅ Excellent credit score!")
        elif credit_score >= 650:
            reasons.append("✅ Good credit score")
        else:
            reasons.append("❌ Low credit score (need 650+)")
        
        # Can they afford?
        monthly_payment = loan_amount / 240  # Assume 20 year loan
        if monthly_payment < salary * 0.4:
            reasons.append("✅ Can afford monthly payments")
        else:
            reasons.append("❌ Monthly payment too high for salary")
        
        # Job experience
        if job_years >= 3:
            reasons.append("✅ Good job experience")
        elif job_years >= 1:
            reasons.append("✅ Has job experience")
        else:
            reasons.append("❌ Need at least 1 year job experience")
        
        # Existing debt
        if debt < salary * 0.3:
            reasons.append("✅ Low existing debt")
        elif debt < salary * 0.4:
            reasons.append("⚠️ Moderate existing debt")
        else:
            reasons.append("❌ Too much existing debt")
        
        # Return everything
        return {
            'approved': approved,
            'confidence': confidence_percent,
            'reasons': reasons
        }


# Testing the Ai
if __name__ == "__main__":
    predictor = LoanPredictor()
    
    print("\n" + "="*50)
    print("TEST 1: Good Applicant")
    print("="*50)
    
    result = predictor.predict(
        salary=100000,
        credit_score=750,
        loan_amount=2000000,
        job_years=5,
        debt=20000
    )
    
    print(f"\n{'✅ APPROVED' if result['approved'] else '❌ REJECTED'}")
    print(f"Confidence: {result['confidence']:.1f}%")
    print("\nReasons:")
    for reason in result['reasons']:
        print(f"  {reason}")
    
    print("\n" + "="*50)
    print("TEST 2: Weak Applicant")
    print("="*50)
    
    result = predictor.predict(
        salary=30000,
        credit_score=580,
        loan_amount=3000000,
        job_years=0,
        debt=15000
    )
    
    print(f"\n{'✅ APPROVED' if result['approved'] else '❌ REJECTED'}")
    print(f"Confidence: {result['confidence']:.1f}%")
    print("\nReasons:")
    for reason in result['reasons']:
        print(f"  {reason}")
