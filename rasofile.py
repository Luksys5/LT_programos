def writetofile(dict):
        f = open("kodai","w")
        for x in dict:
                f.write(x+"+"+dict.get(x)+"\n")
        f.close()
def ftotextf(mf,dict):
        mystr = ""
        fw = open("newfile","w")
        with open(mf) as f:
                while True:
                        y = f.read(1)
                        if not y:
                                print "EOF"
                                return
                        try :
                                mystr += y
                        except TypeError:
                                mystr += str(y)
                        if mystr in dict:
                                fw.write(dict.get(mystr))
                                mystr = ""
                        elif y in dict:
                                fw.write(dict.get(y))
                                mystr = ""

        f.close()
        fw.close()

