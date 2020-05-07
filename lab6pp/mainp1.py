class BaseClass:
    num_base_calls = 0

    def call_me(self, caller):
        print(" metoda BaseClass, caller= ", caller)
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self, caller):
        print(" metoda LeftSubClass, caller= ", caller)
        BaseClass.call_me(self, "LeftSubClass")
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_calls = 0

    def call_me(self, caller):
        print("Apel met din RightSubClass, caller= ", caller)
        BaseClass.call_me(self, "RightSubClass")
        self.num_right_calls += 1


class SubClass(LeftSubclass, RightSubClass):
    num_sub_calls = 0

    def call_me(self, caller):
        print("Apel met  SubClass, caller= ", caller)
        BaseClass.call_me(self, "SubClass")
        self.num_sub_calls +=1


if __name__ == '__main__':
    subclass_instance = SubClass()
    print(SubClass.__mro__)
    subclass_instance.call_me("__main__")
    print(subclass_instance.num_sub_calls,
          subclass_instance.num_left_calls,
          subclass_instance.num_right_calls,
          subclass_instance.num_base_calls)
