def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test
celsius = 25
fahrenheit = 77

print(f"{celsius} degrees Celsius is equal to {celsius_to_fahrenheit(celsius):.2f} degrees Fahrenheit.")
print(f"{fahrenheit} degrees Fahrenheit is equal to {fahrenheit_to_celsius(fahrenheit):.2f} degrees Celsius.")
