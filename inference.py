class Inference:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "step_count": 0,
            "status": "reset"
        }
        return self.state

    def step(self, action: int):
        self.state["step_count"] += 1
        self.state["last_action"] = action

        done = self.state["step_count"] >= 5

        return self.state, 1, done, {"info": "ok"}

    def state(self):
        return self.state