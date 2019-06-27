#include<iostream>
#include<vector>
#include<utility>
#include<queue>
#include<stack>
#include<math.h>
#include<algorithm>
#include<string>
using namespace std;
#define whatis(x) cout<<#x<<" : "<<x<<endl

int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int hashfn[10] = {} ;
int months(int i) {
    int temp = i;
        int l  = temp % 10;
        temp = temp / 10;
        if( ( l != temp ) && hashfn[l]>0 && hashfn[temp] > 0)  {
            hashfn[l]--;
            hashfn[temp]--;
            return i;
        }
        else if( l == temp && hashfn[l]>1 ) {
                hashfn[l]--;
                hashfn[l]--;
                return i;
        }
return -1;
}
vector<int> switch2pre (vector<int> &upd) {
    vector<int> upd2(10, 0);
    for(int i = 0; i<10; i++) {
        hashfn[i] = upd[i];
        upd2[i] = upd[i];
    }
    return upd2;
}
vector<int> updated () {
    vector<int> upd2(10, 0);
    for(int i = 0; i<10; i++) {

        upd2[i] = hashfn[i];
    }
    return upd2;

}
int main() {

    vector<int> upd(10, 0);
    for(int i = 0; i<12; i++) {
        int d;
        char ch;
        cin>>d;
        if(i != 11)
        cin>>ch;
        hashfn[d]++;
        upd[d]++;
    }

    //initialised
     int mm = -1, dd = -1, hh = -1, ss = -1;
    for(int i = 12; i>0; i--) {
        //For MONTHS
        vector<int> upd2 = switch2pre(upd);

        mm = months(i);

        if(mm != -1) {

            upd2 = updated();

            for(int j = days[i-1]; j>0; j--) {

                vector<int> upd3 = switch2pre(upd2);

                dd = months(j);

                if(dd!=-1)
                    {

                    upd3 = updated();

                    for(int k =23; k>=0; k--)
                        {

                        vector<int> upd4 = switch2pre(upd3);

                        hh = months(k);

                        if(hh != -1) {

                            upd4 = updated();

                               for(int z = 59; z>=0; z-- )
                                {

                              vector<int> upd5 = switch2pre(upd4);

                            ss = months(z);

                        if(ss != -1) break;
                        }
                    if(ss!=-1)
                    break;
                    }

                    }
            if(ss!=-1)
            break;
                }
            }
        if(ss!=-1)
        break;
        }
    }
    if( mm == -1 || ss == -1 || dd == -1 | hh == -1)
        cout<<0;
    else

    cout << mm<< "/" << dd<< "/" << hh << " :" <<  ss ;

    return 0;
}
