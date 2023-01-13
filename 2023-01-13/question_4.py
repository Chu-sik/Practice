# question_4
# print와 format을 사용하여 다음과 같은 표 묘양을 출력하세요.
# format의 width와 align 기능을 활용하세요
# 글꼴로 인해 칸 및 정렬이 맞지 않을 수 있습니다.
# 글꼴을 Consolas로 변경해 보세요
#	Shell 상단의 Options-Configuer IDLE - Font Face: Consolas 설정 후 OK
# %수치는 파이썬 코드에서 계산하고, 소수점 첫째 자리까지만 표시하세요

# 실행예시 생략

print(format('MENU', ">10"), format('VOTE', ">6"), format('(%)', ">8"),
	sep='')
print('-' * 24)
print(format('PIZZA', ">10"), format('4', ">6"), format(4/9*100, ">8.1f"),
	sep='')
print(format('CHICKEN', ">10"), format('3', ">6"), format(3/9*100, ">8.1f"),
	sep='')
print(format('BURGER', ">10"), format('2', ">6"), format(2/9*100, ">8.1f"),
	sep='')
