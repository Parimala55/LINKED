# -*- coding: utf-8 -*-
"""stack_singly_linked_list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/Parimala55/0b1005daf63c6fa6df936070419e572a/stack_singly_linked_list.ipynb
"""

class Node:
  def __init__(self,x):
    self.data=x
    self.next=None
class stack:
  def __init__(self):
    self.top=None
#push operation
  def push(self):
    x=int(input("Enter element to be inserted into stack "))
    new=Node(x)
    if self.top is None:
      self.top=new
      self.top.next=None
    else:
      new.next=self.top
      self.top=new
  def pop(self):
    if self.top is None:
      print("stack is empty")
    elif self.top.next is None:
      print("poped element is:",self.top.data)
      print("---------------")
      self.top=None
    else:
      temp=self.top
      print ("the poped element is:" ,temp.data)
      temp=temp.next
      temp=None

  def display(self):
    if self.top is None:
      print("element of the stack are:")

    else:
      print("display element is:")
      temp=self.top
      while temp:
        print(temp.data)
        temp=temp.next
      print("top of stack is",self.top.data)


      #inserting the choice
s=stack()
while(1):#true 1 is true
  print("enter the option from below")
  print("1-push operation\n2-pop operation\n3-display\n4-exit")
  option=int(input())
  if option==1:
    print("push operation")
    print("---------------")
    s.push()
  elif option==2:
    print("pop operation")
    print("-------------------")
    s.pop()
  elif option==3:
    print("display")
    print("--------------------")
    s.display()
  else:
    break