def reducer(grouped_data):
    reduced_data = {}

    if hasattr(grouped_data, 'items'):
        iterator = grouped_data.items()
    else:
        iterator = grouped_data

    for key, values in iterator:
        try:
            reduced_data[key] = sum(values)
        except TypeError:
            reduced_data[key] = sum(int(v) for v in values)

    return reduced_data