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
    cin >> t;
    while(t--){
        ll n,ans=1;
        cin>>n;
        fr(n)
        {
            ll a=i,b=a*2;
            if (b<=n) ans=max(ans,gcd(a,b));
            else break;
        }
        cout<<ans<<"\n";
    }
    return 0;
}