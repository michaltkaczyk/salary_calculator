def calculate_pension_insurance_contribution(gross_wage):

    _pension_insurance_contribution_percentage = 0.0976
    pension_insurance_contribution = gross_wage * _pension_insurance_contribution_percentage

    return pension_insurance_contribution


def calculate_disability_pension_insurance_contribution(gross_wage):

    _disability_pension_insurance_contribution_percentage = 0.0150
    disability_pension_insurance_contribution = gross_wage * _disability_pension_insurance_contribution_percentage

    return disability_pension_insurance_contribution


def calculate_sickness_insurance_contribution(gross_wage):

    _sickness_insurance_contribution_percentage = 0.0245
    sickness_insurance_contribution = gross_wage * _sickness_insurance_contribution_percentage

    return sickness_insurance_contribution


def calculate_health_insurance_contribution(base_wage, deductible):

    _health_insurance_contribution_nondeductible_percentage = 0.0900
    _health_insurance_contribution_deductible_percentage = 0.0775

    if deductible:
        health_insurance_contribution = base_wage * _health_insurance_contribution_deductible_percentage
    else:
        health_insurance_contribution = base_wage * _health_insurance_contribution_nondeductible_percentage

    return health_insurance_contribution


def calculate_income_deduction(same_town):

    _same_town_employee_deduction = 111.25
    _different_town_employee_deduction = 139.06

    if same_town:
        income_deduction = _same_town_employee_deduction
    else:
        income_deduction = _different_town_employee_deduction

    return income_deduction


def calculate_income_tax_advance(income):

    _income_tax_percentage = 0.1800
    _monthly_tax_allowance = 46.33

    income_tax_advance = (income * _income_tax_percentage) - _monthly_tax_allowance

    return income_tax_advance


def gross_to_net(gross_wage, same_town=True):

    pension_insurance_contribution = calculate_pension_insurance_contribution(gross_wage)
    disability_pension_insurance_contribution = calculate_disability_pension_insurance_contribution(gross_wage)
    sickness_insurance_contribution = calculate_sickness_insurance_contribution(gross_wage)

    social_insurance_contribution =\
        pension_insurance_contribution + disability_pension_insurance_contribution + sickness_insurance_contribution

    base_wage = gross_wage - social_insurance_contribution

    health_insurance_nondeductible_contribution = calculate_health_insurance_contribution(base_wage, deductible=False)

    income = base_wage - calculate_income_deduction(same_town)

    income_tax_advance_full = calculate_income_tax_advance(income)

    health_insurance_deductible_contribution = calculate_health_insurance_contribution(base_wage, deductible=True)

    income_tax_advance_deducted = round(income_tax_advance_full - health_insurance_deductible_contribution)

    net_wage = round(gross_wage - social_insurance_contribution - health_insurance_nondeductible_contribution -\
                     income_tax_advance_deducted, 2)

    print("Wynagrodzenie brutto:", "{:.2f} zł".format(gross_wage), sep=" ")
    print()
    print("Składki na ubezpieczenia społeczne:", "{:.2f} zł".format(social_insurance_contribution), sep=" ")
    print("\tUbezpieczenie emerytalne:", "{:.2f} zł".format(pension_insurance_contribution), sep=" ")
    print("\tUbezpieczenie rentowe:", "{:.2f} zł".format(disability_pension_insurance_contribution), sep=" ")
    print("\tUbezpieczenie chorobowe:", "{:.2f} zł".format(sickness_insurance_contribution), sep=" ")
    print()
    print("Składka na ubezpieczenie zdrowotne:",
          "{:.2f} zł".format(health_insurance_nondeductible_contribution), sep=" ")
    print()
    print("Zaliczka na podatek dochodowy:", "{:.2f} zł".format(income_tax_advance_deducted), sep=" ")
    print()
    print("Wynagrozenie netto:", "{:.2f} zł".format(net_wage), sep=" ")

    return net_wage
