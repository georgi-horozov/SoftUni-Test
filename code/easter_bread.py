budget = float(input()) # БЮДЖЕТА КОЙТО ИМАМЕ
flour_price = float(input()) # ЦЕНАТА НА 1 КГ БРАШНО

eggs_price = flour_price * 0.75 # ЦЕНАТА НА ЕДНА КОРА ЯЙЦА
milk_price = (flour_price * 1.25) * 0.25 # ЦЕНАТА НА 250 мл МЛЯКО ЗА ЕДИН КОЗУНАК
price_loaf = flour_price + eggs_price + milk_price # ЦЕНАТА НА ПРОДУКТИТЕ ЗА ЕДИН КОЗУНАК

bread_counter = 0
coloured_count_eggs = 0
while price_loaf <= budget: # ДОКАТО ЦЕНАТА Е ПО-МАЛКА ОТ БЮДЖЕТА
    bread_counter += 1 # БРОЯЧ НА КОЗУНАЦИТЕ, КОЙТО СЕ УВЕЛИЧАВА С 1
    budget -= price_loaf
    coloured_count_eggs += 3 # БРОЯТ НА ЦВЕТНИТЕ ЯЙЦА, КОЙТО СЕ УВЕЛИЧАВА С 3
    if bread_counter % 3 == 0: # УСЛОВИ, ПРИ КОЕТО ГУБИМ ЦВЕТНИ ЯЙЦА
        coloured_count_eggs -= (bread_counter - 2)

print(f"You made {bread_counter} loaves of Easter bread! Now you have {coloured_count_eggs} eggs and {budget:.2f}BGN left.")