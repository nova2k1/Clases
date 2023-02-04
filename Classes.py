class Steam:
    def __init__(self, dota, dota2):
        self.dota = dota
        self.dota2 = dota2

    def cs(self):
        print("cs in Steam")

    def css(self):
        print("css in Steam")

    def cs_1_6(self):
        print("cs_1_6 in Steam")


class Epic(Steam):
    def __init__(self, dota, dota2, dota3):
        super().__init__(dota, dota2)
        self.dota3 = dota3

    def cs_1_6(self):
        print("cs_1_6 in Epic")


class Origin(Steam):
    def __init__(self, dota="default_dota", dota2="default_dota2"):
        super().__init__(dota, dota2)

    def Apex(self):
        print("Apex in Origin")

    def Titanfall(self):
        print("Titanfall in Origin")


a = Steam('dota_value', 'dota2_value')
b = Epic('dota_value', 'dota2_value', 'dota3_value')
c = Origin()

a.cs()
a.css()
a.cs_1_6()

b.cs()
b.css()
b.cs_1_6()

c.cs()
c.css()
c.cs_1_6()
c.Apex()
c.Titanfall()

