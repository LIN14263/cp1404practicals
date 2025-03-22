import datetime

class Project:
    """
    Represents a project with a name, start date, priority, cost estimate, and completion percentage.
    """

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        if isinstance(start_date, str):
            self.start_date = datetime.datetime.strptime(start_date.strip(), "%d/%m/%Y").date()
        else:
            self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def update(self, new_percentage=None, new_priority=None):
        if new_percentage is not None:
            self.completion_percentage = new_percentage
        if new_priority is not None:
            self.priority = new_priority

    def is_complete(self):
        return self.completion_percentage == 100
