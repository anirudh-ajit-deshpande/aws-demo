import boto3
import os
import datetime
# comment
print ("######################################")
print ("Welcome to the world of CI/CD - Kudos!")
print ("######################################")

a = 5
b = 7

def add():
    print(a+b)

def sub():
    print(a-b)
    
def multi():
    print(a*b)

def div():
    print(a/b)

def mod():
    print(a%b)

print ("##### Performing operations #######")
add()
sub()
multi()
div()
mod()
print ("##### Operations COMPLETE !!!!!#######")