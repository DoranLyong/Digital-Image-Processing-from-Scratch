"""
이미지 산술 연산 맛보기  
- 행렬의 합과 차에 대해 함께 생각해 보자 
"""
#%% 
import turtle                                # 그래픽 처리를 위한 모듈; (ref) http://www.kmooc.kr/assets/courseware/v1/5b1357613179c66a4896e6712c186c4a/asset-v1:HGUk+HGU02+2018_T1+type@asset+block/6%EC%A3%BC%EC%B0%A8_01_turtle%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0.pdf
import numpy as np                           # 벡터, 행렬 데이터를 쉽게 처리하기 위한 모듈


# %%
# 도형을 나타내는 이미지 데이터 행렬
faceImg = np.array(                                      # 얼굴 그림 
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

smileImg = np.array(                                     # 표정 그림 
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


pixelSize = 10   # pixel 사이즈의 반지름

#%%
# (x,y) 위치에 pSize 크기의 픽셀을 pCol 색으로 그리는 함수
def putPixel(x, y, pSize, pCol):               # 메인 소스 코드에서 호출하는 픽셀 채우기 함수
    turtle.speed(0)                            # 그리는 속도 조절; (ref) https://www.geeksforgeeks.org/turtle-speed-function-in-python/
    turtle.penup()                             # 좌표 이동을 위해 펜기능을 비활성화   
    turtle.goto(x*pSize,(-1)*y*pSize)          # 주어진 좌표로 이동
    turtle.pendown()                           # 펜기능을 다시 활성화
    turtle.begin_fill()                        # 다각형을 그릴 때 내부를 채우기
    turtle.fillcolor(pCol)                     # 다각형의 채움색 설정하기
    turtle.setheading(45)                      # 시작 각도를 45도로 지정
    turtle.circle(pSize/2, steps = 4)          # 정사각형 픽셀 도출하기
    turtle.end_fill()                          # 채우기 끝


#%%
if __name__ == "__main__":

   
    """ faceImage 이미지 그려보기 
    """
    Hf, Wf = faceImg.shape  # 이미지 패치의 기하학적 형태 정보를 얻는다 

    for j in range (0, Hf) :                                 # (a) faceImage 이미지 출력
        for i in range (0, Wf) :
            if (faceImg[j, i] > 0):
                putPixel( i,j, pixelSize, "orange")           # 각 배열 요소의 값이 0보다 크면 오렌지색으로 출력
            else:
                putPixel( i,j, pixelSize, "white")            # 각 배열 요소의 값이 0이면 흰색으로 출력


    """ smileImage 그려보기 
    """
    Hs, Ws = smileImg.shape  # 이미지 패치의 기하학적 형태 정보를 얻는다 

    for j in range (0, Hs) :                                 
        for i in range (0, Ws) :
            if (smileImg[j, i] > 0):
                putPixel(i+20, j, pixelSize, "red")           # 각 배열 요소의 값이 1보다 크면 빨간색으로 출력
                                                              # faceImage 에서 오른쪽으로 +20 오프셋 된 위치에 그린다 
            else:
                putPixel(i+20, j, pixelSize, "white")         # 각 배열 요소의 값이 1보다 작으면 흰색으로 출력


    """ 행렬의 합을 이용해서 두 이미지를 결합하기
    """
    addImage = np.array(faceImg + smileImg)              # (이미지 산술연산) 두 이미지의 요소간 합 
    print(addImage)                                      # addImg의 성분 출력하기

    Ha, Wa = addImage.shape 

    for j in range (0, Ha) : 
        for i in range (0, Wa) :
            if (addImage[j, i] > 1) :                     # addImage 행렬의 성분값이 2 이상이면 빨간색으로 출력하기
                putPixel(i+40,j,pixelSize, "red")         # # faceImage 에서 오른쪽으로 +40 오프셋 된 위치에 그린다 

            elif (addImage[j, i] > 0) :                   # addImage 행렬의 성분값이 1이면 오렌지색으로 출력하기
                putPixel(i+40,j,pixelSize, "orange")        
                
            else :                                        # ddImage 행렬의 성분값이 0 이하이면 흰색으로 출력하기
                putPixel(i+40,j,pixelSize, "white")         



    """ (숙제) 행렬의 차을 이용해서 두 이미지의 차이 표현하기 
    """
    diffImage = np.array(faceImg - smileImg)   # (이미지 산술연산) 두 이미지의 요소간 차이
    print(diffImage)   
