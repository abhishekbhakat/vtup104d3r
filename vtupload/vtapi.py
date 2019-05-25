import hashlib
import requests
from requests.exceptions import ConnectionError

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

    def checkapi(api):
        url = 'https://www.virustotal.com/vtapi/v2/url/report'
        resource = 'virustotal.com'
        params = {'apikey': api, 'resource': resource}
        try:
        	response = requests.get(url, params=params)
        	if not response:
        		return False
        except ConnectionError as e :
        	return False
        return True