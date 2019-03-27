from subprocess import check_output
output = check_output(["uptime"]).decode("utf-8").split()

print (output)
time = output[0]
user = output[-7]
load_1 = output [-3]
load_2 = output [-2]
load_3 = output [-1]
load_average = load_1 + load_2 + load_3

print (time)
print (user)
print ("Load average for the last 1 minute, 5 minutes and 15 minutes is: ", load_average)