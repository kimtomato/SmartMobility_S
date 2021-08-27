#!/usr/bin/python3

s = input("Enter a number between 2 ~ 20 :")
n = int(s)

for k in range (n):
    print(f"{(2*k+1)*'*':>{n+k}}")
    
