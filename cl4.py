class A:
    def __init__(self):
        print("initialization of class A")
class B:
    def __init__(self):
        print("initalization of class B")

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("initialization of C")
        
    def features_all(self):
        print("GooD")
        
    def call_feature(self):
        super().feature_one()

c1 = C()

c1.call_feature()
        
