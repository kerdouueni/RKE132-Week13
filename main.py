from animal import Animal, Cat, Dog

my_cat = Cat("Kusti")
my_dog = Dog("Aplha")
neighbours_dog = Dog("Laif")
neighbours_cat = Cat("Aadu")

my_cat.cat_sees(my_dog)
my_cat.cat_sees(neighbours_cat)

my_dog.dog_sees(neighbours_dog)
my_dog.dog_sees(my_cat)