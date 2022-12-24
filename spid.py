# This script is meant to maintain a list of (semi-)PID based on URIs of dataset

import json
import hashlib

def get_hash(string):
	sha = hashlib.sha256(string.encode())
	return sha.hexdigest()[:9]

with open("catalog.json") as f:
	data = json.load(f)

with open("id-db.json") as f:
	db = json.load(f)

for key, record in sorted(list(data.items()), key=lambda x: x[1]["url"]):
	if record["url"] not in db["values"]:
		current_id = get_hash(record["url"])
		db["values"][record["url"]] = current_id
		db["ids"][current_id] = record["url"]
		data[key]["_pid"] = current_id
	if "_pid" not in record:
		data[key]["_pid"] = db["values"][record["url"]]

with open("id-db.json", "w") as f:
	json.dump(db, f, indent=2)

with open("catalog.json", "w") as f:
	json.dump(
		{
			record["_pid"]: record
			for _, record in sorted(list(data.items()), key=lambda x: x[1]["url"])
		},
		f,
		indent=2
	)
