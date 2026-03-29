import random

class JobSchedulerEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.time = 0
        self.cpu = 0
        self.jobs = self.generate_jobs()
        return self.state()

    def generate_jobs(self):
        return [
            {"id": i, "load": random.randint(10, 30), "deadline": random.randint(5, 15)}
            for i in range(5)
        ]

    def state(self):
        return {
            "time": self.time,
            "cpu": self.cpu,
            "jobs": self.jobs
        }

    def step(self, action):
        if job:
            self.cpu += job["load"]
            self.jobs.remove(job)
            time_factor = max(0, (job["deadline"] - self.time) / job["deadline"])
            reward += time_factor
            job = next((j for j in self.jobs if j["id"] == action), None)

        if job:
            self.cpu += job["load"]
            self.jobs.remove(job)

            if self.time <= job["deadline"]:
                reward += 1
            else:
                reward -= 0.5

        if self.cpu > 100:
            reward -= 1

        self.time += 1
        done = len(self.jobs) == 0

        return self.state(), reward, done, {}