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
