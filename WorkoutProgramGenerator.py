import random

print("This is a program that will generate a new workout program every week so that you never feel plateaued")

upper_back_exercises = ["Bent-over-Rows", "Seated Cable Rows", "Dumbbell Rows", "High Cable Rows"]
middle_back_exercises = ["Seated Cable Rows", "Bent-Over Dumbbell Rows", "Reverse-Grip Bent-Over Rows"]
lower_back_exercises = ["Deadlifts"]
upper_chest_exercises = ["Incline Barbell Bench Press", "Incline Dumbbell Bench Press", "Incline Dumbbell Flyes"]
middle_chest_exercises = ["Flat Bench Press", "Flat Dumbbell Press", "Chest Press Machine", "Dumbbell Flyes"]
lower_chest_exercises = ["Decline Bench Press", "Decline Dumbbell Press", "Decline Dumbbell Flyes"]
upper_shoulder_exercises = ["Overhead Press", "Dumbbell Shoulder Press", "Lateral Raises", "Face Pulls"]
middle_shoulder_exercises = ["Seated Dumbbell Shoulder Press", "Lateral Raises"]
lower_shoulder_exercises = ["Dumbbell Shrug", "Barbell Shrug", "Bent-Over Rear Delt Raises"]
upper_leg_exercises = ["Lunges", "Leg Press", "Leg Extensions", "Romanian Deadlifts"]
middle_leg_exercises = ["Sumo Squats", "Leg Press (Narrow Stance)", "Hip Thrusts"]
lower_leg_exercises = ["Calf Raises", "Standing Calf Raises", "Seated Calf Raises", "Leg Press Calf Raises"]
upper_bicep_exercises = ["Barbell Curls", "Dumbbell Hammer Curls", "Preacher Curls", "Incline Dumbbell Curls", "Concentration Curls", "Cable Curls"]
middle_bicep_exercises = ["Alternating Dumbbell Curls", "Cable Hammer Curls", "21s", "EZ-Bar Preacher Curls"]
lower_bicep_exercises = ["Reverse Grip Barbell Curls", "Reverse Grip Dumbbell Curls", "Preacher Hammer Curls", "Cable Reverse Curls", "Seated Dumbbell Supination Curls"]
upper_tricep_exercises = ["Close Grip Bench Press", "Overhead Tricep Extensions", "kull Crushers", "Cable Overhead Tricep Extensions"]
middle_tricep_exercises = ["Tricep Pushdowns", "Tricep Rope Pushdowns"]
lower_tricep_exercises = ["Tricep Pushdowns with Reverse Grip", "Seated Overhead Dumbbell Extension", "Tricep Dumbbell Kickbacks"]

def generate_workout_plan(exercises):
    return random.sample(exercises, k=2)

workout_plan = {
    "Monday": [generate_workout_plan(upper_back_exercises + middle_back_exercises), generate_workout_plan(upper_bicep_exercises + middle_bicep_exercises)],
    "Tuesday": [generate_workout_plan(middle_back_exercises + lower_back_exercises), generate_workout_plan(middle_bicep_exercises + lower_bicep_exercises)],
    "Wednesday": [generate_workout_plan(upper_chest_exercises + middle_chest_exercises), generate_workout_plan(upper_tricep_exercises + middle_tricep_exercises)],
    "Thursday": [generate_workout_plan(middle_chest_exercises + lower_chest_exercises), generate_workout_plan(middle_tricep_exercises + lower_tricep_exercises)],
    "Friday": [generate_workout_plan(upper_leg_exercises + middle_leg_exercises + lower_leg_exercises), generate_workout_plan(upper_shoulder_exercises + middle_shoulder_exercises + lower_shoulder_exercises)],
    "Saturday": [generate_workout_plan(upper_shoulder_exercises + middle_shoulder_exercises + lower_shoulder_exercises)],
}

for day, exercises in workout_plan.items():
    print(f"{day}: {exercises}")
