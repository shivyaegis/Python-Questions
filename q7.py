# Write a menu based program to perform the operation on queue in python.

n = int(input("INPUT SIZE OF QUEUE ="))
def DisplayStack(stack):
    if len(stack) == 0:
        print("QUEUE IS EMPTY ! ")
    else:
        print("top",stack[0])
        print("rear",stack[-1])

def Push(value):
 if len(stack) < n:
  stack.append(value)
 else:
  print("OVERFLOW CASE ERROR")
def Pop():
 if len(stack) > 0:
  stack.remove(stack[0])
 else:
  print("UNDERFLOW CASE ERROR")
stack = []
while 2>1:
    a = int(input("QUEUE IMPLEMENTATION\n1>enqueue\n2>dequeue\n3>top & rear\n4>exit\n\ninput a s.no ="))
    if a == 1:
        print("\n\nENQUEUE FUNCTION")
        Push(int(input("INPUT A VALUE =")))
    elif a == 2:
        print("\n\nDEQUEUE FUNCTION")
        Pop()
    elif a == 3:
        print("\n\n--")
        DisplayStack(stack)
    elif a == 4:
        break