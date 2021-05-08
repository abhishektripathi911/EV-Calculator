acwp=int(input("Enter the value of ACWP\n"))
bac=int(input("Enter the value of BAC\n"))
perc_comp=int(input("Enter percentage completed\n"))
perc_actual=int(input("Enter percentage actual\n"))
bcws=((perc_comp/100)*bac)
bcwp=((perc_actual/100)*bac)
cv=bcws-acwp
cpi=bcws/acwp
sv=bcws-bcwp
spi=bcws/bcwp
EAC=acwp+((bac-bcwp)/(cpi*spi))
ETC=EAC-acwp
VAC=bac-EAC
TCPI=((bac-bcwp)/(bac-acwp))
print("BCWS "+str(bcws))
print("BCWP "+str(bcwp))
print("CV "+str(cv))
print("EAC "+str(EAC))
print("ETC "+str(ETC))
print("VAC "+str(VAC))
print("TCPI "+str(TCPI))
if cv<0:
    print("Cost is under budget")
else:
    print("Cost is over-budget")
print("SV "+str(sv))
if sv<0:
    print("Project is behind the schedule")
else:
    print("Project is on Schedule")
print("CPI "+str(cpi))
print("SPI "+str(spi))
if VAC>0:
    print("The Project is expected to finish under budget")
elif VAC==0:
    print("The Project is expected to finish on budget")
else:
    print("The Project is expected to finish over budget")
if TCPI>1:
    print("The Future Efficiency of the Project must be greater than the original plan")
elif TCPI=1:
    print("The Future Efficiency of the Project must be the same as the original plan")
else:
    print("The Future Efficiency of the Project must be greater than the original plan")