# kaur-manpreet-assignment-2

**Student:** Manpreet Kaur  
**Project folder (exact):** `kaur-manpreet-assignment-2`  
**Main Python file (exact):** `kaur_m_assignment_2.py`

---

## 1) Overview

This program recommends a **PRF chequing account** and computes the **monthly fee** from user inputs:

- Age (and student status if age < 60)  
- Number of debit transactions per month  
- Use of **non-PRF ABMs** (y/n)  
- Use of **e-Transfers** (y/n)  
- Typical monthly closing balance

**Assignment requirements satisfied**

- Prompts appear in the **required order**; the **student?** prompt is asked **only if age < 60**.  
- Prefer **Preferred** over **Ultimate** unless Ultimate is clearly required.  
- Senior (≥ 60) and Student (< 60) discounts implemented.  
- Minimum-balance **fee waivers** implemented.  
- Output format: **blank line**, **40 dashes**, then:
  ```
  Recommended account: <Type> Account
  Monthly fee: $<two decimals>
  ```
- Prohibited keywords/functions not used: `continue`, `break`, `exit()`.

---

## 2) Tools

- **VS Code**  
- **Git Bash** (Windows)  
- **Git**  
- **Python 3.10+** (3.11 recommended)

---

## 3) Project Structure

```
kaur-manpreet-assignment-2/
├─ .git/                    # full Git history (MUST be included in the submission ZIP)
├─ README.md
└─ kaur_m_assignment_2.py
```

> If you create a virtual environment (e.g., `.venv/`), do **not** include it in the ZIP.

---

## 4) How to Run (Windows + Git Bash)

Open a terminal in this folder and run:

```bash
cd "/d/Bonus Tasks/F work/2025/9-Sept/Python Programming/kaur-manpreet-assignment-2"
python kaur_m_assignment_2.py
```

**Inputs requested (in order)**

1. Enter customer age  
2. (If age < 60) Is the customer a student? (y/n)  
3. Number of debit transactions per month  
4. Does the customer use non-PRF ABMs? (y/n)  
5. Does the customer send e-Transfers? (y/n)  
6. Typical monthly closing balance

**Output example**

```
----------------------------------------
Recommended account: Preferred Account
Monthly fee: $8.47
```

---

## 5) Business Rules Implemented

### Base monthly fees
| Plan       | Fee  |
|------------|-----:|
| Basic      |  3.95 |
| Basic Plus | 11.95 |
| Preferred  | 16.95 |
| Ultimate   | 30.95 |

### Minimum balance to waive fee
| Plan       | Balance to Waive |
|------------|-----------------:|
| Basic      | —                |
| Basic Plus | 3000             |
| Preferred  | 4000             |
| Ultimate   | 6000             |

### Recommendation logic (summary)

- If **non-PRF ABM** **and** **e-Transfers** are used → **Ultimate**  
- Else if **debits > 25** *or* **non-PRF ABM** *or* **e-Transfers** → **Preferred**  
- Else if **debits > 12** → **Basic Plus**  
- Else → **Basic**  
- Prefer **Preferred** unless **Ultimate** is clearly required.

### Discounts & waivers

- If balance ≥ plan’s waiver threshold → **fee = $0.00**  
- **Seniors (≥ 60):** Basic **waived**; other plans **30% off**  
- **Students (< 60):** **50% off**  
- Fees rounded to **two decimals**.

---

## 6) Test Cases (and actual results)

> The program includes a built-in test suite. Run it with:
>
> ```bash
> python kaur_m_assignment_2.py test
> ```

### A) Account recommendation

| ID | Inputs (age, student, debits, non-PRF, e-Transfers, balance) | Expected | Actual | Result |
|----|---------------------------------------------------------------|----------|--------|--------|
| T1 | 25, y, 8, n, n, 0                                            | Basic        | Basic        | PASS |
| T2 | 40, n, 20, n, n, 0                                           | Basic Plus   | Basic Plus   | PASS |
| T3 | 30, n, 40, n, n, 0                                           | Preferred    | Preferred    | PASS |
| T4 | 35, n, 10, y, n, 0                                           | Preferred    | Preferred    | PASS |
| T5 | 28, n, 10, y, y, 0                                           | Ultimate     | Ultimate     | PASS |
| T6 | 22, y, 10, n, y, 0                                           | Preferred    | Preferred    | PASS |

### B) Monthly fee

| ID | Account | Age | Student | Balance | Expected Fee | Actual Fee | Result |
|----|---------|----:|:-------:|--------:|-------------:|-----------:|:------:|
| F1 | Basic      | 65 | n | 0    | $0.00  | $0.00  | PASS |
| F2 | Preferred  | 22 | y | 0    | $8.47  | $8.47  | PASS |
| F3 | Preferred  | 45 | n | 4200 | $0.00  | $0.00  | PASS |
| F4 | Basic Plus | 59 | n | 2000 | $11.95 | $11.95 | PASS |
| F5 | Ultimate   | 60 | n | 0    | $21.66 | $21.66 | PASS |
| F6 | Ultimate   | 35 | y | 6000 | $0.00  | $0.00  | PASS |

**Automated test run summary**
```
Running built-in tests...

Account Type Tests
------------------
PASS | T1 Basic: low usage: expected=Basic, actual=Basic
PASS | T2 Basic Plus: mid usage: expected=Basic Plus, actual=Basic Plus
PASS | T3 Preferred: unlimited debits needed: expected=Preferred, actual=Preferred
PASS | T4 Preferred: needs non-PRF ABM: expected=Preferred, actual=Preferred
PASS | T5 Ultimate: non-PRF ABM + e-Transfers: expected=Ultimate, actual=Ultimate
PASS | T6 Preferred: e-Transfers only: expected=Preferred, actual=Preferred

Monthly Fee Tests
-----------------
PASS | A Senior Basic waived: expected=$0.00, actual=$0.00
PASS | B Student Preferred 50% off: expected=$8.47, actual=$8.47
PASS | C Preferred waived by balance: expected=$0.00, actual=$0.00
PASS | D Basic Plus no discounts: expected=$11.95, actual=$11.95
PASS | E Senior Ultimate 30% off: expected=$21.66, actual=$21.66
PASS | F Ultimate waived by balance: expected=$0.00, actual=$0.00

Summary: 12/12 tests passed.
```

---

## 7) Daily Git Workflow (small, descriptive commits)

From the project folder:

```bash
# Example “chunked” history
git add -A
git commit -m "Step 1: Scaffold project (.gitignore, README, initial module)"
git push

git add kaur_m_assignment_2.py
git commit -m "Step 2: Add input prompts in required order"
git push

git add kaur_m_assignment_2.py
git commit -m "Step 3: Define plan fees and min-balance waivers"
git push

git add kaur_m_assignment_2.py
git commit -m "Step 4: Implement account recommendation logic"
git push

git add kaur_m_assignment_2.py
git commit -m "Step 5: Add fee calculation (waivers + senior/student discounts)"
git push

git add kaur_m_assignment_2.py
git commit -m "Step 6: Finalize CLI output format"
git push

