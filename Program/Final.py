import datetime 
print("           WELCOME TO THEATRE          ")
print("PLEASE ENTER THE DEATAILS:")
name=input("Name: ")
age=int(input("Age: "))
while True:
      if age>=18:
            break
      else:
            continue
print("Enter Male or Female or Transgender")
while True:
      gen=input("Gender: ")
      if gen=="male" or gen=="female" or gen=="Male" or gen=="Female" or gen=="transgender" or gen=="Transgender":
            break
      else:
            print("You have entered incorrect Gender")
            continue
print("Enter your Date, Month and Year of the movie you want to go")       
while True:
      dd=int(input("Date: "))
      dm=int(input("Month: "))
      dy=int(input("Year: "))
      today=datetime.datetime.now()
      c=datetime.datetime(dy,dm,dd)
      if c>today:
            break
      else:
            print("You have Entered incorrect date")
            print("Please, try again")
            continue
      
      
      
print("Choose the Name of the Movie") 

print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                                        BOOK YOUR SHOW                                                                                      ")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("|   SI.NO    |                    MOVIE NAME                          |             LANGUAGE             |                                               TIMMINGS                           ")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("|            |                                                        |                                  |                                                                            ")
print("|     1      |                    Kaappaan                            |              Tamil               |             11:15 AM,11:50 AM,02:45 PM,03:15 PM,03:50 PM,06:45 PM,07:15 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     2      |                    Oththa Seruppu Size-7               |              Tamil               |             10:15 AM,12:30 PM,01:45 PM,02:15 PM,04:30 PM,05:45 PM,06:15 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     3      |                    Sivappu Manjal Pachai               |              Tamil               |             10:15 AM,11:25 AM,01:45 PM,02:15 PM,03:25 PM,05:45 PM,06:15 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     4      |                    Dream Girl                          |              Hindi               |             09:15 AM,10:50 AM,02:35 PM,01:15 PM,02:50 PM,06:35 PM,05:15 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     5      |                    Namma Veetu Pillai                  |              Tamil               |             09:45 AM,10:30 AM,01:15 PM,01:45 PM,02:30 PM,05:15 PM,05:45 PM ")                                   
print("|            |                                                        |                                  |                                                                            ")
print("|     6      |                    Chhichhore                          |              Hindi               |             09:45 AM,10:30 AM,01:35 PM,01:45 PM,02:30 PM,05:35 PM,05:45 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     7      |                    Comali                              |              Tamil               |             09:45 AM,10:30 AM,02:00 PM,01:45 PM,02:30 PM,06:00 PM,05:45 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     8      |                    Gaddalakonda Ganesh                 |              Telugu              |             09:30 AM,11:40 AM,01:35 PM,01:30 PM,03:40 PM,05:35 PM,05:30 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     9      |                    Abominable                          |              English             |             09:55 AM,11:40 AM,12:55 PM,01:55 PM,03:40 PM,04:55 PM,05:55 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     10     |                    Rambo:Last Blood                    |              English             |             09:00 AM,11:30 AM,01:30 PM,01:00 PM,03:30 PM,05:30 PM,05:00 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     11     |                    Nerkonda Paarvai                    |              Tamil               |             10:15 AM,11:50 AM,03:35 PM,02:15 PM,03:50 PM,07:35 PM,06:15 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     12     |                    Geetha Govindam                     |              Telugu              |             09:15 AM,10:50 AM,01:35 PM,01:15 PM,02:50 PM,05:35 PM,05:15 PM ")                                                               
print("|            |                                                        |                                  |                                                                            ")
print("|     13     |                    Love,Action,Drama                   |              Malayalam           |             08:15 AM,09:50 AM,01:35 PM,12:15 PM,02:50 PM,05:35 PM,04:15 PM ") 
print("|            |                                                        |                                  |                                                                            ")
print("|     14     |                    IT:Chapter Two                      |              English             |             09:30 AM,11:00 AM,02:20 PM,01:30 PM,03:00 PM,06:20 PM,05:30 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     15     |                    Section 375                         |              Hindi               |             09:45 AM,10:50 AM,02:30 PM,01:45 PM,02:50 PM,06:30 PM,05:45 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     16     |                    Gang Leader                         |              Telugu              |             09:30 AM,10:30 AM,11:30 PM,01:30 PM,02:30 PM,03:30 PM,05:30 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     17     |                    The Zoya Factor                     |              Hindi               |             08:15 AM,11:50 AM,01:35 PM,12:15 PM,03:50 PM,05:35 PM,04:15 PM ")
print("|            |                                                        |                                  |                                                                            ")
print("|     18     |                    Mission Mangal                      |              Hindi               |             09:55 AM,10:30 AM,02:30 PM,01:55 PM,02:30 PM,06:30 PM,05:55 PM ")




movie=[]
ch=int(input("Enter the SI.NO of the Movie Name: "))
t=input("Enter the Time of the film: ")
if ch==1:
      while True:
            movie="Kaappaan"
            if t=="11:15 AM" or t=="03:15 PM" or t=="07:15 PM":
                  screen="Screen 1"
                  break
            elif t=="11:50 AM" or t=="03:50 PM":
                  screen="Screen 2"
                  break
            elif t=="02:45 PM" or t=="06:45 PM":
                  screen="screen 3"
                  break
            else:
                  print("You have entered incorrect Time.Please, try again")
                  continue
elif ch==2:
      while True:
            movie="Oththa Serppu Size-7"
            if t=="10:15 AM" or t=="02:15 PM" or t=="06:15 PM":
                  screen="Screen 1"
                  break
            elif t=="12:30 PM" or t=="04:30 PM":
                  screen="Screen 2"
                  break
            elif t=="01:45 PM" or t=="05:45 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==3:
      while True:
            movie="Sivappu Manjal Pachai"
            if t=="10:15 AM" or t=="02:15 PM" or t=="06:15 PM":
                  screen="Screen 1"
                  break
            elif t=="11:25 AM" or t=="03:25 PM":
                  screen="Screen 2"
                  break
            elif t=="01:45 PM" or t=="05:45 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==4:
      while True:
            movie="Dream Girl"
            if t=="10:15 AM" or t=="02:15 PM" or t=="06:15 PM":
                  screen="Screen 1"
                  break
            elif t=="12:30 PM" or t=="04:30 PM":
                  screen="Screen 2"
                  break
            elif t=="01:45 PM" or t=="05:45 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==5:
      while True:
            movie="Namma Veetu Pillai"
            if t=="09:45 AM" or t=="01:45 PM" or t=="05:45 PM":
                  screen="Screen 1"
                  break
            elif t=="10:30 AM" or t=="02:30 PM":
                  screen="Screen 2"
                  break
            elif t=="01:15 PM" or t=="05:15 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==6:
      while True:
            movie="Chhichhore"
            if t=="09:45 AM" or t=="01:45 PM" or t=="05:45 PM":
                  screen="Screen 1"
                  break
            elif t=="10:30 AM" or t=="02:30 PM":
                  screen="Screen 2"
                  break
            elif t=="01:35 PM" or t=="05:35 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==7:
      while True:
            movie="Comali"
            if t=="09:45 AM" or t=="01:45 PM" or t=="05:45 PM":
                  screen="Screen 1"
                  break
            elif t=="10:30 AM" or t=="02:30 PM":
                  screen="Screen 2"
                  break
            elif t=="02:00 PM" or t=="06:00 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==8:
      while True:
            movie="Gaddalakonda Ganesh"
            if t=="09:30 AM" or t=="01:30 PM" or t=="05:30 PM":
                  screen="Screen 1"
                  break
            elif t=="11:40 AM" or t=="03:40 PM":
                  screen="Screen 2"
                  break
            elif t=="01:35 PM" or t=="05:35 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==9:
      while True:
            movie="Abominable"
            if t=="09:55 AM" or t=="01:55 PM" or t=="05:55 PM":
                  screen="Screen 1"
                  break
            elif t=="11:40 AM" or t=="03:40 PM":
                  screen="Screen 2"
                  break
            elif t=="12:55 PM" or t=="04:55 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==10:
      while True:
            movie="Rambo:Last Blood"
            if t=="09:00 AM" or t=="01:00 PM" or t=="05:00 PM":
                  screen="Screen 1"
                  break
            elif t=="11:30 AM" or t=="03:30 PM":
                  screen="Screen 2"
                  break
            elif t=="01:30 PM" or t=="05:30 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==11:
      while True:
            movie="Nerkonda Paarvai"
            if t=="10:15 AM" or t=="11:50 PM" or t=="03:35 PM":
                  screen="Screen 1"
                  break
            elif t=="11:30AM" or t=="03:30 PM":
                  screen="Screen 2"
                  break
            elif t=="03:35 PM" or t=="07:35 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==12:
      while True:
            movie="Geetha Govindam"
            if t=="09:15 AM" or t=="01:15 PM" or t=="05:15 PM":
                  screen="Screen 1"
                  break
            elif t=="10:50 AM" or t=="02:30 PM":
                  screen="Screen 2"
                  break
            elif t=="01:35 PM" or t=="05:35 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==13:
      while True:
            movie="Love,Action,Drama"
            if t=="08:15 AM" or t=="12:15 PM" or t=="04:15":
                  screen="Screen 1"
                  break
            elif t=="09:50 PM" or t=="02:50 PM":
                  screen="Screen 2"
                  break
            elif t=="01:35 PM" or t=="05:35 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==14:
      while True:
            movie="IT:Chapter Two"
            if t=="09:30 AM" or t=="01:30 PM" or t=="05:30":
                  screen="Screen 1"
                  break
            elif t=="11:00 PM" or t=="03:00 PM":
                  screen="Screen 2"
                  break
            elif t=="02:20 PM" or t=="06:20 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==15:
      while True:
            movie="Section 375"
            if t=="09:45 AM" or t=="01:45 PM" or t=="05:45":
                  screen="Screen 1"
                  break
            elif t=="10:50 PM" or t=="02:50 PM":
                  screen="Screen 2"
                  break
            elif t=="02:30 PM" or t=="06:30 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==16:
      while True:
            movie="Gang Leader"
            if t=="09:30 AM" or t=="01:30 PM" or t=="05:30":
                  screen="Screen 1"
                  break
            elif t=="10:30 PM" or t=="02:30 PM":
                  screen="Screen 2"
                  break
            elif t=="11:30 PM" or t=="03:30 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==17:
      while True:
            movie="The Zoya Factor"
            if t=="08:15 AM" or t=="12:15 PM" or t=="04:15":
                  screen="Screen 1"
                  break
            elif t=="11:50 PM" or t=="03:50 PM":
                  screen="Screen 2"
                  break
            elif t=="01:45 PM" or t=="05:45 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue
elif ch==18:
      while True:
            movie="Mission Mangal"
            if t=="09:55 AM" or t=="01:55 PM" or t=="05:55":
                  screen="Screen 1"
                  break
            elif t=="10:30 PM" or t=="02:30 PM":
                  screen="Screen 2"
                  break
            elif t=="02:30 PM" or t=="06:30 PM":
                  screen="Screen 3"
                  break
            else:
                  print("You have entered incorrect Time")
                  print("Please, try again")
                  continue


print("Rs.225 ELITE_2D")
print("_______________________________________________________________________________________________________________________")
print("A1  A2  A3  A4  A5  A6  A7  A8  A9  A10  A11  A12  A13  A14  A15  A16  A17  A18  A19  A20  A21  A22  A23  A24  A25  A26")
print("B1  B2  B3  B4  B5  B6          B9  B10  B11  B12  B13  B14  B15  B16  B17  B18            B21  B22  B23  B24  B25  B26")
print("C1  C2  C3  C4  C5  C6          C9  C10  C11  C12  C13  C14  C15  C16  C17  C18            C21  C22  C23  C24  C25  C26")
print("D1  D2  D3  D4  D5  D6          D9  D10  D11  D12  D13  D14  D15  D16  D17  D18            D21  D22  D23  D24  D25  D26")
print("E1  E2  E3  E4  E5  E6          E9  E10  E11  E12  E13  E14  E15  E16  E17  E18            E21  E22  E23  E24  E25  E26")
print("F1  F2  F3  F4  F5  F6          F9  F10  F11  F12  F13  F14  F15  F16  F17  F18            F21  F22  F23  F24  F25  F26")
print("                                                                                                                       ")
print("                G5  G6          G9  G10  G11  G12  G13  G14  G15  G16  G17  G18            G21  G22  G23  G24  G25  G26")
print("                H5  H6          H9  H10  H11  H12  H13  H14  H15  H16  H17  H18            H21  H22  H23  H24  H25  H26")
print("                I5  I6          I9  I10  I11  I12  I13  I14  I15  I16  I17  I18            I21  I22  I23  I24  I25  I26")

print("Rs.150 BUDGET")
print("________________________________________________________________________________________________________________________")
print("                J5  J6          J9  J10  J11  J12  J13  J14  J15  J16  J17  J18            J21  J22  J23  J24  J25  J26")
print("                K5  K6          K9  K10  K11  K12  K13  K14  K15  K16  K17  K18            K21  K22  K23  K24  K25  K26")


print("                       |-----------------------------------------------------------------|                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |                                                                 |                             ")
print("                       |-----------------------------------------------------------------|                             ")
print("                                          All eyes this way please!                                                    ")

m=[]
price=0
amount=0
n=int(input("Enter the number of tickets you want to book: "))
for i in range(0,n):
  x=input("Enter the seat number:      ")
  m.insert(i,x)
l=len(m)
for i in range (0,l):
  if m[i]=="A1" or m[i]=="A2" or m[i]=="A3" or m[i]=="A4" or m[i]=="A5" or m[i]=="A6" or m[i]=="A7" or m[i]=="A8" or m[i]=="A9" or m[i]=="A10" or m[i]=="A11" or m[i]=="A12" or m[i]=="A13" or m[i]=="A14" or m[i]=="A15" or m[i]=="A16" or m[i]=="A17" or m[i]=="A18" or m[i]=="A19" or m[i]=="A20" or m[i]=="A21" or m[i]=="A22" or m[i]=="A21" or m[i]=="A22" or m[i]=="A23" or m[i]=="A24" or m[i]=="A25" or m[i]=="A26":
      price=225
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="B1" or m[i]=="B2" or m[i]=="B3" or m[i]=="B4" or m[i]=="B5" or m[i]=="B6" or m[i]=="B9" or m[i]=="B10" or m[i]=="B11" or m[i]=="B12" or m[i]=="B13" or m[i]=="B14" or m[i]=="B15" or m[i]=="B16" or m[i]=="B17" or m[i]=="B18" or m[i]=="B21" or m[i]=="B22" or m[i]=="B23" or m[i]=="B24" or m[i]=="B25" or m[i]=="B26":
      price=225
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="C1" or m[i]=="C2" or m[i]=="C3" or m[i]=="C4" or m[i]=="C5" or m[i]=="C6" or m[i]=="C9" or m[i]=="C10" or m[i]=="C11" or m[i]=="C12" or m[i]=="C13" or m[i]=="C14" or m[i]=="C15" or m[i]=="C16" or m[i]=="C17" or m[i]=="C18" or m[i]=="C21" or m[i]=="C22" or m[i]=="C23" or m[i]=="C24" or m[i]=="C25" or m[i]=="C26":
      price=225
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="D1" or m[i]=="D2" or m[i]=="D3" or m[i]=="D4" or m[i]=="D5" or m[i]=="D6" or m[i]=="D9" or m[i]=="D10" or m[i]=="D11" or m[i]=="D12" or m[i]=="D13" or m[i]=="D14" or m[i]=="D15" or m[i]=="D16" or m[i]=="D17" or m[i]=="D18" or m[i]=="D21" or m[i]=="D22" or m[i]=="D23" or m[i]=="D24" or m[i]=="D25" or m[i]=="D26":
      price=225
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="E1" or m[i]=="E2" or m[i]=="E3" or m[i]=="E4" or m[i]=="E5" or m[i]=="E6" or m[i]=="E9" or m[i]=="E10" or m[i]=="E11" or m[i]=="E12" or m[i]=="E13" or m[i]=="E14" or m[i]=="E15" or m[i]=="E16" or m[i]=="E17" or m[i]=="E18" or m[i]=="E21" or m[i]=="E22" or m[i]=="E23" or m[i]=="E24" or m[i]=="E25" or m[i]=="E26":
      price=225
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="F1" or m[i]=="F2" or m[i]=="F3" or m[i]=="F4" or m[i]=="F5" or m[i]=="F6" or m[i]=="F9" or m[i]=="F10" or m[i]=="F11" or m[i]=="F12" or m[i]=="F13" or m[i]=="F14" or m[i]=="F15" or m[i]=="F16" or m[i]=="F17" or m[i]=="F18" or m[i]=="F21" or m[i]=="F22" or m[i]=="F23" or m[i]=="F24" or m[i]=="F25" or m[i]=="F26":
      price=225
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="G1" or m[i]=="G2" or m[i]=="G3" or m[i]=="G4" or m[i]=="G5" or m[i]=="G6" or m[i]=="G9" or m[i]=="G10" or m[i]=="G11" or m[i]=="G12" or m[i]=="G13" or m[i]=="G14" or m[i]=="G15" or m[i]=="G16" or m[i]=="G17" or m[i]=="G18" or m[i]=="G21" or m[i]=="G22" or m[i]=="G23" or m[i]=="G24" or m[i]=="G25" or m[i]=="G26":
      price=225
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="H1" or m[i]=="H2" or m[i]=="H3" or m[i]=="H4" or m[i]=="H5" or m[i]=="H6" or m[i]=="H9" or m[i]=="H10" or m[i]=="H11" or m[i]=="H12" or m[i]=="H13" or m[i]=="H14" or m[i]=="H15" or m[i]=="H16" or m[i]=="H17" or m[i]=="H18" or m[i]=="H21" or m[i]=="H22" or m[i]=="H23" or m[i]=="H24" or m[i]=="H25" or m[i]=="H26":
      price=225
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="I1" or m[i]=="I2" or m[i]=="I3" or m[i]=="I4" or m[i]=="I5" or m[i]=="I6" or m[i]=="I9" or m[i]=="I10" or m[i]=="I11" or m[i]=="I12" or m[i]=="I13" or m[i]=="I14" or m[i]=="I15" or m[i]=="I16" or m[i]=="I17" or m[i]=="I18" or m[i]=="I21" or m[i]=="I22" or m[i]=="I23" or m[i]=="I24" or m[i]=="I25" or m[i]=="I26":
      price=225
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="J5" or  m[i]=="J6" or  m[i]=="J9" or  m[i]=="J10" or  m[i]=="J11" or  m[i]=="J12" or  m[i]=="J13" or  m[i]=="J14" or  m[i]=="J15" or  m[i]=="J16" or  m[i]=="J17" or  m[i]=="J20" or  m[i]=="J21" or  m[i]=="J21" or  m[i]=="J22" or  m[i]=="J23" or  m[i]=="J24" or  m[i]=="J25" or  m[i]=="J26":
      price=150
      print("Your {} seat : Price {}".format(m[i],price))
  elif m[i]=="K5" or  m[i]=="K6" or  m[i]=="K9" or  m[i]=="K10" or  m[i]=="K11" or  m[i]=="K12" or  m[i]=="K13" or  m[i]=="K14" or  m[i]=="K15" or  m[i]=="K16" or  m[i]=="K17" or  m[i]=="K20" or  m[i]=="K21" or  m[i]=="K21" or  m[i]=="K22" or  m[i]=="K23" or  m[i]=="K24" or  m[i]=="K25" or  m[i]=="K26": 
      price=150
      print("Your {} seat : Price {}".format(m[i],price))


  amount=amount+price




print("Your Name                       :",name)
print("Your age                        :",age)
print("Your gender                     :",gen)
print("Date                            :",dd,"-",dm,"-",dy)
print("Number of seats you have booked :",n)
print("Seat numbers                    :",m)
print("Movie Name                      :",movie)
print("Timmings                        :",t)
print("Screen                          :",screen)
print("The total amount to be paid     :",amount)
print("Important note:")
print("Payment should be done on the day of the show")





