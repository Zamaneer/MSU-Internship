#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:33:56 2020

@author: nabilz
"""

class Time(object):
    
    __hour = [i for i in range(25)]
    
    __mins = [i for i in range(61)]
    
    __secs = [i for i in range(61)]
    
    def __init__(self, hour = 0, minute = 0, sec = 0 ):
        
        '''Construct a Time using three integers '''
        
        self.__hour = hour
        self.__minute = minute
        self.__sec = sec
        
    def __repr__(self):
        
        '''Return a string to formally represent a Time'''
        
        rep_str = "Class Time: {:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__minute, self.__sec)

        return rep_str
    
    def from_str(self, time_str):
        
        '''Convert a string in form hh:mm:ss to a Time'''
        
        hour, minute, sec = [int(i) for i in time_str.split(":")]
        
        self.__hour = hour
        self.__minute = minute
        self.__sec = sec
        
    def add_time(self, time_toadd):
        
        ''' Adds a provided object (time_toadd) to self. Returns
            another time object that is the sum of the two'''
              
        sum_hours = self.__hour + time_toadd.__hour
        sum_minutes = self.__minute + time_toadd.__minute
        sum_secs = self.__sec + time_toadd.__sec

        if sum_secs >= 60:
            sum_minutes += 1
	
        if sum_minutes >= 60:
            sum_hours += 1
	
        new_minute = sum_minutes % 60
        new_sec = sum_secs % 60
        new_hour = sum_hours % 24
        
        added_time = Time(new_hour, new_minute, new_sec)
        
        return added_time
        
        
        
        
        