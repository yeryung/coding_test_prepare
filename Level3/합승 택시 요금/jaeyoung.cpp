#include <string>
#include <sstream>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = 0;
    
    std::vector<std::vector<int>> dist;
    
    //할당
    dist.resize(n+1);
    for(int i = 1; i < dist.size(); i++){
        dist[i].resize(n+1,99999999);
        dist[i][i] = 0;
    }
    
    //만들기
    for(int i = 0; i < fares.size(); i++){
            vector<int>& data = fares[i];
            int from = data[0];
            int to = data[1];
            int fare = data[2];
        
            dist[from][to] = fare;
            dist[to][from] = fare;
    }
    
    //플로이드
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n ; j++){
            for(int k = 1; k <= n ; k++){
                if(dist[j][k] > dist[j][i] + dist[i][k]){
                    dist[j][k] = dist[j][i] + dist[i][k];
                }
            }
        }
    }
    
    int r = 99999999;
    for(int i = 1; i <= n; i++){
        int tempResult = dist[s][i] + dist[i][a] + dist[i][b];
        if(r > tempResult)
            r = tempResult;
    }
    
    answer = r;
    return answer;
}
