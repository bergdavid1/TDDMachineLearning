class NumberGuesser(object):
	"""Guesses numbers based on the history of your input"""

	def __init__(self, initial_guesses):
		self.__guessed_numbers = initial_guesses[0:1]

	def guess(self):
		if len(self.__guessed_numbers) == 0:
			return None

		return self.__guessed_numbers[0]
