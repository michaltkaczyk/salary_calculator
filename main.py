def gross_to_net(gross_wage, same_town=True):

    _pension_insurance_contribution_percentage = 0.0976
    _disability_pension_insurance_contribution_percentage = 0.0150
    _sickness_insurance_contribution_percentage = 0.0245
    _health_insurance_contribution_percentage = 0.0900

    _same_town_employee_deduction = 111.25
    _different_town_employee_deduction = 139.06

    # Składki na ubezpieczenia społeczne
    pension_insurance_contribution = gross_wage * _pension_insurance_contribution_percentage
    disability_pension_insurance_contribution = gross_wage * _disability_pension_insurance_contribution_percentage
    sickness_insurance_contribution = gross_wage * _sickness_insurance_contribution_percentage

    social_insurance_contribution =\
        pension_insurance_contribution + disability_pension_insurance_contribution + sickness_insurance_contribution

    # Przychód
    income = gross_wage - social_insurance_contribution

    # Składka na ubezpieczenie zdrowotne
    health_insurance_contribution = income * _health_insurance_contribution_percentage

    # Koszty uzyskania przychodu:
    tax_deductible_expences = _same_town_employee_deduction if same_town else _different_town_employee_deduction

    print("Wynagrodzenie brutto:", "{:.2f}".format(gross_wage), sep=" ")
    print()
    print("Składki na ubezpieczenia społeczne:")
    print("\tUbezpieczenie emerytalne:", "{:.2f}".format(pension_insurance_contribution), sep=" ")
    print("\tUbezpieczenie rentowe:", "{:.2f}".format(disability_pension_insurance_contribution), sep=" ")
    print("\tUbezpieczenie chorobowe:", "{:.2f}".format(sickness_insurance_contribution), sep=" ")
    print("Suma składek na ubezpieczenia społeczne:", "{:.2f}".format(social_insurance_contribution), sep=" ")
    print()
    print("Składka na ubezpieczenie zdrowotne:", "{:.2f}".format(health_insurance_contribution), sep=" ")

    summary = {
        'Pension Insurance Contribution': pension_insurance_contribution,
        'Disability Pension Insurance Contribution': disability_pension_insurance_contribution,
        'Sickness Insurance Contribution': sickness_insurance_contribution,
        'Health Insurance Contribution': health_insurance_contribution}

    return summary
