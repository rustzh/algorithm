#include <iostream>
#include <string.h>

using namespace std;

int visited[50][50] = {0,};
int a[50][50] = {0,};

void dfs(int x, int y, int m, int n){
    visited[x][y] = 1;
    if (a[x-1][y]==1 && (x-1)>=0){
        if (visited[x-1][y]==0) {
            visited[x-1][y] = 1;
            dfs(x-1, y, m, n);
        }
    }
    if (a[x+1][y]==1 && (x+1)<m){
        if (visited[x+1][y]==0){
            visited[x+1][y] = 1;
            dfs (x+1, y, m, n);
        }
    }
    if (a[x][y-1]==1 && (y-1)>=0){
        if (visited[x][y-1]==0){
            visited[x][y-1] = 1;
            dfs(x, y-1, m, n);
        }
    }
    if (a[x][y+1]==1 && (y+1)<n){
        if (visited[x][y+1]==0){
            visited[x][y+1] = 1;
            dfs(x, y+1, m, n);
        }
    }
}

int main(){
    int t;
    cin >> t;
    
    for (int c=0; c<t; c++){
        int m, n, k;
        cin >> m >> n >> k;

        for (int i=0; i<k; i++){
            int x1, y1;
            cin >> x1 >> y1;
            a[x1][y1] = 1;
        }

        int cnt;
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if (visited[i][j]==0 && a[i][j]==1){
                    dfs(i,j,m,n);
                    cnt++;
                }
            }
        }
        cout << cnt << endl;

        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                visited[i][j] = 0;
                a[i][j] = 0;
            }
        }
        cnt = 0;
    }

    return 0;
}