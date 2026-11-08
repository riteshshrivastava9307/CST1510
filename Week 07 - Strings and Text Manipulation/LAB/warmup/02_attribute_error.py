value_text = "unknown"

try:
    value = float(value_text)
    print(value)
except ValueError:
    print("Invalid number:", value_text)