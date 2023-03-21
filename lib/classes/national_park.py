import statistics
from statistics import mode
from .trip import Trip

class NationalPark:

    def __init__(self, name):
        self.set_name(name)
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if hasattr(self, "_name"):
            print("Cannot change Park name!")
        elif (type(name) is str):
            self._name = name
            self.natpark_trips = []
            self.visitor_list = []

    name = property(get_name, set_name)

    def trips(self):
        self.natpark_trips = []
        for trip in Trip.all:
            if trip.national_park == self:
                self.natpark_trips.append(trip)
        return self.natpark_trips

    def visitors(self):
        self.trips()
        self.visitor_list = []
        for trip in self.natpark_trips:
            if trip.visitor not in self.visitor_list:
                self.visitor_list.append(trip.visitor)
        return self.visitor_list

    def total_visits(self):
        self.trips()
        return len(self.natpark_trips)
    
    def best_visitor(self):
        self.visitors() 
        return(mode(self.visitor_list))

