from speedtest import Speedtest

class Connection_speed:
    def __init__(self):
        pass

    def download(self):
        try:
            self.speed_test = Speedtest()
            return self.speed_test.download()
        except:
            return None

    def upload(self):
        try:
            self.speed_test = Speedtest()
            return self.speed_test.upload()
        except:
            return None