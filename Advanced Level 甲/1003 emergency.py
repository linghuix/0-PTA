#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import numpy as np

"""city in country
        has rescueTeam"""
class City (object):

    def __init__(self, name):
        self.name = name
    
    def set_rescueTeam(self,rescueTeams):
        self.rescueTeam = rescueTeams
    
    def get_rescueTeam(self):
        pass
    


"""country 
        has many city"""
class Country:

    def __init__(self,):
        pass
    
    # read initial data from terminal
    def init_from_input(self,):
        # city number, loads, location, destination
        string = input("input initial data\n");
        array = string.split(' ')
        array = list(map(int,array))
        self.city_n = array[0]
        self.loads = array[1]
        self.location = array[2]
        self.destination = array[3]
        
        # cities initalization
        self.cities = []
        string = input("input initial city data\n");
        array = string.split(' ')
        array = list(map(int,array))
        for i in range(self.city_n):
            city = City(i)
            city.set_rescueTeam(array[i])
            self.cities.append(city)
        
        # 
        self.Maxdistance = 10000
        self.distance = np.ones((self.city_n,self.city_n))*self.Maxdistance
        for i in range(self.loads):
            string = input("input initial distance data\n");
            array = string.split(' ')
            array = list(map(int,array))
            self.distance[array[0],array[1]] = array[2]
            
    def dijikstra(self):
        pre_city = np.zeros(self.city_n)
        complete = np.zeros(self.city_n)
        complete[self.location] = 1
        shortest_path_num = 1
        transfer = self.location
        
        for i in range(self.city_n):
            pre_city[i] = self.location
            
        for i in range(self.city_n):
            Min_distance = self.Maxdistance;
            # find mix distance(location,transfer）
            for j in range(self.city_n):
                if complete[j]!=1 and Min_distance > self.distance[transfer,j]:
                    Min_distance = self.distance[transfer,j]
                    transfer = j
            complete[transfer] = 1
            # update pre_city
            for j in range(self.city_n):
                if complete[j]!=1 and self.distance[transfer,j]!= self.Maxdistance and self.distance[self.location,j] > self.distance[self.location,transfer]+self.distance[transfer,j]:
                    self.distance[self.location,j] = self.distance[self.location,transfer]+self.distance[transfer,j]
                    pre_city[j] = transfer
                if j == self.destination and self.distance[self.location,j] == self.distance[self.location,transfer]+self.distance[transfer,j]:
                    shortest_path_num += 1
        print(pre_city,shortest_path_num)
        
    
if __name__ == '__main__':
    country = Country()
    country.init_from_input()
    country.dijikstra()
    print(country.cities, country.location,country.destination)
    print(country.distance)
    #sys.exit(main())





