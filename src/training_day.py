from exercise import Exercise


class TrainingDay:

    def __init__(self, id):
        self._id = id
        self._training_day = []

    def return_id(self):

        return self._id

    def create_exercise(self):
        name = input("Enter name of exercise: ").strip().lower()
        set = int(input("Enter number of sets: "))
        reps = int(input("Enter number of reps per set: "))
        weight = float(input("Enter weight"))
        exercise = Exercise(name, set, reps, weight)
        self._training_day.append(exercise)

    def print_exercises(self):
        for exercise in self._training_day:
            print(exercise)


