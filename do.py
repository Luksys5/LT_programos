
myint = int(raw_input("Irasykite vartotoja 1 \n Parodykite vartotojus 2 \n"))
if myint == 1:
    from postreq import *
    
    bound = "--AaB03x"
    adata = readdata(bound)
    send(adata,bound)
else:
    from getreq import *
    getreq(Req,servak1)
