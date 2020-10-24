class XException(Exception):
	def __init__(self, message):
		self.message = message

	def print_message(self):
		print("Message: {0}".format(self.message))