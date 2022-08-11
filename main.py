import steganography as steg
import random
import os, time


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
        bit = [' ']
        num = 0
        bits = [1,2,3,4,5,6,7,8]
        colors = ['R','G','B']
        for mess in coverMessage:
            coverMessage[num]= str(num)+' '+mess
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
                    print(colorUsed + bitUsed, cover)
                    image = steg.encode(imageName, encrypt1(cover), colorUsed + bitUsed )
                    coverImage = "DC.png"
                    steg.write(coverImage,image)
                    imageName = "DC.png"
                    break
            # time.sleep(5)
    
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
            print("--- "+str(int(base))+'%', end="\r")
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

def decrypt():
    coverImage = input('Photo File Name: ')
    # decodeinst = input('C or G: ')
    colors ={
        "R",
        "G",
        "B"
    }
    for colorUsed in colors:
                for bitUsed in range(8):
                    bitUsed = bitUsed +1
                    # print(bitUsed, colorUsed)
                    message = steg.decode(coverImage, colorUsed + str(bitUsed) )
                    print(colorUsed + '  -> ', ' Bit Size:',bitUsed)
                    if message == "No message found":
                        continue
                    else:
                        print(encrypt1(message), message, colorUsed+ str(bitUsed))

steg.selfTest()
while True:
    mode = input('Decrypt, Encrypt, Or Remove:')
    if mode == 'E' or mode =='e':
        betaencrypt()
    elif 'r' in mode:
        try:
            os.remove('DC.png')
            print('Image Removed')
        except FileNotFoundError:
            print('No file found')
    else:
        try:
            betadecrypt()
        except KeyboardInterrupt:
            continue
        
        