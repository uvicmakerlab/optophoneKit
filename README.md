# Optophone Kit

Repository for the Optophone Kit, part of the Maker Lab's [Kits for Cultural History series](http://maker.uvic.ca/kch/). The optophone was a reading aid for the blind that converted text to sound in the 20th century, beginning in the 1910s and extending until at least the 1960s. To read more about the process of remaking the optophone, see our [blog posts](http://maker.uvic.ca/?s=optophone&search=) at [maker.uvic.ca](http://maker.uvic.ca/).

These files are part of research conducted by Tiffany Chan, Katherine Goertz, Danielle Morgan, Victoria Murawski, and Jentery Sayers. Thanks to Robert Baker (Blind Veterans UK), Mara Mills (New York University), and Matthew Rubery (Queen Mary University of London) for their support and feedback.

## Overview
* [Instructions](#instructions)
  * [Dependencies](#depends)
  * [Workflows](#workflows)
  * [Notes on Using the Scripts](#notes)
* [Change Log](#changeLog)
* [License](#license)

### <a name="instructions"></a>Instructions
These instructions detail the workflow and steps for converting an image into plaintext and then into a stream of optophonic sounds. Currently, the repo contains 3 scripts, written in the Python programming language. As the Kit develops, some of the scripts may change or be combined together (see the [change log](#changelog)).

1. [OCRscript.py](OCRscript.py) - takes an image from the PiCamera, runs it through OCR (Optical Character Recognition)
2. [toneGen.py](toneGen.py) - creates and saves optophonic sounds for later playback.
3. [optoscript.py](optoscript.py) - takes a string of characters as its input and plays the corresponding sounds.

#### <a name="depends"></a>Dependencies
To run these scripts, you will need to download and install Python. See the [Python website](https://www.python.org/) for instructions on how to do this. Note that the optophone project uses Python version 2.7. The scripts and dependencies should be able to work with Python 3, but there may be slight differences in the dependencies and scripts.

There are also several dependencies (Python modules or packages) that must be installed before the scripts can work. These include:

* [PiCamera](https://www.raspberrypi.org/documentation/usage/camera/python/README.md) - for taking a picture with the Raspberry Pi camera.
* [OpenCV](http://opencv.org/) - a computer vision and image processing program. This project uses version 3.0.0. See [installation instructions](http://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/).
* [Pillow/PIL](https://pillow.readthedocs.io/en/3.3.x/index.html) - Python Imaging Library, also for working with images.
* [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki) - a free OCR program.
* [pyTesser](https://code.google.com/archive/p/pytesser/) - a Python wrapper for Tesseract (basically, how Python talks to Tesseract).
* [pyGame](http://pygame.org/docs/) - for playing sounds with Python.

For the optophone project, these were all installed on a Raspberry Pi. Except for OCRscript.py, all the scripts should work on a laptop or personal computer. You can also modify OCRscript.py (see [OCRscript.py](OCRscript.py) for more) to take an arbitrary image as its input instead of an image from a Raspberry Pi camera.

####<a name="workflow"></a>Workflow

1. **Set up everything you need.** Set up all the hardware (the Raspberry Pi, PiCamera) and any other peripherals (e.g. monitor, mouse, keyboard) you might need. Download and install any dependencies. Download all the python scripts.

2. **Create and save tones for the optophone to play.** Currently, [optoscript.py](optoscript.py) only plays the tones for lowercase a,b, and c. You can download the sound files in the tones folder to use them for playback or modify and run [toneGen.py](toneGen.py) to generate different tones (note you will probably have to change the dictionary in optoscript.py to match). To make things easier, you can keep the tones in the same directory (folder) as your scripts. Otherwise, make sure the script can find the correct file path to your sound files.

3. **Take a picture of the print material and turn it into plaintext.** Position the camera to take a picture of the text. Ideally, you will want an image with bright lighting and where the text will take up as much of the image as possible (i.e. little to no background). This will make the image easier for the computer to read. [OCRscript.py](OCRscript.py) and Tesseract (the OCR program) will optimize the image as best as they can as well. Modify OCRscript.py as necessary (see [Notes](#notes) below) and run it. OCRscript.py will conver the image into a plaintext file named results.txt.

4. **Run optoscript.py** to read the results.txt file (make sure results.txt is in the same folder/directory as optoscript.py) and play the associated sounds.

#### <a name="notes"></a>Notes on Using the Scripts
The current scripts were made for testing small samples of code. To use them to express your own text as tones, you may have to modify it. For example, the dictionary of tones, as it is recorded in optopscript.py, only contains 3 entries for lowercase a,b, and c. You would have to change the dictionary to include the tones for other characters before you could play them.

Other places where code may be modified are noted in the scripts themselves.

## <a name="changeLog"></a>Change Log
This is version 1.0 of the repository. This version contains snippets of code, and a video and animated GIF demonstrating how the optophone may have scanned type.

##<a name="license"></a>License
This repository is licensed [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
