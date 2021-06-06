"""
This scratch file is meant to tests different things I trying.

This goes from module activity to restructuredtext shit.
"""
from Chapter02.image_viewer import ImageViewer
from Chapter02.image_viewer import image_file_path

if __name__ == '__main__':
    viewer = ImageViewer()
    image = viewer.load_rgb_image(image_file_path)
