#include <stdio.h>
#include <vector>

using namespace std;

int time = 0;

void dfs(int node, vector<bool> &visited, vector<vector<int>> &graph, vector<int> &d, vector<int> &f)
{
    visited[node] = 1;
    d[node] = time++;

    for (int i = 0; i < graph[node].size(); i++)
    {
        int neighbor = graph[node][i];
        if (!visited[neighbor])
            dfs(neighbor, visited, graph, d, f);
    }
    f[node] = time++;
}

int isParent(int a, int b, vector<int> &d, vector<int> &f)
{
    return (d[a] < d[b]) && (f[b] < f[a]);
}

int main()
{
    int n;
    scanf("%d", &n);

    vector<vector<int>> graph(n + 1);
    vector<bool> visited(n + 1);
    vector<int> d(n + 1);
    vector<int> f(n + 1);

    int num, root;
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &num);

        if (!num)
            root = i;
        else
            graph[num].push_back(i);
    }

    dfs(root, visited, graph, d, f);

    int m, a, b;
    scanf("%d", &m);

    for (int i = 0; i < m; i++)
    {
        scanf("%d %d", &a, &b);
        printf("%d\n", isParent(a, b, d, f));
    }

    return 0;
}