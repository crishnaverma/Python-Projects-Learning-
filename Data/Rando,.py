import json
with open("Data/data.json") as f:
    data = json.load(f)

num_dic={"one":1,"two":2, "three":3,"four":4,"five":5}
clean_data = []
unique_set = set()

def better_data(data):
    # for rating 
    for user in data:
        raw_data=str(user["rating"]).strip().lower()
        if raw_data in num_dic:
            raw_data=num_dic[raw_data]
            user["rating"] =raw_data

# for age
        raw_age = user.get("age")
        if raw_age == None:
            user["age"] = "none"
        
#removeing duplication
        if user["name"] in unique_set:
            continue
        unique_set.add(user["name"])
        clean_data.append(user)
    return clean_data 


print(better_data(data))
with open("Data/data.json", "w") as f:
    json.dump(clean_data, f)
