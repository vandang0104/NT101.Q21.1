#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string cleanText(string text) {
    string r = "";
    for (char c : text) {
        if (isalpha(c)) r += toupper(c);
    }
    return r;
}
//Ci = (pi + ki) mod 26
string encrypt(string text, string key) {
    string res = "";
    int m = key.length();
    for (int i = 0; i < text.length(); i++) {
        // công thức dịch chuyển từng ký tự
        char c = (text[i] - 'A' + (key[i % m] - 'A')) % 26 + 'A';
        res += c;
    }
    return res;
}
//pi = (Ci - ki + 26) mod 26
string decrypt(string cipher, string key) {
    string res = "";
    int m = key.length();
    for (int i = 0; i < cipher.length(); i++) {
        char p = (cipher[i] - key[i % m] + 26) % 26 + 'A';
        res += p;
    }
    return res;
}
int main() {
    string key, text;
    int choice;
    while (true) {
        cout << "1. Ma hoa" << endl;
        cout << "2. Giai ma" << endl;
        cout << "0. Thoat chuong trinh" << endl;
        cout << "Lua chon cua ban: ";
        cin >> choice;
        cin.ignore();
        if (choice == 0) {
            break;
        }
        cout << "Nhap khoa: ";
        getline(cin, key);
        key = cleanText(key);
        if (choice == 1) {
            cout << "Nhap Plaintext: ";
            getline(cin, text);
            text = cleanText(text);
            cout << "Ket qua Ciphertext: " << encrypt(text, key) << endl;
        }
        else if (choice == 2) {
            cout << "Nhap Ciphertext: ";
            getline(cin, text);
            text = cleanText(text);
            cout << "Ket qua Plaintext: " << decrypt(text, key) << endl;
        }
        else {
            cout << "Lua chon khong hop le, vui long nhap lai!" << endl;
        }
        cout << "--------------------------" << endl;
    }
    return 0;
}
