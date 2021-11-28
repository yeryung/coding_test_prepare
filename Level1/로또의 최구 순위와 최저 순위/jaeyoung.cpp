#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    
    int result = 0;
    int zero = 0;
    for(int i =0 ; i< 6 ;i++){
        int data = lottos[i];
        
        if(data == 0){
            zero++;
            continue;
        }
        
        for(int j = 0 ; j< 6;j++){
            if(data == win_nums[j]){
                result++;
            } 
        }
        
    }
    
    int a = 7-(result+zero);
    if(a==7)
        a= 6;
    int b = 7-(result);
    if(b==7)
        b= 6;
    
    answer.push_back(a);
    answer.push_back(b);
    
    
    return answer;
}