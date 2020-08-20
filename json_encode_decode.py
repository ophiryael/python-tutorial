import json

initial_obj = {"foo": 1, "bar": 2, "baz": 3}

json_obj = json.dumps(initial_obj)
py_obj = json.loads(json_obj)

print("json:", repr(json_obj))
print("python:", repr(py_obj))
