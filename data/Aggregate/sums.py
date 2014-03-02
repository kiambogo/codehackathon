import json
import csv

final_names = {};

input_file = csv.DictReader(open("spending2.csv"))

for row in input_file:
	encoded = json.dumps(row)
	json_format = json.loads(encoded)
	for key, value in json_format.iteritems(): 
		print json_format.get('Value')
		if (json_format.get('Ministry') in final_names): #mine already exists
			if (json_format.get('Department') in final_names[json_format.get('Ministry')]['children']): #dept already exists
				if (json_format.get('Item') in final_names[json_format.get('Ministry')]['children'][json_format.get('Department')]['children']): #item already exists
					(final_names[json_format.get('Ministry')]['children'][json_format.get('Department')]['children'][json_format.get('Item')])['sum'] += int(json_format.get('Value'))
					(final_names[json_format.get('Ministry')]['children'][json_format.get('Department')])['sum'] += int(json_format.get('Value'))
					(final_names[json_format.get('Ministry')]['sum']) += int(json_format.get('Value'))
				else:
					(final_names[json_format.get('Ministry')]['children'][json_format.get('Department')]['children'])[json_format.get('Item')] = {
						'item': json_format.get('Item'),
						'sum': int(json_format.get('Value'))
					}
					(final_names[json_format.get('Ministry')]['children'][json_format.get('Department')])['sum'] += int(json_format.get('Value'))
					(final_names[json_format.get('Ministry')]['sum']) += int(json_format.get('Value'))
					break

			else:
				(final_names[json_format.get('Ministry')]['children'])[json_format.get('Department')] = {
					'department': json_format.get('Department'),
					'sum': int(json_format.get('Value')),
					'children': {
						json_format.get('Item'): {
							'item': json_format.get('Item'),
							'sum': int(json_format.get('Value'))
						}
					}
				}
				(final_names[json_format.get('Ministry')]['sum']) += int(json_format.get('Value'))
				break

		else:
			
			final_names[json_format.get('Ministry')] = {
				'ministry': json_format.get('Ministry'),

				'sum': int(json_format.get('Value')),
				'children': {
					json_format.get('Department'): {
						'department': json_format.get('Department'),
						'sum': int(json_format.get('Value')),
						'children': {
							json_format.get('Item'): {
								'item': json_format.get('Item'),
								'sum': int(json_format.get('Value'))
							}
						}
					}
				}
			}
			break
	
f = open('new.json', 'w')
f.write (json.dumps(final_names, indent=4))