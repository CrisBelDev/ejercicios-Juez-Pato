def is_balanced(numero):
    s_par=0
    s_impar=0
    for i in range(len(numero)):
        if i % 2 == 0:
            s_par += int(numero[i])
        else:
            s_impar += int(numero[i])
    if s_par == s_impar:
        return True
N = int(input())
for i in range(N):
    numero = input()
    if(is_balanced(numero)):
        print("SI")
    else:
        print("NO")