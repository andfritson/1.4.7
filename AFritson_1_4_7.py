import PIL
import matplotlib.pyplot as plt
import os.path

#Open the files in the same directory as iPython
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'Earth1.JPG')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

