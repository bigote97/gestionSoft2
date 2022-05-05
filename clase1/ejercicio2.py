nota1 = eval(input('Ingrese nota del primer examne: '))
nota2 = eval(input('Ingrese nota del segundo examne: '))
nota3 = eval(input('Ingrese nota del tercer examne: '))
promedio = (nota1 + nota2 + nota3)/3
if (promedio < 6 or nota3 < 6):
    print('Reprobado por burro.')
else:
    print('Aprobado.')
print('El alumno obtuvo un promedio de: ', promedio)