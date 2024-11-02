#include <iostream>
#include <unordered_set>
#include <list>
#include <queue>
#include <limits.h>

using namespace std;

int main()
{
    int n, k, p, count = 0;
    cin >> n >> k >> p;

    list<int> counter[n];
    int history[p];
    for (int i = 0; i < p; i++)
    {
        cin >> history[i];
        counter[--history[i]].push_back(i);
    }

    unordered_set<int> floor;
    priority_queue<pair<int, int>> garage;
    for (int i = 0; i < p; i++)
    {
        int curr = history[i];
        counter[curr].pop_front();

        if (floor.find(curr) == floor.end())
        {
            if (floor.size() >= k)
            {
                floor.erase(garage.top().second);
                garage.pop();
            }
            count++;
            floor.insert(curr);
        }

        if (counter[curr].empty())
            garage.push({INT_MAX, curr});
        else
            garage.push({counter[curr].front(), curr});
    }

    cout << count << endl;

    return 0;
}