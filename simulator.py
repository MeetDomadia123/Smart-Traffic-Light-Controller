import matplotlib.pyplot as plt
from traffic_generator import genrate_traffic_data
from fuzzy_controller import get_green_time as fuzzy_green_time
from neural_model import build_and_train_model, predict_green_time
import time

# Train the neural model
model = build_and_train_model()

def simulate_traffic_cycles(cycles=5, use_both=True):
    print("------\n Smart Traffic Simulation \n------")

    fuzzy_times = []
    neural_times = []
    final_times = []

    for i in range(cycles):
        print(f"Cycle {i+1}:")
        traffic_data = genrate_traffic_data()
        print(f"Traffic Data: {traffic_data}")

        # Get Fuzzy Logic time
        total_vehicles = sum(traffic_data.values())
        fuzzy_time = fuzzy_green_time(total_vehicles)
        print(f"Fuzzy Logic Green Time: {fuzzy_time:.2f} sec")

        # Get Neural Network result
        nn_time = predict_green_time(model, traffic_data)
        print(f"Neural Network Green Time: {nn_time:.2f} sec")

        # Final decision (average both)
        if use_both:
            final_time = (fuzzy_time + nn_time) / 2
        else:
            final_time = nn_time
        print(f"Final Green Time: {final_time:.2f} sec")

        print(f" Simulating green light for {final_time:.2f} seconds...\n")
        time.sleep(2)  # Simulate time


        fuzzy_times.append(fuzzy_time)
        neural_times.append(nn_time)
        final_times.append(final_time)


    plot_results(fuzzy_times, neural_times, final_times)

def plot_results(fuzzy_times, neural_times, final_times):
    cycles = range(1, len(final_times) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(cycles, fuzzy_times, marker='o', label='Fuzzy Logic Time', color='blue')
    plt.plot(cycles, neural_times, marker='s', label='Neural Network Time', color='black')
    plt.plot(cycles, final_times, marker='^', label='Final Green Time', color='green')

    plt.title('Green Time per Cycle')
    plt.xlabel('Cycle Number')
    plt.ylabel('Green Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("green_time_plot.png") 
    plt.show()

if __name__ == "__main__":
    simulate_traffic_cycles(cycles=5, use_both=True)
