from fastapi import FastAPI

app = FastAPI()

# Dummy state (replace with your real logic if you have OpenEnv env)
state_data = {"status": "ready"}

@app.post("/reset")
def reset():
    global state_data
    state_data = {"status": "reset_done"}
    return state_data

@app.post("/step")
def step(action: int):
    global state_data
    state_data = {
        "action_received": action,
        "status": "running"
    }
    return {
        "state": state_data,
        "reward": 1,
        "done": False,
        "info": "ok"
    }

@app.get("/state")
def state():
    return state_data