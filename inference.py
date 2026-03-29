class Inference:
    def __init__(self):
        self.state = {"status": "ready"}

    def reset(self):
        self.state = {"status": "reset_done"}
        return self.state

    def step(self, action: int):
        self.state = {
            "action_received": action,
            "status": "running"
        }
        return self.state, 1, False, {"info": "ok"}

    def get_state(self):
        return self.state