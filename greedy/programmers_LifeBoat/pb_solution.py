def solution(people, limit):
    people = sorted(people)
    people_in_boat = [False] * len(people)
    answer = 0
    left, right = 0, len(people) - 1
    while left < right:
        boat = people[left] + people[right]
        if boat > limit:
            people_in_boat[right] = True
            answer += 1
            right -= 1
        else:
            people_in_boat[left] = True
            people_in_boat[right] = True
            answer += 1
            left += 1
            right -= 1
    return answer + people_in_boat.count(False)


print(solution([70, 50, 80, 50], 100) == 3)
print(solution([70, 80, 50], 100) == 3)
