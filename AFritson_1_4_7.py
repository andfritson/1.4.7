import PIL
import matplotlib.pyplot as plt
import os.path
import PIL.ImageDraw
import numpy as np

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'Earth1.JPG')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
fig,axes = plt.subplots(1,2)
axes[1].imshow(student_img, interpolation='none')
fig.show()

# Open, resize, and display earth

recycle_file = os.path.join(directory, 'Recycle Sign.png')
recycle_img = PIL.Image.open(recycle_file)
recycle_small = recycle_img.resize((600, 600)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(recycle_img)
axes2[1].imshow(recycle_small)
fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(recycle_small, (0, 100), mask=recycle_small) 
student_img.paste(recycle_small, (700, 940), mask=recycle_small) 
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.show()