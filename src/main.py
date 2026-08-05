print("Student Score Analyzer")
print("----------------------")

number_of_students = int(input("How many student scores do you want to enter? "))

scores = []

for i in range(number_of_students):
    while True:
        score = float(input(f"Enter score for student {i + 1}: "))

        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("Invalid score. Please enter a score from 0 to 100.")

total_score = 0
pass_count = 0
fail_count = 0

highest_score = scores[0]
lowest_score = scores[0]

for score in scores:
    total_score += score

    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

    if score > highest_score:
        highest_score = score

    if score < lowest_score:
        lowest_score = score

average_score = total_score / len(scores)

print()
print("Analysis Result")
print("---------------")
print(f"Number of students: {len(scores)}")
print(f"Total score: {total_score:.2f}")
print(f"Average score: {average_score:.2f}")
print(f"Highest score: {highest_score:.2f}")
print(f"Lowest score: {lowest_score:.2f}")
print(f"Number of students who passed: {pass_count}")
print(f"Number of students who failed: {fail_count}")


