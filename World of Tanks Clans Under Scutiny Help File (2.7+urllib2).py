#Python 2.7
from Tkinter import *

import urllib2
def Loop(Clan_Id='None'):
        try:
                #Get the Clan Id or WG Clan Link
                '''if Clan_Id =='None':
                        #print('New')
                        Clan_Id = raw_input('What is the Clan ID?: ')
                if Clan_Id == 'Link':
                        #print('New')
                        Clan_Id = raw_input('What is the WG Clan Link?: ')
                        Clan_Id = Clan_Id.split('/')[4]
                if len(Clan_Id) > 10: #If the Id is longer than an usual ID
                        Clan_Id = Clan_Id.split('/')[4] #Assume it is a WG Clan Link'''
                Clan_Id = str(Clan_Id)
                #Get the Data from the Wargaming API
                response = urllib2.urlopen('https://api.worldoftanks.eu/wgn/clans/info/?application_id=demo&fields=name%2Ctag%2Cmembers_count%2Cclan_id&clan_id='+Clan_Id)
                html = response.read()
                #Reorganise the Data pulled into a better layout
                List=[]
                EndList=[]
                Text = html.split(',')
                #print(Text)
                for entry in range(len(Text)):
                        #print(Text[entry])
                        Entry = Text[entry].split(':')
                        for x in range(len(Text[entry].split(':'))):
                                Old=Text[entry].split(':')[x].strip('{')
                                Old=Old.strip('}')
                                List.append(Old)
                        for y in range(7,len(List)):
                                #print(List[y])
                                #print(y)
                                y = y+2
                                if y==10 or y==12:
                                        continue
                                try:
                                        #print(List[y]+':'+List[y+1])
                                        EndList.append(List[y]+':'+List[y+1])
                                except:
                                        #print(y)
                                        pass
                #Output the Data Beautiful
                #print(EndList)
                del EndList[0:3]
                #print(EndList) 
                #print('Clan Tag: '+((EndList[2].split(':'))[1]).strip('"')+'\n'+
                #'Clan Name: '+((EndList[1].split(':'))[1]).strip('"')+'\n'+
                #'WG Clan Link: '+('http://eu.wargaming.net/clans/'+Clan_Id+'/')+'\n'+
                #'No. Of Players: '+((EndList[0].split(':'))[1]).strip('"'))
                #print('End')
                raise ValueError
        except:
                try:
                        text.insert(INSERT, 'Clan Tag: '+((EndList[2].split(':'))[1]).strip('"')+'\n'+
                        'Clan Name: '+((EndList[1].split(':'))[1]).strip('"')+'\n'+
                        'WG Clan Link: '+('http://eu.wargaming.net/clans/'+Clan_Id+'/')+'\n'+
                        'No. Of Players: '+((EndList[0].split(':'))[1]).strip('"'))
                        text.insert(END, "\n---New Clan---\n")
                        text.grid(row=0, column=0)
                        root.mainloop()
                        raise ValueError
                        
                except:
                        exit()
                        #print('There was an Error, probably to do with an Incorrect Clan ID')
                        if raw_input('Enter \'r\' to Re enter a Clan ID else this program will quit \n') == 'r':
                                Loop()
                        else:
                                pass

def onclick():
        pass
root = Tk()
root.title("Clans Under Scrutiny Help")
e = Entry(root)
e.grid(row=1, column=1)
e.focus_set()
Label(text='Insert Clan Id: (eg. 500045726, Our Clan)').grid(row=1,column=0)
def callback():
    Loop(e.get())
b = Button(root, text="Enter Clan_Id", width=10, command=callback)
b.grid(row=1, column=2)
text = Text(root)
text.grid(columnspan=3, row=0, column=0)
root.mainloop()
'''
master = Tk()

e = Entry(master)
e.pack()
e.focus_set()

def callback():
    print e.get()
b = Button(master, text="Enter", width=10, command=callback)
b.pack()

mainloop()'''
#End Test
Loop()


