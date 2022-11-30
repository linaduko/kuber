print("HI \nWelcome to my simple test!")

f = open('wordpress-deployment.yaml', mode='r')
line = f.readlines()
m = line[0]
if "v2" in m:
       print("OK")
else:
    raise SystemError()