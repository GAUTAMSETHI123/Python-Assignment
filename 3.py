n = int(input())
st = str(bin(n)).replace("0b", "")
max = 0
count = 0
for i in st:
    if i == '1':
        count += 1
        if count > max:
            max = count
    else:
        count = 0
print(max)
