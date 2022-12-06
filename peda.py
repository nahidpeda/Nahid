import os

os.system('clear')



N="""

███╗░░██╗░█████╗░██╗░░██╗██╗██████╗░
████╗░██║██╔══██╗██║░░██║██║██╔══██╗
██╔██╗██║███████║███████║██║██║░░██║
██║╚████║██╔══██║██╔══██║██║██║░░██║
██║░╚███║██║░░██║██║░░██║██║██████╔╝
╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░
"""
A="""

[1] Gmail
[2] Gmail2
[3] web
[4] web2
[5] Facbook
[6] Facbook2
[7] Github
[8] Github2
[9]
"""
kk="""
[1] Mano
[2] Exit
"""
Github2="""
gmail: pedanahid19@gmail.com

pass : Nahid@20087
"""
Github="""
gmail: nahidpeda00@gmaio.com

pass : Nahid@20087
"""
Gmail="""
gmail: pedanahid0@gmail.com

pass : nahidpeda@2008
"""
Gmail2="""
gmail: nahidpeda00@gmail.com

pass : Nahid@20087
"""
web="""
web  : http://nahidff001.rf.gd

Admin: http://nahidff001.rf.gd/wp-admin/

"""
web2="""

web  : http://nahidgameshopbd.rf.gd

Admin: http://nahidgameshopbd.rf.gd/wp-admin/
"""
print(N+A)

mad=input("Enter your id nambee: ")
if mad=="1":
      os.system('clear')
      print(N+Gmail)
if mad=="2":
     os.system('clear')
     print(N+Gmail2)
if mad=="3":
      os.system('clear')
      print(N+web)
if mad=="4":
      os.system('clear')
      print(N+web2)
if mad=="5":
      os.system('clear')
      print(N)
if mad=="6":
      os.system('clear')
      print(N)
if mad=="7":
      os.system('clear')
      print(N+Github)
if mad=="8":
      os.system('clear')
      print(N+Github2)
else:
      print("  ")

print(kk)
kk=input("Enter your cods namber: ")
if kk=="1":
      os.system('python peda.py.py')
if kk=="1":
      os.system('exit')
