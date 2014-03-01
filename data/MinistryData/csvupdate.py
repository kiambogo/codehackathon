

f_in = open("MinistryData.csv","r")

f_out = open("MinistryDataNew.csv","w")

headers = f_in.readline().strip().split(',')



b = {'SO1': "Personnel", 'SO2': "Transportation and Communications", 'SO3': "Information", 'SO4': "Professional and Special Services", 'SO5': "Rentals", 'SO6': "Repair and Maintenance", 'SO7': "Utilities, Materials and Supplies", 'SO8': "Acquisition of Land, Buildings and Works", 'SO9': "Acquistion of Machinery and Equipment", 'SO10': "Transfer Payments", 'SO11': "Public Debt Charges", 'SO12': "Other Subsidies and Payments"}
for line in f_in:
	l = line.strip().split(',')
	for x in range (2, 13):
		output = [];
		if( int(l[x]) > 0):
			f_out.write(l[0].strip() + ",")
			f_out.write(l[1].strip() + ",")
			f_out.write(b.get(headers[x]) + ",")
			f_out.write(str(int(l[x]) * 1000) + "\n")

f_in.close()
f_out.close()


