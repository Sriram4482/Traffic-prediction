import googlemaps

class TrafficEnvironment:
    def __init__(self, api_key="AIzaSyC0CKSmvpDOZpAF8bCg6zUNVnOBueSghMI"):
        """Initialize the Traffic Environment with a Google Maps API Key."""
        self.gmaps = googlemaps.Client(key=api_key)
        print("TrafficEnvironment initialized!")

    def get_live_traffic(self, source, destination):
        """Fetch live traffic data from Google Maps API."""
        try:
            result = self.gmaps.distance_matrix(source, destination, mode="driving", departure_time="now")
            traffic_time = result["rows"][0]["elements"][0].get("duration_in_traffic", {}).get("value")
            if traffic_time:
                return traffic_time
            else:
                print("Traffic data not available, using normal duration.")
                return result["rows"][0]["elements"][0]["duration"]["value"]
        except Exception as e:
            print("Error fetching traffic data:", e)
            return None

    def run(self, source="Times Square, NY", destination="Central Park, NY"):
        """Run the traffic simulation and fetch live traffic data."""
        print("Running traffic simulation...")
        traffic_time = self.get_live_traffic(source, destination)
        if traffic_time is not None:
            print(f"Live Traffic Time (seconds): {traffic_time}")
        else:
            print("Could not retrieve traffic data.")
