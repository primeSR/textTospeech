import json, csv

json_file = 'desc.json'

with open(json_file, "r", encoding='utf-8') as jsf:
  jsf = jsf.read()
  js_reader = json.loads(jsf)


with open('desc.csv',"w", encoding='utf-8') as csf:
  csv_write = csv.writer(csf)
  c = 0
  for cont in js_reader:
    if c == 0:
      header = cont.keys()
      csv_write.writerow(header)
      c+=1
    csv_write.writerow(cont.values())


