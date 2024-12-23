import time

#colors
red='\033[91m'
b='\033[21m'
gren='\033[92m'
yellow='\033[93m'
cyan='\033[96m'
blue='\033[94m'

print (red+b+"""
                    
 ____  ___ ___  ____  ____   _____   ____  ___     ____
 /    ||   |   ||    ||    \ |     | /    ||   \   /    |
|  o  || _   _ | |  | |  _  ||__/  ||  o  ||    \ |  o  |
|     ||  \_/  | |  | |  |  ||   __||     ||  D  ||     |
|  _  ||   |   | |  | |  |  ||  /  ||  _  ||     ||  _  |
|  |  ||   |   | |  | |  |  ||     ||  |  ||     ||  |  |
|__|__||___|___||____||__|__||_____||__|__||_____||__|__|
???  ??????     ?????????  ????????????????  ?????????? ???  ??
                   
"""+b+red)

print (gren+b+"            <===[[ coded by Aminzada ]]===>"+b+gren)
print (" ")
print (yellow+b+"     <---( search on youtube Aminzada Tech)--->"+b+yellow)
print (" ")

length=int(raw_input(cyan+b+"Enter the number of characters: "+b+cyan))
print (" ")
name=raw_input(cyan+b+"Name your wordlist wit (.txt) extension: "+b+cyan)
tic = time.clock()
print (" ")
print (blue+b+"<><><><><><><><><><><><><><><><><><><><><>"+b+blue)
print (" ")
print (yellow+b+"Wordlist Generating Please Wait!"+b+yellow)
print (" ")
print (blue+b+"<><><><><><><><><><><><><><><><><><><><><>"+b+blue)
print (" ")
lista=[0 for x in xrange(length)]
x=length-1
string="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
list_of_results=[]
file1=file(name,"w")
while(x>-1):
    result=""
    if lista[x]==len(string)-1:
        for z in xrange (length):
            result+=string[lista[z]]
        lista[x]=0
        x-=1
    elif x==length-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
    else:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
        if x>0:
            x+=1
        else:
            x=length-1
    file1.write(result+"\n")
toc = time.clock()
ttn = toc - tic
print (red+b+"<<<========================================>>>"+b+red)
print (" ")
print (gren+b+"Completed in "+str(ttn)+" seconds."+b+gren)
print (" ")
print (gren+b+"Please check "+str(name)+" in your lazy bee directoy"+b+gren)
print (" ")
print (red+b+"<<<========================================>>>"+b+red)
print (" ")
