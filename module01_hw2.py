class Meta(type):
    # тут повинно бути ваше рішення
    class_number = 0

    def __new__(mcs, name, base, namespace, **kwargs):
        instance = super().__new__(mcs, name, base, namespace)
        instance.class_number = mcs.class_number
        mcs.class_number += 1
        return instance


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
