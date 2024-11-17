import json

FILENAME = "input.json"

# TODO решите задачу
def task() -> float:
    with open(FILENAME, "r") as f:
        json_data = json.load(f)

    sum_ = 0

    for item in json_data:
        result = item.get("score", 0) * item.get("weight", 0)
        sum_ += result

    return round(sum_, 3)

print(task())

