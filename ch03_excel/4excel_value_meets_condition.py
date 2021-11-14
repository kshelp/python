#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = "sales_2013.xlsx"
output_file = "4excel_value_meets_condition.xlsx"

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

sale_amount_column_index = 3
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	# data라는 빈 리스트를 만든다. 출력 파일에 쓰고자 하는 입력 파일의 모든 행을 
	# 이 리스트에 채울 것이다.
	data = []  # ["Customer Name","Invoice Number",...,"2345",
	# 헤더 행의 값을 추출한다.
	header = worksheet.row_values(0)
	# 헤더 행을 필터링 조건으로 판별하는 것은 의미가 없으므로 그대로 data에 추가한다.
	data.append(header)
	for row_index in range(1,worksheet.nrows): # range(1,7): 1~6
			row_list = []
			# Sale Amount 열의 데이터 값을 담을 sale_amount라는 변수를 만든다. 
			# cell_value() 함수는 13행에서 정의된 sales_amount_column_index의 
			# 인덱스를 사용하여 Sale Amount 열을 찾는다.
			sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)
			if sale_amount > 1400.0:
				for column_index in range(worksheet.ncols): # range(5):0~4
					cell_value = worksheet.cell_value(row_index,column_index)
					cell_type = worksheet.cell_type(row_index, column_index)
					if cell_type == 3:
						date_cell = xldate_as_tuple(cell_value,workbook.datemode)
						date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
						row_list.append(date_cell)
					else:
						row_list.append(cell_value)
			if row_list:
				data.append(row_list)

	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)