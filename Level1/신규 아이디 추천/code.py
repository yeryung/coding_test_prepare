import re

def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    p = re.compile('[0-9a-z_.\-]+')
    fl = p.findall(new_id)
    new_id = ''.join(fl)
    
    # 3단계
    new_id = re.sub(r'\.\.+','.', new_id)
    
    # 4단계 
    new_id = new_id.strip('.')
    
    # 5단계
    if new_id == '':
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16 :
        new_id = new_id[:15].rstrip('.')
    
            
    # 7단계
    if len(new_id) <=2 :
        while(len(new_id)<3):
            new_id = new_id + new_id[-1]
        
    answer = new_id
    
    return answer


if __name__ == "__main__":
    print(solution(new_id))