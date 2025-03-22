"""
using time: 50 minutes
"""

import datetime
from project import Project

def load_projects(filename):
    projects = []
    try:
        with open(filename, "r") as file:
            header = file.readline()
            for line in file:
                if line.strip() == "":
                    continue
                parts = line.strip().split("\t")
                if len(parts) < 5:
                    continue
                name, start_date_str, priority_str, cost_estimate_str, completion_percentage_str = parts
                try:
                    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
                except ValueError:
                    continue
                project = Project(name, start_date, int(priority_str),
                                  float(cost_estimate_str), int(completion_percentage_str))
                projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return projects

def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            date_str = project.start_date.strftime("%d/%m/%Y")
            file.write(f"{project.name}\t{date_str}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    incomplete = [p for p in projects if p.completion_percentage < 100]
    complete = [p for p in projects if p.completion_percentage == 100]

    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")

def filter_projects_by_date(projects):
    date_input = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return

    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(p)

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    date_input = input("Start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Project not added.")
        return
    try:
        priority = int(input("Priority: "))
        cost_estimate_input = input("Cost estimate: ").replace("$", "")
        cost_estimate = float(cost_estimate_input)
        completion_percentage = int(input("Percent complete: "))
    except ValueError:
        print("Invalid numeric input. Project not added.")
        return

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
    except (ValueError, IndexError):
        print("Invalid project choice.")
        return

    print(project)
    new_percentage_str = input("New Percentage: ")
    new_priority_str = input("New Priority: ")

    if new_percentage_str.strip() != "":
        try:
            new_percentage = int(new_percentage_str)
        except ValueError:
            print("Invalid percentage. Keeping old value.")
            new_percentage = project.completion_percentage
    else:
        new_percentage = project.completion_percentage

    if new_priority_str.strip() != "":
        try:
            new_priority = int(new_priority_str)
        except ValueError:
            print("Invalid priority. Keeping old value.")
            new_priority = project.priority
    else:
        new_priority = project.priority

    project.update(new_percentage, new_priority)

def print_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def main():
    projects = load_projects("projects.txt")
    if projects:
        print(f"Loaded {len(projects)} projects from projects.txt")
    else:
        print("No projects loaded.")

    while True:
        print_menu()
        choice = input(">>> ").strip().lower()
        if choice == "l":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save_choice = input("Would you like to save to projects.txt? ").strip().lower()
            if save_choice in ["yes", "y"]:
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()