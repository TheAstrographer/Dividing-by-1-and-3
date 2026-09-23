from fractions import Fraction
from decimal import Decimal, getcontext

print("=" * 72)
print("DIVIDING BY 1 AND 3  – Residual Limit (Pure Python)")
print("=" * 72)

# ------------------------------------------------------------------
# 1. Fundamental residual limit
# ------------------------------------------------------------------
print("\n1. Residual Limit")
print("   lim (n → ∞)  1/10^n  =  0\n")

getcontext().prec = 40

print(f"{'n':>4} | {'1/10^n':>18} | {'S_n = 1 - 10^{-n}':>25}")
print("-" * 55)

for n in [1, 2, 3, 5, 8, 12, 20, 30]:
    residual = Decimal(10) ** -n
    s_n = Decimal(1) - residual
    print(f"{n:4d} | {residual:18.12e} | {s_n}")

print("\n→ As n → ∞, residual → 0, therefore  0.999... = 1  exactly.\n")

# ------------------------------------------------------------------
# 2. Definition of partial sums
# ------------------------------------------------------------------
print("2. Partial sums")
print("   S_n = 1 - 10^{-n}\n")

# ------------------------------------------------------------------
# 3. From the identity 0.999... = 1  to  1/3
# ------------------------------------------------------------------
print("3. Recovering 1/3")
print("   0.999... / 3  =  1/3  ⇒  0.333... = 1/3\n")

# ------------------------------------------------------------------
# 4. Algebraic forms (now fully justified)
# ------------------------------------------------------------------
print("4. Algebraic correspondences")
print("   9x = 3  →  0.9x = 0.3")
print("   10x - x = 3  ⇒  9x = 3  ⇒  x = 1/3")
print("   x = 0.3 / 0.9 = 1/3\n")

# Exact arithmetic verification
x = Fraction(1, 3)

print("   Exact checks with fractions:")
print(f"   9x           = {9 * x}")
print(f"   9x == 3      ? {9 * x == 3}")
print(f"   0.9x         = {Fraction(9,10) * x}")
print(f"   0.9x == 0.3  ? {Fraction(9,10) * x == Fraction(3,10)}")
print(f"   0.3 / 0.9    = {Fraction(3,10) / Fraction(9,10)}")
print(f"   Equals 1/3   ? {Fraction(3,10) / Fraction(9,10) == Fraction(1,3)}\n")

# The form written on the paper: S = (3/10) / (9/10)
S = Fraction(3, 10) / Fraction(9, 10)
print(f"   S = (3/10) / (9/10) = {S}")
print(f"   S == 1/3             ? {S == Fraction(1, 3)}\n")

# ------------------------------------------------------------------
# 5. Closing statement
# ------------------------------------------------------------------
print("5. Conclusion")
print("   lim (1 - S_n) = 0  ≜  0.999... = 1")
print("   Dividing by 3 yields  0.333... = 1/3")
print("   Both 9x = 3 and the scaled form 0.9x = 0.3 are exact")
print("   because the residual has been driven to zero.")
print("=" * 72) 
