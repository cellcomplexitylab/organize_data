#open 4 files of the same organ

with open("./Young_flower_control_Biological_Replicate_2/quant.sf") as f:
     control_Biological_Replicate_2 = []
     for line in f:
             control_Biological_Replicate_2.append(line.strip("\n"))

with open("./Young_flower_control_Biological_Replicate_1/quant.sf") as f:
     control_Biological_Replicate_1 = []
     for line in f:
             control_Biological_Replicate_1.append(line.strip("\n"))

with open("./Young_flower_cold27_Biological_Replicate_1/quant.sf") as f:
     cold27_Biological_Replicate_1 = []
     for line in f:
             cold27_Biological_Replicate_1.append(line.strip("\n"))

with open("./Young_flower_cold27_Biological_Replicate_2/quant.sf") as f:
     cold27_Biological_Replicate_2 = []
     for line in f:
             cold27_Biological_Replicate_2.append(line.strip("\n"))


#format lists into dictionaries only the names are needed
#x is a list of names from cold27 rep1
x = []
names = []
for a in cold27_Biological_Replicate_1:
   x.append(a.split("\t")[3])
   names.append(a.split("\t")[0])
#z is a list of names from cold27 rep2
z = []
for i in cold27_Biological_Replicate_2:
   z.append(i.split("\t")[3])

#y is a list of gene names from control rep1
y = []
for i in control_Biological_Replicate_1:
   y.append(i.split("\t")[3])

v= []
for i in control_Biological_Replicate_2:
   v.append(i.split("\t")[3])
print(" control_1 control_2 cold27_1 cold27_2")
for a,b,c,d,e in zip(names,y,v,x,z):
       print("%s %s %s %s %s" % (a,b,c,d,e))

