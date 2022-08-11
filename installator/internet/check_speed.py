from speedtest import Speedtest

class Connection_speed:
    def __init__(self):
        self.speed_test = Speedtest()

    def download(self):
        return self.speed_test.download()

    def upload(self):
        try:
            return self.speed_test.upload()
        except:
            return None