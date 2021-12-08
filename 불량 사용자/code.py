from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    match_list = []
    user_permutation = list(permutations(user_id,len(banned_id)))

    for user in user_permutation:
        cnt = 0
        for k in range(len(user)):
            if match(banned_id[k],user[k]) == True:
                cnt = cnt + 1
        if cnt == len(banned_id):
            if set(user) not in match_list:
                match_list.append(set(user))

    answer = len(match_list)
    
    return answer

def match(banned_id, user_id):
    if len(banned_id) != len(user_id):
        return False
    else:
        for k in range(len(banned_id)):
            if banned_id[k] == '*':
                banned_id = banned_id.replace(banned_id[k],user_id[k],1)
                continue

        if banned_id == user_id:
            return True

        return False
                
if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
    #user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]	
    banned_id = ["fr*d*", "abc1**"]	
    #banned_id = ["*rodo", "*rodo", "******"]
    print(solution(user_id,banned_id))