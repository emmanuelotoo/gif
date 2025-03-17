
# importing the imageio module
import imageio.v3 as iio

# storing the image data from  filenames
filenames = ['dino1.png', 'dino2.png', 'dino3.png']
images = []

# reading the images in the file paths
for filename in filenames:
    images.append(iio.imread(filename))

# turning the image into a gif
iio.imwrite('team.gif', images, duration=500, loop=0)





