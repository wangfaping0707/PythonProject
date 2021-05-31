from objectDmeo.BirdDemo import Bird


class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        # super(SongBird, self).__init__()
        super().__init__()
        self.sound = "Squawk!"

    def sing(self):
        print(self.sound)


sb = SongBird()
print(sb.sound)
sb.eat()
