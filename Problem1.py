class Room:
    def __init__(self, length, height, width):
        self.length = length
        self.height = height
        self.width = width

    def get_window_count(self):
        window_count = self.length // 2 * self.height // 15
        return window_count

    def get_volume(self):
        volume = self.length * self.height * self.width
        return volume
    
room = []

for i in range(5):
    length = int(input("Length: "))
    height = int(input("Height: "))
    width = int(input("Width: "))

    room.append(Room(length, height, width))
    print("Xonadagi oynalar soni:", room[i].get_window_count())
    print("Xonaning hajmi:", room[i].get_volume())
