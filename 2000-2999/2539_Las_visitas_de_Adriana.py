x = int(input())
distance = x - 0  # Distancia entre las dos casas
jumps = distance // 5  # Número mínimo de saltos necesarios

if distance % 5 != 0:
    jumps += 1

if distance <= 5:
    jumps = 1

print(jumps)