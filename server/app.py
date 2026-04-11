from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import JobSchedulerEnv
import uvicorn

app = FastAPI()
env = JobSchedulerEnv()


class ActionInput(BaseModel):
    action: int


@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state, "info": {}}


@app.post("/step")
def step(input_data: ActionInput):
    state, reward, done, info = env.step(input_data.action)

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    return {"state": env.state()}


# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()