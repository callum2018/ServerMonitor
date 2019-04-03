
import os


machine = "london.local"
ping = os.system("ping -c 1 " + machine)
print()

if ping == 0:
  print (machine, 'is running without any complications.')
else:
  print (machine, 'is not running.')
