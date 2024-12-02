#include <cstdio>
#include <vector>

using namespace std;

struct Edge
{
    int tBegin;
    int tEnd;
    int dst;
};

const int INF = 1000000000 + 1;

int main()
{
    int nStations, end, nTrains;
    scanf("%d %d %d", &nStations, &end, &nTrains);
    vector<vector<Edge>> out(1 + nStations);

    for (int i = 0; i < nTrains; ++i)
    {
        int len;
        scanf("%d", &len);
        int prevSt, prevT;
        scanf("%d %d", &prevSt, &prevT);

        for (int j = 1; j < len; ++j)
        {
            int curSt, curT;
            scanf("%d %d", &curSt, &curT);
            out[prevSt].push_back(Edge{prevT, curT, curSt});
            prevSt = curSt;
            prevT = curT;
        }
    }

    vector<int> minTime(1 + nStations, INF);
    minTime[1] = 0;
    std::vector<bool> isFinal(1 + nStations, false);

    while (true)
    {
        int minSt = -1;
        int minT = INF;
        for (int i = 1; i <= nStations; ++i)
        {
            if (!isFinal[i] && minTime[i] < minT)
            {
                minT = minTime[i];
                minSt = i;
            }
        }

        if (minT == INF)
            break;

        isFinal[minSt] = true;
        for (const Edge &edge : out[minSt])
        {
            if (edge.tBegin >= minTime[minSt])
                if (edge.tBegin >= minTime[minSt])
                    if (edge.tEnd < minTime[edge.dst])
                        minTime[edge.dst] = edge.tEnd;
        }
    }

    if (minTime[end] == INF)
        printf("-1");
    else
        printf("%d", minTime[end]);

    return 0;
}