# An automatic guessing game using binary search.
import random

min_n, max_n = 1, 1000
gen_num = random.randint(1,1000)
guess = round((min_n + max_n) / 2)
guess_count = 0
while guess != gen_num:
	if guess > gen_num:
		print("{} is Too High!".format(guess))
		max_n = guess
		guess = round((min_n + max_n) / 2)
		guess_count += 1
	elif guess < gen_num:
		print("{} is Too Low!".format(guess))
		min_n = guess
		guess = round((min_n + max_n) / 2)
		guess_count += 1
	
print("You've got it on {}th time! It's {}.".format(guess_count, gen_num))