import json

json_file = 'report.json'

report = [{"id": 2,"value": "passed"}, 
    {"id": 41,"value": "passed"},
    {"id": 73,"value": "passed"},
    {"id": 110,"value": "failed"},
    {"id": 122,"value": "failed"},
    {"id": 234,"value": "passed"},
    {"id": 238,"value": "passed"},
    {"id": 345,"value": "passed"},
    {"id": 653,"value": "passed"},
    {"id": 690,"value": "failed"},
    {"id": 5321,"value": "passed"},
    {"id": 5322,"value": "failed"}]


res = json.dumps(report, sort_keys=True, indent=4)

with open(json_file, 'w') as f:
    for d in report:
        json.dump(d, f)
        f.write('\n')

