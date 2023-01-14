# Exercise
#
# 체질량 지수(BMI)를 계산하는 다음 코드를 작성해보세요요
# - BMI는 몸무게(kg) / 키(m)^2 으로 계산됩니다.
# - 몸무게, 키를 입력할 때 각각 kg, cm 단위로 입력한다고 생각합니다.
# - 사용자는 정수 또는 실수 형태의 문자열만 입력합니다.
# - 출력시 BMI는 소수점 둘째 자리까지만 출력합니다.
#
# 실행예시
# Enter weight(kg): 60
# Enter height(cm): 180
# Your BMI is 18.52

weight = float(input('Enter weight(kg): '))
height = float(input('Enter height(cm): '))
BMI = weight / (height / 100) ** 2

print(f'Your BMI is {BMI:.2f}')
