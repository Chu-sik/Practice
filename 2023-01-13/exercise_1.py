# exercise_1
# 다음 출력 결과와 같이 반지름에 따른 원의 면적을 계산하여 출력하세요.
#
# 정렬 및 숫자 형식 변경에 foramt() 함수를 사용
# PI 값으로는 3.141592 를 이용하세요
# 출력이 이상하다면 Shell의 글꼴을 Consoias로 바꿔보세요 (Options-COnfigure IDLE)

print(format('R', "^5"), '|', format('AREA', "^10"), sep='')
print(format('1', ">5"), '|', format(1 ** 2 * 3.141592, ">10.1f"), sep='')
print(format('5', ">5"), '|', format(5 ** 2 * 3.141592, ">10.1f"), sep='')
print(format('10', ">5"), '|', format(10 ** 2 * 3.141592, ">10.1f"), sep='')
