#!/usr/bin/env python3
import sys
# datetime 모듈에서 date() 함수를 임포트해서 뒤에서 값을 날짜로 변환하고 
# 날짜 형식으로 포매팅할 수 있게 한다.
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = "sales_2013.xlsx"
output_file = "3excel_parsing_and_write_keep_dates.xlsx"

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	for row_index in range(worksheet.nrows): # range(7): 0~6
		row_list_output = [] #["1234","John Smith","1/6/2013"]
		for col_index in range(worksheet.ncols): # range(5): 0~4
			if worksheet.cell_type(row_index, col_index) == 3:
				# xldate_as_tuple() 함수를 사용하면 날짜, 시간, 날짜+시간을 
				# 나타내는 엑셀의 숫자를 튜플로 변환할 수 있다.
				date_cell = xldate_as_tuple(worksheet.cell_value\
					(row_index, col_index),workbook.datemode)
				print(date_cell) # (2013, 1, 6, 0, 0, 0)
				date_cell = date(*date_cell[0:3]).strftime\
					('%m/%d/%Y')  # "1/6/2013"
				row_list_output.append(date_cell)
				output_worksheet.write(row_index, col_index, date_cell)
			else:
				non_date_cell = worksheet.cell_value\
					(row_index,col_index)
				row_list_output.append(non_date_cell)
				output_worksheet.write(row_index, col_index,\
					non_date_cell)
output_workbook.save(output_file)