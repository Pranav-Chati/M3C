
class Device:

    def __init__(self, name):
        self.name = name

    def get_bandwidth(self):
        if self.name == "tv":
            return 7.5
        elif self.name == "console":
            return 3
        elif self.name == "tv_connected_internet_advice":
            return 5
        elif self.name == "computer_heavy":
            return 25
        elif self.name == "computer_not_heavy":
            return 10
        elif self.name == "video_computer":
            return 5
        elif self.name == "app_web_smartphone":
            return 7
        elif self.name == "tablet":
            return 7
