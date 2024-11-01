#include <iostream>
#include <queue>

using namespace std;

int main()
{
    priority_queue<int, vector<int>, greater<int>> priorityQueue;

    string command;
    int value;

    while (cin >> command)
    {
        if (command == "ADD")
        {
            cin >> value;
            priorityQueue.push(value);
        }

        else if (command == "EXTRACT")
        {
            if (!priorityQueue.empty())
            {
                cout << priorityQueue.top() << endl; // Инвертируем значение при выводе
                priorityQueue.pop();
            }
            else
            {
                cout << "CANNOT" << endl;
            }
        }

        else if (command == "CLEAR")
            priorityQueue = priority_queue<int, vector<int>, greater<int>>();
    }

    return 0;
}