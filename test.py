from time import sleep


print("CHECK REQUIRED FIELDS IN WORDPRESS-DEPLOYMENT.YAML...\n \n ")

f = open('wordpress-deployment.yaml', mode='r')
file = f.read()
if "apiVersion: v1" in file:
    sleep(2)
    print("check apiVersion...")
    sleep(2)
    print("...ok")
else:
    print("ERROR IN WORDPRESS-DEPLOYMENT FILE: incorrect apiVersion")
    raise ValueError()
if "kind:" in file:
    sleep(2)
    print("check kind...")
    sleep(2)
    print("...ok")
else:
    raise ValueError()
if "metadata:" in file:
    sleep(2)
    print("check metadata...")
    sleep(2)
    print("...ok")
else:
    raise ValueError() 
if "spec" in file:
    sleep(2)
    print("check spec...")
    sleep(2)
    print("...ok")
else:
    raise ValueError() 