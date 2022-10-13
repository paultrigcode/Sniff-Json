def validate_filepath(filepath):
    if isinstance(filepath, str) and filepath[-5:] == ".json":
        return True
    else:
        raise ValueError("Invalid File type, File must be a json file")


def type_checker(value):
    if value == True or value == False:
        return None
    if isinstance(value, str):
        return "string"
    if isinstance(value, int):
        return "integer"
    if (
        all(isinstance(x, str) for x in value)
        and value != []
        and not isinstance(value, dict)
    ):
        return "enum"
    if isinstance(value, dict):
        return "array"
