'''
Script for processing an image, running it through OCR 
(Optical Character Recognition), and then writing the results
to a .txt file. Uses OpenCV, PIL, Tesseract, PyTesser.

Part of the Optophone Kit and the Kits for Cultural History 
series by the MLab at the University of Victoria (maker.uvic.ca).

Link to the Optophone Kit repository: github.com/uvicmakerlab/optophoneKit

'''

#Import libraries
import cv2
from PIL import Image
from pytesser import *

'''
To make the image easier for Tesseract to read, convert the image to
grayscale and then use threshold to make the image black and white,
increasing the contrast between text and background.

'''

#Convert image to grayscale
img = cv2.imread("imagetoOCR.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayscale.jpg", gray)

#Blur and threshold. Threshold turns the image B&W, increasing the
#contrast between words and background to make words easier to read.
gray = cv2.imread("grayscale.jpg", 0)
blur = cv2.GaussianBlur(gray,(5,5).0)
thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
	cv2.THRESH_BINARY,11,2)
cv2.imwrite("threshold.jpg", thresh)

#Finally we get to the OCR
img = Image.open("threshold.jpg")
words = image_to_string(img).strip()

#Write the results to a .txt file
f = open("results.txt", "w")
f.write(words)
f.close()