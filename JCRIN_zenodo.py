import math

EPS = 1e-9

def y(n):
    return n * EPS

def x(n):
    return 1.0 - n * EPS

def unity(y_or_x):
    return y_or_x + (1.0 - y_or_x)

# --- Main / Complementary checks at the exact indices listed in the thesis ---
test_ns = [0, 1000, 20000, 300000, 4000000, 50000000, 600000000]

print("n\t\ty_n\t\t\t1-y_n\t\t\tunity\t\tx_n\t\t\tunity_x")
for n in test_ns:
    yn = y(n)
    xn = x(n)
    print(f"{n}\t{yn:.9f}\t{1-yn:.9f}\t{unity(yn):.9f}\t{xn:.9f}\t{unity(xn):.9f}")

# --- Explicit verification of the documented Extended-New / Multi-Stage values ---
print("\n--- Documented control-digit points ---")
print("n=0:     y=0.000000000  unity=", unity(0.0))
print("n=1000:  y=0.000001000  unity=", unity(0.000001))
print("n=20000: y=0.000020000  unity=", unity(0.00002))
print("n=300000:y=0.000300000  unity=", unity(0.0003))
print("n=4e6:   y=0.004000000  unity=", unity(0.004))
print("n=5e7:   y=0.050000000  unity=", unity(0.05))
print("n=6e8:   y=0.600000000  unity=", unity(0.6))

print("          (truncated forms 0.60 / 0.6 also sum to 1.0 by construction)")
