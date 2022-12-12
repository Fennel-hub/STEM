import numpy as np
from PIL import Image

colour_im = np.array(Image.open('./robot-enstein.jpg'))
# Red reduced by 20%, blue enhanced by 15%
for i in range(len(colour_im[:, :, 0])):
    for j in range(len(colour_im[:, :, 0][i])):
        colour_im[:, :, 0][i][j] = colour_im[:, :, 0][i][j] * 0.8
# print(colour_im[:,:,0])
for i in range(len(colour_im[:, :, 2])):
    for j in range(len(colour_im[:, :, 2][i])):
        colour_im[:, :, 2][i][j] = colour_im[:, :, 2][i][j] * 1.15
new_img = Image.fromarray(colour_im)
new_img.save('./new_robot-enstein.jpg')