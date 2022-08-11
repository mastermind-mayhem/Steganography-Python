import steganography as steg
import random
import os, time
from collections import OrderedDict


def encrypt1(text):
    full = ""
    alg = {
        "z": "a",
        "y": "b",
        "x": "c",
        "w": "d",
        "v": "e",
        "u": "f",
        "t": "g",
        "s": "h",
        "r": "i",
        "q": "j",
        "p": "k",
        "o": "l",
        "n": "m",
        "m": "n",
        "l": "o",
        "k": "p",
        "j": "q",
        "i": "r",
        "h": "s",
        "g": "t",
        "f": "u",
        "e": "v",
        "d": "w",
        "c": "x",
        "b": "y",
        "a": "z",
        " ": " ",
        "?": "?",
        "!": "!",
        ",": ",",
    }
    for decode in text:
        #respond(alg[decode])
        if decode not in alg:
            full += decode
        else:
            full += alg[decode]
    return full



def betaencrypt():
    imageName = "slide.jpg"
    coverMessage = input('Hidden message?: ')
    coverMessage = coverMessage.split()
    if len(coverMessage) >= 25:
        print('message is too long')
    else:
        num = 0
        bits = [1,2,3,4,5,6,7,8]
        colors = ['R','G','B']
        for mess in coverMessage:
            coverMessage[num]= str(num)+' '+mess
            num = num + 1
        for cover in coverMessage:
            colorUsed = random.choice(colors)
            bitUsed = str(random.choice(bits))
            print(colorUsed, bitUsed, cover)
            image = steg.encode(imageName, encrypt1(cover), colorUsed + bitUsed )
            coverImage = "DC.png"
            steg.write(coverImage,image)
            imageName = "DC.png"
    
def betadecrypt():
    coverImage = 'DC.png'
    # decodeinst = input('C or G: ')
    colors ={
        "R",
        "G",
        "B"
    }
    messdict= {}
    message = ''
    num = 0
    for colorUsed in colors:
        for bitUsed in range(8):
            bitUsed = bitUsed +1
            # print(bitUsed, colorUsed)
            num += 1
            base = num / 24
            base = base * 100
            # print(num)
            print(str(int(base))+'%', end="\r")
            message = steg.decode(coverImage, colorUsed + str(bitUsed) )
        
            if message == "No message found":
                continue
            else:
                message = message.split()
                messdict[str(int(message[0])+1)] = encrypt1(message[1])
                # print(messdict)
            
            
    compmessage = ''
    num = 1
    for mess in messdict:
        x = messdict[str(num)]
        num = num +1
        compmessage += x
        compmessage += " "
    print("Message: "+compmessage)


steg.selfTest()
while True:

    mode = input('Decrypt, Encrypt, Or Remove:')

    if mode == 'E' or mode =='e':
        betaencrypt()
            # break

    elif 'r' in mode:
        os.remove('DC.png')
        print('Image Removed')

    else:
       
        try:
            betadecrypt()
        except KeyboardInterrupt:
            continue
        
        