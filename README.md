kaur-manpreet-assignment-2

Student: Manpreet Kaur  
Project folder (exact): kaur-manpreet-assignment-2  
Main program file (exact): kaurmassignment_2.py

1) Overview

This program recommends a PRF chequing account and computes the monthly fee from user inputs.

Requirements satisfied

Prompts appear in the required order.
Ask student? only if age < 60.
Prefer Preferred over Ultimate unless Ultimate is clearly required.
Senior (≥ 60) and Student (< 60) discounts applied correctly.
Minimum-balance fee waivers respected.
Output format: a blank line, 40 dashes, then recommendation and monthly fee with $ and two decimals.
Does not use prohibited keywords/functions: continue, break, exit().

2) Tools that will required.
VS Code (text editor)
Git Bash (terminal on Windows)
Git
Python 3.10+ (3.11 recommended)

If you need to install anything, follow your course’s Software Installation Guide.

3) Standards & Conventions

While completing this assessment, follow all course development standards provided by your instructor.  
Prohibited techniques: continue, break, exit().

Inputs requested (in this exact order) 

assignment-2

customer age

(if age < 60) student? (y/n)

number of debit transactions / month

uses non-PRF ABMs? (y/n)

sends e-Transfers? (y/n)

typical monthly closing balance

Required output format (blank line, 40 hyphens, then two lines): 

assignment-2

----------------------------------------
Recommended account: [Account Type] Account
Monthly fee: $[fee with 2 decimals]

Business Rules Implemented

Account features 

assignment-2

		Basic	Basic Plus	Preferred	Ultimate
Debit tx / mth	12	25	Unlimited	Unlimited
Non-PRF ABM / mth	0	0	1	5
e-Transfers / mth	0	0	Unlimited	Unlimited

Base monthly fees & balance waivers 

assignment-2

Plan	Fee	Balance to waive
Basic	3.95	—
Basic Plus	11.95	3000
Preferred	16.95	4000
Ultimate	30.95	6000

Recommendation logic (summary) 

assignment-2

If non-PRF ABM and e-Transfers are used ⇒ Ultimate

Else if debits > 25 OR non-PRF ABM OR e-Transfers ⇒ Preferred

Else if debits > 12 ⇒ Basic Plus

Else ⇒ Basic

Prefer Preferred over Ultimate unless Ultimate is clearly required.

Discounts 

assignment-2

Balance ≥ plan’s minimum ⇒ fee waived

Seniors (≥60): Basic waived; others 30% off

Students (<60): 50% off

Round to nearest cent using Python’s rounding (banker’s rounding note). 

assignment-2

Account Type Test Cases 

assignment-2

Each test records data, expected, and actual result from the program.

ID	Data (age, student, debits, non-PRF, e-Transfers, balance)	Expected	Actual	Outcome
T1	25, y, 8, n, n, 0	Basic		Basic		PASS
T2	40, n, 20, n, n, 0	Basic Plus	Basic Plus	PASS
T3	30, n, 40, n, n, 0	Preferred	Preferred	PASS
T4	35, n, 10, y, n, 0	Preferred	Preferred	PASS
T5	28, n, 10, y, y, 0	Ultimate	Ultimate	PASS
T6	22, y, 10, n, y, 0	Preferred	Preferred	PASS
Monthly Fee Test Cases 

assignment-2

ID	Account	Age	Student	Balance	Expected Fee	Actual Fee	Outcome
F1	Basic		65	n	0	$0.00	$0.00	PASS
F2	Preferred	22	y	0	$8.47	$8.47	PASS
F3	Preferred	45	n	4200	$0.00	$0.00	PASS
F4	Basic Plus	59	n	2000	$11.95	$11.95	PASS
F5	Ultimate	60	n	0	$21.66	$21.66	PASS
F6	Ultimate	35	y	6000	$0.00	$0.00	PASS
