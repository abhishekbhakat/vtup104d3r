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

    def checkconnection():
        try:
            response = requests.get('https://www.virustotal.com/')
            if not response:
                return False
        except ConnectionError as e:
            return False
        return True

    def upload(apikey,filename):
        filehash = vtapi.gethash(filename)
        link = vtapi.checkscanned(apikey,filehash)
        if not link:
            try:
                url = 'https://www.virustotal.com/vtapi/v2/file/scan'
                params = {'apikey': apikey}
                files = {'file': (filename, open(filename, 'rb'))}
                response = requests.post(url, files=files, params=params)
                text = response.json()
                if text['response_code'] ==1 :
                    print("uploaded")
                    return text
                return None
            except Exception as e:
                return None
        return link

    def checkscanned(apikey,filehash):
        try:
            url = 'https://www.virustotal.com/vtapi/v2/file/report'
            params = {'apikey': apikey, 'resource': filehash}
            response = requests.get(url, params=params)
            text = response.json()
            if text['response_code'] == 1 :
                print("prescanned")
                return text
            return None
        except Exception as e:
            return None