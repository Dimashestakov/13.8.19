# Кол-во биллетов
num_tickets = int(input("Введите количество билетов: "))

# Переменные
total_price = 0
discount = 0

for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        # Бесплатный вход для детей до 18 лет
        ticket_price = 0
    elif age < 25:
        # Стоимость билета для посетителей от 18 до 25 лет
        ticket_price = 990
    else:
        # Стоимость билета для посетителей от 25 лет
        ticket_price = 1390

    # Добавление стоимости
    total_price += ticket_price

# Вычисление скидки
if num_tickets > 3:
    discount = total_price * 0.1

# Вычисление итоговой суммы со скидкой
final_price = total_price - discount

#Результаты
print("Общая стоимость билетов:", total_price, "руб.")
if discount > 0:
    print("Скидка:", discount, "руб.")
print("Итоговая сумма к оплате:", final_price, "руб.")
