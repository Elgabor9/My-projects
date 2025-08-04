#include <bits/stdc++.h>
#define ll long long int
#define fr(n) for(ll i=0;i<n;i++)
#define frj(n) for(ll j=0;j<n;j++)
#define rf(n) for(ll i=n-1;i>0;i--)
#define rfj(n) for(ll j=n-1;j>0;j--)
#define Elgabor ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
#define pi 3.1415926535897932

const ll MOD = 1e9 + 7;
const ll N = 1e6;
using namespace std;
/*-----------------------------------------------*\
|       Accept Ya Maleka – no hack, no gear       |
|       AC with grace, the message is clear       |
\*-----------------------------------------------*/

int main()
{
    Elgabor
    ll t = 1;
    //cin >> t;
    while(t--){
        ll fav1=32,fav2=256,sum=0,mini;
        ll f2,f3,f5,f6;
        cin>>f2>>f3>>f5>>f6;
        mini=min(f2,f5);
        mini=min(mini,f6);
        sum+=mini*fav2;
        f2-=mini;
        sum+=min(f2,f3)*fav1;
        cout<<sum<<'\n';
    }
    return 0;
}