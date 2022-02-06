def compose(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h

def calucate_bmi(weight, height):
    return weight / height**2

def evaluate_bmi(bmi):
    msg =  'Obese Class III (Very severely obese)'

    if bmi < 15:
        msg = 'Very severely underweight'
    elif bmi < 16:
        msg = 'Severely underweight'
    elif bmi < 18.5:
        msg =  'Underweight'
    elif bmi < 25:
        msg = 'Normal (healthy weight)'
    elif bmi < 30:
        msg = 'Overweight'
    elif bmi < 35:
        msg = 'Obese Class I (Moderately obese)'
    elif bmi < 40:
        msg = 'Obese Class II (Severely obese)'
    
    return msg

bmi_calculator = compose(evaluate_bmi, calucate_bmi)
weight = 69 # in kg
height = 1.8 # in m

print(bmi_calculator(weight, height))
