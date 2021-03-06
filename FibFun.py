from string import Template
import argparse

class FibFun(object):

    def __init__(self):
        self._a, self._b = 0,1
        self._FibList = "{}".format(self._a)
        self._last = self._b
    
    def GetList(self):
        return self._FibList

    def Fibnth(self,n):
        for i in range(n):
            self._a,self._b = self._b,self._a+self._b
            self._FibList += ",{}".format(self._a)
        
        self._last = self._a
        return self._a



def Main():
    parser = argparse.ArgumentParser()

    parser.add_argument("num",help="Integer value: The fibonacci number you wish to calculate",type=int)
    parser.add_argument("-fl","--fiblist",help="Include full list of fibonacci numbers calculated in response",action="store_true")
    parser.add_argument("-v","--verbose",help="Increase output verbosity. When specifying this argument you do not need to include --fiblist argument to get list",action="store_true")

    args = parser.parse_args()

    tAllVerbose = Template("The ${num}th fibonacci number is : $Fib. \nFull list of numbers generated: $List")

    fib = FibFun()

    fData = dict(num=args.num,Fib=fib.Fibnth(args.num),List=fib.GetList())

    if args.verbose:
        print tAllVerbose.substitute(fData)
    elif args.fiblist:
        print fData.get("List")
    else:
        print fData["Fib"]

if __name__ == "__main__":
    Main()
