#include "ddsTable.h"

int main()
{
    ddsTable("ddsDB.txt", "ddsResult.txt");
    return 0;
}
/* compile test.cpp
g++ -c test.cpp
g++ test.o -L. -lddsTable -o test
*/
