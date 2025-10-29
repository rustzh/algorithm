#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> v;
vector<bool> visited;
int cnt = -1;

void dfs(int n)
{
	if (visited[n])
		return;
	visited[n] = true;
	cnt++;
	for (auto u : v[n])
	{
		dfs(u);
	}

}

int main()
{
	int n, edges;
	cin >> n;
	cin >> edges;

	v.resize(n + 1);
	visited.resize(n + 1);

	for (int i = 0; i < edges; i++)
	{
		int a, b;
		cin >> a >> b;

		v[a].push_back(b);
		v[b].push_back(a);
	}

	dfs(1);
	cout << cnt;

	return 0;
}