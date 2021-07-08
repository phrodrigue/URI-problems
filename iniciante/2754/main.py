a = 234.345
b = 45.698

print(f"{a:.6f} - {b:.6f}")
print(f"{a:.0f} - {b:.0f}")
print(f"{a:.1f} - {b:.1f}")
print(f"{a:.2f} - {b:.2f}")
print(f"{a:.3f} - {b:.3f}")
ae = f"{a:e}"
be = f"{b:e}"
print(f"{ae} - {be}")
print(f"{a:E} - {b:E}")

print(f"{float(ae):0.3f} - {float(be):0.3f}")
print(f"{float(ae):0.3f} - {float(be):0.3f}")