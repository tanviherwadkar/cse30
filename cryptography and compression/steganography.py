# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil

from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    # Read OpenCV image file and return its representation as a binary string.
    def img2binstr(self, image):
      image_str = []

      for i in range(image.shape[0]):
        for j in range(image.shape[1]):
          for k in range(3):
            """
            image_pixel is the current 8-bit pixel's binary value formatted
            as a binary string i.e. string of eights 1s and 0s.

            format() uses the '08b' pattern to format its first parameter,
            i.e. image[i][j][k], as an 8-bit binary string
            """
            image_str.append(format(image[i][j][k], 'b'))

      return "".join(image_str)

    # Encode binary message inside an image
    def encode_image_with_binary(self, image, binary):
        # index of current bit in binary representation of "message"
        b = 0
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(3):
                    """
                    image_pixel is the current 8-bit pixel's binary value formatted
                    as a binary string i.e. string of eights 1s and 0s.

                    format() uses the '08b' pattern to format its first parameter,
                    i.e. image[i][j][k], as an 8-bit binary string
                    """
                    image_pixel = format(image[i][j][k], '08b')

                    # all bits in binary message are scanned, so return altered image
                    if b >= len(binary):
                        return image
                    
                    """
                    replace the least significant bit of image_pixel with
                    the current bit from the binary message.

                    character at index 0 represents most significant bit of image_pixel,
                    and the character at index 7 represents its least significant bit.
                    """
                    image_pixel = image_pixel[:7] + binary[b]

                    """
                    convert the altered binary string "image_pixel" to an integer
                    i.e. using base "2", and update the image with the altered integer value
                    """
                    image[i][j][k]= int(image_pixel, 2)

                    # go to next bit in binary message
                    b = b + 1

        return image

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        print(image) # for debugging
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        binary = self.codec.encode(message + self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary

            # your code goes here
            # you may create an additional method that modifies the image array

            # Encode binary message into image
            self.encode_image_with_binary(image, binary)

            cv2.imwrite(fileout, image)
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        print(image) # for debugging

        # Init flag
        flag = True
        
        # convert into text
        if codec == 'binary':
            self.codec = Codec() 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            # your code goes here
            # you may create an additional method that extract bits from the image array
            binary_data = self.img2binstr(image)
            # update the data attributes:
            self.text = self.codec.decode(binary_data)
            self.binary = self.codec.encode(self.text + self.delimiter)

    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

