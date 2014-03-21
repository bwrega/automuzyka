#!/usr/bin/python


import unittest
from watchdog import guardInEndlessLoop
	
class TestException(Exception):
	pass

class TestWatchDog(unittest.TestCase):
	success_executed=False
	failure_executed=False
	check_executed=False
	def test_success(self):
		funCheck = lambda: True
		def funOnSuccess():
			self.success_executed = True
			raise TestException()
		def funOnFailure():
			self.failure_executed = True
			raise TestException()

		try:
			guardInEndlessLoop(1, funCheck, funOnSuccess, funOnFailure)
		except TestException:
			pass

		self.assertTrue(self.success_executed)
		self.assertFalse(self.failure_executed)
	def test_failure(self):
		funCheck = lambda: False
		def funOnSuccess():
			self.success_executed = True
			raise TestException()
		def funOnFailure():
			self.failure_executed = True
			raise TestException()

		try:
			guardInEndlessLoop(1, funCheck, funOnSuccess, funOnFailure)
		except TestException:
			pass

		self.assertFalse(self.success_executed)
		self.assertTrue(self.failure_executed)
	def test_check_executes(self):
		def funCheck():
			self.check_executed=True
			raise TestException()

		try:
			guardInEndlessLoop(1, funCheck, lambda: True, lambda: True)
		except TestException:
			pass

		self.assertTrue(self.check_executed)

if __name__ == '__main__':
	unittest.main()

