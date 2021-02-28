import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt
from matplotlib import pyplot
from scipy.optimize import curve_fit
import math

import openpyxl


def general_exponential(x, c_1, c_2, c_3):
    return c_1 * pow(c_2, x) + c_3


def strict_exponential(x, c_1, c_2):
    return c_1 * pow(1.5, x) + c_2


fit_function = strict_exponential

df = pd.read_excel(sheet_name=0, io=r"C:\Users\yusef\Downloads\TCP_2021_data_FINAL.xlsx", engine='openpyxl')
data = df.values

# choose the input and output variables

years, average_us_peak = data[7:12, 1], data[7:12, 4]
average_us_peak_mobile = data[7:12, 8]

average_uk_peak = data[7:12, 5]
average_uk_peak_mobile = data[7:12, 9]

print(average_us_peak)
print(average_us_peak_mobile)

average_us = []
average_uk = []

for i in range(5):
    sum_us = average_us_peak[i] + average_us_peak_mobile[i]
    average = sum_us / 2
    average_us.append(average)

    sum_uk = average_uk_peak[i] + average_uk_peak_mobile[i]
    average = sum_uk / 2
    average_uk.append(average)

for year in years:
    year = year - 2016

years = [1, 2, 3, 4, 5][::-1]
print(f"averages:{average_us}")

print(f"years: {years}")

# pyplot.plot(years, average_us, 'o')
# pyplot.title("Average Download Speed in The United States During 2017 - 2021 (Mbps)")
# pyplot.xlabel("Years After 2016")
# pyplot.show()

print(f"Average uk stuff: {average_uk}")

# curve fit
popt, _ = curve_fit(fit_function, years, average_uk)
# summarize the parameter values
a, b = popt

# Outputting the curve function coefficients
# print(f"{a} * {b} ^ x + {c}")
print(f"{a} * 1.5 ^ x + {b}")



# plot input vs output
pyplot.scatter(years, average_uk)
# define a sequence of inputs between the smallest and largest known inputs
x_line = np.linspace(min(years), max(years), 20)
# calculate the output for the range
y_line = fit_function(x_line, a, b)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.title("UK Average Mbps from 2017 - 2021")
pyplot.xlabel("Years After 2016")
pyplot.ylabel("Average Bandwidth (in Mbps)")
pyplot.show()

# loc = r"C:\Users\yusef\Downloads\TCP_2021_data_FINAL.xlsx"
#
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# print(sheet.cell_value(0, 0))

# Give the location of the file
# path = r"C:\Users\yusef\Downloads\TCP_2021_data_FINAL.xlsx"
#
# # To open the workbook
# # workbook object is created
# wb_obj = openpyxl.load_workbook(path)
#
# # Get workbook active sheet object
# # from the active attribute
# sheet_obj = wb_obj.active
#
# # Cell objects also have a row, column,
# # and coordinate attributes that provide
# # location information for the cell.
#
# # Note: The first row or
# # column integer is 1, not 0.
#
# # Cell object is created by using
# # sheet object's cell() method.
#
# values = []
# x = np.linspace(2017, 2021, 5)
#
# counter = 1
#
# for row in range(9, 14):
#     values.append(sheet_obj.cell(row=row, column=5).value)
#
# print(values)
#
# values = values[::-1]
# plt.plot(x, np.array(values), 'o', color='black')
# plt.show()
#
#
# def exponential(x, a, b):
#     return a ^ x + b
