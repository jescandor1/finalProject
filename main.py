import json
import scheduler

sample_data = [
    {"name": "Computational Math", "id": "MAD 2502", "periods": ["M1", "W2", "F3"], "credits": 3},
    {"name": "Calculus 3", "id": "MAC 2313", "periods": ["M1", "R2", "F3"], "credits": 4},
    {"name": "Programming With Data in R", "id": "STA 3100", "periods": ["M5", "T7", "W8"], "credits": 3},
    {"name": "Computational Linear Algebra", "id": "MAS 3114", "periods": ["T5", "R5"], "credits": 3}
]
#writes json file
with open("data.json", "w") as f:
    json.dump(sample_data, f, indent=4)

def load_courses(filename):
    """
    Converts data in a json file to Course objects
    :param filename: file to be read and data loaded
    :return: Course objects
    """
    with open(filename, "r") as infile:
        data = json.load(infile)
        courses = [
            scheduler.Course(
                record["name"],
                record["id"],
                record["periods"],
                record["credits"]
            )
            for record in data
        ]
    return courses


def main():
    filename = "data.json"

    courses = load_courses(filename)

    # print test
    for course in courses:
        print(course)
    print(1)
    for course in scheduler.Course.get_schedule(courses):
        print(course)

if __name__ == '__main__':
    main()