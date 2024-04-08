class Job:
    def __init__(self, id, duration):
        self.id = id
        self.duration = duration
        self.dependencies = []
        self.earliest_start = 0
        self.earliest_finish = 0
        self.latest_start = float('inf')
        self.latest_finish = float('inf')
        self.slack = 0

def cpm(jobs):
    # Calculate earliest start and finish times
    for job in jobs:
        if not job.dependencies:
            job.earliest_start = 0
            job.earliest_finish = job.duration
        else:
            job.earliest_start = max(dep.earliest_finish for dep in job.dependencies)
            job.earliest_finish = job.earliest_start + job.duration
    
    # Calculate latest start and finish times
    last_job = max(jobs, key=lambda job: job.earliest_finish)
    last_job.latest_finish = last_job.earliest_finish
    last_job.latest_start = last_job.earliest_start
    for job in reversed(jobs):
        if job != last_job:
            job.latest_finish = min(next_job.latest_start for next_job in job.dependencies)
            job.latest_start = job.latest_finish - job.duration
    
    # Calculate slack time
    for job in jobs:
        job.slack = job.latest_start - job.earliest_start
    
    # Find critical path
    critical_path = [job.id for job in jobs if job.slack == 0]
    
    return critical_path

# Example usage
job1 = Job(1, 3)
job2 = Job(2, 4)
job3 = Job(3, 2)
job4 = Job(4, 5)

job2.dependencies = [job1]
job3.dependencies = [job1]
job4.dependencies = [job2, job3]

jobs = [job1, job2, job3, job4]

optimal_sequence = cpm(jobs)
print("Optimal sequence for processing jobs:", optimal_sequence)
