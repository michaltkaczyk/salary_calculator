def gross_to_net(gross_wage):

    _pension_insurance_contribution_percentage = 0.0976
    _disability_pension_insurance_contribution_percentage = 0.0150
    _sickness_insurance_contribution_percentage = 0.0245
    _health_insurance_contribution_percentage = 0.0900

    pension_insurance_contribution = gross_wage * _pension_insurance_contribution_percentage
    disability_pension_insurance_contribution = gross_wage * _disability_pension_insurance_contribution_percentage
    sickness_insurance_contribution = gross_wage * _sickness_insurance_contribution_percentage

    social_insurance_contribution =\
        pension_insurance_contribution + disability_pension_insurance_contribution + sickness_insurance_contribution

    health_insurance_contribution =\
        (gross_wage - social_insurance_contribution) * _health_insurance_contribution_percentage

    print("Wynagrodzenie brutto:", "{:.2f}".format(gross_wage), sep=" ")
    print()
    print("Składki na ubezpieczenia społeczne:")
    print("\tUbezpieczenie emerytalne:", "{:.2f}".format(pension_insurance_contribution), sep=" ")
    print("\tUbezpieczenie rentowe:", "{:.2f}".format(disability_pension_insurance_contribution), sep=" ")
    print("\tUbezpieczenie chorobowe:", "{:.2f}".format(sickness_insurance_contribution), sep=" ")
    print("Suma składek na ubezpieczenia społeczne:", "{:.2f}".format(social_insurance_contribution), sep=" ")
    print()
    print("Składka na ubezpieczenia społeczne:", "{:.2f}".format(health_insurance_contribution), sep=" ")
