#include <bits/stdc++.h>
using namespace std ;



int main (){
    string s ;
    getline(cin,s) ;
    string test = "ETAOINSHRDLUCMFWYPVBGKJXQZ";
    map<char,int> mp ;
    for(int i=0;i<s.size();++i){
        char c = toupper(s[i]) ;
        if(c >= 'A' && c <= 'Z' ){
            mp[c]++ ;
        }
    }
    vector <pair<char,int>> v (mp.begin(),mp.end()) ;
    sort(v.begin(),v.end(),[](pair<char,int> a,pair<char,int> b){
        return a.second > b.second ;
    }) ;

    if(v.empty()) return 0;
    for(char x : test){
        int k = (v[0].first - x +26) %26;
        string result = "" ;
            for(int i=0;i<s.size();++i){
                char c = s[i] ;
                
                if(!isalpha(c)){
                    result +=c ;
                    continue ;
                }else if(isupper(c)){
                    c = (c - 'A' - k + 26) % 26 + 'A' ;
                    result += c ;
                }else if(islower(c)){
                    c = (c - 'a' - k + 26) % 26 + 'a' ;
                    result += c ;
                }
            }
        cout << "Check the text after decrypting, index of k is" << k << endl ; 
        cout << result << endl ;
        cout << "If the text is true, type 1. Otherwise type 0 \n" ;
        int hh ;
        cin >> hh ;
        if(hh) break ;
    }
}