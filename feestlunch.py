crossaint = float(input('aantal crossaint '))
bedragCross = 0.39
stokbrood = float(input('aantal stokbroden '))
bedragBrood = 2.78
kortingsbon = float(input('aantal kortingsbonnen '))
korting = 0.50
factuurtekst = 'de feestlunch kost bij de bakker ' + str((crossaint) * (bedragCross) + (stokbrood) * (bedragBrood) - (korting) * (kortingsbon)) + ' euro voor de croissantjes en de stokbroden als de kortingsbonnen nog geldig zijn!'

print(factuurtekst)
