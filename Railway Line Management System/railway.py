def read_trips(filename):
    """Read the trip database"""
    data= dict()
    try:
        with open(filename) as trips_file:
            for line in trips_file:
                parts = line.split()
                trip_code = parts.pop(0)
                data[trip_code] = list()
                for info in parts:
                    train, hour, minute = info.split(':')
                    data[trip_code].append((train, (int(hour), int(minute))))
    except:
        print(f"Yeuch. Can't read \"{filename}\"")
        data = dict()
    return data

def read_operations(fileName):
    operations=list()
    try:
        with open(fileName,"r") as inf:
            for line in inf:
                operations.append(tuple(line.split()))
    except OSError:
        exit("error opening the file!")
    print(operations)
    return operations

def find_trips(data,station):
    trips=dict()
    for id,stop in data.items():
        for s, time in stop:
            if s==station:
                trips[id]=time
    return trips

def print_stations(data):
    stations=set()
    for stops in data.values():
        for s,_ in stops:
            stations.add(s)
        print("Ordered list of stations served: ", ", ".join(sorted(stations)), ".", sep='')


def print_trips_from(data,station,time):
    trips=find_trips(data,station)
    tmp=[]
    for trip_id , stops in trips.items():
        final_destination=data[trip_id][-1][0]
        if stops > time and final_destination != station:
            tmp.append(f"{id} {stops[0]:02d}:{stops[1]:02d} bound for {final_destination}")
    print (f"timetable for {station} station from {time[0]:02d}:{time[1]:02d} onwards: ", 
           "; ".join(tmp),
           ".",
           sep="",
           )


def print_shortest_journey(data,departure,time,arrival):
    trips_from=find_trips(data,departure)
    trips_to=find_trips(data,arrival)
    tmp=[]
    for id in set(trips_from) & set(trips_to):
        if time <= trips_from[id] < trips_to[id]:
            travel_time=60*(trips_to[id][0]- trips_from[id][0] +(trips_to[id][1]- trips_from[id][1]))
            tmp.append((travel_time,id))
    tmp.sort()
    travel_time,id=tmp[0]
    print(
        f"Shortest journey from {departure} to {arrival} from {time[0]:02d}:{time[1]:02d} onwards "
        + f"Train: {id} Departure: {departure} {trips_from[id][0]:02d}:{trips_from[id][1]:02d}; "
        + f"Arrival: {arrival} {trips_to[id][0]:02d}:{trips_to[id][1]:02d}; "
        + f"Journey Duration: {travel_time//60}h {travel_time%60}min."
    )


def main():
    data=read_trips("corse.txt")
    for operation in read_operations("operazioni.txt"):
        if operation[0]=="Stazioni":
            print_stations(data)
        elif operation[0]=="Orario":
            h,m=operation[2].split(":")
            print_trips_from(data, operation[1], (int(h), int(m)))

        elif operation[0]=="Viaggio":
            h,m=operation[2].split(":")
            print_shortest_journey(data, operation[1],(int(h), int(m)), operation[3])
        print()        
main()