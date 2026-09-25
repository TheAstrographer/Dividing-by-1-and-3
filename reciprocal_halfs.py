import decimal
from decimal import Decimal

def print_exact_jcrin_reciprocals():
    # 1. Elevate precision context to 45 digits to expose the complete, uncut decimal structure
    decimal.getcontext().prec = 45
    
    print("=" * 85)
    print("                JCRIN EXACT RECIPROCAL DISCOVERY MANIFEST                ")
    print("=" * 85)
    
    # 2. Assign the exact halved parameters bounded to the 10-decimal limit
    half_x = Decimal('0.4938271605')
    half_comp = Decimal('0.0061728395')
    
    # 3. Compute pure multiplicative reciprocals (Inversion Axis)
    recip_x = Decimal('1') / half_x
    recip_comp = Decimal('1') / half_comp
    
    # 4. Stream the raw output to show the asymmetric behavior
    print(f"[Reciprocal of Halved Primary (1 / 1/2 x)]:\n  ↳ {recip_x}\n")
    print(f"[Reciprocal of Halved Complement (1 / (1/2 x - 1)^-1)]:\n  ↳ {recip_comp}")
    print("=" * 85)
    
    # 5. Structural Interaction Check
    interaction_product = recip_x * half_x
    comp_product = recip_comp * half_comp
    print(f"[Interaction Validation]")
    print(f"  ↳ Primary Verification (Recip * Base)    = {interaction_product}")
    print(f"  ↳ Complement Verification (Recip * Base) = {comp_product}")
    print("=" * 85)

if __name__ == "__main__":
    print_exact_jcrin_reciprocals()
