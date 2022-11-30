print("HI \nWelcome to my simple test!")

f = open('wordpress-deployment.yaml', mode='r')
line = f.readlines()
m = line[0]
try:
    if "v2" in m:
        print("OK")
    except:
        print('ERROR:\n', traceback.format_exc())