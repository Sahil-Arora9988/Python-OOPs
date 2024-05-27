class Station:
    def __init__(self,name,distance,cost):
        self.name=name
        self.distance = distance
        self.cost = cost

class Stations:
        def __init__(self):
            self.stations = [
                Station(name = "Beas",distance = 100, cost =40 ),
                Station(name = "Jalandhar",distance = 200, cost =55 ),
                Station(name = "Ludhiana",distance = 300, cost =80 ),
                Station(name = "Panipat",distance = 400, cost =105 ),
                Station(name = "Sonipat",distance = 500, cost =120 )
            ]


        def get_stations(self):
             options= ""
             for station in self.stations:
                  options = options + f"\n Name: {station.name}, Cost: {station.cost}"
             return options
                  
        
        def find_station(self,station_name):
            for station in self.stations:
                 if station.name == station_name: 
                     return station           
             





        