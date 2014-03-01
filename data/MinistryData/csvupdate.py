

f_in = open("MinistryData.csv","r")

f_out = open("MinistryDataNew.csv","w")

headers = f_in.readline().strip().split(',')



for line in f_in:
	l = line.strip().split(',')
	for x in range (2, 13):
		output = [];
		if( int(l[x]) > 0):
			f_out.write(l[0].strip() + ",")
			f_out.write(l[1].strip() + ",")
			f_out.write(headers[x] + ",")
			f_out.write(str(int(l[x]) * 1000) + "\n")
			#output.append(line[0])
			#output.append(line[1])
			#output.append(headers[x])
			#output.append(str( line[x] )
			#f_out.write(",".join(output))

f_in.close()
f_out.close()


