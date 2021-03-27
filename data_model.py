class Polynomial:
    def __init__(self,*coeffs):
        self.coeffs=coeffs
    def __repr__(self):
        return "Polynomial(*{!r})".format(self.coeffs)
    def __add__(self, other):
        return Polynomial(*(x+y for x,y in zip(self.coeffs,other.coeffs)))
    def __len__(self):
        return len(self.coeffs)
    def __sub__(self, other):
        return Polynomial(*(x-y for x,y in zip(self.coeffs,other.coeffs)))
    def __call__(self, *args, **kwargs):
        pass

if __name__=="__main__":
    p1=Polynomial(1,2,3)
    p2=Polynomial(3,2,3)
    print(p1)
    print(p2)
    print(p1+p2)
    print(len(p1))
    print(p1-p2)
