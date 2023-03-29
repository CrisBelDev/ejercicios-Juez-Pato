T = int(input())
num_list = []
PR = ['2', '3', '5', '7']

def veri(num):
    c = 0
    sum = 0
    for i in range(4):
        for j in range(len(num)):
            if PR[i] == num[j]:
                c += 1
                con = int(num[j])
                sum += con
    if sum % 2 == 0 and c >= 3:
        return True
    return False

for i in range(T):
    num = input()
    num_list.append(num)

con = 0
for num in num_list:
    if veri(num):
        con += 1

print(con)
