import hashlib
import requests

BLOCKSIZE = 65536

class vtapi(object):
	"""docstring for vtapi"""
	def __init__(self, arg):
		super(vtapi, self).__init__()
		self.arg = arg

	def gethash(filepath):
		hasher = hashlib.sha1()
		with open(filepath, 'rb') as afile:
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:
			    hasher.update(buf)
			    buf = afile.read(BLOCKSIZE)
		return hasher.hexdigest()