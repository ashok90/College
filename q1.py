

def main():

    A=[1,2]
    def mysteryfunction(A,right):
        #print "triggered"+str(right)

        if right == 0:
            return A[0]
        else:
            val = mysteryfunction(A, right-1)
            #print val
            if A[right] > val:
                print "ini"
                val = A[right]
        return val



    m=mysteryfunction(A,1)
    print m

if __name__ == "__main__":
    main()