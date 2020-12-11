def transform(legacy_data):
    res = {}
    for k, v in legacy_data.items():
        for i in v:
            res[i.lower()] = k
    return res