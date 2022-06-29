def solution(people, limit):
    people = sorted(people)
    answer = 0
    left, right = 0, len(people) - 1
    while left < right:
        boat = people[left] + people[right]
        if boat > limit:
            answer += 1
            right -= 1
        else:
            answer += 1
            left += 1
            right -= 1
    return answer + 1 if left == right else answer


print(solution([70, 50, 80, 50], 100) == 3)
print(solution([70, 80, 50], 100) == 3)
