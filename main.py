import googlemaps


gmaps = googlemaps.Client(key="AIzaSyC0CKSmvpDOZpAF8bCg6zUNVnOBueSghMI")  

def get_live_traffic(source, destination):
    result = gmaps.distance_matrix(source, destination, mode="driving", departure_time="now")
    
    try:
        traffic_time = result["rows"][0]["elements"][0]["duration_in_traffic"]["value"]
        return traffic_time
    except KeyError:
        print("Traffic data not available, using normal duration.")
        return result["rows"][0]["elements"][0]["duration"]["value"]


source = input("Enter the source location: ")
destination = input("Enter the destination location: ")


traffic_time = get_live_traffic(source, destination)


print(f"Live Traffic Time from {source} to {destination}: {traffic_time // 60} minutes")
