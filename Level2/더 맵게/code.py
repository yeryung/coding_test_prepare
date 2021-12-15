import sys
import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        num1 = hq.heappop(scoville)
        num2 = hq.heappop(scoville)
        new_scoville = num1 + (num2 * 2)
        hq.heappush(scoville, new_scoville)
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution(scoville, K))