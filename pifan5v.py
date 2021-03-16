#!/usr/bin/python3
import sys
import time
#from gpiozero import LED
from gpiozero import CPUTemperature # CPUTemperature(), float
from gpiozero import PWMLED

start=50.0 # Start temperature for the fan to spin
top=70.0 # Throttle temperature

def get_tmp():
    return CPUTemperature().temperature

control = PWMLED(14) # Set GPIO14 (pin 8 as control)

while True: 
    try:
        current_temp = CPUTemperature().temperature # Get pi temperature
        
        # Set PWM duty cycle:
        if current_temp > start+(top-start)*0.75:
            pwm_target = 100 # 100%
        elif current_temp >  start+(top-start)*0.2:
            pwm_target = 75 # 75%
        elif current_temp >  start+(top-start)*0.25:
            pwm_target = 50 # 50%     
        elif current_temp > start:
            pwm_target = 25 # 25%
        else:
            pwm_target = 0 # fan off

        time.sleep(1)
        control.value = pwm_target/100.0
        print("Temp: {}\t Fan:{}%".format(current_temp,pwm_target))
    except KeyboardInterrupt:
        #print("Ending program")
        sys.exit()