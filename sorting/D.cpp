#include <iostream>
#include <vector>

using namespace std;

int swapCounter(vector<int> &a)
{
    int n = a.size();
    bool swapped;
    int counter = 0;
    for (int i = 0; i < n - 1; ++i)
    {
        swapped = false;
        for (int j = 0; j < n - i - 1; ++j)
        {
            if (a[j + 1] < a[j])
            {
                counter++;
                swap(a[j], a[j + 1]);
                swapped = true;
            }
        }
        if (!swapped)
        {
            break;
        }
    }

    return counter;
}

int main()
{
    int n, x;
    cin >> n;
    vector<int> a;
    for (int i = 0; i < n; ++i)
    {
        cin >> x;
        a.push_back(x);
    }

    int k = swapCounter(a);
    cout << k;

    return 0;
}