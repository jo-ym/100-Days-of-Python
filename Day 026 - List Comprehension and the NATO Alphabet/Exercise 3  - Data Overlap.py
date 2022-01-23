with open('file1.txt', mode='r') as f:
    file1 = f.readlines()

with open('file2.txt', mode='r') as f:
    file2 = f.readlines()

result = [int(num.strip()) for num in file1 if num in file2]

# Write your code above 👆

print(result)
