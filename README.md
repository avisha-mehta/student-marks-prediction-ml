# Student Marks Prediction Using Machine Learning

A small, beginner-friendly B.Tech first-year mini project using **Python** and **Linear Regression**.

## Project idea
The program learns from a small example dataset containing study hours and marks. It then estimates marks for the number of study hours entered by the user.

> Important: The included data is illustrative/demo data. The predictions are only for learning and should not be treated as accurate predictions of real student performance.

## Concepts demonstrated
- Reading a CSV dataset
- Input features (`study_hours`) and target (`marks`)
- Training a Linear Regression model
- Making a prediction from user input
- Basic validation of user input

## Requirements
- Python 3.9 or newer
- pip

## Run the project
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install the dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run:

   ```bash
   python main.py
   ```

5. Enter a number between `0` and `10` when asked for study hours. Type `q` to exit.

On some Windows computers, use `py` instead of `python`.

## Files
- `main.py` — trains the model and asks for user input
- `study_marks.csv` — small sample dataset
- `requirements.txt` — Python dependency list

## Possible future improvements
- Plot the dataset and regression line
- Add more realistic, ethically collected data
- Create a simple web interface

## Academic note
This is an introductory demonstration of Linear Regression. Explain the code in your own words and follow your college's rules about project submissions.
