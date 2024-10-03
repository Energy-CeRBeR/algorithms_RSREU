#include <iostream>
#include <vector>

using namespace std;

bool is_answer(int distance, vector<int> &p, int n, int k)
{
    int count = 1;
    int last_p = p[0];
    for (int i = 1; i < n; ++i)
    {
        if (last_p + distance <= p[i])
        {
            count++;
            last_p = p[i];
        }

        if (count == k)
        {
            return true;
        }
    }

    return false;
}

int main()
{
    int n, k;
    cin >> n >> k;

    vector<int> a;
    for (int i = 0; i < n; ++i)
    {
        int num;
        cin >> num;
        a.push_back(num);
    }

    int left = 0;
    int right = 1000000000;
    int middle;
    while (right - left > 1)
    {
        middle = (left + right) / 2;
        if (is_answer(middle, a, n, k))
        {
            left = middle;
        }
        else
        {
            right = middle;
        }
    }

    cout << left;

    return 0;
}