import random
def grade(total_reward):
    return max(0.0, min(1.0, total_reward / 5))
def easy():
    return [{"id": i, "load": 10, "deadline": 15} for i in range(3)]

def medium():
    return [{"id": i, "load": random.randint(10, 30), "deadline": 10} for i in range(6)]

def hard():
    return [{"id": i, "load": random.randint(20, 50), "deadline": 5} for i in range(10)]