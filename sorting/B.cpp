#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<int> &a)
{
    int n = a.size();
    int key, j;
    for (int i = 1; i < n; ++i)
    {
        key = a[i];
        j = i;
        while (j >= 1 && a[j - 1] > key)
        {
            a[j] = a[j - 1];
            j--;
        }
        a[j] = key;
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