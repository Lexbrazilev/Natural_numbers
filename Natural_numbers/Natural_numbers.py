n = int(input())
a = 0
for i in range(1, n+1):
    if n % i == 0:
        a = a + 1
print("Количество натуральных делителей числа:", a)        
