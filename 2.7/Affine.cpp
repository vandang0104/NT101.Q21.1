#include <iostream>
#include <string>

using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int modInverse(int a, int m) {
    a = a % m;
    for (int x = 1; x < m; x++) {
        if ((a * x) % m == 1) {
            return x;
        }
    }
    return -1; 
}

string cleanText(string text) {
    string r = "";
    for (char c : text) {
        if (isalpha(c)) r += toupper(c);
    }
    return r;
}

string encryptAffine(string text, int a, int b) {
    string cipher = "";
    for (char c : text) {
        int x = c - 'A';
        int encryptedChar = (a * x + b) % 26;
        cipher += (char)(encryptedChar + 'A');
    }
    return cipher;
}

string decryptAffine(string cipher, int a, int b) {
    string plain = "";
    int a_inv = modInverse(a, 26);
    
    if (a_inv == -1) return "Loi: Khong ton tai nghich dao modulo!";

    for (char c : cipher) {
        int y = c - 'A';
        int decryptedChar = (a_inv * (y - b + 26)) % 26;
        plain += (char)(decryptedChar + 'A');
    }
    return plain;
}

int main() {
    cout << "=== CHUONG TRINH MAT MA AFFINE ===\n\n";

    int a ;
    int b ;
    cout << "Nhap a: " ;
    cin >> a ;
    cout << "Nhap b: " ;
    cin >> b ;
    string plaintext ;
    cout << "Nhap plain text: " ;
    cin.ignore() ;
    getline(cin,plaintext) ;

    cout << "Khoa K = (a = " << a << ", b = " << b << ")\n";
    
    if (gcd(a, 26) != 1) {
        cout << "Khoa 'a' khong hop le! Phai nguyen to cung nhau voi 26.\n";
        return 0;
    }

    string cleanPlain = cleanText(plaintext);
    cout << "Ban ro ban dau     : " << cleanPlain << endl;
    
    string ciphertext = encryptAffine(cleanPlain, a, b);
    cout << "Ban ma (Ciphertext): " << ciphertext << endl;

    string decryptedText = decryptAffine(ciphertext, a, b);
    cout << "Ban ro sau giai ma : " << decryptedText << endl;

    if (cleanPlain == decryptedText) {
        cout << "\n=> KET LUAN: Chuong trinh hoat dong CHINH XAC!" << endl;
    }

    return 0;
}