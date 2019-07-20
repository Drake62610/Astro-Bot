import os

#clear activity.log
try:
    os.system("rm "+os.path.dirname(os.path.abspath(__file__))+"/../../activity.log")
    print("removing activity.log")
except e:
    print(e)
try:
    os.system("touch "+os.path.dirname(os.path.abspath(__file__))+"/../../activity.log")
    print("activity.log successfully created")
except e:
    print(e)
