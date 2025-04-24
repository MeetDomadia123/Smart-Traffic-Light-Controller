import random

def genrate_traffic_data():
    return{

        'north':random.randint(0,20),
        'south':random.randint(0,20),
        'east':random.randint(0,20),
        'west':random.randint(0,20),
    }


if __name__ == "__main__":
    data = genrate_traffic_data()
    print("Sample Traffic:", data)
