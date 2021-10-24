#include <bits/stdc++.h>
using namespace std;

#define Least_Significant_Bit(i) (i) & -(i)

vector <int> Binary_Indexed_Tree;

int TREE_SIZE = 1e5 + 10;

void update(int index, int value) {
    while(index <= TREE_SIZE) {
        Binary_Indexed_Tree[index] += value;
        index += Least_Significant_Bit(index);
    }
}

int query(int index) {
    int sum = 0;
    while(index > 0) {
        sum += Binary_Indexed_Tree[index];
        index -= Least_Significant_Bit(index);
    }
    return sum;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    Binary_Indexed_Tree.assign(TREE_SIZE, 0);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        string operation;
        cin >> operation;
        if(operation == "U") {
            /// Update
            int index, value;
            cin >> index >> value;
            update(index, value);
        }
        if(operation == "Q") {
            /// Query
            int index;
            cin >> index;
            cout << query(index) << "\n";
        }
    }
    return 0;
}
