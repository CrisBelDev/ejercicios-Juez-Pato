#include <iostream>
#include <set>
#include <cmath>

using namespace std;

bool is_prime(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    
    set<int> primes;
    while (t--) {
        int x;
        cin >> x;
        if (is_prime(x)) {
            primes.insert(x);
        }
    }
    
    for (int prime : primes) {
        cout << prime << " ";
    }
    
    return 0;
}
