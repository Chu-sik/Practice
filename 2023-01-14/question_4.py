# question 4 - python1 day3

letter = input('Enter a lowercase letter: ')
upper_letter = chr(ord(letter) - (ord('a') - ord('A')))

print(f'Conversion result: {letter} -> {upper_letter}')
