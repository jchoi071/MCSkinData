# MCSkinData

A simple Python 3 program that writes and/or reads text data as RGB triplets to the unused portions of a Minecraft skin.

There are two files; MCSkinDataWriteRead.py and MCSkinDataRead.py. The first program writes the data, then reads it and outputs it to the console for verification. The second program only reads the data. The text encoding used is ASCII; every 8-bit ASCII character is encoded as one number of an RGB triplet. The choice of RGB triplets specifically was to allow someone with only a basic image editor such as Microsoft Paint to manually decode the data simply by using the color picker and reading the RGB values.

The program uses the Pillow image library, specifically version 6.1.0. 

TODO:
Implement better file opening method - pass filename via command line
Implement error detection by using the alpha channel as a parity byte
Implement Unicode encoding (probably will not be done)
