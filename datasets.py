"""
CREATE FAKE LOAN DATA
Makes 500 fake people who want loans
"""

import pandas as pd
import numpy as np

print("🏦 Making fake loan applications...")

# Set random seed (makes it the same every time)
np.random.seed(42)

# How many fake people?
n = 500

# Create fake people with their details
people = pd.DataFrame({

    # How much they earn per month (₹30,000 to ₹2,00,000)
    'monthly_salary': np.random.randint(30000, 200000, n),
    
    # Credit score (300 to 850)
    # Higher = better (like a report card for money)
    'credit_score': np.random.randint(300, 850, n),
    
    # How much loan they want (₹1,00,000 to ₹50,00,000)
    'loan_amount': np.random.randint(100000, 5000000, n),
    
    # How many years they've worked (0 to 30 years)
    'job_years': np.random.randint(0, 30, n),
    
    # How much debt they already have (₹0 to ₹1,00,000)
    'existing_debt': np.random.randint(0, 100000, n),

})

print(f"✅ Created {n} fake people")

# DECIDE WHO GETS LOAN (Simple Rules)
# IF Bank say yes:
# 1. Credit score is good (650+)
# 2. They can afford monthly payment (salary/3 > loan/100)
# 3. They have job experience (1+ years)
# 4. Not too much existing debt

people['approved'] = (
    (people['credit_score'] >= 650) &                    # Good credit
    (people['monthly_salary'] * 3 > people['loan_amount'] / 100) &  # Can afford
    (people['job_years'] >= 1) &                         # Has job
    (people['existing_debt'] < people['monthly_salary'] * 0.4)  # Not too much debt
).astype(int)  # Convert True/False to 1/0

print(f"✅ {people['approved'].sum()} people approved")
print(f"✅ {len(people) - people['approved'].sum()} people rejected")

# Saving to file
people.to_csv ('loan_data.csv', index = False)
print("✅ saved to: loan_data.csv")

print("\nFirst 5 people:")
print(people.head())
