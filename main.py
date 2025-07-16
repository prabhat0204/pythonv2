# -*- coding: utf-8 -*-
from __future__ import print_function
import converter

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = raw_input("Enter your choice (1/2): ")

    if choice == "1":
        c = float(raw_input("Enter temperature in Celsius: "))
        f = converter.celsius_to_fahrenheit(c)
        print("Temperature in Fahrenheit: {:.2f}".format(f))
    elif choice == "2":
        f = float(raw_input("Enter temperature in Fahrenheit: "))
        c = converter.fahrenheit_to_celsius(f)
        print("Temperature in Celsius: {:.2f}".format(c))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
