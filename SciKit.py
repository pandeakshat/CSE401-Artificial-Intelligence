import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
curr = ctrl.Antecedent(np.arange(0, 11, 1), 'Curricular Grade')
extracurr = ctrl.Antecedent(np.arange(0, 11, 1), 'Extra-Curricular Grade')
grade = ctrl.Consequent(np.arange(0, 11, 1), 'Result')

# Auto-membership function population is possible with .automf(3, 5, or 7)
curr.automf(7)
extracurr.automf(7)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
grade['fail'] = fuzz.trimf(grade.universe, [0, 0, 4])
grade['promoted'] = fuzz.trimf(grade.universe, [4, 4, 7])
grade['merit-list'] = fuzz.trimf(grade.universe, [7, 10, 10])


rule1 = ctrl.Rule(curr['poor'] | extracurr['poor'], grade['fail'])
rule2 = ctrl.Rule(curr['average'] | extracurr['average'], grade['promoted'])
rule3 = ctrl.Rule(extracurr['good'] | curr['good'], grade['merit-list'])

grading_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

grading = ctrl.ControlSystemSimulation(grading_ctrl)
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
grading.input['Curricular Grade'] = 7   
grading.input['Extra-Curricular Grade'] = 8

# Crunch the numbers

grading.compute()
print("Resulting Grade :" , round(grading.output['Result']*10,3), "%")
print("SGPA =" , round(grading.output['Result'], 2))
alphagrade=grading.output['Result']
if alphagrade <= 4:
    print("F")
elif alphagrade>4 and alphagrade<=5:
    print("E")
elif alphagrade>5 and alphagrade<=6:
    print("D")
elif alphagrade>6 and alphagrade<=7:
    print("C")
elif alphagrade>7 and alphagrade<=8:
    print("B")
elif alphagrade>8 and alphagrade<=9:
    print("A")
elif alphagrade>9:
    print("S")
else: 
    print("Error! Please input proper grades")
grade.view(sim=grading)
