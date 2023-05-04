import random, requests
from string import ascii_letters, digits
import base64, itertools
import hashlib
import base64

possible_letters = ascii_letters + digits
def base64_encode(string: str) -> str:
    return base64.urlsafe_b64encode(string.encode()).decode()
def base64_decode(string: str) -> str:
    return base64.urlsafe_b64decode(string.encode()).decode()
def generate_rs(n: int) -> str:
    return ("").join(random.choices(possible_letters, k=n))
def generate_uuid(parts: [int] = (8, 4, 4, 4, 10)) -> str:
    return ("-").join(map(generate_rs, parts))
def xor_cipher(string: str, key: str) -> str:
    result = ""
    for string_char, key_char in zip(string, itertools.cycle(key)):
        result += chr(ord(string_char) ^ ord(key_char))
    return result
def generate_chk(values: [int, str] = [], key: str = "", salt: str = "") -> str:
    values.append(salt)
    string = ("").join(map(str, values))
    hashed = hashlib.sha1(string.encode()).hexdigest()
    xored = xor_cipher(hashed, key)
    final = base64.urlsafe_b64encode(xored.encode()).decode()
    return final

dbURL = input("GDPS Database URL: ")
userPrefix = input("Username Prefix (example user: Sevenworks = Sevenworks2947205): ")
passw = input("Password for Accounts: ")

while True:
  haha = ''.join(random.choices(ascii_letters, k=8))
  usern = userPrefix+haha
  with open("accounts.txt", "a") as f:
    print("User: "+usern, file=f)
    print("Pass: "+passw, file=f)
    print("--------------------", file=f)

  data = {
      "userName": usern,
      "password": passw,
      "email": "eminem@rapgod.walmart",
      "secret": "Wmfv3899gc9"
  }

  req = requests.post(dbURL+"/accounts/registerGJAccount.php", data=data)
  print("Response (Register): " + req.text)

#  Activation and Stat Hacking is not working for whatever reason.
#  Fixing this later...

  data2 = {
      "udid": generate_uuid(),
      "userName": usern,
      "password": passw,
      "secret": "Wmfv3899gc9"
  }

  req2 = requests.post(dbURL+"/accounts/loginGJAccount.php", data=data2)
  print("Response (Login): " + req2.text)
#  accid = req2.text.split(",")[0]
#
#  data3 = {
#      "accountID": accid,
#      "gjp": base64_encode(xor_cipher(str(passw), "37526")), # This would be PasswordFinders' password encoded with GJP encryption
#      "userName": us,
#      "stars": 696969,
#      "demons": 69,
#      "diamonds": 420420,
#      "icon": 0,
#      "color1": 1,
#      "color2": 1,
#      "iconType": 0,
#      "coins": 69,
#      "userCoins": 420,
#      "special": 2,
#      "accIcon": 0,
#      "accShip": 0,
#      "accBall": 0,
#      "accBird": 0,
#      "accDart": 0,
#      "accRobot": 0,
#      "accGlow": 0,
#      "accSpider": 0,
#      "accExplosion": 1,
#      "secret": "Wmfd2893gb7",
#      "seed": ''.join(random.sample("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM", 10))
#  }
#  data3['seed2'] = generate_chk([data3['accountID'], data3['userCoins'], data3['demons'], data3['stars'], data3['coins'], data3['iconType'], data3['icon'], data3['diamonds'], data3['accIcon'], data3['accShip'], data3['accBall'], data3['accBird'], data3['accDart'], data3['accRobot'], data3['accGlow'], data3['accSpider'], data3['accExplosion']], "85271", "xI35fsAapCRg")
#
#  req3 = requests.post(dbURL+'/updateGJUserScore22.php', data=data3)
#  print("Response (Stats Hack): " + req3.text)
