#include <iostream>
using namespace std;

void Lectura() {
    int n;
    while (cin >> n) {
        if (n == 0) break;
        int s = 0;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            s += x;
        }
        cout << s << endl;
    }
}

int main() {
    Lectura();
    return 0;
}
