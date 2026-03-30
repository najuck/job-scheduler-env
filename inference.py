from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

state_data = {}


class ActionInput(BaseModel):
    action: int


@app.post("/reset")
def reset():
    global state_data
    state_data = {
        "step_count": 0,
        "last_action": -1,
        "status": "reset"
    }
    return state_data


@app.post("/step")
def step(input_data: ActionInput):
    global state_data

    action = input_data.action

    state_data["step_count"] += 1
    state_data["last_action"] = action
    state_data["status"] = "running"

    done = state_data["step_count"] >= 5
    reward = 1

    return {
        "state": state_data,
        "reward": reward,
        "done": done,
        "info": {}
    }


@app.get("/state")
def state():
    return state_data