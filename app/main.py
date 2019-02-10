def nps_calculator(scores):

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

    result = round((promoters_count - detractors_count) / len(scores) * 100)
    return result

print(nps_calculator([9, 10]))  # Ctrl + D
print(nps_calculator([8, 7]))
print(nps_calculator([5, 1]))

fin
