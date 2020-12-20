class Secretive:
    def _inaccessible(self):
        print("Bet you can't see me...")

    def accessible(self):
        print("The secret message is:")
        self._inaccessible()


