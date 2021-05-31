#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s="wsam ie pjo ysgtm eyipbya .P axg niphay y,\n mey syw ahgm ewhrg tw hmysyam wh meyiepjo\n ys .Ag jygtmeyk pmys ie pjo ysavw kkoyjgsy\n whmy sy amwh rmephmewagh y!Me yigu ynay utg\n smew ajya apr ywap awjfkya no a mwmnmw\n ghiwfeyswhve wieuwr wm aepby oyyhae wtmy\n uox8 fkpiya. Me y fpaavgs uwa mxSrN03u wd\n dvwmegnmmey dngmya. Mew awameyt";
    float l=s.size();
    map<char, int> freq;
    map<char, char> Map;

    float len=0;

    cout<<s<<"\n"<<endl;
    for(int i=0;i<l;i++)
    {
        freq[s[i]]++;
        if((s[i]>=65 && s[i]<=90)||(s[i]>=97 && s[i]<=122))
            len++;
    }

    cout<<"Observed Frequencies"<<endl;
    for(auto it:freq)
    {
        if((it.first>=65 && it.first<=90)||(it.first>=97 && it.first<=122))
        cout<<it.first<<" : "<<it.second<<" = "<<(it.second/len)*100<<"%"<<endl;
    }

    Map['a']='s'; Map['b']='v'; Map['d']='q'; Map['e']='h'; Map['f']='p'; Map['g']='o'; Map['h']='n'; Map['i']='c'; Map['j']='m'; Map['k']='l';
    Map['m']='t'; Map['n']='u'; Map['o']='b'; Map['p']='a'; Map['r']='g'; Map['s']='r'; Map['t']='f'; Map['u']='d'; Map['v']='w'; Map['w']='i';
    Map['x']='y'; Map['y']='e'; Map['A']='S'; Map['M']='T'; Map['N']='U'; Map['P']='A'; Map['S']='R';
    // Digits are backward shifted by 4
    Map['0']='6'; Map['3']='9'; Map['8']='4';

    cout<<"\n  Decrypted text : \n"<<endl;
    for(int i=0;i<l;i++)
    {
        if((s[i]>=65 && s[i]<=90)||(s[i]>=97 && s[i]<=122) || s[i]=='8' || s[i]=='0' || s[i]=='3')
            s[i]=Map[s[i]];
    }

    cout<<s<<endl;
    return 0;
}
