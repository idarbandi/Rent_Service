fibo = [0,1]
n = 0
r = 1
while fibo[-1] < 58:
    fibonaci = fibo[n] + fibo[r]
    fibo.append(fibonaci)
    n += 1
    r += 1
print(fibo)