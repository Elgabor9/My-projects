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
        ll n,sum1=0,sum2=0;
        cin >> n;
        vector<vector<ll>> v(n,vector<ll>(n));
        for(ll i=0;i<n;i++)
        {
            for(ll j=0;j<n;j++)
            {
                cin >> v[i][j];
            }
        }
        for(ll i=0;i<n;i++)
        {
            sum1+=v[i][i];
        }
        for(ll i=0;i<n;i++)
        {
            sum2+=v[i][n-1-i];
        }
        cout<<abs(sum1-sum2)<<'\n';
    }
    return 0;
}