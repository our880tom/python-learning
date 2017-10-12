class TheThing(object):
	"""docstring for TheThing"""
	def __init__(self):
		self.number = 0

	def some_function(self):
		print "I got called."

	def add_me_up(self, more):
		self.number += more
		return self.number

# two different thingd

a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print a.add_me_up(20)
print b.add_me_up(20)
print b.add_me_up(20)

print a.number
print b.number
		