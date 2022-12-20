length_square = int(input( 'Введите длину стороны квадрата: '))

print( 'Вывод: ')

perimeter_square = length_square * 4

area_square = length_square ** 2

print( 'Периметр: ', perimeter_square) 

print( 'Площадь: ', area_square) 

length_rectangle = int(input( 'Введите длину прямоугольника: ' ))

width_rectangle = int(input( 'Введите ширину прямоугольника: ' ))

perimeter_rectangle = (length_rectangle + width_rectangle) * 2

area_rectangle = length_rectangle * width_rectangle

print( 'Вывод: ')

print ('Периметр: ', perimeter_rectangle )

print ('Площадь: ', area_rectangle)





a = input ('Введите символ: ') 
 
b = (perimeter_square) + (area_rectangle)
 
print(a * b)




salary = int(input( 'Введите заработную плату в месяц: '))

percent_mortgage = int(input( 'Введите, какой процент(%) уходит на ипотеку: ' ))

percent_life = int(input( 'Введите, какой процент(%) уходит на жизнь: ' ))

print( 'Вывод' )

mortgage_expenses = round((12 * salary)  * (percent_mortgage / 100))

accumulated_over_the_year = round((12 * salary) - (((12 * salary)  *  (percent_life / 100)) + ((12 * salary)  * (percent_mortgage / 100))))

print( 'На ипотеку за год потрачено: ', mortgage_expenses ) 

print('Было накоплено за год: ', accumulated_over_the_year )