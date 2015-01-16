import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'republic.jpg')
#this will pull out the republic image
republic_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(republic_img, interpolation='none')

axes[1].imshow(republic_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(0, 224)
axes[1].set_ylim(224, 0)
fig.show()
#this will get all of the republic image up and done
earth_file = os.path.join(directory, 'lightsaber.png')
lightsaber_img = PIL.Image.open(earth_file)
lightsaber_small = lightsaber_img.resize((200, 200)) 
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(lightsaber_img)
axes2[1].imshow(lightsaber_small)
fig2.show()
'''this here is done with both lightsabers. this will get the regular and 
flipped lightsaber into the program and will resize the image to fit onto
the republic image during the mask'''
earth_file = os.path.join(directory, 'lightsaber_flipped.png')
lightsaber_flipped_img = PIL.Image.open(earth_file)
lightsaber_flipped_small = lightsaber_flipped_img.resize((200, 200)) 
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(lightsaber_flipped_img)
axes3[1].imshow(lightsaber_flipped_small)
fig3.show()
#this will mask both lightsabers onto the image and keep it balanced up too
republic_img.paste(lightsaber_flipped_small, (15, 15), mask=lightsaber_flipped_small)
republic_img.paste(lightsaber_small, (15, 15), mask=lightsaber_small)  
fig4, axes4 = plt.subplots(1, 2)
axes4[0].imshow(republic_img, interpolation='none')
axes4[1].imshow(republic_img, interpolation='none')
axes4[1].set_xlim(0, 224)
axes4[1].set_ylim(224, 0)
fig4.show()
#this is how we got the lightsabers and our final product