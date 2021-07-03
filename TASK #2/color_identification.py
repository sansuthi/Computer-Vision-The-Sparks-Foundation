####################################################################
#                                                                  #
#  TASK#2: COLOR IDENTIFICATION IN IMAGES                          #
#                                                                  #
#  Author: SANDHYA S                                               #
#                                                                  #
#  Problem Statement: Implement an Image Color Detector which      #
#                     identifies all the colors in an image/Video  #
#                                                                  #
####################################################################

import pandas as pd
import cv2

colors = pd.read_csv('colors.csv')
image = cv2.imread('colors.jpg')

clicked = False
r = g = b = xpos = ypos = 0

def spot_color(event, x, y, flags, params):
    if event == cv2.EVENT_MOUSEMOVE:
        global clicked, r, g, b, xpos, ypos
        clicked = True
        xpos = x
        ypos = y
        b, g, r = image[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        
def color_names(R, G, B):
    minimum = 1000
    for i in range(len(colors)):
        difference = abs(R - int(colors.loc[i, 'R']))
        + abs(G - int(colors.loc[i, 'G']))
        + abs(B - int(colors.loc[i, 'B']))
        if difference <= minimum:
            minimum = difference
            colorname = colors.loc[i, 'ColorName']        
    return colorname
        
cv2.namedWindow('Color Identification')
cv2.setMouseCallback('Color Identification', spot_color)
 
while True:
    cv2.imshow('Color Identification', image)
    if clicked:
        cv2.rectangle(image, (0,20), (800,60), (b,g,r), -1)
        text = color_names(r,g,b)+ ' - Red:' + str(r) + ' Green:'+ str(g) + ' Blue:' + str(b)
        cv2.putText(image, text, (50,50), 2, 0.9, (255,255,255), 2, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(image, text, (50,50), 2, 0.9, (0,0,0), 2, cv2.LINE_AA)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()



# Thank You!