"""
File: coin_flip_runs.py
Name: YI-HSIU
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r
NUM_ROLLS = 15


def main():
	"""
	TODO:
	"""
	# """
	# SC001 Final Q4
	# """
	# roll_1 = r.randrange(1, 7)
	# run = 0
	# is_in_a_row = False
	# print('Rolls: ' + str(roll_1))
	#
	# for i in range(NUM_ROLLS - 1):
	# 	roll_2 = r.randrange(1, 7)
	#
	# 	if roll_1 == roll_2:
	#
	# 		if is_in_a_row == False:
	# 			run += 1
	# 			is_in_a_row = True
	#
	# 	else:
	# 		is_in_a_row = False
	#
	# 	roll_1 = roll_2
	# 	print('Rolls: ' + str(roll_1))
	#
	# print('Number of runs: ' + str(run))

	print("Let's flip a coin!")
	is_in_a_row = False  # to setup a switch for count run number
	run_num = 0  # to calculate run numbers
	task_1 = r.randrange(1, 3)
	task_1_concat = str(task_1)  # to store the initial value of task_1

	# print(str(sep_h_t(task_1)))  # test transfer function
	close_num = int(input("Number of runs: "))  # exit flip coins condition

	while True:
		task_2 = r.randrange(1, 3)

		if close_num == run_num:
			break

		if task_1 == task_2:

			if is_in_a_row == False:
				run_num += 1
				is_in_a_row = True

		else:
			is_in_a_row = False

		task_1 = task_2
		task_1_concat += str(task_2)

	print('Number of runs: ' + str(run_num))
	# print(task_1_concat)  # to check concat result of coins

	# To change the 1/2 to H/T
	task_concat_display = ""
	for i in range(len(task_1_concat)):
		ch = task_1_concat[i]
		if ch == "1":
			task_concat_display += "H"
		else:
			task_concat_display += 'T'

	print(str(task_concat_display))  # print out final value for coins with H/T status


def sep_h_t(task):
	"""
	:param task: int(1 or 2)
	:return: 1=H, 2=T
	"""

	if task == 1:
		task = "H"
	else:
		task = "T"
	return task


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
