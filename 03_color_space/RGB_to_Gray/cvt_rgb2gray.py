# -*- coding:utf-8 -*-
"""
(ref) https://e2eml.school/convert_rgb_to_grayscale.html
(ref) https://stackoverflow.com/questions/48379205/how-to-manual-convert-bgr-image-to-grayscale-python-opencv
(ref) https://youngest-programming.tistory.com/232
"""


#%%
from PIL import Image  # PIL 이미지 로드 
import numpy as np  # 영상 배열을 다루기 위함 
import cv2


# %% 이미지 로드 
pil_img = Image.open("RGB_input.jpg")
pil_img.show(title="rgb_input")


# %% 전처리 
rgb_img = np.array(pil_img)  # <PIL> to <numpy> 
rgb_img = (1/255) * rgb_img  # normalization of uint8 image; [0, 255] -> [0, 1]
                             # (ref) https://stackoverflow.com/questions/1735025/how-to-normalize-a-numpy-array-to-within-a-certain-range



# %% 변환 
gray_img = np.empty_like( rgb_img[:,:,0] )  # 1-channel empty array    
H, W = rgb_img.shape[:2] 


for i in range(H): 
    for j in range(W):
        gray_pixel = 0.2126*rgb_img[i, j, 0] + 0.7152*rgb_img[i, j, 1] + 0.0722*rgb_img[i, j, 2]  # 픽셀별 회색톤으로 변환 
        gray_img[i, j] = gray_pixel  # RGB 채널 모두에 회색톤으로 지정 


gray_img = np.uint8( gray_img * 255 )   # denormalize an image; 
                                        # convert the range from [0, 1] to [0, 255]
                                        # (ref) https://stackoverflow.com/questions/30047612/how-to-denormalize-image-in-python


# %% 결과 출력 
pil_gray = Image.fromarray(gray_img)  # (ref) https://www.delftstack.com/ko/howto/matplotlib/convert-a-numpy-array-to-pil-image-python/
pil_gray.show(title="gray_output")
pil_gray.save("gray_output.jpg")




# ================================================================= #
#                      (추가). 다시 RGB로 바꾸기                      #
# ================================================================= #
# %% 
""" 역함수는 구하기 어렵다... 
    (ref) https://www.tutorialspoint.com/dip/grayscale_to_rgb_conversion.htm
    (ref) https://www.quora.com/How-do-I-convert-a-grayscale-image-to-an-RGB-image-in-Python
    (ref) https://www.quora.com/Why-cant-I-convert-a-gray-scale-image-to-an-RGB-image
    (ref) https://darkpgmr.tistory.com/66
    (ref) https://opencv-python.readthedocs.io/en/latest/doc/08.imageProcessing/imageProcessing.html
    (ref) https://kr.mathworks.com/matlabcentral/answers/67137-convert-gray-image-back-to-rgb
"""
rgb_again = np.empty((H, W, 3)) # 3-channel empty array 
gray_norm = (1/255) * gray_img


for i in range(H): 
    for j in range(W):
        red_pixel = 0.2* gray_norm[i, j]
        green_pixel = 0.5 * gray_norm[i, j]
        blue_pixel = 0.3 * gray_norm[i, j]

        rgb_again[i, j] = (red_pixel, green_pixel, blue_pixel)



rgb_again = np.uint8( rgb_again * 255 )


pil_rgb = Image.fromarray(rgb_again)
pil_rgb.show()  # 복원이 잘 안 되는 것을 확인 


# %%
rgb_test = cv2.imread("RGB_input.jpg")

test = cv2.cvtColor(rgb_test, cv2.COLOR_BGR2GRAY)  # OpenCV 함수를 사용하면, 
gray2rgb = cv2.cvtColor(test, cv2.COLOR_GRAY2BGR)  # 둘 사이의 color-map 변환 정보가 있기 떄문에 역변환이 가능함 
#cv2.imshow("test", gray2rgb)
#cv2.waitKey(0)


# %%
gry_test = cv2.imread("gray_output.jpg")
gray2rgb = cv2.cvtColor(gry_test , cv2.COLOR_GRAY2BGR)  # cvtColor 를 통해 변환하지 않은 grayscale image는 
                                                        # color-map 정보가 없기 때문에 변환 자체가 안 됨. (error 발생)

