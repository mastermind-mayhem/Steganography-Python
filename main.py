import steganography as steg
import random
import os, time

etxt = """
Your message has been encrypted and made into "DC.png", feel free to download and send to your friends 
"""
dtxt = """
Make sure you have uploaded the DC.png to this binder and it is accesible
"""
def cipher(text, KEY):
  encrypted = ""
  for ch in text:
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
      newCode = ord(ch) + KEY
      if (newCode > ord('z')):
        newCode -= 26
      encrypted += chr(newCode)
    if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
      newCode = ord(ch) + KEY
      if (newCode > ord('Z')):
        newCode -= 26
      encrypted += chr(newCode)
  return encrypted


def decipher(text, KEY):
  decrypted = ""
  for ch in text:
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
      newCode = ord(ch) - KEY
      if (newCode < ord('a')):
        newCode += 26
      decrypted += chr(newCode)
    if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
      newCode = ord(ch) - KEY
      if (newCode < ord('A')):
        newCode += 26
      decrypted += chr(newCode)
  return decrypted

def betaencrypt():
    imageName = "slide.jpg"
    KEY = int(input('Key: '))
    coverMessage = input('Hidden message?: ')
    coverMessage = coverMessage.split()
    if len(coverMessage) >= 25:
        print('message is too long')
    else:
        bit = [' ']
        num = 0
        bits = [1,2,3,4,5,6,7,8]
        colors = ['R','G','B']
        for mess in coverMessage:
            coverMessage[num]= str(num)+' '+cipher(mess, KEY)
            num = num + 1
        for cover in coverMessage:
            while True:
                colorUsed = random.choice(colors)
                bitUsed = str(random.choice(bits))
                inp = colorUsed + bitUsed 
                # inp = input("hbhfv: ") 
                new = True
                for entry in bit:
                    # print(entry, inp)
                    if entry == inp:
                        # print('duplicate')
                        new = False
                    else:
                        continue
                if new == True:
                    # print('add')
                    bit.append(str(inp))
                    print(colorUsed + bitUsed, decipher(cover, KEY))
                    image = steg.encode(imageName, cover, colorUsed + bitUsed )
                    coverImage = "DC.png"
                    steg.write(coverImage,image)
                    imageName = "DC.png"
                    break
        print('Loading...', end="\r")
        time.sleep(5)
        print('                      ')
        print(etxt)
            # time.sleep(5)
    
def betadecrypt():
    print(dtxt)
    KEY = int(input('Key: '))
    coverImage = 'DC.png'
    # decodeinst = input('C or G: ')
    colors ={
        "R",
        "G",
        "B"
    }
    messdict= {}
    num = 0
    for colorUsed in colors:
        for bitUsed in range(8):
            bitUsed = bitUsed +1
            # print(bitUsed, colorUsed)
            num += 1
            base = num / 24
            base = base * 100
            # print(num)
            print("--- "+str(int(base))+'%', end="\r")
            message = steg.decode(coverImage, colorUsed + str(bitUsed) )
        
            if message == "No message found":
                continue
            else:
                message = message.split()
                # print(message)
                # print(decipher(message[1], KEY))
                # print(str(int(message[0])+1))
                messdict[str(int(message[0])+1)] = decipher(message[1], KEY)
                # print(messdict)      
    compmessage = ''
    num = 1
    for mess in messdict:
        x = messdict[str(num)]
        num = num +1
        compmessage += x
        compmessage += " "
    print("Message: "+compmessage)

# def decrypt():
#     coverImage = input('Photo File Name: ')
#     KEY = int(input('Key: '))
#     # decodeinst = input('C or G: ')
#     colors ={"R","G","B"}
#     for colorUsed in colors:
#                 for bitUsed in range(8):
#                     bitUsed = bitUsed +1
#                     # print(bitUsed, colorUsed)
#                     message = steg.decode(coverImage, colorUsed + str(bitUsed) )
#                     print(colorUsed + '  -> ', ' Bit Size:',bitUsed)
#                     if message == "No message found":
#                         continue
#                     else:
#                         print(decipher(message, KEY), message, colorUsed+ str(bitUsed))

steg.selfTest()
while True:
    mode = input('Decrypt, Encrypt, Or Remove:')
    mode = mode.lower()
    if mode == 'encrypt' or mode == 'e':
        betaencrypt()
    elif 'remove' == mode or mode == 'r':
        try:
            os.remove('DC.png')
            print('Image Removed')
        except FileNotFoundError:
            print('No file found')
    elif mode == 'decrypt' or mode == 'd':
        try: 
            betadecrypt()
        except KeyboardInterrupt:
            continue
    else:
      print('invalid input, please spell as provided')