#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int height, weight;
    double bmi;

    cin >> height >> weight;
    bmi = (10000 * weight) / (height * height);

    cout << bmi << endl;
    if (bmi >= 25){
        cout << "Obesity";
    }
    return 0;
}