#!/usr/bin/env python3
import json


def load_and_deserialize(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def serialize_and_save_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)
