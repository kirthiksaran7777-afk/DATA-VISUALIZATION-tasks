def partition(mapped_data):
    partitions = {}

    for key, value in mapped_data:
        if key not in partitions:
            partitions[key] = []
        partitions[key].append(value)

    return partitions