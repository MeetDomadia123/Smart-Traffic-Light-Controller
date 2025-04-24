Smart Traffic Light Controller:

**🚦 Overview**

A software-only solution for a smart traffic light controller using Neural Networks and Fuzzy Logic. 
This system simulates traffic flow and adjusts the green light time based on real-time traffic data for each direction (North, South, East, West).

**🧑‍💻 Technologies Used**:<br>
  Python<br>
  Neural Networks (TensorFlow)<br>
  Fuzzy Logic (scikit-fuzzy)<br>
  Matplotlib (for graphing)<br>
  VS Code (IDE)<br>
  Git (for version control)<br>

**🔧 How It Works**
  Traffic Generation: Random traffic data is generated for each direction.

  Fuzzy Logic Controller: The green light time is calculated based on predefined rules, considering the total number of vehicles in all directions.

  Neural Network Model: The model predicts the optimal green light time based on historical traffic data and the current traffic situation.

  Hybrid Decision: The final green light time is calculated as an average of the fuzzy logic output and neural network prediction.

  Simulation: The system simulates green light durations for several cycles and prints the results.

