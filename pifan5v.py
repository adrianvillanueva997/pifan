#!/usr/bin/python3
import sys
import time
from gpiozero import LED
from gpiozero import CPUTemperature # CPUTemperature(), float


def get_tmp():
    return CPUTemperature().temperature
