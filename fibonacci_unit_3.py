# -*- coding: utf-8 -*-
"""fibonacci-unit-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/Parimala55/1e1be7099f1e822de1716b1a53d52931/fibonacci-unit-3.ipynb
"""

def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
n=int(input("enter the ele:"))
res=factorial(n)
print(res)# class execution code

def Fibonacci(n):
  if n<=0:
    print("incorrect input")
  elif n==1:
    return 0
  elif n==2:
    return 1
  else:
    return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(11 ))

#fibonacci series
def fibonacci(n):
    fib_series = [0,1]
    for i in range(2, n):
      next_term = fib_series[i - 1] +fib_series[i - 2]
      fib_series.append(next_term)
    return fib_series

n_terms = 10
result = fibonacci(n_terms)
print(result)