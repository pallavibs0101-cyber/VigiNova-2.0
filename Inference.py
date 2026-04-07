import random

# simple simulation using your logic

scenarios = [
    {"text": "User reports chest pain", "correct": "emergency"},
    {"text": "Fire alarm triggered", "correct": "emergency"},
    {"text": "Loud noise outside", "correct": "ignore"}
]

def run():
    total = 0
    correct_count = 0

    print("[START] Running VigiNova inference")

    for i, s in enumerate(scenarios):
        action = random.choice(["emergency", "ignore"])

        if action == s["correct"]:
            reward = 1.0
            correct_count += 1
        else:
            reward = 0.0

        print(f"[STEP] {i+1} | action={action} | reward={reward}")
        total += reward

    score = total / len(scenarios)

    print(f"[END] score={score}")

if __name__ == "__main__":
    run()
