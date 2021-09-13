#shane Boer pizza calculator

print('-------------------------------------------------------------------------')
print('prijzen.')
print('pizza small = 4.99')
print('pizza medium = 7.99')
print('pizza large = 12.99')
print('-------------------------------------------------------------------------')

pizzaSmall = float(input('aantal small pizzas '))
kostenSmall = 4.99
pizzaMedium = float(input('aantal medium pizzas '))
kostenMedium = 7.99
pizzaLarge = float(input('aantal large pizzas '))
kostenLarge = 12.99

print('-------------------------------------------------------------------------')
print('aantal small pizzas  : ' + str(int(pizzaSmall)))
print('prijs small pizzas   : ' + str((pizzaSmall) * (kostenSmall)))
print('-------------------------------------------------------------------------')
print('aantal medium pizzas : ' + str(int(pizzaMedium)))
print('prijs medium pizzas  : ' + str((pizzaMedium) * (kostenMedium)))
print('-------------------------------------------------------------------------')
print('aantal large pizzas  : ' + str(int(pizzaLarge)))
print('prijs large pizzas   : ' + str((pizzaLarge) * (kostenLarge)))
print('-------------------------------------------------------------------------')

print('totaal aantal pizzas : ' + str(int((pizzaSmall) + (pizzaMedium) + (pizzaLarge))))
print('totaal bedrag        : ' + str((pizzaSmall) * (kostenSmall) + (pizzaMedium) * (kostenMedium) + (pizzaLarge) * (kostenLarge)))