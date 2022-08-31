import requests
def getMarketingOptIn(val,api):
    ans_list = []
    if val== None :
        return ans_list
    list_of_strings = val.split(',')
    list_of_integers = [int(x) for x in list_of_strings] 
    url = "https://api.pipedrive.com/v1/personFields?&api_token="+api
    data = requests.get(url).json()
    for i in data["data"]:
        if(i["key"]=="f5257f743ab8c87c2a67dac9413058ce8ac18951"):
            for j in i["options"]:
                for k in list_of_integers:
                    if(k==j["id"]):
                        ans_list.append(j["label"]);
                
    return ans_list;