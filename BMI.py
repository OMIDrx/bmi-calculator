#------------- bmi calculate ----------------
def calculator(w, h):
    return w / pow(h, 2)

#------------- range bmi ---------------------
def bmi_state(bmi, gender, age):
    low = 18.5
    normal = 25
    high = 30
#---------------- gender if -----------------------
    if gender == 'women':
        low += 1
        normal += 1
        high += 1

#---------------------age if---------------------------
    if age >= 45:
        low += 0.5
        normal += 0.5
        high += 0.5
#-------------shart for bmi ----------------
    if bmi <= low:
        return 'underweight'
    elif low < bmi <= normal:
        return 'healthy weight'
    elif normal < bmi <= high:
        return 'overweight'
    else:
        return 'obesity'

#------------------ enter num from user ------------------------
def main():
    print('welcome to bmi calculator\n')

    w = float(input('enter your weight: '))
    while w < 0 or w > 500:
        w = float(input('try again...enter your weight: '))

    h = float(input('enter your height: '))
    while h < 0 or h > 3.00:
        h = float(input('try again...enter your height: '))

    g = input('enter your gender(man/women): ')
    while g not in ['man', 'women']:
        g = input('try again...enter your gender(man/women): ')

    age = int(input('enter your age: '))
    while age < 0 or age > 200:
        age = int(input('try again...enter your age: '))

    #----------------- calculate numbers -----------------------------
    bmi = calculator(w, h)
    s = bmi_state(bmi, g, age)

    #---------------- print Info -------------------------
    print('-' * 20)
    print(f'BMI: {bmi:.2f}')
    print(f'state : {s}')

main()
