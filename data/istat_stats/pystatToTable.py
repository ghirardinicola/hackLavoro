from pyjstat import pyjstat
from collections import OrderedDict
from pprint import pprint
import urllib2
import json

#dataset_url_1 = 'https://raw.githubusercontent.com/ghirardinicola/hackLavoro/master/italiaRAW2014soloProfessioni.json'
dataset_url_1 = 'https://gist.githubusercontent.com/ghirardinicola/dd2aaa5841f5a5d7e4b3/raw/05854048e9ef2dd33df33db6d7fd335d60918e98/occupatiSTAT.json'

# Important: JSON data must be retrieved in order; 
# this can be accomplished using the object_pairs_hook parameter
# of the json.load method. 
occupati_json_data = json.load(urllib2.urlopen(dataset_url_1),
                      object_pairs_hook=OrderedDict)

#with open('occupati.json') as data_file:    
#    occupati_json_data = json.load(data_file,object_pairs_hook=OrderedDict)

#pprint(occupati_json_data)


#occupati_json_data = json.load(json_data,
#                     object_pairs_hook=OrderedDict)

occupati_results = pyjstat.from_json_stat(occupati_json_data, naming="label")

# Get the first result, since we're using only one input dataset
occupati_dataset = occupati_results[0]

occupati_dataset.to_csv('occupati.csv', sep='\t', encoding='utf-8')

#print occupati_dataset

