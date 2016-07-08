# Optophone Kit

Repository for the Optophone Kit, part of the Maker Lab's [Kits for Cultural History series](http://maker.uvic.ca/kch/). To read more about the process of remaking the optophone, see our [blog posts](http://maker.uvic.ca/?s=optophone&search=) at [maker.uvic.ca](http://maker.uvic.ca/).

These files are part of research conducted by Tiffany Chan, Katherine Goertz, Danielle Morgan, Victoria Murawski, and Jentery Sayers. Thanks to Robert Baker (Blind Veterans UK), Mara Mills (New York University), and Matthew Rubery (Queen Mary University of London) for their support and feedback.

## Overview
* [Instructions](#instructions)
  * [Dependencies](#depends)
  * [Workflow](#workflow)
  * [Notes on Using the Scripts](#notes)
* [Change Log](#changeLog)
* [License](#license)

## <a name="instructions"></a>Instructions
These instructions detail the workflow and steps for converting an image into plaintext and then into a stream of optophonic sounds. Currently, the repo contains 3 scripts, written in the Python programming language. As the Kit develops, some of the scripts may change or be combined together (see the [change log](#changelog)).

1. [OCRscript.py](OCRscript.py) - takes an image from the PiCamera, runs it through OCR (Optical Character Recognition)
2. [toneGen.py](toneGen.py) - creates and saves optophonic sounds for later playback.
3. [optoscript.py](optoscript.py) - takes a string of characters as its input and plays the corresponding sounds.

#### <a name="depends"></a>Dependencies
There are several dependencies (Python modules or packages) that must be installed before the scripts can work. These include:

* [PiCamera](https://www.raspberrypi.org/documentation/usage/camera/python/README.md) - for taking a picture with the Raspberry Pi camera.
* [OpenCV](http://opencv.org/) - a computer vision and image processing program. This project uses version 3.0.0. See [installation instructions](http://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/).
* [Pillow/PIL](https://pillow.readthedocs.io/en/3.3.x/index.html) - Python Imaging Library, also for working with images.
* [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki) - a free OCR program.
* [pyTesser](https://code.google.com/archive/p/pytesser/) - a Python wrapper for Tesseract (basically, how Python talks to Tesseract).
* [pyGame](http://pygame.org/docs/) - for playing sounds with Python.

For the optophone project, these were all installed on a Raspberry Pi (but the scripts should also work on your laptop). See the [Python website](https://www.python.org/) for more on how to download and install Python. Note that the optophone project uses Python version 2.7.

####<a name="workflow"></a>Workflow
1. Set up all the hardware (the Raspberry Pi, PiCamera) and any other peripherals (e.g. monitor, mouse, keyboard) you might need. Download and install any dependencies.

2. Modify [OCRscript.py](OCRscript.py) as necessary (see [Notes](#notes) below) and run it. The result should be the text of your image in a plaintext file named results.txt.

4. [optoscript.py](optoscript.py) reads the results.txt file (make sure results.txt is in the same folder/directory as optoscript.py) and matches them to a dictionary of sounds. These sounds are available to download in the tones folder. You may have to modify the script (see [Notes](#notes) for more details).

5. Run optopscript.py to play the sounds.

#### <a name="notes"></a>Notes on Using the Scripts
The current scripts were made for testing small samples of code. To use them to express your own text as tones, you may have to modify it. For example, the dictionary of tones, as it is recorded in optopscript.py, only contains 3 entries for lowercase a,b, and c. You would have to change the dictionary to include the tones for other characters before you could play them.

Other places where code may or should be modified (e.g. file names) are noted in the scripts themselves.

## <a name="changeLog"></a>Change Log
This is version 1.1 of the repository. This version contains snippets of code, and a video and animated GIF demonstrating how the optophone may have scanned type.

##<a name="license"></a>License
This repository is licensed [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
