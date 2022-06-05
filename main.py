import riotapi

def main():
    api = riotapi.RiotAPI('RGAPI-5f9cab76-1498-4f5c-bbd8-cee57c644fab')
    r = api._request()
    print(r['puuid'])

if __name__ == "__main__":
    main()