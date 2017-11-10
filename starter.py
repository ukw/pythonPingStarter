import os
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print(hostname, 'is up!')
  # os.system('python hello.py')
  os.system('hello.bat')
else:
  print(hostname, 'is down!')
  os.system('python starter.py')