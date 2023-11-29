class TVController:

    def __init__(self, channels_list : list):
        self.channels_list = channels_list
        self.turned_channel = self.channels_list[0]

    def first_channel(self):
        self.turned_channel = self.channels_list[0]
        return self.turned_channel
    
    def last_channel(self):
        self.turned_channel = self.channels_list[len(self.channels_list) - 1]
        return self.turned_channel
    
    def turn_channel(self, n):
        if n < 0 or n >= len(self.channels_list):
            return "Incorect channel number"
        else:
            self.turned_channel = self.channels_list[n - 1]
            return self.turned_channel
    
    def next_channel(self):
        i = self.channels_list.index(self.turned_channel)
        if i + 1 == len(self.channels_list):
            self.turned_channel = self.channels_list[0]
            return self.turned_channel
        else:
            self.turned_channel = self.channels_list[i + 1]
            return self.turned_channel
    
    def previous_channel(self):
        i = self.channels_list.index(self.turned_channel)
        if i - 1 < 0:
            self.turned_channel = self.channels_list[len(self.channels_list) - 1]
            return self.turned_channel
        else:
            self.turned_channel = self.channels_list[i - 1]
            return self.turned_channel
    
    def current_channel(self):
        return self.turned_channel
    
    def exists(self, n_or_name):
        for i in range(len(self.channels_list)):
            if n_or_name == i + 1 or n_or_name == self.channels_list[i]:
                return "Yes"
        else:
            return "No"

channels = ["BBC", "Discovery", "TV1000"]

my_controller = TVController(channels)

assert my_controller.first_channel() == "BBC"
assert my_controller.last_channel() == "TV1000"
assert my_controller.turn_channel(1) == "BBC"
assert my_controller.next_channel() == "Discovery"
assert my_controller.previous_channel() == "BBC"
assert my_controller.current_channel() == "BBC"
assert my_controller.exists(4) == "No"
assert my_controller.exists("BBC") == "Yes"