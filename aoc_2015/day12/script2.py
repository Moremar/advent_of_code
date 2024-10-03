import json


def process(json_obj):
    if type(json_obj) is int:
        return json_obj
    elif type(json_obj) is str:
        return 0
    elif type(json_obj) is list:
        return sum([process(sub_json_obj) for sub_json_obj in json_obj])
    elif type(json_obj) is dict:
        if "red" in json_obj.values():
            return 0
        else:
            return sum([process(sub_json_obj) for sub_json_obj in json_obj.values()])
    else:
        raise ValueError("Unknown type: ", type(json_obj))


def solve(obj):
    return process(obj)


def parse(file_name):
    with open(file_name, "r") as f:
        return json.loads(f.readline().strip())


if __name__ == '__main__':
    print(solve(parse("data.txt")))
