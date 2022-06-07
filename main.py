import steganography as steg
import random
import os
steg.selfTest()
while True:

    mode = input('Decrypt, Encrypt, Or Remove:')

    if mode == 'E' or mode =='e':
        imageName = "slide.jpg"
        count = False
        while True:
            try:
                coverMessage = input('Hidden message?: ')
                bitUsed = input('Size(1-8): ')
                colorUsed = input('Color(R,G,B): ')
                image = steg.encode( imageName, coverMessage, colorUsed + bitUsed )
                coverImage = "DC.png"
                steg.write(coverImage,image)
                if count == True:
                    continue
                else:
                    imageName = "DC.png"
            except KeyboardInterrupt:
                print(" ")
                break
            break

    elif 'r' in mode:
        os.remove('DC.png')
        print('Image Removed')

    else:
        coverImage = input('Photo File Name: ')
        # decodeinst = input('C or G: ')
        colors ={
            "R",
            "G",
            "B"
        }
        try:
            for colorUsed in colors:
                for bitUsed in range(8):
                    bitUsed = bitUsed +1
                    # print(bitUsed, colorUsed)
                    message = steg.decode(coverImage, colorUsed + str(bitUsed) )
                    print(colorUsed + '  -> ', ' Bit Size:',bitUsed)
                    if message == "No message found":
                        continue
                    else:
                        print(message, colorUsed+ str(bitUsed))
        except KeyboardInterrupt:
            continue
        
        