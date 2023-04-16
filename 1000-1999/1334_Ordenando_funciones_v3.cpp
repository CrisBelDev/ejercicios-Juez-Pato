#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int sumarDigitos(int x) {
    int suma = 0;
    string numero = to_string(x);
    for (char c : numero) {
        suma += (int)(c - '0');
    }
    return suma;
}

vector<int> ordenarVector(vector<int> v) {
    sort(v.begin(), v.end(), [](int x, int y) {
        int sumaX = sumarDigitos(x);
        int sumaY = sumarDigitos(y);
        return (sumaX == sumaY) ? x < y : sumaX < sumaY;
    });
    return v;
}

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    vector<int> r = ordenarVector(v);
    for (int i = 0; i < r.size(); i++) {
        if (i == r.size() - 1) {
            cout << r[i] << endl;
        } else {
            cout << r[i] << " ";
        }
    }
    return 0;
}
