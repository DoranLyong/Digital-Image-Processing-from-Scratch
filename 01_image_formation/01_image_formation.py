"""
주어진 2차원 배열 정보를 화면으로 출력하기 
"""
#%% 
import turtle                                # 그래픽 처리를 위한 모듈; (ref) http://www.kmooc.kr/assets/courseware/v1/5b1357613179c66a4896e6712c186c4a/asset-v1:HGUk+HGU02+2018_T1+type@asset+block/6%EC%A3%BC%EC%B0%A8_01_turtle%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0.pdf
import numpy as np                           # 벡터, 행렬 데이터를 쉽게 처리하기 위한 모듈


# %%
# 도형을 나타내는 이미지 데이터 행렬
myImg = np.array([[0, 0, 0, 0, 0, 0, 0, 0],\
                  [0, 1, 1, 1, 0, 0, 0, 0],\
                  [1, 1, 1, 1, 1, 0, 0, 0],\
                  [1, 1, 1, 1, 1, 0, 0, 0],\
                  [0, 1, 1, 1, 0, 0, 0, 0],\
                  [0, 0, 0, 0, 0, 0, 0, 0],\
                  [0, 0, 0, 0, 0, 0, 0, 0],\
                  [0, 0, 0, 0, 0, 0, 0, 0]])


pixelSize = 30   # pixel 사이즈의 반지름

#%%
# (x,y) 위치에 pSize 크기의 픽셀을 pCol 색으로 그리는 함수
def putPixel(x, y, pSize, pCol):               # 메인 소스 코드에서 호출하는 픽셀 채우기 함수
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

    H, W = myImg.shape  # 이미지 패치의 기하학적 형태 정보를 얻는다 
    
    for j in range (0, H) :                        # 이미지의 행벡터(Xj)를 방문하기
        for i in range (0, W) :                    # Xj의 각 성분 Xji를 하나씩 방문하기

            if (myImg[j, i] > 0) :                 # 2차원 행렬 벡터 성분 Xji의 값을 확인하기
                putPixel(i,j,pixelSize, "blue")  # Xji > 0 인 경우 오렌지색 칠하기
            else:
                putPixel(i,j,pixelSize, "white")   # Xji <= 0 인 경우 흰색 칠하기


    """ 픽셀의 색상을 바꿔보면서 실험해보자: 
        - 적용 방법; (ref) https://docs.python.org/3/library/turtle.html#turtle.fillcolor
        - 컬러 Hex code ; (ref) https://spreadsheet.dev/how-to-get-the-hexadecimal-codes-of-colors-in-google-sheets
    """


