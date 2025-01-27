"""
The :module:`Chapter02.image_reader` module will contain the class I'll need to read images using OpenCV 4.
"""
import cv2

image_file_path = 'logo.png'
"""
str: The path to the rgb_image I want to display.
"""


class ImageViewer:
    """
    The :class:`ImageViewer` class allows one to view images using an OpenCV 4 window.
    """

    def __init__(self):
        """
        Create a new instance of :class:`ImageViewer`.
        """
        self._cv2 = cv2
        self._image_path = ''

    @property
    def cv2(self):
        """
        cv2: The OpenCV 4 module.
        """
        return self._cv2

    @property
    def image_path(self):
        """
        str: The file path to the rgb_image I loaded in.
        """
        return self._image_path

    @image_path.setter
    def image_path(self, file_path):
        self._image_path = file_path

    def load_rgb_image(self, file_path):
        """
        :method:`load_rgb_image` Load an rgb_image with OpenCV4 into RGB color space.

        Parameters
        ----------
        file_path: str
            The path to the rgb_image I want to load.

        Returns
        -------
        rgb_image: numpy.ndarray
            The OpenCV4 rgb_image I want.
        """
        self.image_path = file_path
        color_flag = self.cv2.COLOR_BGR2RGB
        rgb_image = self.cv2.imread(self.image_path, color_flag)
        return rgb_image

    def show(self, rgb_image, image_title = None):
        """
        Show the image I loaded in, and continue to display it until a key is pressed.

        Parameters
        ----------
        rgb_image: numpy.ndarray
            The image I want to display.
        image_title: str, optional
            The title for the window that will display my image.
        """
        self.cv2.imshow(image_title, rgb_image)
        self.cv2.waitKey(0)
        self.cv2.destroyAllWindows()


if __name__ == '__main__':
    viewer = ImageViewer()
    image = viewer.load_rgb_image(image_file_path)
    viewer.show(image)
    print(type(cv2))
