# Purple cipher machine made in Python 3+ by Daiya Masuda
# Please read Readme.md 
# Code is a bit of mess but it works!
# Run the program in python 3+ and simply follow the instructions.

from builtins import input
from collections import Counter
import string

class Purple:

    
    def __init__(self, vowels, consonanti,speedi,consonantii,speedii, consonantiii,speediii, plugboard, text):
        self.vowels = vowels
        self.consonanti = consonanti
        self.consonantii = consonantii

        self.consonantiii =  consonantiii
        self.plugboard = plugboard
        self.text = text
        self.speedi = 0
        self.speedii = 1
        self.speediii = 2

    def changeSpeed1(self,newSpeed):
        if( 0 <= newSpeed <= 3 ):
            self.speedi = newSpeed
    def changeSpeed2(self,newSpeed):
        if( 0 <= newSpeed <= 3 ):
            self.speedi = newSpeed
    def changeSpeed3(self,newSpeed):
        if( 0 <= newSpeed <= 3 ):
            self.speedi = newSpeed
    def changev(self,newVowel):
        if(newVowel == 25):
            newVowel = 0
        self.vowels = newVowel

    def changeci(self,newConsonant):
        if(newConsonant == 25):
            newConsonant = 0
        self.consonanti = newConsonant

    def changecii(self,newConsonant):
        if(newConsonant == 25):
            newConsonant = 0
        self.consonantii = newConsonant

    def changeciii(self,newConsonant):
        if(newConsonant == 25):
            newConsonant = 0
        self.consonantiii = newConsonant

    def changeSwitch(self,newSwitch):
        self.switch = newSwitch

    def changePlug(self,newplug):
        self.plugboard = newplug

    def changeText(self,newText):
        self.text = newText

    def plugboardEncrypt(self):
        plugboard = [ord(c) for c in self.plugboard]
        plaintext = self.text
        encrypted = []
        for c in plaintext:
            c = c.upper()
            if(c in ['A','E','I','O','U','Y']):
                c = self.changeToVowelIndex(c)
                encrypted.append(plugboard[c])
            elif(c in ['B' , ' C' , ' D' , ' F' , ' G' , ' H' , ' J' , ' K' , ' L' , ' M' , ' N' , ' P' , ' Q' , ' R' , ' S' , ' T' , ' V' , ' X' , ' Z' , ' W']):
                c = (self.changeToConsIndex(c))
                c = int(c) + int(6)
                encrypted.append(plugboard[c])
            else:
                encrypted.append(c)
        final = ''.join(chr(i) for i in encrypted)
        return final

    def changeVowelToAscii(self,newChar):
        if newChar == 1:
            newChar = 'A'
        elif newChar == 2:
            newChar = 'E'
        elif newChar == 3:
            newChar = 'I'
        elif newChar == 4:
            newChar = 'O'
        elif newChar == 5:
            newChar = 'U'
        elif newChar == 6:
            newChar = 'Y'
        return newChar

    def changeToVowelIndex(self,newChar):

        if newChar == 'A':
            newChar = 0
        elif newChar == 'E':
            newChar = 1
        elif newChar == 'I':
            newChar = 2
        elif newChar == 'O':
            newChar = 3
        elif newChar == 'U':
            newChar = 4
        elif newChar == 'Y':
            newChar = 5
        return newChar

    def changeConsToAscii(self,newChar):
        if newChar == 1:
            newChar = 'B'
        elif newChar == 2:
            newChar = 'C'
        elif newChar == 3:
            newChar = 'D'
        elif newChar == 4:
            newChar = 'F'
        elif newChar == 5:
            newChar = 'G'
        elif newChar == 6:
            newChar = 'H'
        elif newChar == 7:
            newChar = 'J'
        elif newChar == 8:
            newChar = 'K'
        elif newChar == 9:
            newChar = 'L'
        elif newChar == 10:
            newChar = 'M'
        elif newChar == 11:
            newChar = 'N'
        elif newChar == 12:
            newChar = 'P'
        elif newChar == 13:
            newChar = 'Q'
        elif newChar == 14:
            newChar = 'R'
        elif newChar == 15:
            newChar = 'S'
        elif newChar == 16:
            newChar = 'T'
        elif newChar == 17:
            newChar = 'V'
        elif newChar == 18:
            newChar = 'W'
        elif newChar == 19:
            newChar = 'X'
        elif newChar == 20:
            newChar = 'Z'
        return newChar

    def changeToConsIndex(self,newChar):
        if newChar == 'B':
            newChar = 0
        elif newChar == 'C':
            newChar = 1
        elif newChar == 'D':
            newChar = 2
        elif newChar == 'F':
            newChar = 3
        elif newChar == 'G':
            newChar = 4
        elif newChar == 'H':
            newChar = 5
        elif newChar == 'J':
            newChar = 6
        elif newChar == 'K':
            newChar = 7
        elif newChar == 'L':
            newChar = 8
        elif newChar == 'M':
            newChar = 9
        elif newChar == 'N':
            newChar = 10
        elif newChar == 'P':
            newChar = 11
        elif newChar == 'Q':
            newChar = 12
        elif newChar == 'R':
            newChar = 13
        elif newChar == 'S':
            newChar = 14
        elif newChar == 'T':
            newChar = 15
        elif newChar == 'V':
            newChar = 16
        elif newChar == 'W':
            newChar = 17
        elif newChar == 'X':
            newChar = 18
        elif newChar == 'Z':
            newChar = 19
        return newChar

    def switchV(self):
        if(self.vowels+1 <= 24):
            self.vowels = self.vowels+1
        else: 
            #中速に指定されたスイッチは、6字側が第25表→第1表に進むときに連れ回りして1段階進む。
            self.vowels = 0
            self.switchMedium()

    def switchSlow(self):
        #低速に指定されたスイッチは、中速が第25表→第01表に進む1文字前に1段階進む。
        if(self.speedi == 2):
            if(self.vowels == 25):
                if(self.consonanti + 1 < 24):
                    self.changeci(self.consonanti+1)
                else:
                    self.changeci(0)
            else:
                if(self.speedii == 1):
                    self.changecii(0)
                elif(self.speediii == 1):
                    self.changeciii(0)

        elif(self.speedii == 2): 
            if(self.vowels == 25):
                if(self.consonantii + 1 < 24):
                    self.changecii(self.consonantii+1)
                else:
                    self.changecii(0)
            else:
                if(self.speedi == 1):
                    self.changeci(0)
                elif(self.speediii == 1):
                    self.changeciii(0)

        elif(self.speediii == 2):
            if(self.vowels == 25):
                if(self.consonantiii + 1 < 24):
                    self.changeciii(self.consonantiii+1)
                else:
                    self.changeciii(0)
            else:
                if(self.speedi == 1):
                    self.changeci(0)
                elif(self.speedii == 1):
                    self.changecii(0)

    def switchMedium(self):
        #中速に指定されたスイッチは、6字側が第25表→第1表に進むときに連れ回りして1段階進む。
        if(self.speedi == 1):
            if(self.vowels == 0):
                if(self.consonanti + 1 <= 24):
                    self.changeci(self.consonanti+1)
                else:
                    self.changeci(0)
                    self.switchSlow()
            else:
                pass
        elif(self.speedii == 1): 
            if(self.vowels == 0):
                if(self.consonantii + 1 <= 24):
                    self.changecii(self.consonantii+1)
                else:
                    self.changecii(0)
                    self.switchSlow()
            else:
                pass
        elif(self.speediii == 1):
            if(self.vowels == 0):
                if(self.consonantii + 1 <= 24):
                    self.changeciii(self.consonantiii+1)
                else:
                    self.changeciii(0)
                    self.switchSlow()
            else:
                pass

    def switchFast(self):
        #高速に指定されたスイッチは、中速または低速が進まない場合に1段階進む。
        if(self.speedi == 0):
            if(self.vowels == 0 or self.consonantii  == 0 or self.consonantiii == 0):
                #pass
                pass
            else:
                self.changeci(self.consonanti+1)
        elif(self.speedii == 0): 
            if(self.vowels == 0 or self.consonanti  == 0 or self.consonantiii == 0):
                #pass
                pass
            else:
                self.changecii(self.consonantii+1)
        elif(self.speediii == 0):
            if(self.vowels == 0 or self.consonanti  == 0 or self.consonantii == 0):
                #pass
                pass
            else:
                self.changeciii(self.consonantiii+1)

    def encrypt(self):
        original = self.text
        originalV = self.vowels
        originalconsi = self.consonanti
        originalconsii = self.consonantii
        originalconsiii = self.consonantiii
        newtext = self.text
        #print("Plain text is ", newtext)
        newtext = self.plugboardEncrypt() #INPUT PLUGBOARD ENCRYPTION
        c = ''
        encrypted = []
        for c in newtext:
            #print('Being Encrypted: ' + c)
            #CHECK IF A CHAR IS VOWEL OR NOT
            vowels = 'AEIOUY'
            #print("Vowels: " ,self.vowels," Gear one : ", self.consonanti, " Gear Two : ", self.consonantii, " Gear Three :", self.consonantiii)

            if all(c in vowels for char in vowels):
                #print('going in Vowel switches: ' , c)
                c = self.changeToVowelIndex(c)
               # print('Out of Vowel switches: ' , c)
                c = self.encryptVowel(c)
               # print('Out of encrytVowel switches: ' , c)
                c = self.changeVowelToAscii(c)
              #  print('coming out from ChangeVowel switches: ' , c)
                #print('Vowel Encrypt done : ', c)
                encrypted.append(c) #ENCRYPT VOWELS
            else: 
               # print('going in Consonant switches: ' , c)
                c = self.changeToConsIndex(c)
                #print('Out of Consoindex: ' , c)
                c = self.encryptConsonant(c)
                #print('Out of encrytCons switches: ' , c)
                c = self.changeConsToAscii(c)
                #print('coming out from ChangeCon switches: ' , c)
                #print('Cons Encrypt done : ', c)

                encrypted.append(c) #ENCRYPT CONSONANT: 1st switch, 2nd switch and third switch. 

        final = ''.join(encrypted)

        self.changeText(final)

        newtext = self.plugboardEncrypt()
        self.changev(originalV)
        self.changeci(originalconsi)
        self.changecii(originalconsii)
        self.changeciii(originalconsiii)
        self.changeText(original)
        return newtext

    def encryptVowel(self,c):
        six = self.vowels
       # print("Vowels: " ,self.vowels," Gear one : ", self.consonanti, " Gear Two : ", self.consonantii, " Gear Three :", self.consonantiii)

        # 1: A 2:E 3:I 4:O 5:U 6:Y
        SIXES_DATA = \
        [[2, 1, 3, 5, 4, 6],
        [6, 3, 5, 2, 1, 4],
        [1, 5, 4, 6, 2, 3],
        [4, 3, 2, 1, 6, 5],
        [3, 6, 1, 4, 5, 2],
        [2, 1, 6, 5, 3, 4],
        [6, 5, 4, 2, 1, 3],
        [3, 6, 1, 4, 5, 2],
        [5, 4, 2, 6, 3, 1],
        [4, 5, 3, 2, 1, 6],
        [2, 1, 4, 5, 6, 3],
        [5, 4, 6, 3, 2, 1],
        [3, 1, 2, 6, 4, 5],
        [4, 2, 5, 1, 3, 6],
        [1, 6, 2, 3, 5, 4],
        [5, 4, 3, 6, 1, 2],
        [6, 2, 5, 3, 4, 1],
        [2, 3, 4, 1, 5, 6],
        [1, 2, 3, 5, 6, 4],
        [3, 1, 6, 4, 2, 5],
        [6, 5, 1, 2, 4, 3],
        [1, 3, 6, 4, 2, 5],
        [6, 4, 5, 1, 3, 2],
        [4, 6, 1, 2, 5, 3],
        [5, 2, 4, 3, 6, 1]]

        a = SIXES_DATA[six]
        x = a.index(c+1)
        #print("Six : ", six)
        #print("x : " , x)
        #print("c : " , c)
        self.switchV()    
        self.switchFast()
        # encrypted.append(plugboard.index(ord(c)) + 65)
       # print("encrypted : " , encrypted)
        return x+1

    def encryptConsonant(self,c):

        gearOne = self.consonanti
        gearTwo = self.consonantii
        gearThree = self.consonantiii

        self.switchFast()
        
       # print("Vowels: " ,self.vowels," Gear one : ", gearOne, " Gear Two : ", gearTwo, " Gear Three :", gearThree, " c: ", c)
        TWENTIES_1_DATA = \
        [[6, 19, 14, 1, 10, 4, 2, 7, 13, 9, 8, 16, 3, 18, 15, 11, 5, 12, 20, 17],
        [4, 5, 16, 17, 14, 1, 20, 15, 3, 8, 18, 11, 12, 13, 10, 19, 2, 6, 9, 7],
        [17, 1, 13, 6, 15, 11, 19, 12, 16, 18, 10, 3, 7, 14, 8, 20, 4, 9, 2, 5],
        [3, 14, 20, 4, 6, 16, 8, 19, 2, 12, 17, 9, 5, 1, 11, 10, 7, 13, 15, 18],
        [19, 6, 8, 20, 13, 5, 18, 4, 10, 3, 16, 15, 14, 12, 7, 2, 17, 11, 1, 9],
        [2, 11, 9, 14, 7, 19, 6, 3, 18, 13, 12, 8, 10, 15, 16, 17, 20, 4, 5, 1],
        [16, 7, 6, 18, 9, 10, 13, 1, 17, 2, 5, 4, 11, 19, 20, 14, 8, 15, 3, 12],
        [1, 20, 7, 16, 12, 14, 5, 18, 15, 10, 13, 6, 8, 3, 4, 9, 11, 17, 19, 2],
        [17, 9, 11, 8, 20, 18, 7, 14, 1, 16, 15, 5, 19, 2, 6, 12, 4, 10, 13, 3],
        [12, 8, 17, 9, 3, 20, 4, 10, 14, 5, 7, 18, 2, 16, 13, 6, 1, 19, 15, 11],
        [20, 1, 16, 11, 2, 17, 9, 4, 8, 15, 10, 13, 3, 18, 14, 5, 6, 7, 12, 19],
        [5, 4, 15, 2, 13, 19, 6, 16, 12, 14, 8, 7, 17, 10, 18, 3, 9, 1, 11, 20],
        [15, 17, 10, 19, 16, 2, 11, 8, 9, 7, 3, 14, 18, 13, 12, 1, 5, 20, 6, 4],
        [11, 12, 7, 3, 8, 15, 16, 6, 4, 20, 2, 5, 1, 9, 19, 18, 10, 14, 17, 13],
        [12, 16, 2, 7, 4, 8, 15, 19, 5, 1, 11, 9, 20, 17, 6, 14, 13, 3, 18, 10],
        [8, 15, 18, 1, 12, 11, 17, 14, 20, 16, 13, 19, 9, 7, 3, 4, 2, 5, 10, 6],
        [7, 3, 5, 18, 17, 13, 19, 20, 14, 11, 9, 10, 2, 6, 1, 15, 12, 16, 4, 8],
        [10, 13, 4, 14, 18, 3, 2, 17, 11, 19, 20, 1, 6, 12, 9, 7, 15, 8, 5, 16],
        [13, 7, 9, 12, 20, 16, 14, 10, 19, 6, 1, 2, 11, 4, 5, 3, 18, 17, 8, 15],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [9, 20, 12, 5, 10, 17, 1, 13, 7, 15, 4, 3, 16, 8, 18, 11, 19, 2, 14, 6],
        [18, 15, 2, 13, 1, 7, 10, 5, 19, 17, 6, 20, 9, 11, 12, 8, 3, 4, 16, 14],
        [16, 18, 19, 10, 11, 20, 5, 9, 1, 4, 12, 13, 7, 6, 17, 2, 14, 15, 3, 8],
        [5, 8, 1, 15, 19, 9, 12, 2, 6, 3, 14, 17, 4, 20, 16, 13, 18, 10, 7, 11],
        [14, 10, 4, 8, 9, 12, 3, 11, 17, 20, 19, 6, 15, 5, 2, 18, 16, 7, 1, 13]]

        TWENTIES_2_DATA = \
        [[15, 9, 1, 5, 17, 19, 3, 2, 10, 8, 11, 18, 12, 16, 6, 13, 20, 4, 14, 7],
        [12, 6, 15, 2, 4, 9, 8, 16, 19, 17, 5, 11, 20, 7, 10, 18, 1, 14, 13, 3],
        [4, 18, 5, 8, 16, 1, 12, 15, 20, 14, 13, 17, 11, 2, 7, 9, 6, 3, 10, 19],
        [6, 11, 2, 20, 14, 7, 18, 12, 15, 3, 8, 5, 10, 1, 17, 19, 9, 16, 4, 13],
        [7, 2, 13, 3, 9, 4, 17, 14, 1, 12, 18, 20, 6, 11, 16, 15, 5, 8, 19, 10],
        [5, 17, 14, 7, 10, 9, 19, 20, 8, 13, 1, 2, 16, 3, 4, 12, 11, 18, 6, 15],
        [8, 4, 3, 11, 19, 13, 2, 9, 12, 16, 10, 17, 14, 15, 20, 6, 18, 1, 7, 5],
        [20, 1, 16, 10, 15, 8, 14, 11, 18, 5, 3, 7, 13, 17, 19, 4, 2, 9, 12, 6],
        [9, 8, 7, 15, 5, 2, 4, 13, 17, 1, 11, 6, 19, 18, 14, 10, 3, 20, 16, 12],
        [10, 12, 11, 18, 8, 16, 20, 17, 5, 6, 9, 3, 4, 19, 13, 7, 1, 14, 15, 2],
        [11, 7, 14, 4, 18, 20, 6, 1, 13, 19, 12, 15, 5, 9, 16, 2, 17, 10, 8, 3],
        [2, 3, 9, 10, 13, 14, 15, 16, 7, 11, 20, 12, 18, 6, 1, 5, 8, 17, 19, 4],
        [16, 10, 15, 1, 17, 3, 13, 9, 4, 7, 6, 8, 2, 14, 5, 11, 12, 19, 18, 20],
        [19, 16, 18, 12, 3, 13, 9, 10, 6, 2, 17, 14, 11, 4, 7, 20, 15, 5, 1, 8],
        [18, 14, 12, 19, 1, 7, 10, 6, 11, 15, 5, 9, 8, 20, 17, 4, 3, 13, 2, 16],
        [20, 3, 19, 2, 4, 5, 11, 14, 9, 10, 18, 16, 15, 12, 8, 7, 13, 6, 17, 1],
        [3, 6, 4, 14, 2, 12, 16, 5, 18, 20, 7, 19, 1, 15, 9, 8, 10, 11, 13, 17],
        [5, 15, 20, 9, 10, 17, 1, 19, 13, 12, 4, 2, 7, 6, 11, 14, 16, 8, 3, 18],
        [14, 20, 13, 17, 5, 18, 8, 4, 2, 15, 16, 1, 9, 19, 3, 6, 7, 10, 12, 11],
        [8, 11, 1, 6, 19, 14, 5, 18, 17, 3, 10, 13, 12, 20, 15, 16, 4, 2, 7, 9],
        [17, 19, 6, 1, 12, 15, 20, 7, 16, 9, 3, 11, 13, 10, 2, 18, 8, 4, 5, 14],
        [1, 5, 12, 20, 6, 11, 14, 8, 9, 7, 19, 4, 3, 13, 10, 17, 18, 16, 15, 2],
        [16, 8, 10, 13, 11, 6, 19, 5, 3, 4, 15, 20, 17, 2, 18, 1, 14, 7, 9, 12],
        [19, 13, 8, 16, 20, 10, 7, 1, 2, 18, 14, 6, 9, 5, 12, 3, 17, 15, 11, 4],
        [13, 1, 17, 15, 7, 4, 16, 3, 14, 5, 2, 10, 18, 8, 11, 9, 19, 12, 20, 6]]

        TWENTIES_3_DATA = \
        [[7, 19, 11, 3, 20, 1, 10, 6, 16, 12, 17, 13, 8, 9, 4, 18, 5, 14, 15, 2],
        [15, 17, 14, 2, 12, 13, 8, 3, 1, 19, 9, 4, 10, 7, 11, 20, 16, 6, 18, 5],
        [2, 11, 20, 12, 1, 19, 4, 10, 9, 14, 6, 15, 13, 3, 7, 16, 18, 8, 5, 17],
        [16, 3, 12, 9, 4, 20, 6, 19, 18, 2, 5, 8, 14, 11, 10, 1, 15, 17, 13, 7],
        [12, 18, 16, 4, 9, 3, 15, 13, 6, 20, 8, 2, 7, 10, 5, 19, 14, 1, 17, 11],
        [13, 9, 5, 6, 8, 7, 12, 17, 14, 18, 20, 10, 2, 19, 11, 15, 4, 3, 1, 16],
        [4, 7, 2, 15, 17, 10, 19, 5, 8, 16, 1, 12, 3, 13, 6, 14, 20, 9, 11, 18],
        [9, 6, 4, 10, 18, 16, 8, 14, 5, 12, 17, 1, 20, 15, 13, 19, 2, 11, 7, 3],
        [5, 14, 18, 17, 13, 15, 11, 12, 7, 8, 3, 6, 1, 2, 20, 4, 9, 10, 16, 19],
        [11, 16, 9, 18, 3, 12, 5, 15, 10, 1, 14, 17, 2, 4, 19, 6, 8, 7, 13, 20],
        [19, 8, 3, 15, 14, 5, 1, 11, 2, 10, 12, 16, 18, 20, 17, 7, 13, 4, 9, 6],
        [1, 12, 17, 13, 9, 7, 14, 2, 15, 4, 5, 11, 6, 16, 3, 8, 18, 19, 20, 10],
        [3, 4, 10, 12, 1, 18, 2, 8, 14, 13, 19, 7, 16, 6, 15, 9, 17, 20, 5, 11],
        [9, 11, 6, 5, 10, 4, 17, 19, 13, 15, 7, 2, 12, 18, 14, 20, 1, 16, 8, 3],
        [8, 13, 14, 16, 19, 12, 20, 7, 10, 3, 15, 9, 4, 17, 1, 11, 5, 2, 6, 18],
        [18, 16, 15, 4, 2, 17, 13, 12, 6, 11, 20, 19, 14, 5, 9, 1, 8, 7, 3, 10],
        [14, 1, 7, 20, 6, 13, 16, 18, 12, 9, 4, 17, 5, 11, 2, 3, 10, 15, 19, 8],
        [17, 19, 1, 11, 7, 2, 18, 4, 3, 8, 10, 5, 15, 12, 16, 9, 6, 13, 20, 14],
        [10, 15, 2, 14, 11, 6, 7, 1, 16, 20, 13, 3, 9, 8, 18, 17, 19, 5, 12, 4],
        [20, 9, 8, 6, 12, 11, 2, 5, 4, 7, 16, 14, 17, 3, 15, 10, 13, 19, 18, 1],
        [11, 20, 13, 8, 16, 10, 18, 14, 19, 6, 15, 4, 1, 17, 7, 5, 3, 9, 2, 12],
        [16, 5, 10, 19, 4, 18, 15, 17, 1, 3, 2, 20, 11, 6, 8, 13, 7, 12, 14, 9],
        [6, 10, 19, 16, 5, 9, 1, 20, 17, 4, 11, 18, 7, 14, 13, 2, 12, 8, 3, 15],
        [8, 7, 5, 1, 15, 14, 9, 16, 11, 17, 18, 6, 19, 20, 3, 12, 4, 2, 10, 13],
        [13, 2, 17, 7, 14, 8, 3, 9, 20, 5, 16, 10, 6, 1, 12, 15, 11, 18, 4, 19]]
        
        #a = SIXES_DATA[six-1]
        #x = a.index(c+1)
        #self.switchV()    
        #self.switchFast()

        encryptedOne = TWENTIES_1_DATA[gearOne]
        x = encryptedOne.index(c+1)
       # print("Vowels: " ,self.vowels," Gear one : ", gearOne, " Gear Two : ", gearTwo, " Gear Three :", gearThree, " x: ", x, " c: ", c)
        encryptedTwo = TWENTIES_2_DATA[gearTwo]
        x = encryptedTwo.index(x+1)
       # print("Vowels: " ,self.vowels," Gear one : ", gearOne, " Gear Two : ", gearTwo, " Gear Three :", gearThree, " x: ", x, " c: ", c)
        encryptedThree = TWENTIES_3_DATA[gearThree]
        x = encryptedThree.index(x+1)
        #print("Vowels: " ,self.vowels," Gear one : ", gearOne, " Gear Two : ", gearTwo, " Gear Three :", gearThree, " x: ", x, " c: ", c)
        self.switchV()

        return x+1

    def decrypt(self):

        original = self.text
        originalV = self.vowels
        originalconsi = self.consonanti
        originalconsii = self.consonantii
        originalconsiii = self.consonantiii
        newtext = self.text
        #print("Plain text is ", newtext)
        newtext = self.plugboardEncrypt() #INPUT PLUGBOARD ENCRYPTION
        c = ''
        encrypted = []
        for c in newtext:
            #print('Being Encrypted: ' + c)
            #CHECK IF A CHAR IS VOWEL OR NOT
            vowels = 'AEIOUY'
            #print("Vowels: " ,self.vowels," Gear one : ", self.consonanti, " Gear Two : ", self.consonantii, " Gear Three :", self.consonantiii)

            if all(c in vowels for char in vowels):
               # print('going in Vowel switches: ' , c)
                c = self.changeToVowelIndex(c)
                #print('Out of Vowel switches: ' , c)
                c = self.decryptVowel(c)
               # print('Out of encrytVowel switches: ' , c)
                c = self.changeVowelToAscii(c)
               # print('coming out from ChangeVowel switches: ' , c)
               # print('Vowel Encrypt done : ', c)
                encrypted.append(c) #ENCRYPT VOWELS
            else: 
               # print('going in Consonant switches: ' , c)
                c = self.changeToConsIndex(c)
                #print('Out of Consoindex: ' , c)
                c = self.decryptConsonant(c)
               # print('Out of encrytCons switches: ' , c)
                c = self.changeConsToAscii(c)
               # print('coming out from ChangeCon switches: ' , c)
               #s print('Cons Encrypt done : ', c)

                encrypted.append(c) #ENCRYPT CONSONANT: 1st switch, 2nd switch and third switch. 

        final = ''.join(encrypted)

        self.changeText(final)

        newtext = self.plugboardEncrypt()
        self.changev(originalV)
        self.changeci(originalconsi)
        self.changecii(originalconsii)
        self.changeciii(originalconsiii)
        self.changeText(original)
        return newtext
    
    def decryptVowel(self,c):
        six = self.vowels
        #print("Vowels: " ,self.vowels," Gear one : ", self.consonanti, " Gear Two : ", self.consonantii, " Gear Three :", self.consonantiii)

        # 1: A 2:E 3:I 4:O 5:U 6:Y
        SIXES_DATA = \
        [[2, 1, 3, 5, 4, 6],
        [6, 3, 5, 2, 1, 4],
        [1, 5, 4, 6, 2, 3],
        [4, 3, 2, 1, 6, 5],
        [3, 6, 1, 4, 5, 2],
        [2, 1, 6, 5, 3, 4],
        [6, 5, 4, 2, 1, 3],
        [3, 6, 1, 4, 5, 2],
        [5, 4, 2, 6, 3, 1],
        [4, 5, 3, 2, 1, 6],
        [2, 1, 4, 5, 6, 3],
        [5, 4, 6, 3, 2, 1],
        [3, 1, 2, 6, 4, 5],
        [4, 2, 5, 1, 3, 6],
        [1, 6, 2, 3, 5, 4],
        [5, 4, 3, 6, 1, 2],
        [6, 2, 5, 3, 4, 1],
        [2, 3, 4, 1, 5, 6],
        [1, 2, 3, 5, 6, 4],
        [3, 1, 6, 4, 2, 5],
        [6, 5, 1, 2, 4, 3],
        [1, 3, 6, 4, 2, 5],
        [6, 4, 5, 1, 3, 2],
        [4, 6, 1, 2, 5, 3],
        [5, 2, 4, 3, 6, 1]]

        a = SIXES_DATA[six]
        x = a[c]
        #print("Six : ", six)
        #print("x : " , x)
        #print("c : " , c)
        self.switchV()    
        self.switchFast()
        # encrypted.append(plugboard.index(ord(c)) + 65)
       # print("encrypted : " , encrypted)
        return x

    def decryptConsonant(self,c):

        gearOne = self.consonanti
        gearTwo = self.consonantii
        gearThree = self.consonantiii

        self.switchFast()
        
        #print("Vowels: " ,self.vowels," Gear one : ", gearOne, " Gear Two : ", gearTwo, " Gear Three :", gearThree, " c: ", c)
        TWENTIES_1_DATA = \
        [[6, 19, 14, 1, 10, 4, 2, 7, 13, 9, 8, 16, 3, 18, 15, 11, 5, 12, 20, 17],
        [4, 5, 16, 17, 14, 1, 20, 15, 3, 8, 18, 11, 12, 13, 10, 19, 2, 6, 9, 7],
        [17, 1, 13, 6, 15, 11, 19, 12, 16, 18, 10, 3, 7, 14, 8, 20, 4, 9, 2, 5],
        [3, 14, 20, 4, 6, 16, 8, 19, 2, 12, 17, 9, 5, 1, 11, 10, 7, 13, 15, 18],
        [19, 6, 8, 20, 13, 5, 18, 4, 10, 3, 16, 15, 14, 12, 7, 2, 17, 11, 1, 9],
        [2, 11, 9, 14, 7, 19, 6, 3, 18, 13, 12, 8, 10, 15, 16, 17, 20, 4, 5, 1],
        [16, 7, 6, 18, 9, 10, 13, 1, 17, 2, 5, 4, 11, 19, 20, 14, 8, 15, 3, 12],
        [1, 20, 7, 16, 12, 14, 5, 18, 15, 10, 13, 6, 8, 3, 4, 9, 11, 17, 19, 2],
        [17, 9, 11, 8, 20, 18, 7, 14, 1, 16, 15, 5, 19, 2, 6, 12, 4, 10, 13, 3],
        [12, 8, 17, 9, 3, 20, 4, 10, 14, 5, 7, 18, 2, 16, 13, 6, 1, 19, 15, 11],
        [20, 1, 16, 11, 2, 17, 9, 4, 8, 15, 10, 13, 3, 18, 14, 5, 6, 7, 12, 19],
        [5, 4, 15, 2, 13, 19, 6, 16, 12, 14, 8, 7, 17, 10, 18, 3, 9, 1, 11, 20],
        [15, 17, 10, 19, 16, 2, 11, 8, 9, 7, 3, 14, 18, 13, 12, 1, 5, 20, 6, 4],
        [11, 12, 7, 3, 8, 15, 16, 6, 4, 20, 2, 5, 1, 9, 19, 18, 10, 14, 17, 13],
        [12, 16, 2, 7, 4, 8, 15, 19, 5, 1, 11, 9, 20, 17, 6, 14, 13, 3, 18, 10],
        [8, 15, 18, 1, 12, 11, 17, 14, 20, 16, 13, 19, 9, 7, 3, 4, 2, 5, 10, 6],
        [7, 3, 5, 18, 17, 13, 19, 20, 14, 11, 9, 10, 2, 6, 1, 15, 12, 16, 4, 8],
        [10, 13, 4, 14, 18, 3, 2, 17, 11, 19, 20, 1, 6, 12, 9, 7, 15, 8, 5, 16],
        [13, 7, 9, 12, 20, 16, 14, 10, 19, 6, 1, 2, 11, 4, 5, 3, 18, 17, 8, 15],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [9, 20, 12, 5, 10, 17, 1, 13, 7, 15, 4, 3, 16, 8, 18, 11, 19, 2, 14, 6],
        [18, 15, 2, 13, 1, 7, 10, 5, 19, 17, 6, 20, 9, 11, 12, 8, 3, 4, 16, 14],
        [16, 18, 19, 10, 11, 20, 5, 9, 1, 4, 12, 13, 7, 6, 17, 2, 14, 15, 3, 8],
        [5, 8, 1, 15, 19, 9, 12, 2, 6, 3, 14, 17, 4, 20, 16, 13, 18, 10, 7, 11],
        [14, 10, 4, 8, 9, 12, 3, 11, 17, 20, 19, 6, 15, 5, 2, 18, 16, 7, 1, 13]]

        TWENTIES_2_DATA = \
        [[15, 9, 1, 5, 17, 19, 3, 2, 10, 8, 11, 18, 12, 16, 6, 13, 20, 4, 14, 7],
        [12, 6, 15, 2, 4, 9, 8, 16, 19, 17, 5, 11, 20, 7, 10, 18, 1, 14, 13, 3],
        [4, 18, 5, 8, 16, 1, 12, 15, 20, 14, 13, 17, 11, 2, 7, 9, 6, 3, 10, 19],
        [6, 11, 2, 20, 14, 7, 18, 12, 15, 3, 8, 5, 10, 1, 17, 19, 9, 16, 4, 13],
        [7, 2, 13, 3, 9, 4, 17, 14, 1, 12, 18, 20, 6, 11, 16, 15, 5, 8, 19, 10],
        [5, 17, 14, 7, 10, 9, 19, 20, 8, 13, 1, 2, 16, 3, 4, 12, 11, 18, 6, 15],
        [8, 4, 3, 11, 19, 13, 2, 9, 12, 16, 10, 17, 14, 15, 20, 6, 18, 1, 7, 5],
        [20, 1, 16, 10, 15, 8, 14, 11, 18, 5, 3, 7, 13, 17, 19, 4, 2, 9, 12, 6],
        [9, 8, 7, 15, 5, 2, 4, 13, 17, 1, 11, 6, 19, 18, 14, 10, 3, 20, 16, 12],
        [10, 12, 11, 18, 8, 16, 20, 17, 5, 6, 9, 3, 4, 19, 13, 7, 1, 14, 15, 2],
        [11, 7, 14, 4, 18, 20, 6, 1, 13, 19, 12, 15, 5, 9, 16, 2, 17, 10, 8, 3],
        [2, 3, 9, 10, 13, 14, 15, 16, 7, 11, 20, 12, 18, 6, 1, 5, 8, 17, 19, 4],
        [16, 10, 15, 1, 17, 3, 13, 9, 4, 7, 6, 8, 2, 14, 5, 11, 12, 19, 18, 20],
        [19, 16, 18, 12, 3, 13, 9, 10, 6, 2, 17, 14, 11, 4, 7, 20, 15, 5, 1, 8],
        [18, 14, 12, 19, 1, 7, 10, 6, 11, 15, 5, 9, 8, 20, 17, 4, 3, 13, 2, 16],
        [20, 3, 19, 2, 4, 5, 11, 14, 9, 10, 18, 16, 15, 12, 8, 7, 13, 6, 17, 1],
        [3, 6, 4, 14, 2, 12, 16, 5, 18, 20, 7, 19, 1, 15, 9, 8, 10, 11, 13, 17],
        [5, 15, 20, 9, 10, 17, 1, 19, 13, 12, 4, 2, 7, 6, 11, 14, 16, 8, 3, 18],
        [14, 20, 13, 17, 5, 18, 8, 4, 2, 15, 16, 1, 9, 19, 3, 6, 7, 10, 12, 11],
        [8, 11, 1, 6, 19, 14, 5, 18, 17, 3, 10, 13, 12, 20, 15, 16, 4, 2, 7, 9],
        [17, 19, 6, 1, 12, 15, 20, 7, 16, 9, 3, 11, 13, 10, 2, 18, 8, 4, 5, 14],
        [1, 5, 12, 20, 6, 11, 14, 8, 9, 7, 19, 4, 3, 13, 10, 17, 18, 16, 15, 2],
        [16, 8, 10, 13, 11, 6, 19, 5, 3, 4, 15, 20, 17, 2, 18, 1, 14, 7, 9, 12],
        [19, 13, 8, 16, 20, 10, 7, 1, 2, 18, 14, 6, 9, 5, 12, 3, 17, 15, 11, 4],
        [13, 1, 17, 15, 7, 4, 16, 3, 14, 5, 2, 10, 18, 8, 11, 9, 19, 12, 20, 6]]

        TWENTIES_3_DATA = \
        [[7, 19, 11, 3, 20, 1, 10, 6, 16, 12, 17, 13, 8, 9, 4, 18, 5, 14, 15, 2],
        [15, 17, 14, 2, 12, 13, 8, 3, 1, 19, 9, 4, 10, 7, 11, 20, 16, 6, 18, 5],
        [2, 11, 20, 12, 1, 19, 4, 10, 9, 14, 6, 15, 13, 3, 7, 16, 18, 8, 5, 17],
        [16, 3, 12, 9, 4, 20, 6, 19, 18, 2, 5, 8, 14, 11, 10, 1, 15, 17, 13, 7],
        [12, 18, 16, 4, 9, 3, 15, 13, 6, 20, 8, 2, 7, 10, 5, 19, 14, 1, 17, 11],
        [13, 9, 5, 6, 8, 7, 12, 17, 14, 18, 20, 10, 2, 19, 11, 15, 4, 3, 1, 16],
        [4, 7, 2, 15, 17, 10, 19, 5, 8, 16, 1, 12, 3, 13, 6, 14, 20, 9, 11, 18],
        [9, 6, 4, 10, 18, 16, 8, 14, 5, 12, 17, 1, 20, 15, 13, 19, 2, 11, 7, 3],
        [5, 14, 18, 17, 13, 15, 11, 12, 7, 8, 3, 6, 1, 2, 20, 4, 9, 10, 16, 19],
        [11, 16, 9, 18, 3, 12, 5, 15, 10, 1, 14, 17, 2, 4, 19, 6, 8, 7, 13, 20],
        [19, 8, 3, 15, 14, 5, 1, 11, 2, 10, 12, 16, 18, 20, 17, 7, 13, 4, 9, 6],
        [1, 12, 17, 13, 9, 7, 14, 2, 15, 4, 5, 11, 6, 16, 3, 8, 18, 19, 20, 10],
        [3, 4, 10, 12, 1, 18, 2, 8, 14, 13, 19, 7, 16, 6, 15, 9, 17, 20, 5, 11],
        [9, 11, 6, 5, 10, 4, 17, 19, 13, 15, 7, 2, 12, 18, 14, 20, 1, 16, 8, 3],
        [8, 13, 14, 16, 19, 12, 20, 7, 10, 3, 15, 9, 4, 17, 1, 11, 5, 2, 6, 18],
        [18, 16, 15, 4, 2, 17, 13, 12, 6, 11, 20, 19, 14, 5, 9, 1, 8, 7, 3, 10],
        [14, 1, 7, 20, 6, 13, 16, 18, 12, 9, 4, 17, 5, 11, 2, 3, 10, 15, 19, 8],
        [17, 19, 1, 11, 7, 2, 18, 4, 3, 8, 10, 5, 15, 12, 16, 9, 6, 13, 20, 14],
        [10, 15, 2, 14, 11, 6, 7, 1, 16, 20, 13, 3, 9, 8, 18, 17, 19, 5, 12, 4],
        [20, 9, 8, 6, 12, 11, 2, 5, 4, 7, 16, 14, 17, 3, 15, 10, 13, 19, 18, 1],
        [11, 20, 13, 8, 16, 10, 18, 14, 19, 6, 15, 4, 1, 17, 7, 5, 3, 9, 2, 12],
        [16, 5, 10, 19, 4, 18, 15, 17, 1, 3, 2, 20, 11, 6, 8, 13, 7, 12, 14, 9],
        [6, 10, 19, 16, 5, 9, 1, 20, 17, 4, 11, 18, 7, 14, 13, 2, 12, 8, 3, 15],
        [8, 7, 5, 1, 15, 14, 9, 16, 11, 17, 18, 6, 19, 20, 3, 12, 4, 2, 10, 13],
        [13, 2, 17, 7, 14, 8, 3, 9, 20, 5, 16, 10, 6, 1, 12, 15, 11, 18, 4, 19]]
        
        #a = SIXES_DATA[six-1]
        #x = a.index(c+1)
        #self.switchV()    
        #self.switchFast()
        encryptedThree = TWENTIES_3_DATA[gearThree]
        x = encryptedThree[c]
        y = self.changeConsToAscii(x)

        #print("Vowels: " ,self.vowels," Gear one : ", gearOne, " Gear Two : ", gearTwo, " Gear Three :", gearThree, " x: ", x, " c: ", c, ' y: ',y)
        encryptedTwo = TWENTIES_2_DATA[gearTwo]
        x = encryptedTwo[x-1]
        y = self.changeConsToAscii(x)
       # print("Y is "+ y)
       # print("Vowels: " ,self.vowels," Gear one : ", gearOne, " Gear Two : ", gearTwo, " Gear Three :", gearThree, " x: ", x, " c: ", c)
        encryptedOne = TWENTIES_1_DATA[gearOne]
        x = encryptedOne[x-1]
        y = self.changeConsToAscii(x)
        #print("Y is "+ y)

       # print("Vowels: " ,self.vowels," Gear one : ", gearOne, " Gear Two : ", gearTwo, " Gear Three :", gearThree, " x: ", x, " c: ", c)
        self.switchV()

        return x


def menu(p1):
    print("Please pick an option: ")
    print(" e for encrypt, d for decrypt, s for settings, i for input text, and x for exit.")
    option = input()

    if "x" in option.lower()[:1]:
        return -1

    if "s" in option.lower()[:1]:
        print("The defalut settings for the machine is: ")
        print("-----------------------------------------------------------------")
        print("Vowel Switch Initial Position: ", p1.vowels )
        print("1st Consonants Switch Initial Position: ", p1.consonanti)
        print("2nd Consonants Switch Initial Position: ", p1.consonantii)
        print("3rd Consonants Switch Initial Position: ", p1.consonantiii)
        print("Switchboard settings: Option 1: 1st switch: ",p1.speedi, ", 2nd switch: ", p1.speedii ,", 3rd switch: ",p1.speediii)
        print("Input plugboard settings: ", p1.plugboard)
        print("-----------------------------------------------------------------")
        settings = 0
        while (settings != 'q'):
            print("Which setting would you like to change?")
            print("Please type 1 for: Vowel Switch Initial Position")
            print("Please type 2 for: 1st Consonants Switch Initial Position")
            print("Please type 3 for: 2nd Consonants Switch Initial Position")
            print("Please type 4 for: 3rd Consonants Switch Initial Position")
            print("Please type 5 for: Switchboard settings: Option 1")
            print("Please type 6 for: Input plugboard settings")
            print("Please type q for quit settings.")
            print("-----------------------------------------------------------------")
            settings = input()
            if(settings == '1'):
                print("You have to set stepping vowel switch initial position. Please pick a number between 1 - 25")
                print("Vowels switch: ")
                vowels = int(input())
                while 1 > vowels > 25:
                    print("Error : Please pick a number between 1 - 25 ")
                    print("Vowels switch: ")
                    vowels = int(input())
                print("-----------------------------------------------------------------")
                p1.changev(vowels-1)
            elif(settings == '2'):
                print("You have to set stepping consonants switch initial positions. Please pick a number between 1 - 25")
                print("Consonants switch 1: ")
                consonanti = int(input())
                while 1 > consonanti > 25:
                    print("Error : Please pick a number between 1 - 25 ")
                    print("Consonants switch 1: ")
                    consonanti = int(input())
                p1.changeci(consonanti-1)
            elif(settings == '3'):
                print("Please pick a number between 1-25. Consonants switch 2: ")
                consonantii = int(input())
                while 1 > consonantii > 25:
                    print("Error : Please pick a number between 1 - 25 ")
                    print("Consonants switch 2: ")
                    consonantii = int(input())
                p1.changecii(consonantii-1)
            elif(settings == '4'):
                print("Please pick a number between 1-25. Consonants switch 3: ")
                consonantiii = int(input())
                while 1 > consonantiii > 25:
                    print("Error : Please pick a number between 1 - 25 ")
                    print("Consonants switch 2: ")
                    consonantiii = int(input())
                p1.changeciii(consonantiii-1)
            elif(settings == '5'):
                print("")
                print("You have to set a switchboard rotate speed settings. ")
                
                print("You have 6 options to pick from: ")
                print("-----------------------------------------------------------------")
                print("Option 1: 1st switch: Fast      2nd switch: Medium    3rd switch: Slow")
                print("Option 2: 1st switch: Fast      2nd switch: Slow      3rd switch: Medium")
                print("Option 3: 1st switch: Medium    2nd switch: Fast      3rd switch: Slow")
                print("Option 4: 1st switch: Medium    2nd switch: Slow      3rd switch: Fast")
                print("Option 5: 1st switch: Slow      2nd switch: Fast      3rd switch: Medium")
                print("Option 6: 1st switch: Slow      2nd switch: Medium    3rd switch: Fast")
                print("-----------------------------------------------------------------")
                print("Please enter a number between 1 and 6")
                switch = int(input())
                while 1 > switch > 6:
                    print("Error : Please pick a number between 1 - 6 ")
                    print("")
                    print("-----------------------------------------------------------------")
                    print("Option 1: 1st switch: Fast      2nd switch: Medium    3rd switch: Slow")
                    print("Option 2: 1st switch: Fast      2nd switch: Slow      3rd switch: Medium")
                    print("Option 3: 1st switch: Medium    2nd switch: Fast      3rd switch: Slow")
                    print("Option 4: 1st switch: Medium    2nd switch: Slow      3rd switch: Fast")
                    print("Option 5: 1st switch: Slow      2nd switch: Fast      3rd switch: Medium")
                    print("Option 6: 1st switch: Slow      2nd switch: Medium    3rd switch: Fast")
                    print("-----------------------------------------------------------------")
                    print("Please enter a number between 1 and 6")
                    switch = int(input())
                    speed1 = 0
                    speed2 = 0
                    speed3 = 0
                    if switch == 1:
                        #                   SLOW          MEDIUM             FAST 
                        speed1 = 2
                        speed2 = 1
                        speed3 = 0
                    elif switch == 2:
                        speed1 = 2
                        speed2 = 0
                        speed3 = 1
                    elif switch == 3:
                        speed1 = 1
                        speed2 = 2
                        speed3 = 0
                    elif switch == 4:
                        speed1 = 1
                        speed2 = 0
                        speed3 = 2
                    elif switch == 5:
                        speed1 = 0
                        speed2 = 2
                        speed3 = 1
                    elif switch == 6:
                        speed1 = 0
                        speed2 = 1
                        speed3 = 2


                    p1.changeSpeed1(speed1)
                    p1.changeSpeed2(speed2)
                    p1.changeSpeed3(speed3)

                # if switch == 1:
                #     #SLOW MEDIUM FAST
                #     switchset= ['consonantiii','consonantii','consonanti']
                # if switch == 2:
                #     switchset= ['consonantii','consonantiii','consonanti']
                # if switch == 3:
                #     switchset= ['consonantiii','consonanti','consonantii']
                # if switch == 4:
                #     switchset= ['consonantii','consonanti','consonantiii']
                # if switch == 5:
                #     switchset= ['consonanti','consonantiii','consonantii']
                # if switch == 6:
                #     switchset= ['consonanti','consonantii','consonantiii']
            elif(settings == '6'):
                print("Current input plugboard settings: "+ p1.plugboard)
                valid_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                plug = ''
                while True:
                    print("Please input plugboard settings. ")
                    print("You have to type all characters between A-Z without any duplicates in any order:")
                    plug = input()
                    plug.upper()
                    if all(char in valid_characters for char in plug):
                        break
                    print("That's invalid, please try again.")
                p1.changePlug(plug)
            elif(settings == 'q'):
                break
            else:
                print("Error, please pick a number between 1-6 or type q to quit settings.")
                settings = input()
        return menu(p1)

    if "i" in option.lower()[:1]:
        print("You can only use A-Z and no special cases or numbers or space.")
        print("Please type a text to be ciphered.")
        string = input()
        string.upper()
        while string.isalpha == False:
            print("Error: Please only use A-Z and no special cases or numbers or space.")
            print("Please type a text to be ciphered.")
            string = input()
            string.upper()
        p1.changeText(string)
        print("Set input text complete... Going back to menu")
        print("")
        return menu(p1)

    if "e" in option.lower()[:1]:
        print('Before encryption: ' + p1.text)
        output = p1.encrypt()
        print("Encrypted string is :",output)
        print("Encryption complete... Going back to menu")
        print("")
        return menu(p1)

    if "d" in option.lower()[:1]:
        output = p1.decrypt()
        print("Decrypted string is :",output)
        print("Decryption complete... Going back to menu")
        print("")
        return menu(p1)

    else:
        print("Error, please make sure you typed the right option.")
        print("")
        return menu(p1)

#print("Hello, welcome to Purple Cipher Machine in Python by Daiya Masuda")
# WHILE CHAR != Q. SETTINGS MENU.
#test = Purple(8,0,2,23,1,5,0,'AEIOUYBCDFGHJKLMNPQRSTVWXZ','ASFHBJNAWFKMWAFMWAKF')
#menu(test)
#print("Exiting... ")

