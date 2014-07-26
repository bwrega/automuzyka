#!/usr/bin/python

from watchdog import guardInEndlessLoop
from settings import Settings
from reactions.reactions import Reactions
from reactions.mocpreactions import MocpReactions
import time
import subprocess

class DroidWatch():
	s = Settings()
	ostatnioWidziany=time.time()
	ostatniPoczatekPrzerwy = 0
	def watch(self):
		guardInEndlessLoop(self.s.czestoscSprawdzaniaWSekundach, self.checkFunction, self.executeOnSuccess, self.executeOnFailure)
	def executeOnSuccess(self):
		currentTime = time.time()
		przerwa = currentTime - self.ostatnioWidziany
		if przerwa>self.s.minimalnyCzasPrzerwyWSekundach:
			self.s.reactions.callbackPowrotPoPrzerwie()
		else:
			self.s.reactions.callbackCalyCzasOnline()
		self.ostatnioWidziany = currentTime
	def executeOnFailure(self):
		currentTime = time.time()
		przerwa = currentTime - self.ostatnioWidziany
		if self.ostatniPoczatekPrzerwy < self.ostatnioWidziany:
			if przerwa>self.s.minimalnyCzasPrzerwyWSekundach:
				self.ostatniPoczatekPrzerwy = currentTime
				self.s.reactions.callbackPoczatekPrzerwy()
			else:
				self.s.reactions.callbackKrotkaPrzerwa()
		else:
			self.s.reactions.callbackWTrakcieDlugiejPrzerwy()

	def checkFunction(self):
		przynajmniejJedenOdpowiedzial=False
		ipIterator=self.s.sprawdzaneIP.__iter__()
		try:
			while not przynajmniejJedenOdpowiedzial:
				ip=ipIterator.next()
				przynajmniejJedenOdpowiedzial = przynajmniejJedenOdpowiedzial or not subprocess.call(["./pingsilently",ip])
		except StopIteration:
			pass
		return przynajmniejJedenOdpowiedzial

if __name__ == '__main__':
	DroidWatch().watch()

