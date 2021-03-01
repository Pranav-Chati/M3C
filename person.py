
class Person:

    def __init__(self, age_group_index, is_heavy_internet_user):
        self.age_group = age_group_index
        self.heavy_internet_user = is_heavy_internet_user
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def max_bandwidth(self):
        if self.heavy_internet_user:
            # return 39.5
            return 35
        else:
            if self.age_group == 0:
                return 15.5
            elif self.age_group == 1:
                return 15.5
            elif self.age_group == 2:
                return 24.5
            elif self.age_group == 3:
                return 24.5
            elif self.age_group == 4:
                return 24.5

    def total_bandwidth_requirement(self):
        total_bandwidth = 0

        for device in self.devices:
            total_bandwidth += device.get_bandwidth()

        return total_bandwidth
