#datos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dal_curs = 1.5

#crudos
crudo_promedio = 5
crudo_dalto = 3.5

# diferencia de duracion

diferencia_con_min = 100 - dal_curs / otros_cursos_min * 100
# division doble para redondear
diferencia_con_max = 100 - dal_curs * 1000 // otros_cursos_max / 10
diferencia_con_prom = 100 - dal_curs / otros_cursos_promedio * 100

tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dal_curs * 1000 // crudo_dalto / 10


print("-----------")
print(f'El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de dalto dura un {diferencia_con_prom}% menos que el promedio')
print("-----------")
print(f'El curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimina el {tiempo_vacio_dalto}% de tiempo vacio')
print("-----------")
print(f'Ver 10 horas de este curso equivalen a ver {otros_cursos_promedio * 100 // dal_curs / 10} horas de otros cursos')
print(f' Ver 10 horas de este curso equivalen a ver {dal_curs * 100 // otros_cursos_promedio / 10} horas de este curso')