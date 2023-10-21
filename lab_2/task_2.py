salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10 # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0       # подушка безопасности, первый месяц покрыт зарплатой
increase_ratio = 1 + increase   # коэффициент роста цен

for _ in range(months): # используется анонимная переменная _
    spend_salary_diff = spend - salary  # ежемесячная убыль капитала
    money_capital += spend_salary_diff  # расчёт капитала

    spend *= increase_ratio    # каждый месяц цены увеличиваются

money_capital = round(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
