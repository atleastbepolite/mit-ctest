import cv2
import numpy as np

def detect_straw_angle(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)
    img_original = image.copy()
    
    # 이미지 전처리
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    # 빨대 선 검출
    lines = cv2.HoughLines(edges,1,np.pi/180,80)

    for i in range(len(lines)):
        for rho, theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0+1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 -1000*(a))

            cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)

    if lines is not None:
        # 빨대 각도 계산
        total_angle = 0
        num_lines = len(lines)

        for line in lines:
            rho, theta = line[0]
            angle = np.rad2deg(theta)  
            total_angle += angle

        straw_angle = total_angle / num_lines
        straw_angle += 90

        print("빨대의 굽은 각도: {:.2f}도".format(straw_angle))


image_path = "input_image2.jpg"
detect_straw_angle(image_path)