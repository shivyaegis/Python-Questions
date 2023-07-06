def function(a):
    y = 0
    y2 = 1
    i = 0
    while i < a:
        print(y , end='')
        x = y + y2
        y = y2
        y2 = x
        i += 1
z = int(input("Enter no of terms"))
(function(z))