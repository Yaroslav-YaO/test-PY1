salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
budget = 0

for i in range(months):
    budget += salary
    budget -= spend
    spend += spend * increase

money_capital = int(-budget)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
