


class Animal():
    fierce = True

    # 类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性
    def __init__(self,type,body_type,character):
        self.type = type
        self.body_type = body_type
        self.character = character
        self.set_fierce()
    def set_fierce(self):
        spec_type = ['中','大']
        if self.body_type in spec_type  and self.type == "食肉":
            self.fierce = True
        else:
            self.fierce = False

class Cat(Animal):
    cry = "喵喵喵...."
    # 增加继承的属性
    def __init__(self,name,type,body_type,character,is_pet=True):
        self.name = name
        self.is_pet = is_pet
        super(Cat,self).__init__(type,body_type,character)

    pass

class Zoo():
    _animals_list = []
    def __init__(self,name):
        self.name = name

    def add_animal(self,animal):

        if animal not in self._animals_list:
            self._animals_list.append(animal)
        else:
            print("{}已经存在{}动物园".format(animal,self.name))

    def showAnimals(self):
        # print(self._animals_list)
        return  self._animals_list



if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')

    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    # have_cat = getattr(z, 'Cat')
    #
    # print(have_cat)

