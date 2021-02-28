import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt
from matplotlib import pyplot
from scipy.optimize import curve_fit
import math

import openpyxl

def objective(x, a, b):
    return pow(a, x) + b


df = pd.read_excel(sheet_name=0, io=r"C:\Users\yusef\Downloads\TCP_2021_data_FINAL.xlsx", engine='openpyxl')
data = df.values


# choose the input and output variables

years, average_us_peak = data[7:12, 1], data[7:12, 4]
average_us_peak_mobile = data[7:12, 9]

print(average_us_peak)
print(average_us_peak_mobile)

averages = []

for i in range(5):
    sum = average_us_peak[i] + average_us_peak_mobile[i]
    average = sum / 2
    averages.append(average)

pyplot.plot(years, averages, 'o')
pyplot.title("Average Download Speed in The United States During 2017 - 2021 (Mbps)")
pyplot.show()

for value in years:
    print(value)
    value = value - 2016
    print(value)

print(years)

# curve fit
popt, _ = curve_fit(objective, years, average_us_peak)
# summarize the parameter values
a, b = popt
print(f"{a} {b}")
# plot input vs output
pyplot.scatter(years, average_us_peak)
# define a sequence of inputs between the smallest and largest known inputs
x_line = range(min(years), max(years), 1)
# calculate the output for the range
y_line = objective(x_line, a, b)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.title("Mbps over time")
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
