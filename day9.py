class Tank:
  def move(self):
    print("Tank bertempur lewat daratan.")

class Pesawat_Tempur:
  def move(self):
    print("Pesawat Tempur bertempur lewat udara.")

class Kapal_Induk:
  def move(self):
    print("Kapal induk bertempur lewat lautan.")

tank = Tank()
pesawat_tempur = Pesawat_Tempur()
kapal_induk= Kapal_Induk()

tank.move()  
pesawat_tempur.move()  
kapal_induk.move()  