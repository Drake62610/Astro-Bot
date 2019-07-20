import os

#clear activity.log
print(os.path.dirname(os.path.abspath(__file__))+"/../module/nendo")
try:
    os.system("rm "+os.path.dirname(os.path.abspath(__file__))+"/../module/nendo/cache.jpg")
    print("removing cache.jpg")
except e:
    print(e)

try:
    db = os.path.dirname(os.path.abspath(__file__))+"/../module/nendo/nendo.db"
    tmp = []
    
    with open(db, 'r') as data:
        dataList = list(data)
        nbCopy = min(5, len(dataList)) 
        for i in range(0, nbCopy):
            tmp.append(dataList[i])
        data.close
    print("removing nendo.db")
    os.system("rm "+os.path.dirname(os.path.abspath(__file__))+"/../module/nendo/nendo.db")
    os.system("touch "+os.path.dirname(os.path.abspath(__file__))+"/../module/nendo/nendo.db")
    print("adding data in newly nendo.db")
    print(tmp)
    with open(db, 'w') as data:
        for line in tmp:
            data.write(line)
        data.close
except e:
    print(e)
