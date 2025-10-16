class A:

    def feature_one(self):
        print("Long Nose")

    def feature_two(self):
        print("Brown Hair")
class B:
    def feature_three(self):
            print("pale skin")

    def feature_four(self):
            print("small ears")
            
class C(A,B):
        
         attrA = 1

         def feature_five(self):
           print("round eyes")

parentB = B()
parentB.feature_four()

child = C()
child.feature_one()
    

