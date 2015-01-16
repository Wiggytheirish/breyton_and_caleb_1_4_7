import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'republic.jpg')

republic_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(republic_img, interpolation='none')

axes[1].imshow(republic_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400)
axes[1].set_ylim(1100, 850)
fig.show()

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'lightsaber.png')

lightsaber_img = PIL.Image.open(student_file)
fig2, axes = plt.subplots(1, 2)
axes[0].imshow(lightsaber_img, interpolation='none')

axes[1].imshow(lightsaber_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400)
axes[1].set_ylim(1100, 850)
fig2.show()

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'lightsaber_flipped.png')

lightsaber_flipped_img = PIL.Image.open(student_file)
fig3, axes = plt.subplots(1, 2)
axes[0].imshow(lightsaber_flipped_img, interpolation='none')

axes[1].imshow(lightsaber_flipped_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400)
axes[1].set_ylim(1100, 850)
fig3.show()


republic_img.paste(lightsaber_img, (17, 200), mask=lightsaber_img) 

fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(republic_img, interpolation='none')
axes3[1].imshow(republic_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.show()