def nps_calculator(scores):
    scores = [10, 7, 10, 5, 9, 3, 8, 9, 10, 7, 10, 5, 9, 3, 8, 9]

detractors_count = 0
neutrals_count = 0
promoters_count = 0

#для каждой оценки из scores нужно делать:
for score in scores:
    if score < 7:
        # detractors_count = detractors_count + 1
        detractors_count += 1

    if 7 <= score <= 8:
        neutrals_count += 1

    if score > 8:
        promoters_count += 1

result = (promoters_count - detractors_count) / len(scores) * 100
print(round(result))