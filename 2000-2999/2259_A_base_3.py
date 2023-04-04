def div_sucesivas(n,base):
    if n == 0:
        return ""
    else:
        
        return div_sucesivas(n//base,base) + str(n%base)
        

numero = int(input())
base = 3
print(div_sucesivas(numero,base))