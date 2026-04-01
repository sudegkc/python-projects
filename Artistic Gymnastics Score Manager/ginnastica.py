def read_file(fileName):
    data=list()
    try:
        with open(fileName,"r") as inf:
            for line in inf:
                line=line.strip()
                if not line:
                    continue
                parts=line.split()
                name=parts[0]
                surname=parts[1]
                sex=parts[2]
                country=parts[3]
                try:
                    scores=[]
                    for x in parts[4:9]:
                        x=float(x)
                        scores.append(x)
                except ValueError:
                    continue
                scores.sort()
                final_score=sum(scores[1:4])

                data.append({
                    "full_name":f"{name} {surname}",
                    "sex":sex,
                    "country":country,
                    "score":final_score

                })
    except OSError:
        exit("error opening the file!")
    return data

def main():
    data=read_file("scores.txt")
    
    female_athletes=[]
    for a in data:
        if a["sex"]=="F":
            female_athletes.append(a)
            
    if female_athletes:
        winner=max(female_athletes,key=lambda x: x["score"])
        print("Female winner:")
        print(f"{winner["full_name"]}, {winner["country"]} - Score {winner["score"]:.1f}\n")
    
    nations=dict()
    for a in data:
        country=a["country"]
        nations[country]=nations.get(country,0) + a["score"]
    
    sorted_nations=sorted(nations.items(), key=lambda x: x[1], reverse=True)

    print("Overall nations ranking: ")
    for i, (country,score) in enumerate(sorted_nations[:3],1):
        print(f"{i}) {country}- Total score: {score:.1f} ")
if __name__=="__main__":
    main()