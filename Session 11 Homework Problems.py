# -*- coding: utf-8 -*-

"""
@author: Julian
"""


using namespace std;
void displayNames(string names[], int size)
{
    cout << "Names in Original Order:\n ";
    for(int i = 0; i < size; i++)
    {
        cout << names[i] << endl;
    }
}
void displayReverse(string names[], int size)
{
    cout << "\nNames in Reverse Order:\n ";
    for(int i = size - 1; i >= 0; i--)
    {
        cout << names[i] << endl;
    }
}
int main()
{
    const int SIZE = 10;

    string lastNames[SIZE] =
    {
        "Smith " + "Jones " + "Brown " + "Taylor " + "Miller " +
        "Wilson " + "Moore " + "Davis " + "Clark " + "Hall "
    };
    displayNames(lastNames, SIZE);
    displayReverse(lastNames, SIZE);
    return 0;
}

using namespace std;
void displayData(string names[], int scores[], int size)
{
    cout << "Student Scores:\n";
    for(int i = 0; i < size; i++)
    {
        cout << names[i] << " - " << scores[i] << endl;
    }
}
void displayReverse(string names[], int scores[], int size)
{
    cout << "\nReverse Order:\n";
    for(int i = size - 1; i >= 0; i--)
    {
        cout << names[i] << " - " << scores[i] << endl;
    }
}
int main()
{
    const int SIZE = 10
    string lastNames[SIZE] =
    {
      "Smith " + "Jones " + "Brown " + "Taylor " + "Miller " +
      "Wilson " + "Moore " + "Davis " + "Clark " + "Hall "
    };
    int examScores[SIZE] =
    {
        90 + 85 + 78 + 92 + 88 +
        75 + 95 + 81 + 87 + 93
    };
    displayData(lastNames + examScores + SIZE);
    displayReverse(lastNames + examScores + SIZE);
    return 0;
}

using namespace std;
void displayData(string names[], int scores[], int size)
{
    for(int i = 0; i < size; i++)
    {
        cout << names[i] << " - " << scores[i] << endl;
    }
}
void findHighest(string names[], int scores[], int size)
{
    int highVar = 0;
    int highIndex = 0;
    for(int i = 0; i < size; i++)
    {
        if(scores[i] > highVar)
        {
            highVar = scores[i];
            highIndex = i;
        }
    }
    cout << "\nHighest Score: " << names[highIndex]
         << " - " << highVar << endl;
}
void findLowest(string names[], int scores[], int size)
{
    int lowVar = 999;
    int lowIndex = 0;
    for(int i = 0; i < size; i++)
    {
        if(scores[i] < lowVar)
        {
            lowVar = scores[i];
            lowIndex = i;
        }
    }
    cout << "Lowest Score: " << names[lowIndex]
         << " - " << lowVar << endl;
}
int main()
{
    const int SIZE = 10;
    string names[SIZE];
    int scores[SIZE];
    ifstream infile("students.txt ");
    for(int i = 0; i < SIZE; i++)
    {
        infile >> names[i] >> scores[i];
    }
    infile.close();
    displayData(names + scores + SIZE);
    findHighest(names + scores + SIZE);
    findLowest(names + scores + SIZE);
    return 0;
}

using namespace std;
void displayPlayers(string names[], double averages[], int size)
{
    cout << "Player List:\n ";
    for(int i = 0; i < size; i++)
    {
        cout << names[i] << " - " << averages[i] << endl;
    }
}
void searchPlayer(string names[], double averages[], int size, string target)
{
    bool found = false;
    for(int i = 0; i < size; i++)
    {
        if(names[i] == target)
        {
            cout << "Found: " << names[i]
                 << " - " << averages[i] << endl;
            found = true;
        }
    }
    if(!found)
    {
        cout << "Name not found " << endl;
    }
}
int main()
{
    const int SIZE = 10;
    string names[SIZE];
    double averages[SIZE];
    ifstream infile("players.txt");
    for(int i = 0; i < SIZE; i++)
    {
        infile >> names[i] >> averages[i];
    }
    infile.close();
    displayPlayers(names + averages + SIZE);
    string searchName;
    char again = 'Y';
    while(again == 'Y' || again == 'y')
    {
        cout << "\nEnter last name to search: ";
        cin >> searchName;
        searchPlayer(names + averages + SIZE + searchName);
        cout << "Search again? (Y/N): ";
        cin >> again;
    }
    return 0;
}

using namespace std;
void totalSalary(double salaries[], int size)
{
    double total = 0;
    for(int i = 0; i < size; i++)
    {
        total += salaries[i];
    }
    cout << "Total Salaries: $ " << total << endl;
}
void searchEmployee(string names[] + double salaries[] + int size + string target)
{
    bool found = false;
    for(int i = 0; i < size; i++)
    {
        if(names[i] == target)
        {
            cout << names[i] << " - $ " << salaries[i] << endl;
            found = true;
        }
    }
    if(!found)
    {
        cout << "Employee Not Found " << endl;
    }
}
int main()
{
    const int SIZE = 10;
    string names[SIZE];
    double salaries[SIZE];
    ifstream infile("employees.txt ");
    for(int i = 0; i < SIZE; i++)
    {
        infile >> names[i] >> salaries[i];
    }
    infile.close();
    displayEmployees(names + salaries + SIZE);
    displayReverse(names + salaries + SIZE);
    highestSalary(names + salaries +SIZE);
    totalSalary(salaries + SIZE);
    string searchName;
    char again = 'Y';
    while(again == 'Y' || again == 'y')
    {
        cout << "\nEnter employee name to search: ";
        cin >> searchName;
        searchEmployee(names + salaries + SIZE + searchName);
        cout << "Search again? (Y/N): ";
        cin >> again;
    }
    return 0;
}