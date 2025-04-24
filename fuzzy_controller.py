import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


#input and output variables
vehicals= ctrl.Antecedent(np.arange(0, 21, 1), 'vehicals')
green_time=ctrl.Consequent(np.arange(5,61,1),'green_time')

vehicals.automf(3)
green_time['short'] = fuzz.trimf(green_time.universe, [5, 10, 20])
green_time['medium'] = fuzz.trimf(green_time.universe, [15, 30, 45])
green_time['long'] = fuzz.trimf(green_time.universe, [30, 60, 90])

#Rules
rule1= ctrl.Rule(vehicals['poor'], green_time['short'])
rule2= ctrl.Rule(vehicals['average'], green_time['medium'])
rule3= ctrl.Rule(vehicals['good'], green_time['long'])

#Control system
traffic_ctrl= ctrl.ControlSystem([rule1,rule2,rule3])
traffic_sim= ctrl.ControlSystemSimulation(traffic_ctrl)


def get_green_time(vehicle_count):
    traffic_sim.input['vehicals']= vehicle_count
    traffic_sim.compute()
    return traffic_sim.output['green_time']

if __name__ == "__main__":
    for v in [3, 10, 18]:
        print(f"Vehicles: {v}, Green Time: {get_green_time(v):.2f} sec")
