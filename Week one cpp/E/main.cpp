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


int main()
{
    Elgabor
    ll t = 1;
    //cin >> t;
    while(t--){
        ll s,e,a,b,m,n,app=0,ora=0;
        cin>>s>>e>>a>>b>>m>>n;
        vector<ll> apples(m),oranges(n);
        fr(m)
        {
            ll x;
            cin>>x;
            apples[i]=x+a;
        }
        fr(n)
        {
            ll x;
            cin>>x;
            oranges[i]=x+b;
        }
        fr(m) if (apples[i]>=s&&apples[i]<=e) app++;
        fr(n) if (oranges[i]>=s&&oranges[i]<=e) ora++;
        cout<<app<<'\n'<<ora<<'\n';
    }
    return 0;
}