#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int cnt = 0;
    int* a = new int[n];
    int* b = new int[n];
    int* aidx = new int[n+1];
    int* visited = new int[n]();

    
    for (int i=0; i<n; i++){
        cin >> a[i];
        aidx[a[i]] = i;
    }
    for (int i=0; i<n; i++){
        cin >> b[i];
    }

    int sn; // start number
    for (int i=0; i<n; i++){
        if ((a[i] == b[i]) || (visited[i])){
            visited[i] = 1;
            continue;
        }
        sn = a[i];
        int num = b[i];
        while (1){
            cnt++;
            visited[aidx[num]] = 1;
            num = b[aidx[num]];
            if (num == sn) break;
        }
    }

    cout << cnt;

    return 0;
}