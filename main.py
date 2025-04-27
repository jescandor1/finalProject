import json
import scheduler

sample_data = [
    {"name": "Analytical Geometry and Calculus 1", "id": "MAC 2311", "periods": (
        ["M3", "W3", "F3"],
        ["M4", "W4", "F4"],
        ["M5", "W5", "F5"]
    ), "credits": 4},
    {"name": "Analytical Geometry and Calculus 2", "id": "MAC 2312", "periods": (
        ["M2", "W2", "F2"],
        ["M6", "W6", "F6"],
        ["M8", "W8", "F8"]
    ), "credits": 4},
    {"name": "Introduction to Computational Mathematics", "id": "MAD 2502", "periods": (
        ["M5", "W5", "F5"],
        ["M6", "W6", "F6"]
    ), "credits": 3},
    {"name": "Introduction to Programming", "id": "COP 3502", "periods": (
        ["M6", "W6", "F6"],
        ["M8", "W8", "F8"]
    ), "credits": 3},
    {"name": "Programming Fundamentals 1 Lab", "id": "COP 3502L", "periods": (
        ["T7"],
        ["R7"]
    ), "credits": 1},
    {"name": "Programming Fundamentals 2", "id": "COP 3503", "periods": (
        ["M7", "W7", "F7"],
        ["M8", "W8", "F8"]
    ), "credits": 3},
    {"name": "Introduction to Statistics 1", "id": "STA 2023", "periods": (
        ["T3", "R3"],
        ["T4", "R4"]
    ), "credits": 3},
    {"name": "Introduction to Statistics 2", "id": "STA 3024", "periods": (
        ["M2", "W2", "F2"],
        ["M5", "W5", "F5"]
    ), "credits": 3},
    {"name": "Statistical Learning", "id": "STA 4210", "periods": (
        ["T5", "R5"],
        ["M7", "W7", "F7"]
    ), "credits": 3},
    {"name": "Data Science Capstone", "id": "STA 4930", "periods": (
        ["W7"],
        ["F5"]
    ), "credits": 3},
    {"name": "Data Structures and Algorithms 1", "id": "COT 3100", "periods": (
        ["M8", "W8", "F8"],
        ["M7", "W7", "F7"]
    ), "credits": 3},
    {"name": "Linear Algebra", "id": "MAS 3114", "periods": (
        ["M5", "W5", "F5"],
        ["M6", "W6", "F6"]
    ), "credits": 3},
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
    print("Here are all of the loaded courses:")
    for course in courses:
        print(course)

    print("Here are all of the loaded courses:")
    for course in scheduler.Course.get_schedule(courses):
        print(course)

if __name__ == '__main__':
    main()