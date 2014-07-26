import subprocess
from reactions import Reactions

class UnblankReactions(Reactions):
	def callbackPowrotPoPrzerwie(self):
		print "callbackPowrotPoPrzerwie - unblanking console"
		subprocess.call(["UnblankConsole"])
	
