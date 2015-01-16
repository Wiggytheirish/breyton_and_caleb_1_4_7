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
axes[1].set_xlim(0, 224)
axes[1].set_ylim(224, 0)
fig.show()

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'lightsaber.png')

lightsaber_img = PIL.Image.open(student_file)
fig2, axes2 = plt.subplots(1, 2)
axes[0].imshow(lightsaber_img, interpolation='none')

axes[2].imshow(lightsaber_img, interpolation='none')
axes[2].set_xticks(range(1050, 1410, 100))
axes[2].set_xlim(0, 2000)
axes[2].set_ylim(1350, 0)
fig2.show()

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'lightsaber_flipped.png')

lightsaber_flipped_img = PIL.Image.open(student_file)
fig3, axes3 = plt.subplots(1, 2)
axes[0].imshow(lightsaber_flipped_img, interpolation='none')

axes[3].imshow(lightsaber_flipped_img, interpolation='none')
axes[3].set_xticks(range(1050, 1410, 100))
axes[3].set_xlim(0, 2000)
axes[3].set_ylim(1350, 0)
fig3.show()


republic_img.paste(lightsaber_img, (244, 244), mask=lightsaber_img) 

fig4, axes4 = plt.subplots(1, 2)
axes3[0].imshow(republic_img, interpolation='none')
axes3[4].imshow(republic_img, interpolation='none')
axes3[4].set_xlim(0, 224)
axes3[4].set_ylim(224, 0)
fig4.show()