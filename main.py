def gross_to_net(gross_wage):
    _skladka_emerytalna_percentage = 0.0976
    _skladka_rentowa_percentage = 0.0150
    _skladka_chorobowa_percentage = 0.0245

    skladka_emerytalna = gross_wage * _skladka_emerytalna_percentage
    skladka_rentowa = gross_wage * _skladka_rentowa_percentage
    skladka_chorobowa = gross_wage * _skladka_chorobowa_percentage

    print("Wynagrodzenie brutto:", "{:.2f}".format(gross_wage), sep=" ")

    print("Składki na ubezpieczenia społeczne:")
    print("Ubezpieczenie emerytalne:", "{:.2f}".format(skladka_emerytalna), sep=" ")
    print("Ubezpieczenie rentowe:", "{:.2f}".format(skladka_rentowa), sep=" ")
    print("Ubezpieczenie chorobowe:", "{:.2f}".format(skladka_chorobowa), sep=" ")