arr = [5, 3, 5, 6, 1, 3, 6, 8, 1]

s = int(input("Введите число для умножения: "))

i = 0

print("До умножения:")
print(arr)

for i in range(len(arr)):
    arr[i] = arr[i] * s

print("После умножения:")
print(arr)