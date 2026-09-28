def mapper(input_file):
    mapped_data = []
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                player = [field.strip() for field in line.split(",")]
                if len(player) >= 3:
                    role = player[2]
                    mapped_data.append((role, 1))
    except FileNotFoundError:
        raise

    return mapped_data
