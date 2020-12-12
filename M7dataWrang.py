# -*- coding: utf-8 -*-

""" The data file for this is WburgWeather.csv """

""" Write programming code to create the cleansed DataFrame here 
    using the variable name dfWeather for your DataFrame as directed 
    in the assignment.     

##make sure the working directory is set properly for a clean import                                           """
import pandas as pd
#map return cleanly
def VRB(row):
    if row['HOURLYWindDirection'] == 'VRB':
        return 'Variable Direction'

dfWeather = pd.read_csv('WburgWeather.csv')

print('Column Labels: ',dfWeather.columns.values)

dfWeather.dropna(subset = ['HOURLYDRYBULBTEMPF'],inplace=True)
dfWeather.dropna(subset = ['HOURLYWETBULBTEMPF'],inplace=True)
dfWeather.dropna(subset = ['HOURLYDewPointTempF'],inplace=True)


dfWeather['HOURLYDRYBULBTEMPF'] = pd.to_numeric(dfWeather['HOURLYDRYBULBTEMPF'], errors='coerce')

dfWeather['HOURLYDRYBULBTEMPC'] = (dfWeather['HOURLYDRYBULBTEMPF']-32)/1.8

dfWeather['HOURLYWETBULBTEMPF'] = pd.to_numeric(dfWeather['HOURLYWETBULBTEMPF'], errors='coerce')
dfWeather['HOURLYWETBULBTEMPC'] = (dfWeather['HOURLYWETBULBTEMPF']-32)/1.8
dfWeather['HOURLYDewPointTempF'] = pd.to_numeric(dfWeather['HOURLYDewPointTempF'], errors='coerce')
dfWeather['HOURLYDewPointTempC'] = (dfWeather['HOURLYDewPointTempF']-32)/1.8

dfWeather['HOURLYWindDirection' ] = dfWeather.apply(VRB,axis='columns')
#make new csv with updates
dfWeather.to_csv('newWeather.csv',index=False)