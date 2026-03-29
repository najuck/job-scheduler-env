from fastapi import FastAPI
from inference import Inference

app = FastAPI()
env = Inference()


@app.post("/reset")
def reset():
    return env.reset()   # ✅ MUST return raw state only


@app.post("/step")
def step(action: int):
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    return env.get_state()