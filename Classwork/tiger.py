class tiger:
  animal_type = "predator"

  def __init__(self,name,age):
    self.age = age
    self.name = name 

  def prey(self):
    print(f"{self.name} eat other animals like rabbits , deer and fox. At {self.age} years old.")
  

tiger1  = tiger("Rohit",23)
tiger2  = tiger("Sohit",43)

tiger1.prey()
tiger2.prey()


