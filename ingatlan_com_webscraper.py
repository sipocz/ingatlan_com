import requests
from bs4 import  BeautifulSoup
#from google.colab import drive
import time
#drive.mount('/content/drive',force_remount=True)




def querycity(city,pmin=20,pmax=40):
    header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    #print("------------------------------------------------")
    #print("+    ",city.capitalize())
    hnev=ansicode(city).lower()

    prefix="https://ingatlan.com/szukites/"
    url=prefix+"elado+haz+"+hnev+"+"+str(pmin)+"-"+str(pmax)+"-mFt"
    #print(url)
    res=requests.get(url,headers=header)
    #print (res.text)
    soup=BeautifulSoup(res.text,"html.parser")
    #print(soup)
    cardcontainer=soup.find_all("a", class_="listing__thumbnail js-listing-active-area")
    #print(cardcontainer)
    urllista=[]
    pricelist=[]
    for cc in cardcontainer:
        #print(cc['href'])
        urlf=cc["href"]
        urllist=urlf.split("/")
        code=urllist[-1]
        #print(code)
        urllista.append(code)

        #pricecontainer=cc.find_all("div",class_="figFav")
        #pricelist.append(pricecontainer[0]["data-price"])    
    
    
    return(urllista)
 
        
        
def query_all_link(city,querymin=0,querymax=150,querydelta=5):
    allist=[]
    print(city+":",end="")
    prefix="https://ingatlan.com/"
    for i in range(querymin,querymax,querydelta):
        #print(i,i+querydelta)
        allist=allist+querycity(city,pmin=i,pmax=i+querydelta)
        print(".", end="")
    allist=list(set(allist))
    allist=[city,prefix]+allist
    #print("")
    #print(allist)
    return(allist)

    import requests




def formatphonenumber(stri):
    if stri[0]=="0":
        stri="3"+stri[1:]
    if len(stri)<10:
        stri="36"+stri    
    out="+"+stri[0:2]+"-("+stri[2:4]+")-"+stri[4:7]+"-"+stri[7:]
    
    return out

def clearphonenumber(stri):
    out=""
    
    for i in stri:
        if i.isnumeric():
            out=out+i
    return(formatphonenumber(out))


def clearengunit(stri):
    out=""
    
    for i in stri:
        if i in ["0","1","2","3","4","5","6","7","8","9"]:
            out=out+i
    return(out)


def onlynumber(stri):
    out=""
    
    for i in stri:
        if i in [",","0","1","2","3","4","5","6","7","8","9"]:
            out=out+i
    return(out)

def ansicode(sti):
    outstr=""
    for i in sti:
        a=i
        if i=="á":
            a="a"
        if i=="Á":
            a="A"
        if i=="é":
            a="e"
        if i=="É":
            a="E"
        if i=="í":
            a="I"
        if i=="Í":
            a="I"
        if i=="ö":
            a="o"
        if i=="Ö":
            a="O"
        if i=="ő":
            a="o"
        if i=="Ő":
            a="O"
        if i=="ó":
            a="o"
        if i=="Ó":
            a="O"
        if i=="ü":
            a="u"
        if i=="Ü":
            a="u"
        if i=="ú":
            a="u"
        if i=="Ú":
            a="u"
        outstr=outstr+a
    return(outstr)

   
        


def queryallinfo(url):
    header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    res=requests.get(url,headers=header)
    #print (res.text)
    soup=BeautifulSoup(res.text,"html.parser")
    print(soup)
    
   
    
    
    
    agentlist=soup.find_all("div", class_="parameter parameter-area-size")
    
    
   
    hazinfo=soup.find_all("div", title="parameter parameter-area-size")
    print(hazinfo)



def printCSV(fname,arr,mode="a"):
    csvfile=open(fname,mode,encoding="UTF-8")
    for row in arr:
        for ind in row:
            print(ind,end=";",file=csvfile)
        print("",end="\n",file=csvfile)
    csvfile.close()
      

def query_all_info():
    header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    baseurl="https://ingatlan.com/lista/elado+haz?page="
    print("HEHHEHE")
    for i in range(2,40000):
        if i %100 ==0 :
            print(i,end=". \n")
        url=baseurl+str(i)
        #print(url)
        res=requests.get(url,headers=header)
        #print (res)
        soup=BeautifulSoup(res.text,"html.parser")
        
        allinfo=soup.find_all("a","listing__link js-listing-active-area")
        out=[]
        for lin in allinfo:
            
            hrefs=lin["href"]
            city=hrefs.split("/")[1]
            #print(city)
            price=lin.header.div.div.div.div.text
            #print(lin.header.div.text)
            #print(lin.div.div.text)

            areas="None"
            area=lin.find_all("div","listing__parameter listing__data--area-size")
            if len (area)>0:
                areas=area[0].text
            plots="None"

            plot=lin.find_all("div","listing__parameter listing__data--plot-size")
            if len (plot)>0:
                plots=plot[0].text

            room=lin.find_all("div","listing__parameter listing__data--room-count")
            
            rooms="None"
            if len(room)>0:
                rooms=room[0].text

            addr=lin.find_all("div","listing__address")
            
            addrs="None"
            if len(addr)>0:
                addrs=addr[0].text
            out.append([city,hrefs,addrs,price,areas,plots,rooms])
            #print(f"{city};{hrefs};{addrs};{price};{areas};{plots};{rooms}")
        printCSV("c:/ingatlan/ingatlan_com20201031.csv",out,mode="a")

    #return([ar,szoba,meret,telek])

query_all_info()        
            







'''
        try:
            allinfo=soup.find_all("href","parameter parameter-lot-size")
            #print(allinfo)
            size=allinfo[0].find_all("span" )
            #print(type(size))
            lotmm=size[1].text
            telek=clearengunit(lotmm)
        except:
            telek=None
        try:
            allinfo=soup.find_all("div","parameter parameter-room")
            #print(allinfo)
            size=allinfo[0].find_all("span" )
            #print(type(size))
            szoba=size[1].text
            szoba=clearengunit(szoba)
        except:
            szoba=None
        try:
            allinfo=soup.find_all("div","parameter parameter-price")
            #print(allinfo)
            size=allinfo[0].find_all("span" )
            #print(type(size))
            ar=size[1].text
            ar=onlynumber(ar)
        except:
            szoba=None
'''




'''
#hely=open('/content/drive/My Drive/Ingatlan/fokusz.txt','r')
telepuleslista=open("/content/drive/My Drive/Ingatlan/helyisegek10.txt",encoding="utf-8-sig")
hely=[]
for telepules in telepuleslista:
    hely.append(telepules.strip())
telepuleslista.close()
print(hely)




#hely=["Szomor","Gyermely"]
print(hely)
prefix="https://ingatlan.com/"
all_link=[]
database=[]
exportfile="/content/drive/My Drive/Ingatlan/ingatlan_com_links.txt"


printCSV(exportfile,database,"a")    
for lak in hely:
    telepules=lak.strip()
    all_link=[]
    all_link.append(query_all_link(telepules,querymax=150))

    time.sleep(1)
    for link_lista in all_link:
        database=[]
        for data in link_lista[2:]:
            url=prefix+data
            print(url)
            homedata=query_all_info2(url)
            database.append([link_lista[0],url,data]+homedata)
        printCSV(exportfile,database)

#print(database)  

'''

