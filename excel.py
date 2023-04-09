import pandas as pd
import seaborn as sns
import matplotlib.pyplot as mlp
print('---------------------'*8)
##print('Enter this type of path')
print(str('Enter this type path:  C:/users/sonu/downloads/insurance.xlsx'))
print('---------------------'*8)
b=input('Enter a path: ')
df=pd.read_excel(b)
print('Your file is')
print('---------------------'*8)
print(df)
print('---------------------'*8)
print('The columns are:  ',df.keys())
for a in df:
    print('---------------------'*8)
    print('Enter 1 to show barplot')
    print('Enter 2 to show graph')
    print('Enter 3 to show piechart')
    print('Enter 4 to show X-Y dependent and independent graph')
    print('---------------------'*8)
    c=int(input('Enter your choice '))
    print('---------------------'*8)
    print('The columns are:    ',df.keys())
    print('---------------------'*8)
    if c == 1:
        d = input('Enter a Column to show Bar ')
        f= df[d].value_counts().values
        sns.barplot(y=df[d].value_counts().values,x=df[d].value_counts().index,hue=f)
        mlp.rcParams["figure.figsize"]=(50,50)
        mlp.xticks(rotation=45,fontsize=10)
        mlp.yticks(rotation=45,fontsize=10)
        print(mlp.show())
        print('---------------------'*8)
        z=int(input('Enter 1 to continue with same link '))
        print('---------------------'*8)
        if z==1:
            continue
        else:
            print('Exit run again for new path.')
            break
    elif c == 2:
        print('Note: This is only for Numeric(123) column, not character(xyz) column. ')
        d = input('Enter x-axis to show line  ')
        g = input('Enter y-axis to show line  ')
        print('---------------------'*8)
        print(df.shape)
        print('row | column')
        z=int(input('Enter number of rows. '))
        print('---------------------'*8)
        sns.lineplot(x=df[d].head(z),y=df[g].head(z),ci=None)
        mlp.rcParams["figure.figsize"]=(50,50)
        mlp.xticks(rotation=45,fontsize=10)
        mlp.yticks(rotation=45,fontsize=10)
        print(mlp.show())
        print('---------------------'*8)
        z=int(input('Enter 1 to continue with same link '))
        print('---------------------'*8)
        if z==1:
            continue
        else:
            print('Exit run again for new path.')
            break
    elif c==3:
        a=input('Enter a column to create a piechart ')
        d=sns.color_palette("tab10")
        e=df[a].value_counts().values
        f=df[a].value_counts().index
        mlp.pie(e,colors=d,labels=f,autopct='%.0f%%',textprops={'fontsize': 8})
        # mlp.rcParams['font.size']=8\
        labels = [f'{l}, {s:0.1f}' for l, s in zip(f, e)]
        # mlp.rcParams['font.size']=8\
        mlp.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
        print(mlp.show())
        print('---------------------'*8)
        z=int(input('Enter 1 to continue with same link '))
        print('---------------------'*8)
        if z==1:
            continue
        else:
            print('Exit run again for new path.')
            break
    elif c==4:
        print('Note: This is only for Numeric(123) column, not Character(xyz) column. ')
        d =input('Enter x-axis to show line')
        e=input('Enter y-axis to show line')
        sns.jointplot(y=df[e],x=df[d],kind="hist")
        mlp.rcParams["figure.figsize"]=(50,50)
        mlp.xticks(rotation=45,fontsize=10)
        mlp.yticks(rotation=45,fontsize=10)
        print(mlp.show())
        print('---------------------'*8)
        z=int(input('Enter 1 to continue with same link '))
        print('---------------------'*8)
        if z==1:
            continue
        else:
            print('Exit run again for new path.')
            break
else:
    print('Exit: Run Again.')
















