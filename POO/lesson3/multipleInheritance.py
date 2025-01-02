class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling mehtod on Base Class")
        self.num_base_calls += 1 


class LeftSubClass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling Method on Left Subclass")
        self.num_left_calls += 1
        

class RightSubClass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling Method on Right Subclass")
        self.num_right_calls += 1
        

class Subclass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling Method on Subclass")
        self.num_sub_calls += 1
