subject = {
    "name" : "",
    "level" : "",
    "score" : "",
    "gpa" : 0.0

}
# makes empty list
subjects = []
# gives user input until finished
def get_subjects():
    while True:
        subject["name"] = input("Enter Name: ")
        subject["level"] = int(input("Enter Level: "))
        subject["score"] = int(input("Enter Score: "))
        subjects.append[subject]
        ans = input("Last Subject? (Y/N) ")
        if ans.lower() == "y":
            break
        return subjects

lvl1 = {
    95: 100,
    94: 99,
    93: 98,
    92: 97,
    91: 96,
    90: 95,
    89: 94,
    88: 93,
    87: 92,
    86: 91,
    85: 90,
    84: 89,
    83: 88,
    82: 87,
    81: 86,
    80: 85,
    79: 84,
    78: 83,
    77: 82,
    76: 81,
    75: 80,
    74: 79,
    73: 78,
    72: 77,
    71: 76,
    70: 75
}

def calcWeightedGPA(subject):
    score = subject["score"]
    level = subject["level"]
    if score < 79:
        return 0

def overallAverage():
    pass

def dispScore():
    pass

def main():
    subjects = get_subjects()