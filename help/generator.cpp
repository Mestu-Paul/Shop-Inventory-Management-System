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
    int i=0,j=30;
    while(getline(cin,s)){
        if(s=="00")break;
        cout<<"# "<<s<<" (at left_frame1)"<<endl;
        cout<<"left_frame_1_lbl_"<<i<<" = tk.Label(left_frame_1,bg=left1_bg, anchor='w', font=('Times New Roman',14), text='"<<s<<" :')"<<endl;
        cout<<"left_frame_1_lbl_"<<i<<".place(x=5,y="<<j<<",relwidth=0.5)"<<endl;
        cout<<endl;
        i++;j+=30;
        // vs.push_back(s);
    }
}