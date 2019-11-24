#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import numpy as np
import copy
import inspect

class debug (object):

    def __init__(self,):
        pass
    def __FILE__(self,frame):
        return frame.f_code.co_filename
    def __LINE__(self,frame):
        return frame.f_lineno

debug=debug()

"""city in country
        has rescueTeam"""
class City (object):

    def __init__(self, name):
        self.name = name
    
    def set_rescueTeam(self,rescueTeams):
        self.rescueTeam = rescueTeams
    
    def get_rescueTeam(self):
        return self.rescueTeam
    


"""country 
        has many city"""
class Country:

    def __init__(self,):
        self.rescueTeam_OnRoute = []
        self.Route = []
        self.shortest_path_num = 0
    
    # read initial data from terminal
    def init_from_input(self,):
        # city number, loads, location, destination
        #string = input("input initial data\n");
        string = input();
        array = string.split(' ')
        array = list(map(int,array))
        self.city_n = array[0]
        self.loads = array[1]
        self.location = array[2]
        self.destination = array[3]

        
        # cities initalization
        self.cities = []
        #string = input("input initial city data\n");
        string = input();
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
            #string = input("input initial distance data\n");
            string = input();
            array = string.split(' ')
            array = list(map(int,array))
            self.distance[array[0],array[1]] = array[2]
            self.distance[array[1],array[0]] = array[2]
            
    def dijikstra(self):
        pre_city = [[] for _ in range(self.city_n)] # pre_city = [[]]*city_n　是错误的,记录达到目的城市的上一个经过的城市
        visit = np.zeros(self.city_n)               # 到城市ｉ的最短路径是否确定
        route_num = np.zeros(self.city_n)           # 到城市ｉ的最短路劲数目
        route_team = np.zeros(self.city_n)          #　到城市ｉ的最短路径上最大救援人员
        route_team[self.location] = self.cities[self.location].get_rescueTeam()
        transfer = self.location                    # 中转站，当前距离出发点最近的城市
        dis = np.ones(self.city_n)*self.Maxdistance # 从出发点开始的距离
        dis[self.location] = 0;
        
        
        for i in range(self.city_n):
            if i==self.location or self.distance[self.location,i]<self.Maxdistance: #　仅能够直达的初始化ｐｒｅ为出发点
                pre_city[i].append(self.location)
                route_num[i] = 1;           # 直达的一条路径
            
        for i in range(self.city_n):
            Min_distance = self.Maxdistance;
            # find mix distance(location,transfer）
            for j in range(self.city_n):
                if visit[j]!=1 and Min_distance > dis[j]:
                    Min_distance = dis[j]
                    transfer = j
            
            visit[transfer] = 1
            if visit[self.destination] == 1:
                break
                
            # update pre_city
            for j in range(self.city_n):
                #print(transfer,j,visit)
                if visit[j]!=1 and self.distance[transfer,j]!= self.Maxdistance:
                    if dis[j] > dis[transfer]+self.distance[transfer,j]:
                        dis[j] = dis[transfer]+self.distance[transfer,j]
                        
                        route_num[j] = route_num[transfer]
                        route_team[j] = route_team[transfer] + self.cities[j].get_rescueTeam()
                        pre_city[j] = list([transfer])

                    elif dis[j] == dis[transfer]+self.distance[transfer,j]:
                        
                        route_num[j] += route_num[transfer]
                        pre_city[j].append(transfer)
                        if route_team[j]<(route_team[transfer]+self.cities[j].get_rescueTeam()):
                            route_team[j] = route_team[transfer]+self.cities[j].get_rescueTeam()
            
        #print(dir())
        #print("dijikstra:",pre_city,'\n')
        return pre_city,route_num,route_team
        
    def generate_Route(self,destination,route,rescueTeam,pretty_Route):
        for i in route[destination]:
            rescue = rescueTeam + self.cities[i].get_rescueTeam()
            if i==self.location:
                self.rescueTeam_OnRoute += list([rescue])       #　保存所有的路径对应的救援人员数据
                self.shortest_path_num += 1
                print(debug.__FILE__(inspect.currentframe()),debug.__LINE__(inspect.currentframe()),"generate_Route:",[self.location]+pretty_Route,self.rescueTeam_OnRoute[-1])
            else:
                self.generate_Route(i,route,rescue,copy.deepcopy(list([i])+pretty_Route))
        
        
if __name__ == '__main__':
    country = Country()
    country.init_from_input()
    pre,num,team = country.dijikstra()
    #print(country.cities, country.location,country.destination)
    #print(country.distance)
    country.generate_Route(country.destination,pre,country.cities[country.destination].get_rescueTeam(),list([country.destination]))
    #print(country.rescueTeam_OnRoute)
    #if(country.rescueTeam_OnRoute != []):
        #print(country.shortest_path_num,max(country.rescueTeam_OnRoute))
    print(debug.__FILE__(inspect.currentframe()),debug.__LINE__(inspect.currentframe()),pre)
    print(debug.__FILE__(inspect.currentframe()),debug.__LINE__(inspect.currentframe()),int(num[country.destination]),int(team[country.destination]))

