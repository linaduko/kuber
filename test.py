print("HI \nWelcome to my simple test!")

f = open('wordpress-deployment.yaml', mode='r')
line = f.readlines()
m = line[0]
try:
        if "v1" in m:
                print("OK")
except ValueError:
        print("ERROR: API VERSION ERROR")
        exit()

