nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]



class MyIterator:

	def __init__(self, list_):
		self.list_= list_
		self.len = len(nested_list)
		self.main_list_cursor = -1
		self.nested_list_cursor = 0


	def __iter__(self):
		self.main_list_cursor +=1
		self.nested_list_cursor = 0
		return self

	def __next__(self):
		if self.nested_list_cursor == len(self.list_[self.main_list_cursor]):
			iter(self)
		if self.main_list_cursor == len(self.list_):
			raise StopIteration
		self.nested_list_cursor += 1
		return self.list_[self.main_list_cursor][self.nested_list_cursor - 1]

	# def __str__(self):
	# 	return '\n'.join(str(item) for item in nested_list[self.start])


def flat_generator(my_list):
	for sub_list in my_list:
		for elem in sub_list:
			yield elem

flat_list = [item for item in MyIterator(nested_list)]
print(flat_list)
# for item in MyIterator(nested_list):
# 		print(item)

# flat_list = [",".join(str(item).split()) for item in MyIterator(nested_list)]
# print(flat_list)
#
# for item in flat_generator(nested_list):
# 	print(item)
