# Stdlib imports


def group_by(field_name, items):
    result = {}
    for item in items:
        if not item.get(field_name):
            result[item.get(field_name)] = [item]
        else:
            result[item.get(field_name)].append(item)

    return result