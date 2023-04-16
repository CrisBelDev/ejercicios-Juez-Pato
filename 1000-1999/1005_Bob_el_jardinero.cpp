#include <iostream>
#include <iomanip>
using namespace std;

double round2(double n) {
    return (int)(n * 100 + 0.5) / 100.0;
}

int main() {
    int casos;
    cin >> casos;
    cin.ignore();
    for (int n = 0; n < casos; n++) {
        string cadena;
        getline(cin, cadena);
        int a = 0, e = 0, i = 0, o = 0, u = 0;
        for (char c : cadena) {
            switch(c) {
                case 'a':
                    a++;
                    break;
                case 'e':
                    e++;
                    break;
                case 'i':
                    i++;
                    break;
                case 'o':
                    o++;
                    break;
                case 'u':
                    u++;
                    break;
                default:
                    break;
            }
        }
        int total = cadena.size();
        cout << "Caso " << n + 1 << ":" << endl;
        cout << "a= " << fixed << setprecision(2) << round2((a * 100.0) / total) << endl;
        cout << "e= " << fixed << setprecision(2) << round2((e * 100.0) / total) << endl;
        cout << "i= " << fixed << setprecision(2) << round2((i * 100.0) / total) << endl;
        cout << "o= " << fixed << setprecision(2) << round2((o * 100.0) / total) << endl;
        cout << "u= " << fixed << setprecision(2) << round2((u * 100.0) / total) << endl;
    }
    return 0;
}
