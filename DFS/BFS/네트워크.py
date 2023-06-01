def deeper(start, computers, visited):
    for j in range(len(computers)):
        if visited[j] == False and computers[start][j] == 1:
            visited[j] = True
            deeper(j, computers, visited)


def solution(n, computers):  # 네트워크
    visited = [False] * n
    answer = 0

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            answer += 1
            deeper(i, computers, visited)

    return answer
