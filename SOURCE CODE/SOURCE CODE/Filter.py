








from scipy.interpolate import UnivariateSpline
import numpy as np
import cv2

class Filter:
    
    def __init__(self):
        self.increment_ch_lut = self._createTable([0, 64, 128, 192, 256],[0, 70, 140, 210, 256])
        self.decrement_ch_lut = self._createTable([0, 64, 128, 192, 256],[0, 30,  80, 120, 192])

    def createCartoon(self, image):
        
        c_r, c_g, c_b = cv2.split(image)
        c_r = cv2.LUT(c_r, self.increment_ch_lut).astype(np.uint8)
        c_b = cv2.LUT(c_b, self.decrement_ch_lut).astype(np.uint8)
        image = cv2.merge((c_r, c_g, c_b))

        c_h, c_s, c_v = cv2.split(cv2.cvtColor(image, cv2.COLOR_RGB2HSV))
        c_s = cv2.LUT(c_s, self.increment_ch_lut).astype(np.uint8)
        return cv2.cvtColor(cv2.merge((c_h, c_s, c_v)), cv2.COLOR_HSV2RGB)

    def _createTable(self, x, y):
        spline = UnivariateSpline(x, y)
        return spline(range(256))