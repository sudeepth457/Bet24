
import random,math,re
from datetime import date
def GenerateOTP():
    otp = ""
    for i in range(5):
        otp += str((math.floor(random.random() * 10)))

    return otp

