def savings(gross_pay,tax_rate,expenses):
    A = gross_pay * tax_rate
    B = gross_pay - A
    C = B - expenses
    return C
gross_pay = int(input('Input Gross Pay centavos form: '))
tax_rate = float(input('lnput Tax rate in decimal form: '))
expenses = int(input('Input Expenses in cetavos form: '))
C = savings(gross_pay,tax_rate,expenses)
print('The total number of centavos remaining',round(final,2),'centavos')

def material_waste(total_material, material_units, num_jobs, job_consumption):
    MATERIAL_CONSUMED = num_jobs*job_consumption
    REMAINING_MATERIAL = total_material - MATERIAL_CONSUMED
    return REMAINING_MATERIAL
material_units = str(input('Enter units used to express a quantity of the material (eg. L, Kg, cm): '))
total_material = int(input('Enter the total material available: '))
num_jobs = int(input('Enter number of jobs to run: '))
job_consumption = int(input('Enter the amount of material consumed per job: '))
REMAINING_MATERIAL = material_waste(total_material, material_units, num_jobs, job_consumption)
print('The amount of remaining materials is ',REMAINING_MATERIAL,material_units,'.',sep="")
    
def interest(principal, rate, periods):
    A = principal * rate
    B = A * periods
    C = principal + B
    return C
principal = int(input('Enter amount invested, expressed in centavos: ₱'))
rate = float(input('Enter the interest rate per period, expressed as a decimal representation of a percentage: '))
periods = int(input('Enter number of periods invested in months: '))
C = interest(principal, rate, periods)
print('The final value of the investment is ₱',round(final,2),sep='')

def body_mass_index(weight, feet, inches):
    kg = weight / 2.2
    A = feet * .3048
    B = inches * 0.0254
    height = A + B
    BMI = kg / (height ** 2)
    return BMI
weight = float(input('Enter weight in lbs: '))
feet = int(input('Enter foot component of height: '))
inches = int(input('Enter inches component of height: '))
BMI = body_mass_index(weight, feet, inches)
print('The BMI is',round(BMI,4))

