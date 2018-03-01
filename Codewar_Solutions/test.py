def openOrSenior(data):
    resulta=[]
    for i in range(len(data)):
        if data[i][0]>54 and data[i][1]>7:
            resulta.append("Senior")
        else:
            resulta.append("Open")
    print(resulta)
    return 
        
data=[[45, 12],[55,21],[19, -2],[104, 20]]
openOrSenior(data)

#test.assert_equals(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]),
#['Open', 'Senior', 'Open', 'Senior'])cls
