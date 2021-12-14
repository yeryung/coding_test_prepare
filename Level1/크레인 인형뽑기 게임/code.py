def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] == 0:
                continue
            else:
                if len(stack) != 0 and stack[-1] == board[i][move-1]:
                    del stack[-1]
                    board[i][move-1] = 0
                    answer = answer + 2
                    break
                else:
                    stack.append(board[i][move-1])
                    board[i][move-1] = 0
                    break
                
    return answer

if __name__ == "__main__":
    print(solution(board,moves))