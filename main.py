import pandas as pd 
file=input("enter file name\n")
df = pd.read_csv(file)
#beneficiery account number to search for transactions
while True:
    acccount_number=input("enter account number for transaction\n")
    #look for matching beneficiery


    l=[]
    for i in range(len(df['Narration'])):
        if acccount_number in str(df['Narration'][i:i+1]):
            l.append(list(df.loc[i]))
    if len(l)==0:
            print("no data found , enter correct account number")
            option=int(input("enter 0 for exit 3 for continue: "))
            if option==0:
                exit(0)
            
    else:
            
        while True:
            print("1.transactions history\n2.total withdrawal \n3.search another account\nenter 0 for exit")
            option=int(input("select option"))

            if option==1:
                print(l)
            elif option==2:
                total=0
                for amount in l:
                    total+=float(amount[-3])
                print(f"total amount withdrawn: {total}")
            else:
                break
    if option==0:
        exit(0)

                

