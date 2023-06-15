import math

# 이미지 크기 입력
n, m = map(int, input().split())

# Depth map 입력
depth_map = []
for _ in range(n):
    row = list(map(int, input().split()))
    depth_map.append(row)

# 두 점의 좌표 입력
x1, y1 = map(int, input().split()) 
x2, y2 = map(int, input().split())  

# 두 점의 깊이 차이 계산
depth1 = depth_map[y1][x1]  
depth2 = depth_map[y2][x2]  
depth_diff = depth2 - depth1  

# 이미지 상에서 두 점 사이의 거리 계산
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

result = math.sqrt(distance**2 + depth_diff**2)

