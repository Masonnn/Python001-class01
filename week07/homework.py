class Zoo(object):

    def __init__(self, zoo_name):
        self.animal_in_zoo = []
        self.zoo_name = zoo_name

    def add_animal(self, animal):
        if animal in self.animal_in_zoo:
            print(f'{animal} already exists')
            return self.animal_in_zoo[animal]
        self.animal_in_zoo.append(animal)
        self.__dict__[type(animal).__name__] = animal


from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, animal_type, size, disposition):
        self.animal_type = animal_type  # 类型
        self.size = size  # 体型
        self.disposition = disposition  # 性格

    @property
    def is_ferocious(self):  # 是否凶猛动物
        if (self.size == '中' or self.size == '大') and self.disposition == '凶猛' and self.animal_type == '食肉':
            return True
        return False


# class ToBePetMixin(object):
#     def to_be_pet(self, disposition):
#         if disposition is '温顺':
#             return True
#         return False


class Cat(Animal):
    roaring = "喵喵喵"

    def __init__(self, cat_name, animal_type, size, disposition):
        self.cat_name = cat_name
        super(Cat, self).__init__(animal_type, size, disposition)

    @property
    def is_pet(self):
        if self.disposition == '温顺':
            return True
        return False
        # return ToBePetMixin.to_be_pet(self.disposition)

    def helloKitty(self):
        print(f"Here is {self.cat_name}")
        print(self.roaring)
        print(f"Am I to be a pet? {self.is_pet}")


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat1.helloKitty()
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
