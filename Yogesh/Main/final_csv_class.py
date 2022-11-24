import json
import csv
from single_file_excel_process import single_xlsx_processing as sfex

import paths as pp


class final_csv:
    def __init__(self, id):
        self.id = id
        self.csvpath = ""
        self.final_function()

    # Loads yogi json
    def loadmain(self):
        with open(pp.mainLog, "r") as mainlog:
            mainjso = json.load(mainlog)
            return mainjso

    # gets path of xlsx,stores path of processed csv and returns reqID dict
    def getreq(self):
        d = self.loadmain()
        reqxlpath = d["pending"][self.id]["reqFile"]
        self.csvpath = sfex(reqxlpath, self.id).opcsvfile
        print("Processed csv created")
        return d["pending"][self.id]

    # Prepare item menu as a list
    # Items as list of lists

    def rows_ofmenu_lists(self):
        with open(self.csvpath, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            menu_data = data[19:50]
            items_data = []
            for i in menu_data:
                if i[0] != ' ':
                    items_data.append(i)
            # print(items_data,"\n")
        return items_data

    # Creates dictionary if 2 lists given
    def createD(self, d, l):
        a = dict(zip(l, d))
        return a

    # Creates list of dictionaries
    def listcreation(self, li):
        superlist = []
        for i in li[1:]:
            if i[1] != '':
                superlist.append(self.createD(i, li[0]))
                # devi = li.index(i)
                li.remove(i)
        # print(li,"\n")
        return superlist

    # creates dict with xlsx path as key and cname as value
    def clientDict(self):
        d = {}
        for i, j in self.req_id_dict["quotedComp"].items():
            if j["quote"]:
                d[j["MailInfo"]["Attachments"][0]] = j['cName']
        print(d)
        return d

    # makes final big csv
    def makeFinal(self, jsonfile, FF):
        x = jsonfile
        # print(x)
        with open(FF, 'w') as F:
            F.write(self.writeLine(x[0], 'k'))
            for i in x:
                F.write(self.writeLine(i, 'v'))

            print('Done')

    # write lines for final big csv
    def writeLine(self, dic, t, u=0):
        temp = ''
        if t == 'k':
            d = list(dic.keys())
        else:
            d = list(dic.values())
        for i in d:
            if d.index(i) > 3:
                if t == 'k':
                    temp += str(i) + ',,'
                else:
                    temp += str(i[0]) + ',{},'.format(i[1])
            else:
                temp += str(i) + ','
        if t == 'k':
            temp += '\n'
            for i in d:
                if d.index(i) > 3:
                    temp += 'Rate,Amount,'
                else:
                    temp += ','
            temp += '\n'
        # if u != devi:
        #     temp += '\n{}\n'.format(u)
        #     devi = u
        # else:
        #     temp+='\n'
        temp += '\n'
        # print(temp)
        return temp

    # final and main function

    def final_function(self):
        self.req_id_dict = self.getreq()
        rows_as_list_req = self.rows_ofmenu_lists()
        # print(rows_as_list_req)
        #
        cli_dict = self.clientDict()
        lastdictlist = []
        dict_of_rows_request = self.listcreation(rows_as_list_req)
        # print(dict_of_rows_request)

        for x in dict_of_rows_request:
            for y, z in cli_dict.items():
                self.csvpath = sfex(y, self.id).opcsvfile

                rows_as_list_comp = self.rows_ofmenu_lists()
                dict_of_rows_comp = self.listcreation(rows_as_list_comp)
                # print(dict_of_rows_comp)

                for rows in dict_of_rows_comp[0:]:
                    if rows["Rate"] == ' ':
                        rows["Rate"] = 0
                    if rows["Amount"] == ' ':
                        rows["Amount"] = 0
                    if rows["Quantity"] == ' ':
                        rows["Quantity"] = 0
                    # print(rows)
                    rows["Amount"] = int(float(rows["Rate"])) * \
                        int(float(rows["Quantity"]))

                    if x["Material Code"] == rows["Material Code"]:
                        x[z] = {'Rate': rows["Rate"], 'Amount': rows["Amount"]}

        for x in dict_of_rows_request:
            lastdict = {"Description of Goods": x["Description of Goods"], "Material Code": x["Material Code"],
                        "Qty": x["Quantity"], "UOM": x["UOM"]}
            for y in cli_dict.values():
                lastdict[y] = [x[y]["Rate"], x[y]["Amount"]]
            # lastdict = {"Description of Goods" : x["Description of Goods"],"Material Code" : x["Material Code"], "Qty" : x["Quantity"], "UOM" : x["UOM"], cli_dict.keys()[]: [x[cli_dict[y]]["Rate"],x[cli_dict[y]]["Amount"]]}
            lastdictlist.append(lastdict)
        # print(dict_of_rows_request)
        # print(lastdictlist)

        self.makeFinal(lastdictlist, f"{pp.reports + self.id}.csv")
