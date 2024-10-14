#include <stdio.h>
#include <math.h>
#include <algorithm>

bool check_answer(int w, int h, int n, long long a)
{
    return (a / w) * (a / h) >= n;
}

int main()
{
    int w, h, n;
    scanf("%d %d %d", &w, &h, &n);

    long long left = 0;
    long long right = (sqrt(n) + 1) * std::max(w, h);
    while (left <= right)
    {
        long long middle = (left + right) / 2;
        if (check_answer(w, h, n, middle))
            right = middle - 1;
        else
            left = middle + 1;
    }

    printf("%lld", left);

    return 0;
}