import pandas as pd

import csv

from names import names


df=pd.read_csv('december.csv',parse_dates=['Date'],dayfirst=True)

df['Withdrawal Amt.'].fillna(0,inplace=True)


april=df.loc[df['Date'].dt.month==4]
may=df.loc[df['Date'].dt.month==5]
june=df.loc[df['Date'].dt.month==6]
july=df.loc[df['Date'].dt.month==7]
august=df.loc[df['Date'].dt.month==8]
september=df.loc[df['Date'].dt.month==9]
october=df.loc[df['Date'].dt.month==10]
november=df.loc[df['Date'].dt.month==11]
december=df.loc[df['Date'].dt.month==12]




with open('current.csv',mode='a',newline='') as file:

        header=['Name','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Total']

        thewriter = csv.writer(file)

        thewriter.writerow(header)



for name in names:


    apr_tr=april[april['Narration'].str.contains(name,na=False)]
    may_tr=may[may['Narration'].str.contains(name,na=False)]
    jun_tr=june[june['Narration'].str.contains(name,na=False)]
    jul_tr=july[july['Narration'].str.contains(name,na=False)]
    aug_tr=august[august['Narration'].str.contains(name,na=False)]
    sep_tr=september[september['Narration'].str.contains(name,na=False)]
    oct_tr=october[october['Narration'].str.contains(name,na=False)]
    nov_tr=november[november['Narration'].str.contains(name,na=False)]
    dec_tr=december[december['Narration'].str.contains(name,na=False)]

    april_withdrawal=0
    may_withdrawal=0
    june_withdrawal=0
    july_withdrawal=0
    august_withdrawal=0
    september_withdrawal=0
    october_withdrawal=0
    november_withdrawal=0
    december_withdrawal=0


    # months_tr=[apr_tr,may_tr,jun_tr,jul_tr,aug_tr,sep_tr,oct_tr,nov_tr]
    # month_wt=[april_withdrawal,may_withdrawal,june_withdrawal,july_withdrawal,august_withdrawal,september_withdrawal,october_withdrawal,november_withdrawal]

    # for num in range(8):
    #     for amount in months_tr[num].loc[:,'Withdrawal Amt.']:
    #         month_wt[num]+=amount
    #         print(month_wt[num])


            

    for amount in apr_tr.loc[:,'Withdrawal Amt.']:

        april_withdrawal+=amount

    for amount in may_tr.loc[:,'Withdrawal Amt.']:
        
        may_withdrawal+=amount
        

    for amount in jun_tr.loc[:,'Withdrawal Amt.']:

        june_withdrawal+=amount
        
    for amount in jul_tr.loc[:,'Withdrawal Amt.']:

        july_withdrawal+=amount
        
    for amount in aug_tr.loc[:,'Withdrawal Amt.']:

        august_withdrawal+=amount

    for amount in sep_tr.loc[:,'Withdrawal Amt.']:

        september_withdrawal+=amount
        
    for amount in oct_tr.loc[:,'Withdrawal Amt.']:

        october_withdrawal+=amount

    for amount in nov_tr.loc[:,'Withdrawal Amt.']:

        november_withdrawal+=amount
    
    for amount in dec_tr.loc[:,'Withdrawal Amt.']:

        december_withdrawal+=amount


    total_withdrawal=april_withdrawal+may_withdrawal+june_withdrawal+july_withdrawal+august_withdrawal+september_withdrawal+october_withdrawal+november_withdrawal+december_withdrawal


    listdata=[name,april_withdrawal,may_withdrawal,june_withdrawal,july_withdrawal,august_withdrawal,september_withdrawal,october_withdrawal,november_withdrawal,december_withdrawal,total_withdrawal]

    
    with open('current.csv',mode='a',newline='') as file:

        thewriter = csv.writer(file)

        thewriter.writerow(listdata)

