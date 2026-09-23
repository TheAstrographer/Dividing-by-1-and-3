from fractions import Fraction
from decimal import Decimal, getcontext

print("=" * 70)
print("DIVIDING BY 1 AND 3  –  Residual Limit in Pure Python")
print("=" * 70)

# -------------------------------------------------------
# 1. The fundamental residual limit
# -------------------------------------------------------
print("\n1. Residual Limit")
print("   lim (n→∞) 1/10^n = 0\n")

getcontext().prec = 50   # high precision for illustration

print(f"{'n':>4} | {'10^{-n}':>20} | {'1 - 10^{-n}':>25}")
print("-" * 55)

for n in [1, 2, 3, 5, 10, 15, 20, 30]:
    residual = Decimal(10) ** -n
    s_n = Decimal(1) - residual
    print(f"{n:4d} | {residual:20.15e} | {s_n}")

print("\nAs n → ∞ the residual vanishes → 0.999... = 1 exactly in the reals.\n")

# -------------------------------------------------------
# 2. Definition of the partial sums
# -------------------------------------------------------
print("2. Partial sums")
print("   S_n = 1 - 10^{-n}\n")

# -------------------------------------------------------
# 3. From the limit identity to 1/3
# -------------------------------------------------------
print("3. Recovering 1/3 from the identity 0.999... = 1")
print("   0.999... / 3 = 1/3  ⇒  0.333... = 1/3\n")

one = Decimal(1)
one_third = one / Decimal(3)
print(f"   1 / 3 = {one_third}\n")

# -------------------------------------------------------
# 4. Classic algebraic proof (now justified by the residual limit)
# -------------------------------------------------------
print("4. Algebraic route (justified by the residual limit)")
print("   Let x = 0.333...")
print("   10x = 3.333...")
print("   10x - x = 3")
print("   9x = 3")
print("   x = 1/3\n")

x = Fraction(1, 3)
print(f"   Exact check: 9x = {9 * x}")
print(f"   9x == 3 ? {9 * x == 3}\n")

# -------------------------------------------------------
# 5. Scaled version that stays inside the unit interval
# -------------------------------------------------------
print("5. Scaled version: 0.9x = 0.3")
print("   x = 0.3 / 0.9 = 1/3\n")

scaled_x = Fraction(3, 10) / Fraction(9, 10)
print(f"   0.3 / 0.9 = {scaled_x}")
print(f"   Equals 1/3 ? {scaled_x == Fraction(1, 3)}\n")

# Alternative form shown on the paper: S = (3/10) / (9/10)
S = Fraction(3, 10) / Fraction(9, 10)
print(f"   S = (3/10) / (9/10) = {S}")
print(f"   S == 1/3 ? {S == Fraction(1, 3)}\n")

# -------------------------------------------------------
# 6. Final verification with the residual identity
# -------------------------------------------------------
print("6. Closing the circle")
print("   Because lim (1 - S_n) = 0, we have 0.999... = 1")
print("   Dividing both sides by 3 yields 0.333... = 1/3")
print("   All algebraic manipulations (9x=3 or 0.9x=0.3) are therefore exact.\n")

print("=" * 70)
print("Conclusion:")
print("The residual 10^{-n} → 0 forces 0.999... = 1 with zero error.")
print("Dividing that identity by 3 recovers 1/3 cleanly.")
print("Both the classic and the scaled algebraic proofs follow directly.")
print("=" * 70)
