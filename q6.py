# Write a menu based program to perform the operation on stack in python.

n = int(input("INPUT STACK SIZE ="))
def DisplayStack(stack):
    if len(stack) == 0:
        print("STACK IS EMPTY!")
    else:
        print(stack[len(stack)-1])

def Push(value):
 if len(stack) < n:
  stack.append(value)
 else:
  print("OVERFLOW ERROR CASE")
def Pop():
 if len(stack) > 0:
  stack.pop()
 else:
  print("UNDERFLOW ERROR CASE")
stack = []
while 2>1:
    a = int(input("STACK IMPLEMENTATION\n1>push\n2>pop\n3>top\n4>exit\n\ninput a s.no ="))
    if a == 1:
        print("\n\nPUSH FUNCTION\n")
        Push(int(input("INPUT A VALUE =")))
    elif a == 2:
        print("\n\nPOP FUNCTION")
        Pop()
    elif a == 3:
        print("\n\nSTACK")
        DisplayStack(stack)
    elif a == 4:
        break