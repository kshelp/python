#!/usr/bin/env python3
import pandas as pd
import sys

input_file = "sales_2013.xlsx"
output_file = "pandas_parsing_and_write_keep_dates.xlsx"

data_frame = pd.read_excel(input_file, sheetname='january_2013')

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()