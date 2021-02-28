import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt
from matplotlib import pyplot
from scipy.optimize import curve_fit
import math
import openpyxl


def average_of_list(ls):
    return sum(ls) / len(ls)


df = pd.read_excel(sheet_name=1, io=r"C:\Users\yusef\Downloads\TCP_2021_data_FINAL.xlsx", engine='openpyxl')
data = df.values

monthly_prices_2020 = data[5:20, 5]
monthly_prices_2012 = data[21:26, 5]

speeds_2020 = data[5:20, 3]
speeds_2012 = data[21:26, 3]

average_speed_2012 = average_of_list(speeds_2012)
average_speed_2020 = average_of_list(speeds_2020)

average_monthly_price_2020 = average_of_list(monthly_prices_2020)
average_monthly_price_2012 = average_of_list(monthly_prices_2012)

print(f"Average 2020 Monthly Price: {average_monthly_price_2020}")
print(f"Average 2012 Monthly Price: {average_monthly_price_2012}")

print(f"Average 2020 Speed: {average_speed_2020}")
print(f"Average 2012 Speed: {average_speed_2012}")

average_cost_per_mbps_2012 = average_monthly_price_2012 / average_speed_2012
average_cost_per_mbps_2020 = average_monthly_price_2012 / average_speed_2020

print(f"Average $ per MBPS 2012: {average_cost_per_mbps_2012}")
print(f"Average $ per MBPS 2020: {average_cost_per_mbps_2020}")

ratio_of_mbps = average_cost_per_mbps_2020 / average_cost_per_mbps_2012

print(ratio_of_mbps)

ratio_per_year = pow(ratio_of_mbps, 1/8)

print(ratio_per_year)
