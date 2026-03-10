# Taking input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# ---- MEAN ----
total = 0
count = 0

for num in numbers:
    total += num
    count += 1

mean = total / count
print(f"Mean is: {mean}")

# ---- MEDIAN ----
# Manual sorting (Bubble Sort)
n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp

if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

print(f"Median is: {median}")

# ---- MODE ----
max_count = 0
mode = None

for i in range(n):
    count = 0
    for j in range(n):
     if numbers[i] == numbers[j]:
            count += 1

    if count > max_count:
        max_count = count
        mode = numbers[i]

print(f"Mode is: {mode}")
