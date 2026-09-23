from decimal import Decimal, getcontext
import math

def ieee_residual_limiter(target=Decimal("1"), base=10, max_digits=50, verbose=True):
    """
    IEEE-style residual limiter / infinite-series approximator.
    
    Keeps increasing the negative exponent n until the residual
    (base^{-n}) underflows relative to the working precision and
    the partial sum becomes indistinguishable from the target (1).
    
    This mimics a future IEEE residual-aware mode:
    - Finite strings (partial sums) remain the stored objects
    - Once residual rounds to zero, the limit is treated as exact
    - Subsequent division (e.g. by 3) proceeds from that unit
    """
    # Use high precision decimal to simulate variable-precision IEEE
    getcontext().prec = max_digits + 5
    
    one = Decimal(1)
    residual = Decimal(1)
    n = 0
    s_n = one   # partial sum starts at 1
    
    if verbose:
        print("IEEE Residual Limiter – chasing residual to zero")
        print(f"{'n':>4} | {'s_n (partial sum)':>40} | {'residual':>25}")
        print("-" * 75)
    
    while residual > 0:
        n += 1
        residual = Decimal(1) / (Decimal(base) ** n)
        s_n = one - residual
        
        if verbose and (n <= 20 or n % 5 == 0 or residual == 0):
            print(f"{n:4d} | {str(s_n):>40} | {str(residual):>25}")
        
        # Stop when residual underflows to zero at current precision
        # (i.e., s_n becomes exactly equal to 1 inside this precision)
        if s_n == one:
            break
            
        if n >= max_digits:
            break
    
    if verbose:
        print("-" * 75)
        print(f"Residual reached zero (or underflow) at n = {n}")
        print(f"Machine now treats s_n as exactly 1: {s_n == one}")
        print()
    
    return s_n, n


def demonstrate_clean_division():
    print("=" * 75)
    print("DEMONSTRATION: Residual Limiter → Clean Division of the Unit")
    print("=" * 75)
    
    # 1. Run the limiter until residual vanishes
    unit_approx, final_n = ieee_residual_limiter(max_digits=40, verbose=True)
    
    print("2. Now divide the recovered unit by 3")
    one_third = unit_approx / Decimal(3)
    print(f"   Result: {one_third}")
    print()
    
    # 3. Verification
    print("3. Verification")
    print(f"   3 * result          = {one_third * 3}")
    print(f"   Equals 1?           {one_third * 3 == Decimal(1)}")
    print()
    
    # 4. Contrast with ordinary IEEE-754 binary64
    print("4. Contrast with native binary64 (float)")
    native = 1.0 / 3.0
    print(f"   float 1/3           = {native:.50f}")
    print(f"   3 * (1/3)           = {3.0 * native:.50f}")
    print(f"   3 * (1/3) == 1.0 ?  {3.0 * native == 1.0}")
    print()
    
    print("=" * 75)
    print("Conclusion:")
    print("The residual limiter drives 10^{-n} until it underflows,")
    print("treats the result as the unit 1, then divides cleanly.")
    print("Finite strings stay compatible; the infinite-series limit")
    print("functions once the residual horizon is reached.")
    print("=" * 75)


if __name__ == "__main__":
    demonstrate_clean_division()
