from fastapi import FastAPI

app = FastAPI()

state = None


@app.post("/reset")
def reset():
    global state
    state = {
        "step_count": 0,
        "status": "reset"
    }
    return {
        "state": state,
        "reward": 0,
        "done": False,
        "info": "reset_success"
    }


@app.post("/step")
def step(action: int):
    global state

    state["step_count"] += 1
    state["last_action"] = action
    state["status"] = "running"

    done = state["step_count"] >= 5

    return {
        "state": state,
        "reward": 1,
        "done": done,
        "info": "step_success"
    }


@app.get("/state")
def get_state():
    return state