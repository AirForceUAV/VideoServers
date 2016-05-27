from time import time,sleep
import VideoServers


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    def __init__(self):
        VideoServers.ClientNum += 1
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        #if VideoServers.ImagesQueue.empty() == False:
        image = VideoServers.ImagesQueue.get() 
        sleep(.01)
        return image
        return self.frames[int(time()) % 3]

    def __del__(self):
        VideoServers.ClientNum -= 1
