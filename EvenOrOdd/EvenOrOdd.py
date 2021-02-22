import sys

class EvenOrOdd:
    def even(self,n):
        return (not n%2)

    def check(self,n):
        n=self.validate(n)
        if (n):      
            if(self.even(n)):
                print("Even")
            else:
                print ("Odd")
        else:
            print("This is not a Valid Input")
    def validate(self,n):
        try:
            x=int(n)
            return x
        except ValueError:
            pass


x=EvenOrOdd()
x.check(sys.argv[1])
