import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt

df = pd.read_excel(sheet_name=0, io=r"C:\Users\yusef\Downloads\TCP_2021_data_FINAL.xlsx", engine='openpyxl')
print(df)

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='black')
plt.show()


# loc = r"C:\Users\yusef\Downloads\TCP_2021_data_FINAL.xlsx"
#
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
#
# print(sheet.cell_value(0, 0))


