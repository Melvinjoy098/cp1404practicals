import datetime

class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.estimate = float(estimate)
        self.completion = int(completion)

    def display(self):
        print(f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%")


def load_projects_from_file(filename="projects.txt"):
    projects = []
    with open(filename, "r") as f:
        headers = f.readline()  # Skip the header line
        for line in f:
            name, start_date, priority, estimate, completion = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, estimate, completion))
    return projects
