import os
import xlrd
import csv

# Converting Excel to CSV
def csv_from_excel(filename):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open(os.path.splitext(filename)[0]+'.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

    
if __name__=="__main__":
    filename = "D:/IA/sathish.xlsx"
    if os.path.splitext(filename)[1] == ".xlsx":
        csv_from_excel(filename)
    else:
        print("File extension not supported!!")
