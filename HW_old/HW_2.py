basic_mortgage_rate = b_m_r = 10

salary_project = s_p =  0.5

insurance_project = i_p = 1.5

discount_for_children = d_f_c = 1



vladivostok = 'республика саха' or 'камчатский край' or 'приморский край' or 'хабаровский край' or 'амурская область' or 'магаданская область' or 'сахалинская область' or 'еврейская автономная область' or 'чукотский автономный округ'

vladivostok = vladivostok

region = input( 'Введите Ваш регион: ' )

region = region.lower()

if region != vladivostok:
  
  salary = input( ' В нашем ли банке зарплатный проект? Введите ДА или НЕТ: ' )

  salary = salary.lower()
  
  if salary == 'да':
    
    insurance = input( 'Будет ли оформлено в нашем банке страхование? Введите ДА или НЕТ: ' )

    insurance = insurance.lower()
    
    if insurance == 'да':
      
      children = int(input( 'Укажите, пожалуйста, количество ваших детей: ' ) )
      
      if children >= 3:
        
        print('Ваша процентная ставка по ипотеке =', b_m_r - s_p - i_p - d_f_c, '%')
        
      else:
      
        print('Ваша процентная ставка по ипотеке =', b_m_r - s_p - i_p, '%')
      
    else: 
      
      children = int(input( 'Укажите, пожалуйста, количество ваших детей: ' ) )

      if children >= 3:
        
        print('Ваша процентная ставка по ипотеке =', b_m_r - s_p - d_f_c, '%')
        
      else: 
      
        print('Ваша процентная ставка по ипотеке =', b_m_r - s_p, '%')
    
      
  else:
    
    insurance = input( 'Будет ли оформлено в нашем банке страхование? Введите ДА или НЕТ: ' )

    insurance = insurance.lower()

    if 'да' == insurance:
      
      children = int(input( 'Укажите, пожалуйста, количество ваших детей: ' ) )
      
      if children >= 3:
        
        print('Ваша процентная ставка по ипотеке =', b_m_r - i_p - d_f_c, '%')
        
      else: 
      
        print('Ваша процентная ставка по ипотеке =', b_m_r - i_p, '%')
      
    else:
      
      children = int(input( 'Укажите, пожалуйста, количество ваших детей: ' ) )

      if children >= 3:
        
        print('Ваша процентная ставка по ипотеке =' , b_m_r - d_f_c, '%')
        
      else: 
      
        print('Ваша процентная ставка по ипотеке =', b_m_r, '%' )

else: 
  region == vladivostok
  
  print( 'Ваша ставка процентная ставка по ипотеке  = 2%' )


#########################################################################################################################




month = input( 'Введите месяц рождения: ' ).lower()

date = int(input( 'Введите дату рождения: ' ))

if month == 'март' and 21 <= date <= 31 or month == 'апрель' and 1 <= date <= 20:

  print( 'Овен' )

elif month == 'апрель' and 21 <= date <= 30 or month == 'май' and 1 <= date <= 20:
  print( 'Телец' )

elif month == 'май' and 21 <= date <= 31 or month == 'июнь' and 1 <= date < 21:

  print( 'Близнецы' )

elif month == 'июнь' and 22 <= date <= 30 or month == 'июль' and 1 <= date <= 22:

  print( 'Рак' )

elif month == 'июль' and 23 <= date <= 31 or month == 'август' and 1 <= date <= 22:

  print( 'Лев' )

elif month == 'август' and 23 <= date <= 31 or month == 'сентябрь' and 1 <= date <= 23:

  print( 'Дева' )

elif month == 'сентябрь' and 24 <= date <= 30 or month == 'октябрь' and 1 <= date <= 23:

  print( 'Весы' )

elif month == 'октябрь' and 24 < date <= 31 or month == 'ноябрь' and 1 <= date <= 22:

  print( 'Скорпион' )

elif month == 'ноябрь' and  23 <= date <= 30 or month == 'декабрь'  and 1 <= date <= 21:

  print( 'Стрелец' )

elif month == 'декабрь' and 22 <= date <= 31 or month == 'январь' and 1 <= date <= 20:

  print( 'Козерог' )

elif month == 'январь' and 21 <= date <= 31 or month == 'февраль' and 1 <= date <= 18:

  print( 'Водолей' )

elif month == 'февраль' and 19 <= date <= 29 or month == 'март' and 1 <= date <= 20:

  print( 'Рыбы' )

else:
  print ('Введенные данные не корректны' )