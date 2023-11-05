from project import Project

def load_projects_from_file(filename="projects.txt"):
    projects = []
    with open(filename, "r") as f:
        headers = f.readline()  # Skip the header line
        for line in f:
            name, start_date, priority, estimate, completion = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, estimate, completion))
    return projects

def display_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)add new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def display_projects(projects, completed=False):
    for project in projects:
        if (project.completion == 100) == completed:
            project.display()

def main():
    projects = load_projects_from_file()
    while True:
        display_menu()
        choice = input(">>> ").lower()
        
        if choice == "d":
            print("Incomplete projects: ")
            display_projects(projects, False)
            print("Completed projects: ")
            display_projects(projects, True)
        elif choice == "a":
            name = input("Let's add a new project\nName: ")
            start_date = input("Start date (dd/mm/yy): ")
            priority = input("Priority: ")
            estimate = input("Cost estimate: $")
            completion = input("Percent complete: ")
            projects.append(Project(name, start_date, priority, estimate, completion))
        elif choice == "u":
            for i, project in enumerate(projects):
                print(f"{i} ", end="")
                project.display()
            project_choice = int(input("Project choice: "))
            new_percentage = int(input("New Percentage: "))
            projects[project_choice].completion = new_percentage
            new_priority = int(input("New Priority: "))
            projects[project_choice].priority = new_priority
        elif choice == "f":
            filter_date = input("Show projects that start after date (dd/mm/yy): ")
            for project in projects:
                if project.start_date > filter_date:
                    project.display()
        elif choice == "q":
            print("Thank you for using custom-built project management software.")
            break

if __name__ == "__main__":
    main()
