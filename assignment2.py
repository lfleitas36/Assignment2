#Assignment 2   Leslie Fleitas ID: 6189077
#I used information from PPt Lesson#2 Part 1 and 2 for the completition of this assignment
#and https://www.tutorialspoint.com/How-to-check-if-a-character-is-upper-case-in-Python

import sys
import socket

#Task 1 (Constructor)
class Assignment2:
    def __init__(self, year):
        self.year = year

    #Task 2 (Age)
    def tellAge(self, currentYear):

        age = currentYear - self.year
        sys.stdout.write("Your age is %d\n" % age)

    #Task 3 (List)
    def listAnniversaries(self):
        aniv_List = []

        age = 2022 - self.year
        count = 10
        while count <= age:
            aniv_List.append(count)
            count += 10

        return aniv_List

    #Task 4 (String Manipulation)
    def modifyYear(self, n):

        txtYear = str(self.year)
        txtMltpNum = str(self.year * n)
        nmber = (txtYear[:-2] * n + txtMltpNum[0::2])

        return nmber

    #Task 5 (Loop and Conditional statements)
    @staticmethod
    def checkGoodString(string):


       if len(string)>=9 and (string[0].islower()): #check if the string is at least 9 char long and first letter upper

          count = 0
          for d in string: #for every char in the string verify if is a number
              if d.isdigit(): #if is a number increment the count (next line)
                  count +=1

              else:
                  pass

          if count == 1:
              return True
          else:
              return False

       else:

           return False

       return bool()

    #Task 6 (Socket)
    @staticmethod
    def connectTcp(host, port):
        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn = sock.connect((host, port))
            sock.close()
            return True

        except:

            return False







#a = Assignment2(2000)
# a.tellAge(2022)
# ret = a.listAniversaries()
# print(ret)
# ret1 = a.modifyYear(5)
# print(ret1)
# ret2 = a.checkGoodString("foobar0more")
# print(ret2)
# ret2 = a.checkGoodString("Foobar0more")
# print(ret2)
# ret2 = a.checkGoodString("Foobarmore")
# print(ret2)
# retval = a.connectTcp("www.google.com", 80)
# if retval:
#      print("Connection established correctly")
# else:
#      print("Some error")




