import os
from playermapper import mapper
from playerpartitioner import partition
from playersorter import sorter
from playerreducer import reducer
from playersplitter import splitter
current_folder = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_folder, "player.txt")

def main():
    mapped = mapper(input_file)

    print("MAP OUTPUT")
    print(mapped)

    split_data = splitter(mapped)
    print("\nSPLITTER OUTPUT")
    print(split_data)

    partitioned = partition(mapped)

    print("\nPARTITION OUTPUT")
    print(partitioned)

    sorted_data = sorter(partitioned)

    print("\nSORT OUTPUT")
    print(sorted_data)

    result = reducer(sorted_data)

    print("\nREDUCE OUTPUT")
    for role, count in result.items():
        print(role, ":", count)

if __name__ == "__main__":
    main()