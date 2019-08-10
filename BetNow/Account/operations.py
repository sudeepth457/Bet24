
import random,math,re
from datetime import date
def GenerateOTP():
    otp = ""
    for i in range(5):
        otp += str((math.floor(random.random() * 10)))

    return otp

def productcalculate(product):
    prod = product.split(" ")
    if len(prod) == 4:
        underlier = prod[0]
        expiry = prod[1]
        strike = prod[2]
        excercise = prod[3]
        return underlier,expiry,strike,excercise
    else:
        return "False"
    return underlier, expiry, strike, excercise

def calculatepremium(quantity,strike):
    strike = float(int(strike)/100)
    premium = float(quantity)*(strike)
    cutofff= premium-10
    return  premium,cutofff

def calculateexpiry(exp):
    months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'nov', 'oct', 'dec')
    cnt =len(exp)
    t = date.today()
    y =str(t.year)
    d=str(Generatedate())
    if cnt == 5 and re.match("[[0-9]{2}[A-Za-z]{3}", exp): #20dec
          for i in months:
              if i in exp:
                  m = str(monthnumber(i))
                  d = exp[0:2]
                  y = str(t.year)
                  list = [y, m, d]
                  s = "-"
                  expirydate = s.join(list)
                  return expirydate
                  return
    elif cnt == 3 and re.match("[A-Za-z]{3}",exp): #dec
          m = str(monthnumber(exp))
          d = str(Generatedate())
          y =str(t.year)
          list = [y, m, d]
          s = "-"
          expirydate = s.join(list)
          return expirydate
    elif cnt == 4 and re.match("[1-9]{1}[A-Za-z]{3}",exp):   #2dec
          for i in months:
              if i in exp:
                  print(i)
                  m = monthnumber(i)
                  y = str(t.year)
                  d = "0"+exp[0:1]
                  list = [y,m,d]
                  s = "-"
                  expirydate = s.join(list)
                  return expirydate
    elif cnt == 7 and re.match("[0-9]{2}[A-Za-z]{3}[0-9]{2}",exp): #20dec19
          for i in months:
              if i in exp:
                  m = monthnumber(i)
                  d = exp[0:2]
                  y = "20"+exp[5:]
                  list = [y, m, d]
                  s = "-"
                  expirydate = s.join(list)
                  return expirydate
    elif cnt == 6 and re.match("[1-9]{1}[A-Za-z]{3}[0-9]{2}",exp): #2dec19
          for i in months:
              if i in exp:
                  m = monthnumber(i)
                  d = "0"+exp[0:1]
                  y = exp[4:]
                  list = [y, m, d]
                  s = "-"
                  expirydate = s.join(list)
                  return expirydate
    elif cnt == 9 and re.match("[0-9]{2}[A-Za-z]{3}[0-9]{4}",exp): #20dec2019
         for i in months:
             if i in exp:
                 m = monthnumber(i)
                 d = exp[0:2]
                 y = exp[6:]
                 print(y)
                 list = [y, m, d]
                 s = "-"
                 expirydate = s.join(list)
                 return expirydate
    elif cnt == 8 and re.match("[1-9]{1}[A-Za-z]{3}[0-9]{4}",exp): #2dec2019
        for i in months:
            if i in exp:
                m = monthnumber(i)
                d = "0"+exp[0]
                y = exp[4:]
                list = [y, m, d]
                s = "-"
                expirydate = s.join(list)
                return expirydate

def Generatedate():
    date = random.randint(10, 31)
    return date

def monthnumber(exp):
    switcher = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12',
    }
    return switcher.get(exp,"invalid")



