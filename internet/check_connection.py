from urllib import request

class Connection_status:
    def __init__(self):
        pass

    def status(self, host = 'http://google.com'):
        try:
            request.urlopen(host)
            return True
        except:
            return False