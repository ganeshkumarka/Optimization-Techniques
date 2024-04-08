class Task:
    def __init__(self, id, duration):
        self.id = id
        self.duration = duration
        self.dependencies = []
        self.earliest_start = 0
        self.latest_start = float('inf')
        self.slack = 0

def cpm(tasks):
    # Calculate earliest start times
    for task in tasks:
        if not task.dependencies:
            task.earliest_start = 0
        else:
            task.earliest_start = max(dep.earliest_start + dep.duration for dep in task.dependencies)

    # Calculate latest start times
    last_task = max(tasks, key=lambda task: task.earliest_start)
    last_task.latest_start = last_task.earliest_start
    for task in reversed(tasks):
        if task != last_task:
            task.latest_start = min(next_task.earliest_start for next_task in task.dependencies) - task.duration

    # Calculate slack time
    for task in tasks:
        task.slack = task.latest_start - task.earliest_start

    # Find critical path
    critical_path = [task.id for task in tasks if task.slack == 0]

    # Calculate project completion time
    project_completion_time = max(task.earliest_start + task.duration for task in tasks)

    return critical_path, project_completion_time

# Example usage
task1 = Task(1, 3)
task2 = Task(2, 4)
task3 = Task(3, 2)
task4 = Task(4, 5)

task2.dependencies = [task1]
task3.dependencies = [task1]
task4.dependencies = [task2, task3]

tasks = [task1, task2, task3, task4]

critical_path, completion_time = cpm(tasks)

print("Critical path:", critical_path)
print("Project completion time:", completion_time)
