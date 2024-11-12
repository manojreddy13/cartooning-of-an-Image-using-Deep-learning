










import cv2
import numpy as np

class CartoonImage:
    
    def __init__(self):
        pass

    def createCartoon(self, image):
        totalDownSamples = 4      # num steps to down scale
        totalBilateralFilters = 14  # steps for filtering using bilateral technique

        image_color = image

        for _ in range(totalDownSamples):
            image_color = cv2.pyrDown(image_color)

        for _ in range(totalBilateralFilters):
            image_color = cv2.bilateralFilter(image_color, d=9, sigmaColor=9, sigmaSpace=7)

        for _ in range(totalDownSamples):
            image_color = cv2.pyrUp(image_color)

        image_color = cv2.resize(image_color, image.shape[:2])

        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        image_blur = cv2.medianBlur(image_gray, 7)

        image_edge = cv2.adaptiveThreshold(image_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9,C=2)

        image_edge = cv2.cvtColor(image_edge, cv2.COLOR_GRAY2BGR)
        image_edge = cv2.resize(image_edge, image.shape[:2])
        image_cartoon = cv2.bitwise_and(image_color, image_edge)
        #image_cartoon = cv2.stylization(image_cartoon, sigma_s=60, sigma_r=0.07)
        return image_cartoon