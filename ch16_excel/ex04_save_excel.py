import glob
import pandas as pd

excel_file_name = './ch16_excel/담당자별_판매량_통합.xlsx'

excel_total_file_writer = pd.ExcelWriter(excel_file_name, engine='xlsxwriter')
total_data1.to_excel(excel_total_file_writer, index=False, sheet_name='담당자별_판매량_통합')
excel_total_file_writer.save()

glob.glob(excel_file_name)