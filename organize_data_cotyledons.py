#cotyledons

# read through all files and append content to the list of lists
#not working yet
def open_file(file_path, label):
   with open(file_path) as f:
      doc= []
      for line in f:
         doc.append(line.strip("\n"))
      label = doc
#open 4 files of the same organ

open_file("./Cotyledons_control_Biological_Replicate_2/quant_comma.sf", "Cotyledons_control_Biological_Replicate_2")

open_file("./Cotyledons_control_Biological_Replicate_1/quant_comma.sf", "Cotyledons_control_Biological_Replicate_1")

open_file("./Cotyledons_cold27_Biological_Replicate_2/quant_comma.sf", "Cotyledons_cold27_Biological_Replicate_2")

open_file("./Cotyledons_cold27_Biological_Replicate_1/quant_comma.sf", "Cotyledons_cold27_Biological_Replicate_1")

#temp

with open("./Cotyledons_control_Biological_Replicate_2/quant_comma.sf") as f:
     Cotyledons_control_Biological_Replicate_2 = []
     for line in f:
             Cotyledons_control_Biological_Replicate_2.append(line.strip("\n"))

with open("./Cotyledons_control_Biological_Replicate_1/quant_comma.sf") as f:
     Cotyledons_control_Biological_Replicate_1 = []
     for line in f:
             Cotyledons_control_Biological_Replicate_1.append(line.strip("\n"))

with open("./Cotyledons_cold27_Biological_Replicate_1/quant_comma.sf") as f:
     Cotyledons_cold27_Biological_Replicate_1 = []
     for line in f:
             Cotyledons_cold27_Biological_Replicate_1.append(line.strip("\n"))

with open("./Cotyledons_cold27_Biological_Replicate_2/quant_comma.sf") as f:
     Cotyledons_cold27_Biological_Replicate_2 = []
     for line in f:
             Cotyledons_cold27_Biological_Replicate_2.append(line.strip("\n"))


#format lists into dictionaries only the names are needed
#x is a list of names from cold27 rep1
x = []
names = []
for a in Cotyledons_cold27_Biological_Replicate_1:
   x.append(a.split(",")[3])
   names.append(a.split(",")[0])

#z is a list of names from cold27 rep2
z = []
for i in Cotyledons_cold27_Biological_Replicate_2:
   z.append(i.split(",")[3])

#y is a list of gene names from control rep1
y = []
for i in Cotyledons_control_Biological_Replicate_1:
   y.append(i.split(",")[3])

v= []
for i in Cotyledons_control_Biological_Replicate_2:
   v.append(i.split(",")[3])
print(" control_1 control_2 cold27_1 cold27_2")
for a,b,c,d,e in zip(names,y,v,x,z):
       print("%s %s %s %s %s" % (a,b,c,d,e))

