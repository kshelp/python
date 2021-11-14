#!/usr/bin/env python3
import sys
# xlrd 모듈에서 open_workbook() 함수를 임포트하여 엑셀 파일을 읽고 파싱하는데 
# 사용할 수 있게 한다.
from xlrd import open_workbook

input_file = "sales_2013.xlsx"

# open_workbook() 함수를 사용하여 엑셀 입력 파일을 workbook이라는 이름의 객체로 연다.
workbook = open_workbook(input_file)
# print(type(workbook))
# workbook에 있는 워크시트 수를 출력한다.
print('Number of worksheets:', workbook.nsheets)

for worksheet in workbook.sheets():
	print("Worksheet name:", worksheet.name, "\tRows:", \
			worksheet.nrows, "\tColumns:", worksheet.ncols)
