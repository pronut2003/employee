class AppYear:
    def __init__(self):
        self.sy = None
        self.ey = None

    def __str__(self):
        return f"{self.sy}-{self.ey}"

    def set_sy(self,sy):
        if sy>1900 and sy<2100:
            self.sy = sy
            return True
        else:
            print("invalid start year")
            return False

    def set_ey(self,ey):
        if self.sy is None:
            return False
        elif ey == self.sy+1:
            self.ey = ey
            return True
        else:
            print("invalid end year")
            return False





