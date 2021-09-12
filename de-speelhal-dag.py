aantalPersonen = float(input('aantal personen '))
kostenPersonen = 7.45
vipVr = float(input('aantal minuten '))
kostenVr = 0.37
factuurkosten = 'dit geweldige dagje uit in de speelhal met of zonder vip VR Game Seat kost je maar ' + str((aantalPersonen) * (kostenPersonen) + (vipVr) / 5 * (kostenVr)) + ' euro'

print(factuurkosten)



