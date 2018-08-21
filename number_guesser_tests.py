from NumberGuesser import NumberGuesser


def given_no_information_when_asked_to_guess_test():
	number_guesser = NumberGuesser([])
	result = number_guesser.guess()
	assert result is None, "Then it should provide no result."


def given_training_data_with_unique_values():
	training_data = [3,1,4,5,7,6,2]
	number_guesser = NumberGuesser(training_data)
	result = number_guesser.guess()

	assert result in training_data, "Then, it should guess training values only."


def given_one_training_value_test():
	training_data = [3]
	number_guesser = NumberGuesser(training_data)
	result = number_guesser.guess()

	assert result in training_data, "Then, it should guess training values only."

#
# def given_training_data_with_repeated_values():
# 	training_data = [3,1,4,5,7,6,3,3,2,3,4,2,6]
# 	number_guesser = NumberGuesser(training_data)
# 	result = number_guesser.guess()
# 	assert result in training_data, "Then, values should be weighted."
