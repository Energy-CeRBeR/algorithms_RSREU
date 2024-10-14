#include <stdio.h>
#include <algorithm>

using namespace std;

bool calculate(int time, int x, int y, int target)
{
    return (time / x + time / y) >= target;
}

int main()
{
    int n, x, y;
    scanf("%d %d %d", &n, &x, &y);

    n--;
    int cur_time = min(x, y);

    int left = 0;
    int right = 1000000000;
    while (left <= right)
    {
        int middle = (left + right) / 2;
        if (calculate(middle, x, y, n))
            right = middle - 1;
        else
            left = middle + 1;
    }

    printf("%d", left + cur_time);

    return 0;
}