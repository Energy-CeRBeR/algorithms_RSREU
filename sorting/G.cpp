#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void CountSort(std::vector<int> &a)
{
    int n = a.size();
    int k = *max_element(a.begin(), a.end());
    std::vector<int> counter(k + 1);
    for (int i = 0; i < n; i++)
    {
        counter[a[i]]++;
    }
    a.clear();

    for (int i = 0; i < k + 1; i++)
    {
        a.insert(a.end(), counter[i], i);
    }
}

int main()
{
    int x;
    vector<int> a;
    while (cin >> x)
    {
        a.push_back(x);
    }

    CountSort(a);

    for (auto x : a)
    {
        cout << x << " ";
    }

    return 0;
}