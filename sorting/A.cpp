#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<int> &a)
{
    for (int i = 0; i < a.size(); ++i)
    {
        int mx = a[i];
        int mx_index = i;
        for (int j = i + 1; j < a.size(); ++j)
        {
            if (a[j] > mx)
            {
                mx = a[j];
                mx_index = j;
            }
        }

        if (mx_index != i)
        {
            swap(a[i], a[mx_index]);
        }
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