"""
The :module:`Chapter02.image_reader` will contain the class I'll need to read images using OpenCV 4.
"""
import cv2

image_file_path = 'Chapter02\02-exercices\logo.png'
"""
str: The relative path to the image file I want to load.
"""


def display_image(image, color_flag=cv2.COLOR_BGR2RGB, title=None):
    """
    display_image A function to display an image loaded in with OpenCV.

    This function will display an image until I press a button on the keyboard.

    Args:
        image (ndarray): The image (read by OpenCV) I want to display.
        color_flag (int): The colorspace I want to load the image with. By default, the image will be loaded into a RGB colorspace.
        title (str, optional): The title I want the display window to use.
    """
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image = cv2.imread(image_file_path)
    display_image(image)
