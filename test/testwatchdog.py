#!/usr/bin/python

import unittest
import watchdog.guardInEndlessLoop

class TestWatchDog(unittest.TestCase):
	class TestException(Exception):
		pass
	def test_success(self):
		success_executed=False
		failure_executed=False
		funCheck = lambda: True
		#funOnSuccess = (lambda: success_executed=True) and (lambda: raise TestException())
		funOnSuccess = lambda: success_executed=True
		#funOnFailure = (lambda: failure_executed=True) and (lambda: raise TestException())
		funOnFailure = lambda: failure_executed=True

		try:
			guardInEndlessLoop(1, funCheck, funOnSuccess, funOnFailure)
		except TestException:
			pass

		assertTrue(success_executed)
		assertFalse(failure_executed)

if __name__ == '__main__':
	unittest.main()

