# Object Filtering OpenCV

## Description
This is a small utility script that allows you to pre-process your positive and negative images to finally train them into Haar Cascades. As of now, only pre-processing is available.  
I shall set up a shell script to work with the files and develop the cascade as well in the future, but for now, this is where it remains.  
## How to use
This project requires you to have Python and OpenCV on your computer to work. Once verified, run `objectdemarcation.py`. This will open a window where you need to make a selection.  
You need to demarcate the RoI using which you can crop the image to focus on your selected image feature.
The images with their selected RoIs will all be recorded and stored in a .txt file which you can use.
