import json
import csv

def main():
    # sensor1 id : sensor2 id
    result = {}

    # Read in SensorData1
    sensorData1Map = {}
    with open('SensorData1.csv', 'r') as sensor1:
        csvData = csv.reader(sensor1)
        next(csvData)

        # Check if csv is empty (assuming csv contains headers)
        first = next(csvData, None)
        if first is None:
            print("Sensor Data 1 is empty")
            with open('output.json', 'w') as json_file:
                json.dump(result, json_file, indent=4)
            return
        csvData = [first] + list(csvData)

        # Create hashmap from sensor1 data (latitude, longitude) : id
        for row in csvData:
            key =  ((f"{float(row[1]):.2f}"), f"{float(row[2]):.2f}")
            sensorData1Map[key] = row[0]

    # Read in SensorData2
    with open('SensorData2.json', 'r') as sensor2:
        sensorData2 = json.load(sensor2)

        # Check if json is empty (assuming an empty json is [])
        if not sensorData2:
            with open('output.json', 'w') as jsonFile:
                json.dump(result, jsonFile, indent=4)
            print("Sensor Data 2 is empty")
            return

    # Iterate through sensor2 data and append to result if key matches sensorData1Map key
    for item in sensorData2:
        key = ((f"{float(item['latitude']):.2f}"), f"{float(item['longitude']):.2f}")
        if key in sensorData1Map:
           result[sensorData1Map[key]] = item['id']
    
    # print result to output file
    with open('output.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)
    print("JSON output file updated")
    return

if __name__ == "__main__":
    main()
