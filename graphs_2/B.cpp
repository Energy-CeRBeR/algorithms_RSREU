#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = 2009000999;

vector<int> dijkstra(int n, vector<vector<pair<int, int>>> &graph, int start)
{
    vector<int> dist(n, INF);
    dist[start] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});

    while (!pq.empty())
    {
        int cur_dist = pq.top().first;
        int cur_vertex = pq.top().second;
        pq.pop();

        if (cur_dist > dist[cur_vertex])
            continue;

        for (auto &edge : graph[cur_vertex])
        {
            int neighbor = edge.first;
            int weight = edge.second;
            int d = cur_dist + weight;
            if (d < dist[neighbor])
            {
                dist[neighbor] = d;
                pq.push({d, neighbor});
            }
        }
    }

    return dist;
}

int main()
{
    int num;
    cin >> num;

    for (int t = 0; t < num; ++t)
    {
        int n, m;
        cin >> n >> m;

        vector<vector<pair<int, int>>> graph(n);

        for (int i = 0; i < m; ++i)
        {
            int a, b, weight;
            cin >> a >> b >> weight;
            graph[a].push_back({b, weight});
            graph[b].push_back({a, weight});
        }

        int start;
        cin >> start;

        vector<int> dist = dijkstra(n, graph, start);

        for (int i = 0; i < n; ++i)
            cout << dist[i] << " ";
        cout << endl;
    }

    return 0;
}