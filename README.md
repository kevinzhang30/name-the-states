# Name the States

**Name the States** is a Python-based educational game where players try to fill a U.S. map by correctly naming all 50 states. This game uses the **pandas** library to handle state data efficiently, loading state names and coordinates from a CSV file and saving unguessed states for future learning. Furthermore, the game provides immediate feedback by displaying the correct guesses on a visual map using the turtle graphics library.

## Features
- **Map Visualization**: Players see a map of the U.S., and correctly guessed states appear in their corresponding locations.
- **State Tracking**: The game tracks your progress and shows how many states you've correctly guessed.
- **Efficient Data Handling**: The **pandas** library is used to load data from a CSV file and manage the list of states, making the game scalable and easy to update.
- **Give Up or Exit Option**: Players can give up and reveal all remaining states, or exit and save unguessed states to a CSV file for later study.
- **CSV Integration**: Load state names and coordinates from `50_states.csv`, and save missed states to `states_to_learn.csv` using **pandas** for data handling.

## Libraries Used
- **Pandas**: Handles reading and managing data from CSV files, including loading the state names and coordinates and saving unguessed states.
- **Turtle**: Displays the map and state names on the screen.

## How to Play
1. Run the Python script.
2. The game will prompt you to enter the name of a U.S. state.
3. Correct answers will be displayed on the map in their respective locations.
4. The game ends when:
   - All 50 states are guessed.
   - You give up (type "Give Up"), revealing all remaining states.
   - You exit (type "Exit"), saving the unguessed states in `states_to_learn.csv`.

## Setup Instructions
1. Clone the repository:  
   ```bash
   git clone https://github.com/kevinzhang30/NameTheStates.git
   ```
2. Install the required libraries:
   ```bash
   pip install pandas turtle
   ```
3. Ensure you have a CSV file (`50_states.csv`) that contains the names and coordinates of the 50 states in the following format:
   ```
   state,x,y
   Alabama,100,200
   Alaska,50,150
   ...
   ```
4. Run the game:
   ```bash
   python main.py
   ```

## File Structure
- `main.py`: The main Python script that runs the game.
- `50_states.csv`: A CSV file containing the names and coordinates of the 50 states.
- `blank_states_img.gif`: An image of the U.S. map used for display.
- `states_to_learn.csv`: A CSV file that is generated when the player exits, containing the names of the states that the player didn't guess.

## Controls
- **Text Input**: Type the name of a U.S. state when prompted.
- **"Give Up" Command**: Type "Give Up" to reveal all unguessed states.
- **"Exit" Command**: Type "Exit" to save unguessed states to `states_to_learn.csv` using **pandas**.

## Future Enhancements
- Add a timer to increase the challenge.
- Implement state capitals as a second level of difficulty.
- Include hints for harder-to-guess states.

