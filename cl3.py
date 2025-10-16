class A:
    def __init__(self):
        print("initialization of class A")
    def feature_one(self):
        print("Long Nose")

    def feature_two(self):
        print("Brown Hair")

class B:
    def __init__(self):
        print("initialization of class B")
    def feature_three(self):
        print("Pale skin")

    def feature_four(self):
        print("Small Ears")

class C(A,B):

    attrA = 1

    def feature_five(self):
        print("Round Eyes")

parentB = B()
parentB.feature_four()
child=C()
child.feature_one()

class D(C):
    def feature_six(self):
        print("Long Hands")

grandchild = D()

grandchild.feature_five()

b1 = B()
