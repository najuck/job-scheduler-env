from env.environment1 import JobSchedulerEnv

env = JobSchedulerEnv()
state = env.reset()

total_reward = 0

for _ in range(50):
    if state["jobs"]:
        action = state["jobs"][0]["id"]
    else:
        break

    state, reward, done, _ = env.step(action)
    total_reward += reward

    if done:
        break

print("Final Score:", total_reward)