in_weight = input('您的体重KG')
in_height = input('您的身高m')

weight = float(in_weight)
height = float(in_height)

print(weight)
print(height)

bmi = weight / (height * height)


if bmi <= 18.5 :
	print(bmi , '过轻')
elif 18.5 < bmi <= 25 :
	print(bmi , '正常')
elif 25 < bmi <= 28 :
	print(bmi , '过重')
elif 28 < bmi <= 32 :
	print(bmi , '肥胖')
else :
	print(bmi , '严重肥胖')
