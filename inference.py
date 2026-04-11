import os
import requests
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:7860")
MODEL_NAME = os.getenv("MODEL_NAME", "job-scheduler-env")
HF_TOKEN = os.getenv("HF_TOKEN")

# OpenAI client (for requirement)
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run():
    print("START")

    # Reset environment
    res = requests.post(f"{API_BASE_URL}/reset")
    state = res.json()

    total_reward = 0

    for step_num in range(50):
        jobs = state.get("jobs", [])
        if not jobs:
            break

        action = jobs[0]["id"]

        res = requests.post(f"{API_BASE_URL}/step", json={"action": action})
        data = res.json()

        state = data["state"]
        reward = data["reward"]
        done = data["done"]

        total_reward += reward

        print(f"STEP {step_num} reward={reward}")

        if done:
            break

    print("END")
    print("Final Score:", total_reward)


if __name__ == "__main__":
    run()