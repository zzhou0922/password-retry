password = 'a123456'
attempt = 3

while attempt > 0:
	attempt = attempt - 1
	guess = input('Please enter the password: ')
	if guess == password:
		print('Login successfully!')
		break
	else:
		print('Password incorrect!')
		if attempt > 0:
			print(attempt, 'more attempt(s).')
		else:
			print('Login failed!')



# while True version
# password = 'a123456'
# guess = input('Please enter the password: ')
# attempt = 3

# while True:
# 	attempt = attempt - 1
# 	if guess == password:
# 		print('Login successfully!')
# 		break
# 	elif attempt == 0:
# 		print('Login failed!')
# 		break
# 	elif guess != password and attempt > 0:		
# 		print('Password incorrect! ' + str(attempt) + ' more attempt(s).')
# 		guess = input('Please enter the password: ')

	