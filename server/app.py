from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

state_data = None


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
    return {"state": state_data, "info": {}}


@app.post("/step")
def step(input_data: ActionInput):
    global state_data

    if state_data is None:
        reset()

    action = input_data.action

    state_data["step_count"] += 1
    state_data["last_action"] = action
    state_data["status"] = "running"

    done = state_data["step_count"] >= 5

    return {
        "state": state_data,
        "reward": 1.0,
        "done": done,
        "info": {}
    }


@app.get("/state")
def state():
    global state_data

    if state_data is None:
        reset()

    return {"state": state_data}


# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()