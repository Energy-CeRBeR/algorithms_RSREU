#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>
#include <queue>
#include <limits>

using namespace std;

long long dijkstra(unordered_map<int, set<pair<int, int>>> &graph, int n, int start, int end)
{
    vector<long long> dist(n + 1, std::numeric_limits<long long>::max()); // Изменено на long long
    dist[start] = 0;

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq; // Изменено на long long
    pq.push({0, start});

    while (!pq.empty())
    {
        long long cur_dist = pq.top().first;
        int cur_vertex = pq.top().second;
        pq.pop();

        if (cur_vertex == end)
            return dist[cur_vertex];

        if (cur_dist > dist[cur_vertex])
            continue;

        for (auto &edge : graph[cur_vertex])
        {
            int neighbor = edge.first;
            int weight = edge.second;
            long long d = cur_dist + weight;
            if (d < dist[neighbor])
            {
                dist[neighbor] = d;
                pq.push({d, neighbor});
            }
        }
    }

    return -1;
}

int main()
{
    int n, k;
    cin >> n >> k;

    unordered_map<int, set<pair<int, int>>> graph;
    for (int i = 0; i < k; ++i)
    {
        int a, b, l;
        cin >> a >> b >> l;
        graph[a].insert({b, l});
        graph[b].insert({a, l});
    }

    int a, b;
    cin >> a >> b;

    long long result = dijkstra(graph, n, a, b);
    cout << result << endl;

    return 0;
}