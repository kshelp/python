#!/usr/bin/env python3
import sys
# xlrd의 open_workbook() 함수를 임포트한다.
from xlrd import open_workbook
from xlwt import Workbook

input_file = "sales_2013.xlsx"
output_file = "2excel_parsing_and_write.xlsx"

# xlwt의 Workbook 객체를 인스턴스화하여 결과를 출력하여 엑셀 통합 문서에 쓸 수 있다.
output_workbook = Workbook()
# xlwt의 add_sheet() 함수를 사용하여 출력하는 엑셀 통합 문서 안에 jan_2013_output 
# 이라는 워크시트를 추가한다.
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# xlrd의 open_workbook() 함수는 입력되는 엑셀 통합 문서를 workbook 객체로 연다.
with open_workbook(input_file) as workbook:
	# workbook 객체에 sheet_by_name() 함수를 사용하여 january_2013이라는 이름의 
	# 워크시트에 연결한다.
	worksheet = workbook.sheet_by_name('january_2013')
	for row_index in range(worksheet.nrows): # range(7): 0~6
		for column_index in range(worksheet.ncols): # range(5): 0~4
			output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
output_workbook.save(output_file)



