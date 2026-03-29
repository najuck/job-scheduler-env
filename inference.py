class Inference:
    def __init__(self):
        self.state = None

    def reset(self):
        self.state = {
            "step_count": 0,
            "last_action": -1,
            "status": "reset"
        }
        return self.state

    def step(self, action: int):
        if self.state is None:
            return self.reset(), 0, False, {"error": "not reset"}

        self.state["step_count"] += 1
        self.state["last_action"] = action
        self.state["status"] = "running"

        done = self.state["step_count"] >= 5
        reward = 1

        return self.state, reward, done, {}

    def get_state(self):
        return self.state


# ✅ REQUIRED GLOBAL OBJECT
model = Inference()


# ✅ REQUIRED ENTRY FUNCTION FOR OPENENV
def predict(input_data):
    return model.reset()