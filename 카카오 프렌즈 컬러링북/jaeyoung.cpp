#include <vector>
#include <queue>
#include <utility>
#include <iostream>
using namespace std;


int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    
    queue<pair<int,int>> q;
    
    for(int i = 0; i<m;i++){
        for(int j = 0; j < n; j++){
            
            if(picture[i][j] != 0){
                
                int result = 0;
                int color = picture[i][j];
                q.push(pair<int,int>(i,j));
                picture[i][j] = 0;
                
                while(!q.empty()){
                    pair<int,int> data = q.front();
                    int x = data.first;
                    int y = data.second;
                    q.pop();
                    
                    result++;
                    
                    for(int l = 0; l < 4; l++){
                        int xx = x + dx[l];
                        int yy = y + dy[l];
                        if(xx < m && xx >=0 && yy < n && yy >=0){
                            if(picture[xx][yy] == color){
                                q.push(pair<int,int>(xx,yy));
                                picture[xx][yy] = 0;
                            }
                        }
                    }
                }
                if(result > max_size_of_one_area){
                    max_size_of_one_area = result;
                }
                number_of_area++;
            }
        }
    }
    
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}