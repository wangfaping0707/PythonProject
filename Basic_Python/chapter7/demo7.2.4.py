class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me .....")

    def accessible(self):
        print("The secret message is:")



s = Secretive()
# s.__inaccessible()
s.accessible()
# 以这种方式可以访问类中私有的成员和方法
s._Secretive__inaccessible()