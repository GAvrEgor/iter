nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class MyIterator:

	def __init__(self, nested_list):
		self.start = -1
		self.end = len(nested_list)

	def __iter__(self):
		return self

	def __next__(self):
		self.start += 1
		if self.start == self.end:
			raise StopIteration
		return self

	def __str__(self):
		return '\n'.join(str(item) for item in nested_list[self.start])


def flat_generator(my_list):
	for sub_list in my_list:
		for elem in sub_list:
			yield elem


for item in MyIterator(nested_list):
		print(item)

