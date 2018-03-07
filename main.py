list = [0,0,0,0,0,0,0,0,0,0]

def right():
	#第二题的条件
	if list[4] == sec_fif(list[1]):
		#第三题的条件
		if thi(list[2]):
			#第四题条件
			if fou(list[3]):
				#第五题条件
				if fif(list[4]):
					#第六题条件
					if six(list[5]):
						#第七题条件
						if sev(list[6]):
							#第八题条件
							if eig(list[7]):
								#第九题条件
								if nin(list[8]):
									#第十题条件
									if ten(list[9]):
										return True
	else:
		return False
#第七题求出现次数最少的选项
def minNum():
	#每个选项的次数
	choice_0 = 0
	choice_1 = 0
	choice_2 = 0
	choice_3 = 0
	minnum = 10
	maxChoice = ""
	for choice in list:
		if choice == 0:
			choice_0 += 1
		elif choice == 1:
			choice_1 += 1
		elif choice == 2:
			choice_2 += 1
		elif choice == 3:
			choice_3 += 1
	if choice_0<=minnum:
		minnum = choice_0
		maxChoice = "choice_0"
	if choice_1<=minnum:
		minnum = choice_1
		maxChoice = "choice_1"
	if choice_2<=minnum:
		minnum = choice_2
		maxChoice = "choice_2"
	if choice_3<=minnum:
		minnum = choice_3
		maxChoice = "choice_3"
	return maxChoice
#第十题求选项中出现次数最多和出现次数最少的差
def max_min_subtract():
	#每个选项的次数
	choice_0 = 0
	choice_1 = 0
	choice_2 = 0
	choice_3 = 0
	for choice in list:
		if choice == 0:
			choice_0 += 1
		elif choice == 1:
			choice_1 += 1
		elif choice == 2:
			choice_2 += 1
		elif choice == 3:
			choice_3 += 1
	return max(choice_0,choice_1,choice_2,choice_3)-min(choice_0,choice_1,choice_2,choice_3)	
def sec_fif(choice):
	if choice == 0:
		return 2
	if choice == 1:
		return 3
	if choice == 2:
		return 0
	if choice == 3:
		return 1
def thi(choice):
	if choice == 0:
		if list[5]==list[1] and list[1]==list[3] and list[2]!=list[5]:
			return True
	elif choice == 1:
		if list[2]==list[1] and list[1]==list[3] and list[5]!=list[2]:
			return True
	elif choice == 2:
		if list[2]==list[5] and list[5]==list[3] and list[1]!=list[2]:
			return True
	elif choice == 3:
		if list[2]==list[5] and list[5]==list[1] and list[1]!=list[3]:
			return True
	else:
		return False
def fou(choice):
	if choice == 0:
		if list[0] == list[4]:
			return True
	elif choice == 1:
		if list[1] == list[6]:
			return True
	elif choice == 2:
		if list[0] == list[8]:
			return True
	elif choice == 3:
		if list[5] == list[9]:
			return True
	else:
		return False
def fif(choice):
	if choice == 0:
		if choice == list[7]:
			return True
	elif choice == 1:
		if choice == list[3]:
			return True
	elif choice == 2:
		if choice == list[8]:
			return True
	elif choice == 3:
		if choice == list[6]:
			return True
	else:
		return False
def six(choice):
	if choice == 0:
		if list[1] == list[3]:
			return True
	elif choice == 1:
		if list[0] == list[5]:
			return True
	elif choice == 2:
		if list[2] == list[9]:
			return True
	elif choice == 3:
		if list[4] == list[8]:
			return True
	else:
		return False
def sev(choice):
	if choice == 0:
		if minNum() == "choice_2":
			return True
	elif choice == 1:
		if minNum() == "choice_1":
			return True
	elif choice == 2:
		if minNum() == "choice_0":
			return True
	elif choice == 3:
		if minNum() == "choice_3":
			return True
	else:
		return False
def eig(choice):
	if choice == 0:
		if list[0] != list[6]+1 or list[0] != list[6]-1:
			return True
	elif choice == 1:
		if list[0] != list[4]+1 or list[0] != list[4]-1:
			return True
	elif choice == 2:
		if list[0] != list[1]-1 or list[0] != list[1]-1:
			return True
	elif choice == 3:
		if list[0] != list[9]-1 or list[0] != list[9]-1:
			return True
	else:
		return False
def nin(choice):
	if choice == 0:
		if (list[0]==list[5])!=(list[5]==list[4]):
			return True
	elif choice == 1:
		if (list[0]==list[5])!=(list[9]==list[4]):
			return True
	elif choice == 2:
		if (list[0]==list[5])!=(list[1]==list[4]):
			return True
	elif choice == 3:
		if (list[0]==list[5])!=(list[8]==list[4]):
			return True
	else:
		return False
def ten(choice):
	if choice == 0:
		if max_min_subtract() == 3:
			return True
	elif choice == 1:
		if max_min_subtract() == 2:
			return True
	elif choice == 2:
		if max_min_subtract() == 4:
			return True
	elif choice == 3:
		if max_min_subtract() == 1:
			return True
	else:
		return False

if __name__ == '__main__':
	for choice01 in range(0,4):
		list[0] = choice01
		for choice02 in range(0,4):
			list[1] = choice02
			for choice03 in range(0,4):
				list[2] = choice03
				for choice04 in range(0,4):
					list[3] = choice04
					for choice05 in range(0,4):
						list[4] = choice05
						for choice06 in range(0,4):
							list[5] = choice06
							for choice07 in range(0,4):
								list[6] = choice07
								for choice08 in range(0,4):
									list[7] = choice08
									for choice09 in range(0,4):
										list[8] = choice09
										for choice10 in range(0,4):
											list[9] = choice10
											if right():
												for choice in list:
													if choice == 0:
														print("A", end='')
													elif choice == 1:
														print("B", end='')
													elif choice == 2:
														print("C", end='')
													elif choice == 3:
														print("D", end='')
												print("")	