# imports required modules
from urllib.request import Request, urlopen;
import json;

# counter (e.g. 0 = page 1, 102 = page 2, 204 = page 3, and so on...)
offsetCounter = 0;

# creates empty dictionary to store data in
shoeDictionary = {'Brand':[], 'Name':[], 'Actual Price':[], 'Discounted Price':[], 'Image Link':[], 'Alternate Image Link':[]};

while True:
    # XHR url containing required data
    url = 'https://www.zalora.com.my/_c/v1/desktop/list_catalog_full?url=%2Fwomen%2Fshoes&sort=popularity&dir=desc&offset=' + str(offsetCounter) + '&limit=102&category_id=4&occasion=Casual&brand=87&gender=women&segment=women&special_price=false&all_products=false&new_products=false&top_sellers=false&catalogtype=Main&lang=en&is_brunei=false&search_suggest=false&enable_visual_sort=true&enable_filter_ads=true&compact_catalog_desktop=false&name_search=false&solr7_support=false&pick_for_you=false&learn_to_sort_catalog=false&is_multiple_source=true&enable_similar_term=true';

    # makes a GET request to the url and opens a connection
    request = Request(url, headers={'User-Agent': 'XYZ/3.0'});
    connection = urlopen(request);

    # translates JSON data into a Python dictionary
    jsonData = json.loads(connection.read());

    if len(jsonData['response']['docs']) > 0:
        for i in range(len(jsonData['response']['docs'])): # iterates over entire json object

            shoeDictionary['Brand'].append(jsonData['response']['docs'][i]['meta']['brand']);
            shoeDictionary['Name'].append(jsonData['response']['docs'][i]['meta']['name']);
            shoeDictionary['Actual Price'].append(jsonData['response']['docs'][i]['meta']['price']);
            shoeDictionary['Discounted Price'].append(jsonData['response']['docs'][i]['meta']['special_price']);
            shoeDictionary['Image Link'].append(jsonData['response']['docs'][i]['image']);
            shoeDictionary['Alternate Image Link'].append(jsonData['response']['docs'][i]['image_extra'][0]['url']);

            i = i + 1;
        
        offsetCounter = offsetCounter + 102; # adds 102 to offset counter

        continue;
    else: # if len(jsonData['response']['docs'] = 0, then break the loop
        break;

# writes into json files
with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(shoeDictionary, outfile, ensure_ascii=False, indent=4);

# test
print("Does this mean the script worked?");

# starts application
if __name__ == "__zaloraaldowebscraper__":
    main();