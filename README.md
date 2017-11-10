# pythonPingStarter
Python Script that pings to check if Internet is live before executing a bat, good for mining scripts


1.Create new Python file, let's call it starter.py and paste the following code:
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
  
2.Create a hello.bat file in the same folder as the Python Script and paste this script:
@echo Hello world. !!!
@pause


3.Run starter.py and see the magic (disable your internet connection to test it properly)


Made by ukw.

Thanks.

If you find this useful buy me a beer in crypto:
ETH Address: 0x339f49bfcc21f1d605909811e9492cb34da3f2fb
ZEC Address: t1gcZMApJnNHHmcVboXRUVFYtVQcLVBLfDw
BTC Address: 12Rcu5sL95fJnhmvwZ2TAkJ7U5HSGMV6rC
DGE Address: DBxxN6bhARgRzGCpx8BraWAxzBdGubzf27
LTC Address: LYYPdCM9pNj8jxXDKAkR5wDNsx4hYa7DRC
DSH Address: XwpTSGQw4BG6in2jFvf9FR5gS8WD6MWdB1
