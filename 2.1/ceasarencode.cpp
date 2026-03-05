#include <iostream>

using namespace std ;

int main() {
    string n ;
    int m ;
    string result = "" ;
    getline(cin,n) ;
    cin >> m ;
    for(int i=0;i<n.size();++i){
        char c = n[i] ;
        if(n[i] == ' '|| n[i] == ',' || n[i] == '.'){
            result +=c ;
            continue ;
        }
        else if(isupper(n[i])){
            c = (c - 'A' + m) % 26 + 'A' ;
            result += c ;
        }else if(islower(n[i])){
            c = (c - 'a' + m) % 26 + 'a' ;
            result += c ;
        }
    }
    cout << result ;
}