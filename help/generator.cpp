#include <bits/stdc++.h>
using namespace std;
void file(){
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
}
int main(){
    file();
    string s;
    vector<string>vs;
    int i=0;
    while(getline(cin,s)){
        if(s=="00")break;
        cout<<"# "<<s<<" (at left_frame0)"<<endl;
        cout<<"left0_frame_btn_"<<i<<" = tk.Button(left_fram0,text=\""<<s<<"\", fg=left0_fg, bg=left01_bg, font=('Times New Roman1',10))"<<endl;
        cout<<"left0_frame_btn_"<<i<<".pack(side=tk.TOP,fill=tk.X,padx=5, pady=2)"<<endl;
        cout<<endl;
        // vs.push_back(s);
    }
}