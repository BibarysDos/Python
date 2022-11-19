a = int(input())

break1 = a//2
break2 = (a-1)//2

minute = 9 * 60 + a * 45 + break1 * 5 + break2 * 15

print(f'{minute//60} {minute%60}')
