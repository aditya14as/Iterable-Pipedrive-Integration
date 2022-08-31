import requests
def getProgramAttended(val,api):
    ans_list = []
    if val== None :
        return ans_list
    list_of_strings = val.split(',')
    list_of_integers = [int(x) for x in list_of_strings] 
    url = "https://api.pipedrive.com/v1/personFields?&api_token="+api
    data = requests.get(url).json()
    for i in data["data"]:
        if(i["key"]=="15cecbf33424293b1c095ebe2bd1457447f74f63"):
            for j in i["options"]:
                for k in list_of_integers:
                    if(k==j["id"]):
                        ans_list.append(j["label"]);
                
    return ans_list;