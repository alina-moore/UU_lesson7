my_dict = {"Kevin" : 1999, "Max" : 2001 , "Zick" : 1994, "Mable" : 2012}
print("Словарик:" , my_dict)
print("Существующее значение:" , my_dict.get("Zick"))
print("Несуществующее значение:" , my_dict.get("Alexa"))
my_dict.update({"Nami" : 1992, "Mal" : 1989})
boom = my_dict.pop("Mable")
print("Удалено:" , boom)
print("Новый словарик:" , my_dict)

print()

my_set = {"Луна" , 12345, False, False, 12345}
print("Множество:" , my_set)
my_set.add(42.17)
my_set.add((1, 2, 3, 4))
my_set.remove(12345)
print("Новое множество:" , my_set)
