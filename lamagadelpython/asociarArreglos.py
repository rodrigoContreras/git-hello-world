nombres = ['Juan','Pedro', 'Diego','Martina', 'Lulu']
notas = [0, 1, 2, 3, 4]

calificaciones = dict(zip(nombres, notas))

print(calificaciones)
print(max(calificaciones.values()))
print(min(calificaciones.values()))
print(max(calificaciones.items()))
print(min(calificaciones.items()))