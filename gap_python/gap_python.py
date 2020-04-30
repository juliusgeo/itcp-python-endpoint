import pexpect
import string
class ITCP(object):
	def __init__(self):
		self.gap = self.__spawn__()

	def __spawn__(self):
		gap = pexpect.spawn('../../catpit/gap-valgrind/bin/gap.sh', encoding='ascii', codec_errors='ignore', timeout=120)
		gap.expect('gap>')
		gap.sendline('LoadPackage("ITCP");')
		gap.expect('gap>')
		return gap

	def __execfunction__(self, s):
		try:
			self.gap.sendline(s)
			self.gap.expect('gap>')
			return ''.join([i for i in self.gap.before if i in string.digits + string.ascii_letters + string.punctuation])
		except:
			print(self.gap.read(size=500))
			self.gap.close()
			self.gap = self.__spawn__()
			return "An error occurred, please try again"
