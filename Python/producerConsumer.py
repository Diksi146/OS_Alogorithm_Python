def main():
    bufferSize = int(input("\t Enter the Buffer size of the problem :- "))
    global filledSize
    filledSize = 0

    def producer(n):
        global filledSize
        if filledSize == bufferSize:
            print(" Buffer is Full... ")
        else:
            global produced
            produced = 0
            while n:
                if filledSize == bufferSize:
                    print(" Buffer is Full ...")
                    print(
                        f" {produced} no of items produced from given operation input")
                    produced = 0
                    break
                else:
                    filledSize += 1
                    produced += 1
                n -= 1

    def consumer(n):
        global filledSize
        if filledSize <= 0:
            print(" Buffer is Empty... ")
        else:
            global consumed
            consumed = 0
            while n:
                if filledSize == 0:
                    print(" Buffer is Empty... ")
                    print(
                        f" {produced} no of items consumed from given operation input")
                    consumed = 0
                else:
                    filledSize -= 1
                    consumed += 1
                n -= 1

    flag = 1
    while(flag):
        print("\t Producer Consumer Problem ")
        print("\t   1. Produce Items")
        print("\t   2. Consume Items")
        print("\t   3. Exit")
        code = int(input("Enter Your Choice :- "))
        if code == 1:
            n = int(input("Enter the number of Inputs you want to produce :- "))
            producer(n)
        elif code == 2:
            n = int(input("Enter the number of Inputs you want to consume :- "))
            consumer(n)
        elif code == 3:
            flag = 0
            break
        else:
            print("Enter The correct Choice !!!")


main()
