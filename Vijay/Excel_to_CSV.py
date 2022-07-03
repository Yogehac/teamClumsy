import os
import pandas as pd

def excel_to_csv(filename):
    read_file = pd.read_excel (filename)
  
    read_file.to_csv (os.path.splitext(filename)[0]+'.csv', 
                      index = None,
                      header = True)

    df = pd.DataFrame(pd.read_csv(os.path.splitext(filename)[0]+'.csv'))


def getCSV(filename):
    if os.path.splitext(filename)[1] == ".csv":
        with open(filename, 'r') as file:
            return file.readlines()
    else:
        excel_to_csv(filename)
        with open(os.path.splitext(filename)[0]+'.csv', 'r') as file:
            return file.readlines()
'''  
if __name__=="__main__":
    filename = "D:/IA/excel/sathish.xlsx"
    getCSV(filename)
'''
