#include <iostream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int score;
    string pnp;

    cin >> score;
    pnp = score == 100 ? "pass" : "failure";
    cout << pnp;

    return 0;
}