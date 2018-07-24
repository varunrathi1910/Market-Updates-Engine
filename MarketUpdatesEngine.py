from __future__ import division
from time import gmtime, strftime
from operator import itemgetter
from pyfcm import FCMNotification
import random
import pymysql
M=[' lag',' sluggish',' have been slow-moving',' have been weary',' trending flat',' are tedious',' have been lackluster',' are dull',' show no movement',\
    ' are bullish',' escalate',' climb','leaped','jumped','soar high','rise','advance','are surging', 'have skyrocketed',' are bullish',\
    ' sink',' tank',' fall',' take a nosedive',' take a plunge',' tumble',' have plummetted',' are slippery','topple',' stagger along','slide','collapse',' have tripped','skid',' slip', 'bearish']
P=[' lags',' sluggish',' moves slowly',' weary',' trends flat',' is tedious',' lackluster',' dull',' show no movement',\
   ' is bullish',' escalates',' climbs','leaps','jumps','soars high','rises','advances',' surges',' skyrockets',' is bullish',\
   ' sinks',' tanks',' falls',' takes a nosedive',' takes a plunge',' tumbles',' plummets',' staggers along','slides','collapses', 'skids',' slips', 'bearish']
conn = pymysql.connect(host='Enter hostname', port=Enter portname, user='Enter username', passwd='Enter your password', db='Enter database name')
cur = conn.cursor()
cur.execute("""select id,name,fcm from user""")
MainData=cur.fetchall()
MainList=list(list(i) for i in MainData)
for j in MainList:
    userid=int(j[0]);
    registration_id = j[2]
    message_title = "Market Updates"
    pv1=0;pv2=0;sectname='';MaxSector='';mvcount=0;mv=0;pMax=0;
    query = """select * from Portfolio where userid=%s"""
    cur.execute(query,userid)
    data=cur.fetchall()
    PortFolio=list(data)
    Portfolio=[list(i) for i in PortFolio]
    for i in Portfolio:
        i.pop()
        i.pop()
        i.pop(0)
        i.pop(0)
    NumStock=map(itemgetter(2),Portfolio)#list containing number of stocks
    PriceStock=map(itemgetter(1),Portfolio)#list containing price of stocks
    for i in range(0,len(NumStock)) :
           pv1+=NumStock[i]*PriceStock[i]#Calculating portfolio value
    sum2=0       
    for i in Portfolio:
        query="""select * from stock_data where ticker=%s"""
        cur.execute(query,i[0])
        data =cur.fetchone()
        sum2=float(data[1])
        pv2+=sum2*i[2]
    if(pv1==0):
        pv=0
    else:       
        pv=((pv2-pv1)/pv1)*100
    """
    Portfolio=[[Name of company,Price of stocks,Number of Stocks,Sector]]
    """
    query="""select * from index_data"""
    cur.execute(query)
    data=cur.fetchall()
    for i in data :
            pchange=float(i[2])
            sectname=i[4]
            if(pchange>pMax):
                    pMax=pchange
                    MaxSector=sectname
            else :
                pass
            mv+=pchange
            mvcount+=1
          
    mv=mv/mvcount
    imv=pMax
    if (mv>2 and pv>2 and imv>2) :
                    """print market string,portfolio string and the interested  market string"""
                    stmta = random.choice(M[9:20])
                    stmtb = random.choice(P[9:20])
                    stmtc = random.choice(M[9:20])
                    while stmtc in (stmta):
                            stmtc=random.choice(M[9:20])
                    finalstring= "Markets",stmta,". Up by ",mv,"% .Portfolio",stmtb,".Up by ",pv,"%.",MaxSector,"stocks",stmtc,". Up by ",imv,"%."
    elif (mv>2 and pv>2 and (-2<=imv<=2)):
                    """print market string,portfolio string """
                    stmta = random.choice(M[9:20])
                    stmtb = random.choice(P[9:20])
                    finalstring= "Markets",stmta,". Up by ",mv,"% .Portfolio",stmtb,".Up by ",pv,"%."
    elif (mv>2 and pv>2 and imv<-2):
                    """print market string,portfolio string and the interested  market string"""
                    stmta = random.choice(M[9:20])
                    stmtb = random.choice(P[9:20])
                    stmtc = random.choice(M[20:35])
                    finalstring= "Markets",stmta,". Up by ",mv,"% .Portfolio",stmtb,".Up by ",pv,"%.",MaxSector,"stocks",stmtc,". Down by ",-imv,"%."
    elif (mv>2 and (-2<=pv<=2) and imv>2):
                    """print market string and the interested market string"""
                    stmta = random.choice(M[9:20])
                    stmtc = random.choice(M[9:20])
                    while (stmtc==stmta):
                            stmtc=random.choice(M[9:20])
                    finalstring= "Markets",stmta,". Up by ",mv,"% .",MaxSector,"stocks",stmtc,". Up by ",imv,"%."
    elif (mv>2 and (-2<=pv<=2) and (-2<=imv<=2)):
                    """print market string and the interested market string"""
                    stmta = random.choice(M[9:20])
                    stmtc = random.choice(M[0:9])
                    finalstring= "Markets",stmta,". Up by ",mv,"% .",MaxSector,"stocks",stmtc,"."
    elif (mv>2 and (-2<=pv<=2) and imv<-2):
                    """print market string and the interested market string"""
                    stmta = random.choice(M[9:20])
                    stmtb = random.choice(M[20:35])
                    finalstring= "Markets",stmta,". Up by ",mv,"% .",MaxSector,"stocks",stmtb,". Down by ",-imv,"%."
    elif (mv>2 and pv<-2 and imv>2):
                    """print market string,portfolio string and the interested market string"""
                    stmta = random.choice(M[9:20])
                    stmtb = random.choice(P[20:35])
                    stmtc = random.choice(M[9:20])
                    while (stmtc==stmta):
                            stmtc=random.choice(M[9:20])
                    finalstring= "Markets",stmta,". Up by ",mv,"% .Portfolio",stmtb,".Down by ",-pv,"%.",MaxSector,"stocks",stmtc,". Up by ",imv,"%."
    elif (mv>2 and pv<-2 and (-2<=imv<=2)):
                    """print market string,portfolio string and the surge string"""
                    stmta = random.choice(M[9:20])
                    stmtb = random.choice(P[20:35])
                    finalstring= "Markets",stmta,". Up by ",mv,"% .Portfolio",stmtb,".Down by ",-pv,"%."
    elif (mv>2 and pv<-2 and imv<-2):
                    """print market string,portfolio string and the interested market string"""
                    stmta = random.choice(M[9:20])
                    stmtb = random.choice(P[20:35])
                    stmtc = random.choice(M[20:35])
                    while (stmtc==stmtb):
                            stmtc=random.choice(M[20:35])
                    finalstring= "Markets",stmta,". Up by ",mv,"% .Portfolio",stmtb,".Down by ",-pv,"%.",MaxSector,"stocks",stmtc,". Down by ",-imv,"%."
    elif((-2<=mv<=2) and pv>2 and imv>2):
                    """print portfolio string and the interested market string"""
                    stmtb = random.choice(P[9:20])
                    stmtc = random.choice(M[9:20])
                    while (stmtc==stmtb):
                            stmtc=random.choice(M[9:20])
                    finalstring= "Portfolio",stmtb,".Up by ",pv,"%.",MaxSector,"stocks",stmtc,". Up by ",imv,"%."            
    elif((-2<=mv<=2) and pv>2 and (-2<=imv<=2)):
                    """print portfolio string and the interested market string"""
                    stmtb = random.choice(P[9:20])
                    stmtc = random.choice(M[0:9])
                    finalstring= "Portfolio",stmtb,".Up by ",pv,"%.",MaxSector,"stocks",stmtc,"."            
    elif((-2<=mv<=2) and pv>2 and imv<-2):
                    """print market string,portfolio string and the surge string"""
                    stmta=random.choice(M[0:9])
                    stmtb=random.choice(P[9:20])
                    finalstring= "Market is",stmta,". Portfolio",stmtb,".Up by ",pv,"%."
    elif((-2<=mv<=2) and (-2<=pv<=2) and imv>2):
                    """print interested market string  and the surge string"""
                    stmtb = random.choice(M[9:20])
                    finalstring= MaxSector,"stocks",stmtb,".Up by ",imv,"%."
    elif((-2<=mv<=2) and (-2<=pv<=2) and (-2<=imv<=2)):
                    """print market string,portfolio string,interested market string  and the surge string"""
                    stmta=random.choice(M[0:9])
                    stmtb=random.choice(P[0:9])
                    while(stmta==stmtb):
                            stmtb=random.choice(P[0:9])
                    stmtd=random.choice(M[0:9])
                    while stmtd in (stmta,stmtb):
                        stmtd=random.choice(M[0:9])
                    finalstring= "Markets",stmta,". Portfolio",stmtb,".",MaxSector,"stocks",stmtd          
    elif((-2<=mv<=2) and (-2<=pv<=2) and imv<-2):
                    """print market string,portfolio string,interested market string  and the surge string"""
                    stmta=random.choice(M[0:9])
                    stmtb=random.choice(P[0:9])
                    while(stmta==stmtb):
                            stmtb=random.choice(P[0:9])
                    stmtd=random.choice(M[20:35])
                    finalstring= "Markets",stmta,". Portfolio",stmtb,".",MaxSector,"stocks",stmtd,".Down by",-imv
    elif((-2<=mv<=2) and pv<-2 and imv>2):
                    """print portfolio string, interested market string and the surge string"""
                    stmtb=random.choice(P[20:33])
                    stmtd=random.choice(M[9:19])
                    finalstring= " Portfolio",stmtb,". Down by",-pv,"%.",MaxSector,"stocks",stmtd,". Up by ",imv,"%. "
    elif((-2<=mv<=2) and pv<-2 and (-2<=imv<=2)):
                    """print market string and portfolio string"""
                    stmta=random.choice(M[0:8])
                    stmtb=random.choice(P[20:33])
                    finalstring= "Markets",stmta,".Portfolio",stmtb,".Down by ",-pv,"%." 
    elif((-2<=mv<=2) and pv<-2 and imv<-2):
                    """print portfolio string and the interested market string"""
                    stmta=random.choice(P[20:33])
                    stmtb=random.choice(M[29:35])
                    while(stmta==stmtb):
                            stmtb=random.choice(M[20:35])
                    finalstring= "Portfolio",stmta,"Down by ",-pv,"%.",MaxSector,"stocks",stmtb,".Down by ",-imv,"%"
    elif(mv<-2 and pv>2 and imv>2):
                    """print market string,portfolio string and the interested  market string"""
                    stmta = random.choice(M[20:35])
                    stmtb = random.choice(P[9:20])
                    stmtc = random.choice(M[9:20])
                    while stmtc in (stmta):
                            stmtc=random.choice(M[9:20])
                    finalstring= "Markets",stmta,".Down by ",-mv,"% .Portfolio",stmtb,".Up by ",pv,"%.",MaxSector,"stocks",stmtc,". Up by ",imv,"%."
    elif(mv<-2 and pv>2 and (-2<=imv<=2)):
                    """print market string,portfolio string and the interested  market string"""
                    stmta = random.choice(M[20:35])
                    stmtb = random.choice(P[9:20])
                    finalstring= "Markets",stmta,".Down by ",-mv,"% .Portfolio",stmtb,".Up by ",pv,"%."
    elif(mv<-2 and pv>2 and imv<-2):
                    """print market string,portfolio string """
                    stmta=random.choice(M[20:32])
                    stmtb=random.choice(P[9:20])
                    finalstring= "Markets",stmta,". Down by ",-mv,"%.Portfolio is ",stmtb,".Up by ",pv,"%."
    elif(mv<-2 and (-2<=pv<=2) and imv>2):
                    """print market string,portfolio string and the interested  market string"""
                    stmta = random.choice(M[20:35])
                    stmtb = random.choice(P[0:9])
                    stmtc = random.choice(M[9:20])
                    finalstring= "Markets",stmta,".Down by ",-mv,"% .",MaxSector,"stocks",stmtc,". Up by ",imv,"%."
    elif((mv<-2 and (-2<=pv<=2) and (-2<=imv<=2)) or (mv<-2 and (-2<=pv<=2) and imv<-2)):
                    """print market string,portfolio string """
                    stmta=random.choice(M[19:32])
                    stmtb=random.choice(P[0:9])
                    finalstring= "Markets",stmta,". Down by ",-mv,"%.Portfolio is ",stmtb

    elif((mv<-2 and pv<-2 and imv>2) or (mv<-2 and pv<-2 and (-2<=imv<=2))):
                    """print market string,portfolio string """
                    stmta=random.choice(M[20:35])
                    stmtb=random.choice(P[20:33])
                    finalstring= "Markets",stmta,". Down by ",-mv,"%.Portfolio is ",stmtb,".Down by",-pv,"%."

    elif(mv<-2 and pv<-2 and imv<-2):
                    """print market string,portfolio string and the interested  market string"""
                    stmta = random.choice(M[20:35])
                    stmtb = random.choice(P[20:33])
                    while stmtb in (stmta):
                            stmtb=random.choice(P[9:20])                
                    stmtc = random.choice(M[20:35])
                    while stmtc in (stmta,stmtb):
                            stmtc=random.choice(M[9:20])
                    finalstring= "Markets",stmta,".Down by ",-mv,"% .Portfolio",stmtb,".Down by ",-pv,"%.",MaxSector,"stocks",stmtc,".Down by ",-imv,"%."
    else :
                    pass
                    #Insert code to remove the second and third row  from the table

    message_body=finalstring
    push_service = FCMNotification(api_key="Enter you API KEY here")
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    print'Result:',result
    print finalstring
conn.commit()
conn.close()
