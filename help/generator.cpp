#include <bits/stdc++.h>
using namespace std;
void file(){
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
}
string Replace(string s, char cur, char rep){
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    for(int i=0; i<s.size(); i++){
        if(s[i]==cur)s[i]=rep;
    }
    return s;
}
int main(){
    file();
    string s;
    vector<string>vs;
    int i=0,j=30;
    cout<<"[";
    while(getline(cin,s)){
        cout<<"'"<<s<<"',";
    }
    cout<<"]"<<endl;
}