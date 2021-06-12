import sys
from PIL import Image, ImageDraw

WRITABLES = [(0, 0, 7, 7), (24, 0, 39, 7), (56, 0, 63, 7)]

imagePath = "schoolgirlsweater_tanukirotate.png"
img = Image.open(imagePath)
draw = ImageDraw.Draw(img)

lengthPass = False
length = 0
while not lengthPass:
    msg = input("Enter the messaage to encode (768 characters max):\n")
    length = len(msg)
    if length > 768:
        print("Message is too long, please try again")
        
    else:
        lengthPass = True

ascii = [ord(c) for c in msg]

for i in range(768 - length):
    ascii = ascii +[0]

it = iter(ascii)
rgb = zip(it, it, it)

counter = 0
writeArea = 0
xy = [0, 0]
for z in rgb:
    draw.point(xy, fill = z)
    if xy[0] >= (WRITABLES[writeArea])[2]:
        xy[0] = (WRITABLES[writeArea])[0]
        xy[1] = xy[1] + 1
    else:
        xy[0] = xy[0] + 1
        
    if xy[1] > (WRITABLES[writeArea])[3] and writeArea + 1 < len(WRITABLES):
        writeArea = writeArea + 1
        xy[0] = (WRITABLES[writeArea])[0]
        xy[1] = (WRITABLES[writeArea])[1]

img.save(imagePath)
img = Image.open(imagePath).convert("RGB")
px = img.load()
counter = 0
writeArea = 0
xy = [0, 0]
decodedString = []

for i in range(256):
    #if (px[xy[0], xy[1]]) == (0, 0, 0):
        #break
    #else:
        decodedString.append(px[xy[0], xy[1]])
        if xy[0] >= (WRITABLES[writeArea])[2]:
            xy[0] = (WRITABLES[writeArea])[0]
            xy[1] = xy[1] + 1
        else:
            xy[0] = xy[0] + 1
            
        if xy[1] > (WRITABLES[writeArea])[3] and writeArea + 1 < len(WRITABLES):
            writeArea = writeArea + 1
            xy[0] = (WRITABLES[writeArea])[0]
            xy[1] = (WRITABLES[writeArea])[1]
        
decodedString = [i for sub in decodedString for i in sub]
decodedString = ''.join(chr(i) for i in decodedString)
print("Decoded String:")
print (decodedString)