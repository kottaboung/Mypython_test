#Inner Function

def ShowMessage():
    print('Main Message on green')

    def Submessage1():
        print('Submessage on green')

        def Submessage2():
            print('Submessage on green')

        Submessage2()
    Submessage1()
ShowMessage()
