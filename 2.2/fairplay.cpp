#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<vector<char>> matrix(5, vector<char>(5));
pair<int,int> pos[26];

string clean(string s){
    string r = "";
    for(char c : s){
        if(isalpha(c)){
            c = toupper(c);
            if(c == 'J') c = 'I';
            r += c;
        }
    }
    return r;
}

void createMatrix(string key){
    string alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    set<char> used;
    string s = "";

    key = clean(key);

    for(char c : key){
        if(!used.count(c)){
            used.insert(c);
            s += c;
        }
    }

    for(char c : alphabet){
        if(!used.count(c)){
            s += c;
        }
    }

    int k = 0;
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            matrix[i][j] = s[k];
            pos[s[k]-'A'] = {i,j};
            k++;
        }
    }
}

string makePairs(string text){
    string r="";
    text = clean(text);

    for(int i=0;i<text.size();i++){
        r+=text[i];
        if(i+1<text.size()){
            if(text[i]==text[i+1]){
                r+='X';
            }
        }
    }

    if(r.size()%2) r+='X';

    return r;
}

string encrypt(string text){
    string r="";

    for(int i=0;i<text.size();i+=2){
        char a=text[i];
        char b=text[i+1];

        int r1=pos[a-'A'].first;
        int c1=pos[a-'A'].second;

        int r2=pos[b-'A'].first;
        int c2=pos[b-'A'].second;

        if(r1==r2){
            r+=matrix[r1][(c1+1)%5];
            r+=matrix[r2][(c2+1)%5];
        }
        else if(c1==c2){
            r+=matrix[(r1+1)%5][c1];
            r+=matrix[(r2+1)%5][c2];
        }
        else{
            r+=matrix[r1][c2];
            r+=matrix[r2][c1];
        }
    }

    return r;
}

int main(){

    string key ;
    cout << "nhap key(Khong cach, so, ki tu): "  ;
    cin >> key ;
    string text ;
    cin >> text ;

    createMatrix(key);

    text = makePairs(text);

    cout << "key matrix\n" ;
    for(int i = 0 ;i<5 ; ++i){
        for(int j = 0;j < 5 ; ++j){
            cout << matrix[i][j] << " " ;
        }
        cout << endl ;
    }

    cout<<"Cipher text: "<<encrypt(text);

}