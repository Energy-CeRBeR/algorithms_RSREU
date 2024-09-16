#include <iostream>
#include <vector>

using namespace std;

void bubbleSort(vector<int> &a)
{
    int n = a.size();
    bool swapped;
    for (int i = 0; i < n - 1; ++i)
    {
        swapped = false;
        for (int j = 0; j < n - i - 1; ++j)
        {
            if (a[j + 1] > a[j])
            {
                swap(a[j], a[j + 1]);
                swapped = true;
            }
        }
        if (!swapped)
        {
            return;
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

    bubbleSort(a);

    for (auto x : a)
    {
        cout << x << " ";
    }

    return 0;
}