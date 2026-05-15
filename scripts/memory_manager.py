import json

PROBLEMS_FILE = "memory/problems_index.json"
TOPIC_FILE = "memory/topic_progress.json"


def load_problems():
    with open(PROBLEMS_FILE, "r") as f:
        return json.load(f)



def save_problems(data):
    with open(PROBLEMS_FILE, "w") as f:
        json.dump(data, f, indent=2)



def load_topic_progress():
    with open(TOPIC_FILE, "r") as f:
        return json.load(f)



def save_topic_progress(data):
    with open(TOPIC_FILE, "w") as f:
        json.dump(data, f, indent=2)