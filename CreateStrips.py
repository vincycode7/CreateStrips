import numpy as np
import matplotlib.pyplot as plt

#code to generate stripes
class Vertical_Stripes(object):
    """
        class to generate vertical white and black strips.

        Parameter:
        =========
        stripes : indicates how many pixels on the x axis should represent one strip.
        height :  indicates the height of the image
        width : indicates the width of the image
        channels : indicates how many channels are there


        Returns
        =======
        returns a h*w*c numpy array

        Example:
        =======
        #initialize class
        strip_image = Vertical_Stripes(strips=2, image_width=50, image_height=50, channels=3)

        #convert to numpy array
        img = strip_image.to_numpy()

    """
    def __init__(self,stripes=5, image_width=10, image_height=10):
        self.stripes = stripes
        self.height = image_height
        self.width = image_width
        self.image = np.zeros((image_height, image_width, 3))

        #generate strips
        self.generate_stripes()

    def generate_stripes(self):
        """
            method to generate the stripes
        """
        for start in range(0,self.width,self.stripes*2):
            self.image[:,start:start+self.stripes,:] = 1

    def to_numpy(self):
        """
            method to convert stripes to numpy array
        """
        return self.image

if __name__ == "__main__":
    strip_image = Vertical_Stripes(stripes=10, image_width=50, image_height=50)
    plt.imshow(strip_image.to_numpy())