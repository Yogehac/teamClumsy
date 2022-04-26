with open('C:\\Users\\DEVI\\OneDrive\\Desktop\\pytry\\eng1.txt')as file :
    # print(file.readlines())
    # row = []
    for line in file.readlines():
        id = 'KSC-05-022a'
        if 'ROLLERDESIGN CHAIN' in line and 'KSC-05-022a' in line :
            # print(line)
            newl = line[line.index(id)+len(id):]
            num = []
            temp = newl
            print(temp) 
            n = '0123456789'
            l = ''
            for x in temp:
                if x not in n :
                    if len(l) > 0:
                        num.append(int(l))
                        l = ''
                elif x in n:
                    l += x
            print(num)
            
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
