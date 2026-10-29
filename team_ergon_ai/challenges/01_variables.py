# 01_variables.py — Python Foundations: Variables & Types for Subsurface Data
import sys

# Ensure clean UTF-8 console output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

print("=" * 60)
print("[*] LESSON 1.1: VARIABLES & DATA TYPES IN OILFIELD AI")
print("=" * 60)

# -------------------------------------------------------------
# 1. THE FOUR CORE DATA TYPES
# -------------------------------------------------------------
# In Python, a variable is just a labeled box storing information.

# TYPE 1: str (String — text enclosed in quotes)
well_name = "OML-42 Well-01"
formation = "Agbada Formation"
lithology = "Sandstone"

# TYPE 2: int (Integer — whole numbers, no decimals)
measured_depth_ft = 9450
report_page = 14
chunk_id = 101

# TYPE 3: float (Floating point — numbers with decimal points)
porosity = 0.235           # 23.5% reservoir porosity
permeability_md = 450.8     # millidarcies (fluid flow speed)
water_saturation = 0.32    # 32% water in pore space

# TYPE 4: bool (Boolean — True or False, capital T / F)
is_commercial = True       # Does this well have economically viable oil?
has_gas_cap = False        # Is there a gas cap above the oil?

# -------------------------------------------------------------
# 2. CHECKING TYPES WITH type()
# -------------------------------------------------------------
print("\n[+] Inspecting variable types:")
print(f"  well_name         : {well_name} -> {type(well_name)}")
print(f"  measured_depth_ft : {measured_depth_ft} -> {type(measured_depth_ft)}")
print(f"  porosity          : {porosity} -> {type(porosity)}")
print(f"  is_commercial     : {is_commercial} -> {type(is_commercial)}")

# -------------------------------------------------------------
# 3. F-STRINGS (Formatted Strings) — YOUR MOST IMPORTANT TOOL
# -------------------------------------------------------------
# In AI/RAG, prompts are dynamically generated using f-strings.
# Put an 'f' before the quotes, and wrap variable names inside {curly braces}.

summary_report = f"""
--- WELL SUMMARY CARD ---
Well Target      : {well_name}
Target Formation : {formation} ({lithology})
Total Depth      : {measured_depth_ft} ft
Net Porosity     : {porosity * 100:.1f}%
Commercial Pay   : {'YES' if is_commercial else 'NO'}
"""
print(summary_report)

# -------------------------------------------------------------
# 4. TYPE CONVERSION (Casting)
# -------------------------------------------------------------
# Crucial: Text extracted from PDFs ALWAYS starts as a string 'str'!
# You cannot do math on a string until you cast it.

raw_depth_from_pdf = "8900"     # This is a string (notice the quotes)
# raw_depth_from_pdf + 100      # ❌ This will CRASH with a TypeError!

converted_depth = int(raw_depth_from_pdf)    # Converted to an int
new_depth = converted_depth + 100            # Now math works: 9000

print(f"[+] Converted depth '{raw_depth_from_pdf}' to integer: {new_depth} ft\n")
print("=" * 60)
print("[+] Lesson 1.1 Complete! You now understand the 4 core types.")
print("=" * 60)
