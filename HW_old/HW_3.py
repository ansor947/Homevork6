boys = input('Введите имена парней: ').split()

girls = input('Введите имена девушек: ').split()

print()

boys.sort()

girls.sort()

list_couples = list(zip(boys, girls))

for boys_name, girls_name in list_couples:

    if len(girls) == len(boys):
        print('Идеальные пары: ')
        print(f' {boys_name} и {girls_name} ')

    else:

        print('Предупреждение, кто-то может остаться без пары!')
        break
print()      

#################################################################################



cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]
person = int(input())
for food_list, ingredients_list in cook_book:
  print()
  print(f'{food_list.capitalize()}: ')
  
  for food in ingredients_list:
    food = f'{food[0]}, {food[1] * person}{food[2]}'
    print(food)