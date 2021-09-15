import sys
input = sys.stdin.readline

num_of_house = int(input())
RGB_house = []

for _ in range(num_of_house):
  RGB_house.append(list(map(int, input().split())))


for i in range(1,num_of_house):
  RGB_house[i][0] = min(RGB_house[i-1][1], RGB_house[i-1][2]) + RGB_house[i][0]
  RGB_house[i][1] = min(RGB_house[i-1][0], RGB_house[i-1][2]) + RGB_house[i][1]
  RGB_house[i][2] = min(RGB_house[i-1][0], RGB_house[i-1][1]) + RGB_house[i][2]
print(min(RGB_house[num_of_house-1]))