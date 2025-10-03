"""
Assignment 2 – PRF Account Recommender
Author: Manpreet Kaur
"""

# 1) INPUTS (in the required order)
age = int(input("Enter customer age: "))

is_student = False
if age < 60:
    student_ans = input("Is the customer a student? (y/n): ").strip().lower()
    is_student = (student_ans == "y")

debit_tx = int(input("Number of debit transactions per month: "))
uses_non_prf_abm = input("Does the customer use non-PRF ABMs? (y/n): ").strip().lower() == "y"
sends_etransfer = input("Does the customer send e-Transfers? (y/n): ").strip().lower() == "y"
closing_balance = float(input("Typical monthly closing balance: "))

# 2) PLAN DATA
FEES = {"Basic": 3.95, "Basic Plus": 11.95, "Preferred": 16.95, "Ultimate": 30.95}
WAIVE_MIN = {"Basic": None, "Basic Plus": 3000.0, "Preferred": 4000.0, "Ultimate": 6000.0}


# 3) RECOMMENDATION
def recommend_account(tx_count, non_prf_abm_used, e_transfer_used):
    # Prefer Preferred; Ultimate only if clearly necessary
    if non_prf_abm_used and e_transfer_used:
        return "Ultimate"
    if tx_count > 25 or non_prf_abm_used or e_transfer_used:
        return "Preferred"
    if tx_count > 12:
        return "Basic Plus"
    return "Basic"

account = recommend_account(debit_tx, uses_non_prf_abm, sends_etransfer)

# 4) FEE CALCULATION
def compute_monthly_fee(plan_name, cust_age, student_flag, avg_closing_balance):
    fee = FEES[plan_name]
    threshold = WAIVE_MIN[plan_name]

    # Waive fee if balance meets threshold (where applicable)
    if threshold is not None and avg_closing_balance >= threshold:
        return 0.00

    # Seniors (>=60)
    if cust_age >= 60:
        if plan_name == "Basic":
            return 0.00
        fee = fee * 0.70
    else:
        # Students (<60)
        if student_flag:
            fee = fee * 0.50

    return round(fee, 2)

monthly_fee = compute_monthly_fee(account, age, is_student, closing_balance)