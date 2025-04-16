import json

sample_data = [
    {"name": "Computational Math", "id": "MAD 2502", "periods": [1, 2, 3], "credits": 3},
]

# Write the data to a JSON file with indentation for readability
with open('data.json', 'w') as f:
    json.dump(sample_data, f, indent=4)
