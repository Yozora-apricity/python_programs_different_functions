# Program to print numbers from 0 to 100 except those ending in zero
for i in range(101):
    if i % 10 == 0:
        continue
    print(i)