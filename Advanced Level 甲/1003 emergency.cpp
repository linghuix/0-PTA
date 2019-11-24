// Dijkstra 算法变形 

#include <iostream>
#include <algorithm>

using namespace std; 

#define maxn 1000
#define INF 99999999

int map_dis[maxn][maxn]; 
int Num[maxn];  // Num[i] ： 从 C1 到 i 有多少条路径  

int Team[maxn]; // Team[i] : 从 C1 到 i 每一条路径中，最大的一条路径。
int locateTeam[maxn]; // locateTeaam[i] 表示 ：  位置 i 上已经有救援队的数量 

int dis[maxn];  // 从 C1 到 i 的最短路径距离 

int N, M, C1, C2; 
int Start, End, Weight; 

bool visit[maxn]; 

// 将 C1 到 C1 的距离 设置成 0， C1 不可以一步到达的点 设置成INF ， 由于这里面有一部分点不能再 Dijkstra 松弛部分松弛，
// 则这些点可能出现 Num[i] 和 Team[i] 没有设置成正确形式的情况 ， 所以提前设置好 
void init_1() {
    for (int i = 0; i < N; i++) {
        dis[i] = map_dis[C1][i]; // 初始化 C1 到 i 的距离 

        if (dis[i] < INF) { // C1 可以 一步到达 i （不能够再）
            Num[i] = 1;
            Team[i] = locateTeam[C1] + locateTeam[i]; //  
        }
        else {
            Num[i] = 0;
            Team[i] = locateTeam[i];
        }
        visit[i] = false;
    }
    Num[C1] = 1; Team[C1] = locateTeam[C1];
    dis[C1] = 0;  visit[C1] = true;
}

// 除了 C1 之外 ， 所有位置距离C1的距离 都是 INF ，把点的信息 放到松弛的地方处理
void init_2() {
    for (int i = 0; i < N; i++) {
        dis[i] = INF; //  map_dis[C1][i]; // 初始化 C1 到 i 的距离 

        visit[i] = false;
    }
    Num[C1] = 1; Team[C1] = locateTeam[C1];
    dis[C1] = 0;
}

void Dijkstra() {
    // 两种初始化 方式都可以 
    //init_1(); 
    init_2(); 

    for (int times = 0; times < N; times++) {
        int pos = 0, mix_dis = INF; 

        for (int i = 0; i < N; i++) {
            if (!visit[i] && mix_dis > dis[i]) {
                pos = i; // 找到当前距离 C1 最近的 新点 
                mix_dis = dis[i]; 
            }
        }
        visit[pos] = true; 

        if (pos == C2) {
            break; 
        }

        // cout << Num[C2] << " " << Team[C2] << endl; 

        for (int i = 0; i < N; i++) {
        
            if(map_dis[pos][i] != INF){ /**因为一开始pos是可以等于出发点的，所以这时会导致 dis[i] == dis[pos] + map_dis[pos][i]*/
                if (!visit[i] && dis[i] > dis[pos] + map_dis[pos][i]) {
                    // 更新距离
                    dis[i] = dis[pos] + map_dis[pos][i]; 

                    Num[i] = Num[pos]; 
                    Team[i] = Team[pos] + locateTeam[i]; //Team[i]; 
                }
                else if(!visit[i] && dis[i] == dis[pos] + map_dis[pos][i]){

                    Num[i] += Num[pos]; 
                    
                    if (Team[i] < Team[pos] + locateTeam[i]) {
                        Team[i] = Team[pos] + locateTeam[i]; 
                    }

                }
            }
        }
    }

    cout << Num[C2] << " " << Team[C2] << endl; 
}

int main() {

    while (cin >> N >> M >> C1 >> C2) {

        for (int i = 0; i < N; i++) {
            cin >> locateTeam[i]; // 本地城市 具有的 队员数量 
        }

        // 初始化地图 ， 不相邻的  距离为 INF
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                map_dis[i][j] = INF;
                if (i == j) {
                    map_dis[i][j] = 0; // 自己到自己的距离 为 0 
                }
            }
        }
        // 输入 M 条边 双向边
        for (int i = 0; i < M; i++) {
            cin >> Start >> End >> Weight;

            map_dis[Start][End] = Weight; 
            map_dis[End][Start] = Weight; 

        }

        Dijkstra(); 
    }

    return 0; 
}
