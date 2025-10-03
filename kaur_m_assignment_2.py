from dataclasses import dataclass

# -----------------------------
# 1) PLAN DATA (fees / waivers)
# -----------------------------

FEES = {
    "Basic": 3.95,
    "Basic Plus": 11.95,
    "Preferred": 16.95,
    "Ultimate": 30.95,
}

# Minimum balance to waive the monthly fee (None = no standard waiver)
WAIVE_MIN = {
    "Basic": None,
    "Basic Plus": 3000.0,
    "Preferred": 4000.0,
    "Ultimate": 6000.0,
}

# -----------------------------
# 2) RECOMMENDATION RULES
# -----------------------------

def recommend_account(tx_count, non_prf_abm_used, e_transfer_used):
    """
    Rule set (simplified from the brief):
      - Basic: up to 12 debits, no non-PRF ABMs, no e-Transfers
      - Basic Plus: up to 25 debits, no non-PRF ABMs, no e-Transfers
      - Preferred: unlimited debits, unlimited e-Transfers, some non-PRF ABM use
      - Ultimate: unlimited e-Transfers + more non-PRF ABMs

    Preference:
      - Choose Preferred unless Ultimate is clearly required.

    Assumption (since we don't ask *how many* non-PRF ABMs):
      - If BOTH (non-PRF ABM is used) AND (e-Transfers are used), usage is heavy -> Ultimate.
      - Else if ANY of: tx_count > 25 OR non_prf_abm_used OR e_transfer_used -> Preferred.
      - Else if tx_count > 12 -> Basic Plus.
      - Else -> Basic.
    """
    if non_prf_abm_used and e_transfer_used:
        return "Ultimate"
    if tx_count > 25 or non_prf_abm_used or e_transfer_used:
        return "Preferred"
    if tx_count > 12:
        return "Basic Plus"
    return "Basic"


def compute_monthly_fee(plan_name, cust_age, student_flag, avg_closing_balance):
    fee = FEES[plan_name]
    waive_threshold = WAIVE_MIN[plan_name]

    # Waive by minimum balance (if the plan has one)
    if waive_threshold is not None and avg_closing_balance >= waive_threshold:
        return 0.00

    # Seniors (>= 60): Basic is waived; others get 30% off
    if cust_age >= 60:
        if plan_name == "Basic":
            return 0.00
        fee = fee * 0.70
    else:
        # Students (< 60 only) get 50% off
        if student_flag:
            fee = fee * 0.50

    # Round to nearest cent
    return round(fee, 2)

# -----------------------------
# 3) INTERACTIVE CLI (assignment output)
# -----------------------------

def run_cli():
    age = int(input("Enter customer age: "))

    is_student = False
    if age < 60:
        student_ans = input("Is the customer a student? (y/n): ").strip().lower()
        is_student = (student_ans == "y")

    debit_tx = int(input("Number of debit transactions per month: "))
    uses_non_prf_abm = input("Does the customer use non-PRF ABMs? (y/n): ").strip().lower() == "y"
    sends_etransfer = input("Does the customer send e-Transfers? (y/n): ").strip().lower() == "y"
    closing_balance = float(input("Typical monthly closing balance: "))

    account = recommend_account(debit_tx, uses_non_prf_abm, sends_etransfer)
    monthly_fee = compute_monthly_fee(account, age, is_student, closing_balance)

    print()
    print("-" * 40)
    print(f"Recommended account: {account} Account")
    print(f"Monthly fee: ${monthly_fee:,.2f}")

# -----------------------------
# 4) BUILT-IN TESTS
# -----------------------------

@dataclass
class AccountTest:
    name: str
    debit_tx: int
    non_prf_abm: bool
    e_transfer: bool
    expected_account: str

@dataclass
class FeeTest:
    name: str
    account: str
    age: int
    is_student: bool
    closing_balance: float
    expected_fee: float

ACCOUNT_TESTS = [
    AccountTest("T1 Basic: low usage", 8, False, False, "Basic"),
    AccountTest("T2 Basic Plus: mid usage", 20, False, False, "Basic Plus"),
    AccountTest("T3 Preferred: unlimited debits needed", 40, False, False, "Preferred"),
    AccountTest("T4 Preferred: needs non-PRF ABM", 10, True, False, "Preferred"),
    AccountTest("T5 Ultimate: non-PRF ABM + e-Transfers", 10, True, True, "Ultimate"),
    AccountTest("T6 Preferred: e-Transfers only", 10, False, True, "Preferred"),
]

FEE_TESTS = [
    FeeTest("A Senior Basic waived", "Basic", 65, False, 0.0, 0.00),
    FeeTest("B Student Preferred 50% off", "Preferred", 22, True, 0.0, round(16.95 * 0.50, 2)),  # 8.48
    FeeTest("C Preferred waived by balance", "Preferred", 45, False, 4200.0, 0.00),
    FeeTest("D Basic Plus no discounts", "Basic Plus", 59, False, 2000.0, 11.95),
    FeeTest("E Senior Ultimate 30% off", "Ultimate", 60, False, 0.0, round(30.95 * 0.70, 2)),   # 21.67
    FeeTest("F Ultimate waived by balance", "Ultimate", 35, True, 6000.0, 0.00),
]

def floats_close(a, b):
    # Tolerance for safe float comparison
    diff = a - b
    if diff < 0:
        diff = -diff
    return diff < 0.005

def run_tests():
    print("Running built-in tests...\n")

    # Account recommendation tests
    passed = 0
    total = 0
    print("Account Type Tests")
    print("------------------")
    for t in ACCOUNT_TESTS:
        total = total + 1
        actual = recommend_account(t.debit_tx, t.non_prf_abm, t.e_transfer)
        ok = (actual == t.expected_account)
        status = "PASS" if ok else "FAIL"
        if ok:
            passed = passed + 1
        print(f"{status} | {t.name}: expected={t.expected_account}, actual={actual}")
    print()

    # Monthly fee tests
    print("Monthly Fee Tests")
    print("-----------------")
    for t in FEE_TESTS:
        total = total + 1
        actual_fee = compute_monthly_fee(t.account, t.age, t.is_student, t.closing_balance)
        ok = floats_close(actual_fee, t.expected_fee)
        status = "PASS" if ok else "FAIL"
        if ok:
            passed = passed + 1
        print(f"{status} | {t.name}: expected=${t.expected_fee:.2f}, actual=${actual_fee:.2f}")

    print()
    print(f"Summary: {passed}/{total} tests passed.")

# -----------------------------
# 5) ENTRY POINT
# -----------------------------

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1].lower() == "test":
        run_tests()
    else:
        run_cli()