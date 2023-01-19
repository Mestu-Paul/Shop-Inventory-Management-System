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
    while(getline(cin,s)){
        cout<<"left_frame_entry"<<Replace(s,' ','_')<<" = tk.Entry(left_frame)"<<endl;
        cout<<"left_frame_entry"<<Replace(s,' ','_')<<".place(relx=0.48,rely="<<0.01+i*0.08<<",relwidth=0.5,relheight=0.06)"<<endl;
        i++;
        cout<<endl;
    }
}