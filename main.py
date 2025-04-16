import json

sample_data = [
    {"name": "Computational Math", "id": "MAD 2502", "periods": [1, 2, 3], "credits": 3},
]
#writes json file
with open("data.json", "w") as f:
    json.dump(sample_data, f, indent=4)


def main():
    filename = "data.json"

    with open(filename, "r") as infile:
        data = json.load(infile)

    # print test
    for record in data:
        name = record.get("name", "N/A")
        student_id = record.get("id", "N/A")
        periods = record.get("periods", [])
        credit = record.get("credits", "N/A")

        print(f"Name: {name}")
        print(f"ID: {student_id}")
        print(f"Periods: {periods}")
        print(f"Credits: {credit}")


if __name__ == '__main__':
    main()