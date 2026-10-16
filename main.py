"""
Student Marks Prediction using Linear Regression
Beginner-friendly B.Tech 1st-year Machine Learning mini project.
Run: python main.py
"""
import csv
from pathlib import Path
from sklearn.linear_model import LinearRegression

DATA_FILE = Path(__file__).with_name("study_marks.csv")

def load_data():
    hours, marks = [], []
    with DATA_FILE.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            hours.append([float(row["study_hours"])])
            marks.append(float(row["marks"]))
    return hours, marks

def main():
    X, y = load_data()
    model = LinearRegression()
    model.fit(X, y)

    print("=" * 45)
    print(" STUDENT MARKS PREDICTION")
    print(" Machine Learning: Linear Regression")
    print("=" * 45)
    print(f"Training examples: {len(X)}")
    print(f"Model R-squared on training data: {model.score(X, y):.2f}")
    print("\nEnter study hours to estimate marks (0 to 10).")
    print("Type 'q' to quit.")

    while True:
        answer = input("\nStudy hours: ").strip().lower()
        if answer in {"q", "quit", "exit"}:
            print("Thanks for trying the project!")
            break
        try:
            hours = float(answer)
            if not 0 <= hours <= 10:
                print("Please enter a number between 0 and 10.")
                continue
            prediction = float(model.predict([[hours]])[0])
            prediction = max(0, min(100, prediction))
            print(f"Estimated marks: {prediction:.1f} / 100")
            print("Note: This is an educational estimate, not a real guarantee.")
        except ValueError:
            print("Please enter a valid number, or type 'q' to quit.")

if __name__ == "__main__":
    main()
