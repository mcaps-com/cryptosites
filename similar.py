try:
    from requests import get
    from urllib.parse import urlparse
except ImportError as err:
    print(f"Failed to import required modules {err}")

def similarGet(website):
    #domain = '{uri.netloc}'.format(uri=urlparse(website))
    #domain = domain.replace("www.", "")
    ENDPOINT = 'https://data.similarweb.com/api/v1/data?domain=' + website
    #print (ENDPOINT)
    resp = get(ENDPOINT)

    if resp.status_code == 200:
        return resp.json()
    else:
        resp.raise_for_status()
        return False

def get_sites():
    with open('sites.csv', 'r') as f:
        lines = f.readlines()
        sites = list()
        for x in lines:
            x = x.replace('\n','')
            a = x.split('\t')
            #print (a[0], a[1])
            sites.append(a[0])

    return sites

sites = get_sites()

#sites = ["coinmarketcap.com", "coingecko.com"]
with open('sites_ranked_similar.csv','w') as f:
    for site in sites:
        try:
            r = similarGet(site)
            rank = r['GlobalRank']['Rank']
            print (site,"=>",rank)
            f.write(site+","+str(rank) + '\n')
        except:
            print ("no rank for ", site)
            continue
