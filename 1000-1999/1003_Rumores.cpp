#include <iostream>
#include <vector>

using namespace std;

void funcion(int m, int x, int y, vector<vector<int>> &matris);

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, m;
        cin >> n >> m;

        vector<vector<int>> matris(m, vector<int>(2));
        for (int j = 0; j < m; j++) {
            int u, v;
            cin >> u >> v;
            matris[j][0] = u;
            matris[j][1] = v;
        }

        int x, y;
        cin >> x >> y;

        funcion(m, x, y, matris);
    }

    return 0;
}

void funcion(int m, int x, int y, vector<vector<int>> &matris) {
    vector<int> lista;
    for (int j = 0; j < m; j++) {
        for (int i = 0; i < m; i++) {
            if (x == matris[i][0]) {
                lista.push_back(matris[i][1]);
            }
        }
        int num = lista.size();
        x = lista[num - 1];
    }
    int num = lista.size();
    for (int i = 0; i < num; i++) {
        int var = lista[i];
        if (var == y) {
            cout << "SI" << endl;
            return;
        }
    }
    cout << "NO" << endl;
}
