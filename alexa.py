import bs4 as bs
import requests
import json

def get_rank(page):
    """ get alexa rank """
    url = "https://www.alexa.com/siteinfo/" + page
    sauce = requests.get(url)
    soup = bs.BeautifulSoup(sauce.content,'html.parser')
    adiv = soup.findAll("div", {"class": "rank-global"})[0]
    i1 = str(adiv).find('hash')+14
    r = str(adiv)[i1:i1+100]
    i2 = r.find('</p')-1
    r = r[:i2]
    r = r.strip()
    r = r.replace(',','')
    r = int(r)
    return r

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

sites_ranked = dict()
#print (sites)
for site in sites[:]:
    rank = get_rank(site)
    print (site, "=>" , rank)
    sites_ranked[site] = rank

with open('sites_ranked.csv','w') as f:
    #sites_ranked_sorted = sorted(sites_ranked.items(), key=lambda x: x[1])
    for k,v in sites_ranked.items():
        f.write(k + '\t' + str(v) + '\n')

"""
with open('sites.json','w') as f:
    #sites_ranked_sorted = {k: v for k, v in sorted(sites_ranked.items(), key=lambda item: item[1])}
    sites_ranked_sorted = sorted(sites_ranked.items(), key=lambda x: x[1])
    x = json.dumps(sites_ranked_sorted,sort_keys=True,indent=4,separators=(',', ': '))
    f.write(x)
"""