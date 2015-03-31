#mystuff = {'bob':'male','carol':"female','ted':'male','alice':'female'}

import pickle

instuff = open('fourpeople.dat','rb')
           mydict = pickle.load(instuff)
           instuff.close()
           print(mydict)
