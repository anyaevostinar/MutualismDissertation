import os.path
import gzip


treatment_prefixes = ['full_mutualism']

reps = range(51,61)
updates = range(0,50001, 1000)

f = 'data/grid_virulence.'

header = "uid treatment rep update virulence\n"

outputFileName = "munged_virulence"

outFile = open(outputFileName, 'w')
outFile.write(header)



for t in treatment_prefixes:
    for r in reps:
        for u in updates:
            fname = t + "_" + str(r) + "/" +  f+str(u)+".dat"
            uid = t + "_" + str(r)
            curFile = open(fname, 'r')
            sum_nums  =0
            count = 0
            for line in curFile:
                if (len(line) > 1 and line[0] != "#"):
                    splitline = line.split()
                    for num in splitline:
                        sum_nums += float(num)
                        count+=1
            file_avg = sum_nums/count
            outFile.write(uid+" "+t+" "+str(r)+" "+str(u)+" "+str(file_avg)+"\n")
                        
            curFile.close()
            
outFile.close()

