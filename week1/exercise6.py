import json
import yaml
import pprint

pp = pprint.PrettyPrinter()

new_list = ['apple', 'orange', {'banana': 'yellow'}, {'grape': ['red', 'purple']}, 'blueberry', {'watermelon': ['green', 'yellow']}]

print new_list
print json.dumps(new_list)

with open("my_file.json", "w") as f:
    json.dump(new_list, f)

with open("my_file.json") as f:
    json_list = json.load(f)

pp.pprint(json_list)

print"---------------------------------------------------------------"

print yaml.dump(new_list, default_flow_style=True)
print yaml.dump(new_list, default_flow_style=False)

with open("my_file.yml", "w") as f:
    f.write(yaml.dump(new_list, default_flow_style=False))

with open("my_file.yml") as f:
    yml_list = yaml.load(f)

pp.pprint(yml_list)





