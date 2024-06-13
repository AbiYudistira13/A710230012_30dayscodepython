class Employee:
  def __init__(self, name, age, salary):
    self.__name = name
    self.__age = age
    self.__salary = salary

  def get_name(self):
    return self.__name

  def set_name(self, name):
    self.__name = name

  def get_age(self):
    return self.__age

  def set_age(self, age):
    self.__age = age

  def get_salary(self):
    return self.__salary

  def set_salary(self, salary):
    self.__salary = salary

# Contoh penggunaan class Employee
employee1 = Employee("Budi", 25, 5000000)

# Mengubah nilai atribut
employee1.set_name("Andi")
employee1.set_age(27)
employee1.set_salary(6000000)

# Mendapatkan nilai atribut
print(f"Nama: {employee1.get_name()}")
print(f"Usia: {employee1.get_age()}")
print(f"Gaji: {employee1.get_salary()}")