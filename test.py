print("CHECK REQUIRED FIELDS IN WORDPRESS-DEPLOYMENT.YAML...\n \n ")

f = open('wordpress-deployment.yaml', mode='r')
file = f.read()
if "apiVersion:" in file:
    print("check apiVersion...")
 
else:
    print("ERROR IN WORDPRESS-DEPLOYMENT FILE")
    raise SystemError()