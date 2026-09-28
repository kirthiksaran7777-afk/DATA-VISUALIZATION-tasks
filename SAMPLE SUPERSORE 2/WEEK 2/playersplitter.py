def splitter(mapped_data):
    split_data = []

    for key,value in mapped_data:
            split_data.append((key, value))

    return split_data