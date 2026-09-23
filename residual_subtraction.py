from fractions import Fraction

print("=" * 70)
print("PURE-PYTHON DEMONSTRATION")
print("0.999... = 1  (zero residual)  →  0.333... = 1/3")
print("=" * 70)

# -------------------------------------------------------------------
# 1. Residual-error argument for 0.999... = 1
# -------------------------------------------------------------------
print("\n1. Residual-error argument for 0.999... = 1\n")
print(f"{'n':>4} | {'s_n = 0.999...9 (n nines)':>28} | {'residual = 1 - s_n':>20}")
print("-" * 60)

for n in range(1, 16):
    residual = Fraction(1, 10**n)
    s_n = 1 - residual
    print(f"{n:4d} | {str(s_n):>28} | {str(residual):>20}")

print("\nAs n → ∞, residual 10^{-n} → 0")
print("Therefore  lim (1 - s_n) = 0  ⇒  0.999... = 1 exactly.\n")

# -------------------------------------------------------------------
# 2. The circle closes: divide the identity by 3
# -------------------------------------------------------------------
print("2. Dividing the identity by 3\n")
print("   1          = 0.999...")
print("   1/3        = 0.999... / 3")
print("   1/3        = 0.333...\n")
print("Because equality is preserved under division by a non-zero constant,")
print("0.333... is exactly equal to 1/3.\n")

# -------------------------------------------------------------------
# 3. Standard algebraic proof made rigorous
# -------------------------------------------------------------------
print("3. Standard algebraic route (now rigorous)\n")
print("   Let x = 0.333...")
print("   10x = 3.333...")
print("   10x - x = 3")
print("   9x = 3")
print("   x = 1/3\n")

# Demonstrate the cancellation of tails with finite but increasing precision
print("   Finite-precision illustration of the cancellation:")
for n in [3, 6, 10]:
    # Approximate 0.333... with n digits
    approx = Fraction(int("3" * n), 10**n)
    ten_x = 10 * approx
    difference = ten_x - approx
    print(f"   n={n:2d}: 10x - x ≈ {difference}  (approaching 3)")

print()

# -------------------------------------------------------------------
# 4. Scaled variant 0.9x = 0.3
# -------------------------------------------------------------------
print("4. Scaled variant that stays inside the unit interval\n")
print("   0.9 * 0.333... = 0.2999...")
print("   and 0.2999... = 0.3   (same residual argument)")
print("   therefore  0.9x = 0.3  ⇒  x = 0.3 / 0.9 = 1/3\n")

# Exact demonstration with fractions
x = Fraction(1, 3)
print(f"   Exact check: 0.9 * (1/3) = {Fraction(9,10) * x}")
print(f"                which equals 0.3 = {Fraction(3,10)}")
print(f"   Equal? {Fraction(9,10) * x == Fraction(3,10)}\n")

# -------------------------------------------------------------------
# 5. Quick contrast with floating-point (the permanent residual)
# -------------------------------------------------------------------
print("5. Contrast with IEEE-754 double (permanent residual)\n")
fp = 1.0 / 3.0
print(f"   float 1/3          = {fp:.50f}")
print(f"   3 * (1/3)          = {3 * fp:.50f}")
print(f"   3 * (1/3) == 1 ?   {3 * fp == 1.0}")
print("   (The residual never reaches zero inside the finite box.)\n")

print("=" * 70)
print("Conclusion: In the reals the residual is chased to exactly zero.")
print("0.999... = 1 and therefore 0.333... = 1/3 with no remaining gap.")
print("=" * 70)
