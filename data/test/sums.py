import json
import csv

linecount = 0;

mine_sum = 0;
dept_sum = 0;
item_sum = 0;

mine_names = {};
dept_names = {};
item_names = {};

dept_children = {};
item_children = {};


input_file = csv.DictReader(open("testdata.csv"))

for row in input_file:
	encoded = json.dumps(row)
	json_format = json.loads(encoded)
	for key, value in json_format.iteritems():
		print "NEWLINE -- ", key, value 
		if (json_format.get('Ministry') in mine_names): #mine already exists
			if (json_format.get('Department') in mine_names[json_format.get('Ministry')]): #dept already exists
				if (json_format.get('Item') in (mine_names[json_format.get('Ministry')])[json_format.get('Department')]): #item already exists
					print "adding existing item in dept:", json_format.get('Department')
					((mine_names[json_format.get('Ministry')])[json_format.get('Department')])['sum'] += int(json_format.get('Value')) #increase the sum for the existing item
				else:
					print "adding new item for dept:", json_format.get('Department')
					((mine_names[json_format.get('Ministry')])[json_format.get('Department')])['item'] = json_format.get('Item') #add the item
					((mine_names[json_format.get('Ministry')])[json_format.get('Department')])['sum'] = json_format.get('Value') #add the sum
			else:
				print "adding new department"
				(mine_names.get(json_format.get('Ministry')))[json_format.get('Department')] = {
					json_format.get('Item'): json_format.get('Value')
				}
		else :
			print "adding new ministry"
			mine_names[json_format.get('Ministry')] = {
				'sum': json_format.get('Value'),
				json_format.get('Department'): {
					json_format.get('Item'): json_format.get('Value')
				}
			} #create hashmap for mine
			break

print mine_names.items()