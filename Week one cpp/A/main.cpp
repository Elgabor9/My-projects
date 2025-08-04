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
        double n,sum=0;
        cin>>n;
        vector<double> v(n);
        fr(n) cin>>v[i];
        fr(n) sum+=v[i];
        double ans=sum/n;
        cout<<fixed<<setprecision(12)<<ans<<endl;
    }
    return 0;
}