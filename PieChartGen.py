import matplotlib.pyplot as plt
from DataFile import RiskAbility,RiskWillingness
if ((RiskAbility>11 and RiskWillingness>8) or (RiskAbility>11 and 5<=RiskWillingness<=8)):
        #Aggressive
	activities =['Equity','Bonds','Real Estate','Cash/Gold']
	slices=[75,10,15,0]
	cols=['c','y','r','b']
	plt.pie(slices,labels=activities,colors=cols,shadow= True,startangle=90)
	plt.title('Aggressive')
	plt.show()
elif ((RiskWillingness>8 and 8<=RiskAbility<=11)or (RiskAbility>11 and RiskWillingness<5)) :
        #Moderately Aggressive
	activities =['Equity','Bonds','Real Estate','Cash/Gold']
	slices=[60,25,15,0]
	cols=['c','m','r','b']
	plt.pie(slices,labels=activities,colors=cols,shadow= True,startangle=90)
	plt.title('Moderately Aggressive')
	plt.show()
elif ((5<=RiskWillingness<=8 and 8<=RiskAbility<=11)):
        #Moderate
	activities =['Equity','Bonds','Real Estate','Cash/Gold']
	slices=[45,40,10,5]
	cols=['c','y','r','b']
	plt.pie(slices,labels=activities,colors=cols,shadow= True,startangle=90)
	plt.title('Moderate')
	plt.show()
elif ((8<=RiskAbility<=11 and RiskWillingness<5) or (RiskAbility<8 and RiskWillingness>8)):
        #Moderately Conservative
	activities =['Equity','Bonds','Real Estate','Cash/Gold']
	slices=[30,55,5,10]
	cols=['c','y','r','b']
	plt.pie(slices,labels=activities,colors=cols,shadow= True,startangle=90)
	plt.title('Moderately Conservative')
	plt.show()
elif((RiskAbility<8 and RiskWillingness<5) or (RiskAbility<8 and 5<=RiskWillingness<=8)):
        #Conservative
	activities =['Equity','Bonds','Real Estate','Cash/Gold']
	slices=[20,70,0,10]
	cols=['c','y','r','b']
	plt.pie(slices,labels=activities,colors=cols,shadow= True,startangle=90)
	plt.title('Conservative')
	plt.show()
else:
        pass
