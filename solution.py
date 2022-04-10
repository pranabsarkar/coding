

data = int(input())


for i in range(1, 30):
    for j in range(1, 30):
        if data % (i * i * i * i) == j:
            print(j)
print(1)

