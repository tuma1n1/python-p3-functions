#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()    

def greet(name = "Gudio"):
    print(f"Hello, {name}!")
    
greet("Gudio")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    
greet_with_default()
greet_with_default("Gudio")

def add(num1, num2):
    return num1 + num2

print(add(2, 3))

def halve(number):
    return number / 2

print(halve(4))
