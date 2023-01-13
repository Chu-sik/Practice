# question_5
# 주어진 초 단위의 시간이 몇 시간 몇 분 몇 초인지 변환해 출력하세요.
# HInt: %(나머지), //(몫) 연산을 활용하세요
# 시간, 분, 초를 직접 적지 말고 파이썬 코드에서 계산되도록 작성하세요
# 분, 초가 한 자리 수인 경우 맨 앞에 0을 붙여 두 자리로 표시하세요 (format 활용)
#
# 실행 예시
# 3636 초는 1 시간 00 분 36 초

print(3636, "초는", 
	3636 // 60 // 60, '시간',
	format(3636 // 60 % 60, "02d"), '분',
	format(3636 % 60, "02d"), '초')
