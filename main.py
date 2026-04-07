import random

# SCENARIOS
scenarios = [
    {
        "id": 1,
        "incident_text": "User reports chest pain.",
        "severity": "high",
        "correct_action": "emergency"
    },
    {
        "id": 2,
        "incident_text": "Fire alarm triggered.",
        "severity": "high",
        "correct_action": "emergency"
    },
    {
        "id": 3,
        "incident_text": "Loud noise outside.",
        "severity": "low",
        "correct_action": "ignore"
    }
]

# PICK RANDOM SCENARIO
scenario = random.choice(scenarios)

print("Incident:", scenario["incident_text"])

# USER ACTION
action = input("Enter action (emergency / ignore): ")

# REWARD LOGIC
reward = 0

if action == scenario["correct_action"]:
    reward += 10
else:
    reward -= 5

print("Reward:", reward)
import random

class VigiNovaEnv:

    def __init__(self):
        self.scenarios = [
            {
                "id": 1,
                "incident_text": "User reports chest pain.",
                "severity": "high",
                "correct_action": "emergency"
            },
            {
                "id": 2,
                "incident_text": "Fire alarm triggered.",
                "severity": "high",
                "correct_action": "emergency"
            },
            {
                "id": 3,
                "incident_text": "Loud noise outside.",
                "severity": "low",
                "correct_action": "ignore"
            }
        ]

    def reset(self):
        self.current = random.choice(self.scenarios)
        return self.current["incident_text"]

    def step(self, action):
        reward = 0

        if action == self.current["correct_action"]:
            reward += 10
        else:
            reward -= 5

        done = True

        return reward, done


# RUN ENVIRONMENT
env = VigiNovaEnv()

obs = env.reset()
print("Incident:", obs)

action = input("Enter action (emergency / ignore): ")

reward, done = env.step(action)

print("Reward:", reward)
{
    "id": 4,
    "incident_text": "Person fainted in school.",
    "severity": "high",
    "correct_action": "emergency"
},
{
    "id": 5,
    "incident_text": "Dog barking loudly at night.",
    "severity": "low",
    "correct_action": "ignore"
}