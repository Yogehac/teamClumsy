import json

with open('req.json','r') as req:
    file = json.load(req)
descdraw = []
for i in file.keys():
    # print(i)
    # print(file[i])
    for j in file[i]:
        # print(j)
        descdraw.append([j["Description"],j["Drawing_No"]])
responselist = []
txtFile = ''
with open(txtFile) as fileT:
    for i in descdraw:
        for line in fileT.readlines():
            if i[0] in line and i[1] in line:
                # print(line)
                newl = line[line.index(i[1]) + len(i[1]):]
                num = []
                temp = newl
                print(temp)
                n = '0123456789'
                l = ''
                for x in temp:
                    if x not in n:
                        if len(l) > 0:
                            num.append(int(l))
                            l = ''
                    elif x in n:
                        l += x
            print(num)
            responselist.append([*i,*num])

        # l = line.strip()
        # if l == '\\n':
        # pass
        # l = line.split('|')
        # row.append(l)
        # for i in line.split(""):
        #     row[-1].append(i)

# print(row)
# for i in row:
#     print(i)

# a = 'hat 123 y 40'
# b = a.split()
# id = 'hat 123 y'
# if id in a:
#     print (a[a.index(id)+len(id):])