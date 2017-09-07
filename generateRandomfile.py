
import random as r


def main():


    def generateRandom(x,y):
        #x - no of records
        #y - file convention]

        dfile = open("R%s.txt" %y, "a+")
        for i in xrange(x):
            data=r.randint(1,99999)
            dfile.write(str(data)+'\n')
        dfile.close()

    def generateIncremental(x,y):
        #x - no of records
        #y - file convention]

        dfile = open("I%s.txt" %y, "a+")

        a=1
        for i in xrange(1,x+1):
            data = r.randint(a, a+5)
            dfile.write(str(data) + '\n')
            a=a+5
        dfile.close()

    def generateDecremental(x, y):
        # x - no of records
        # y - file convention]
        dfile = open("D%s.txt" % y, "a+")
        a = x*10
        for i in xrange(1, x + 1):
            data = r.randint(a-5,a)
            dfile.write(str(data) + '\n')
            a = a - 5
        dfile.close()

    a=1
    for i in xrange(2000,52000,2000):
        print i,a
        #generateRandom(i,a)
        generateDecremental(i,a)
        generateIncremental(i, a)
        a=a+1

if __name__=="__main__":
    main()