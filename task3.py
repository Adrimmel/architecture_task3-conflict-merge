import json


result_json = [{
       "target": "region1.host1.metric_name1",
                     "datapoints": [[123.2323232,1634083200]],    # value, timestamp
}]


result_data = {
    "timestamp": [],
    "host": [],
    "request_type": [],
    "value": []
}

for item in result_json:

    parts = item["target"].split(".")
    host = parts[1]
    request_type = parts[2]


    for datapoint in item["datapoints"]:
        value = datapoint[0]
        timestamp = datapoint[1]

        value_rounded = round(value, 3) #округляем


        result_data["timestamp"].append(timestamp)
        result_data["host"].append(host)
        result_data["request_type"].append(request_type)
        result_data["value"].append(str(value_rounded))  # Преобразуем в строку


print(json.dumps(result_data, indent=4))