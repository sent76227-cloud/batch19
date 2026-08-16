'''
========================================
Assignment 7: Temperature Converter
========================================

A weather application needs to convert temperature from Celsius to Fahrenheit.

Write a Python program that:
- Accepts temperature in Celsius as input.
- Converts it to Fahrenheit using the formula:
  F = (C × 9/5) + 32
- Displays the result.

Example:
Celsius = 25
Fahrenheit = 77.0
'''
tem = int(input("Temperature in Celsius as input "))
fahrenheit = (tem * 1.8) + 32
print(f"Celsius = {tem}\nFahrenheit = {fahrenheit}")