"""
WEBSITE FOR LOAN PREDICTION
Simple webpage where people can check if they get loan
"""

import gradio as gr
from prediction import LoanPredictor

# Load the AI
predictor = LoanPredictor()

def check_loan(salary, credit_score, loan_amount, job_years, debt):
    """
    Function that runs when you click "Check" button
    """
    
    # Get prediction
    result = predictor.predict(salary, credit_score, loan_amount, job_years, debt)
    
    # Make it look nice
    if result['approved']:
        output = f"""
# ✅ LOAN APPROVED!

## Confidence: {result['confidence']:.1f}%

### Why you got approved:
"""
    else:
        output = f"""
# ❌ LOAN REJECTED

## Confidence: {result['confidence']:.1f}%

### Why you got rejected:
"""
    
    # Add reasons
    for reason in result['reasons']:
        output += f"\n{reason}"
    
    return output

# Creating website
demo = gr.Interface(
    fn=check_loan,  # Function to call
    
    # Input sliders
    inputs=[
        gr.Slider(25000, 200000, 80000, 5000, label="💰 Monthly Salary (₹)"),
        gr.Slider(300, 850, 700, 10, label="💳 Credit Score"),
        gr.Slider(100000, 5000000, 2000000, 100000, label="🏠 Loan Amount Wanted (₹)"),
        gr.Slider(0, 30, 5, 1, label="💼 Job Experience (years)"),
        gr.Slider(0, 100000, 20000, 5000, label="📊 Existing Debt (₹)")
    ],
    
    # Output area
    outputs=gr.Markdown(label="Result"),
    
    # Page title
    title="🏦 Loan Approval Checker",
    description="Enter your details below and check if you'll get the loan!",
    
    # Example buttons
    examples=[
        [100000, 750, 2000000, 5, 20000],  # Good person
        [30000, 580, 3000000, 0, 15000],   # Weak person
        [150000, 820, 4000000, 10, 10000], # Excellent person
    ]
)

# Start the website
if __name__ == "__main__":
    print("\n🌐 Starting website...")
    print("📱 URL: http://localhost:7860")
    print("\n💡 Press Ctrl+C to stop")
    
    demo.launch(
        share=False,
        inbrowser=True, 
        server_port=7860
    )
