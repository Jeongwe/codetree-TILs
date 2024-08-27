#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n1, n2;
    int max;
    cin >> n1 >> n2;

    max = n1 > n2 ? n1 : n2;
    cout << max;
    return 0;
}