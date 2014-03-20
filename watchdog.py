#!/usr/bin/python

import time

def guardInEndlessLoop(checkingFrequencyInSeconds, checkingFunction, executeOnSuccess, executeOnFailure):
	while True:
		checkingResult = checkingFunction()
		if checkingResult:
			executeOnSuccess()
		else:
			executeOnFailure()
		time.sleep(checkingFrequencyInSeconds)

