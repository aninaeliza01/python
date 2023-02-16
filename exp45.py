import csv
c_col=['ID','NAME','AGE']
dicd=[{'ID':1,'NAME':'RAOOF','AGE':15},
      {'ID':2,'NAME':'ABINA','AGE':14},
      {'ID':3,'NAME':'AMIL','AGE':16},
      {'ID':4,'NAME':'ARDRA','AGE':16},
      {'ID':5,'NAME':'BINISHA','AGE':14},
      {'ID':6,'NAME':'GAYATRI','AGE':16},
      {'ID':7,'NAME':'DILNA','AGE':15},
      {'ID':8,'NAME':'ANINA','AGE':16},
      {'ID':9,'NAME':'NIVYA','AGE':10},
      {'ID':10,'NAME':'RIMSHA','AGE':18},]
try:
    with open("file.csv","w")as f:
        w=csv.DictWriter(f,fieldnames=c_col)
        w.writeheader()
        for i in dicd:
            w.writerow(i)
except IOError:
    print("input/output error")
d=csv.DictReader(open("file.csv"))
print("CSV file output is:")
for i in d:
    print(i)