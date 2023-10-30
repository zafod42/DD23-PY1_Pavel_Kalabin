money_capital = 20000                   # Подушка безопасности
salary = 5000                           # Ежемесячная зарплата
spend = 6000                            # Траты за первый месяц
increase = 0.05                         # Ежемесячный рост цен

dept_free_days = 0                      # Последний месяц, посчитанный в цикле уже будет с долгами
increase_ratio = 1 + increase           # коэффициент роста цен
while True:
    spend_salary_diff = spend - salary  # ежемесячная убыль средств из капитала
    money_capital -= spend_salary_diff
    if money_capital < 0:               # постусловие - если не выполняется, то считаем месяц
        break                           # иначе - заканчиваем цикл
    
    spend *= increase_ratio             # каждый месяц цены увеличиваются в increase_ratio раз
    dept_free_days += 1
    
print("Количество месяцев, которое можно протянуть без долгов:", dept_free_days)
