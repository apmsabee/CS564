import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime

from guizero import App, Window, PushButton, Text, TextBox, Combo, MenuBar, ListBox
from guizero import Text, Picture, Drawing, Box, TitleBox
from guizero import info, warn, error, yesno, question

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import Tk, Label

from guizero import App, Text, TextBox, PushButton, Slider, Picture, CheckBox, Combo, ListBox, ButtonGroup, info
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    
def page1_get_info(query_no, season, date, hometeam, visitteam, inn, bat, bowl):
    query_path = 'page_1_query' + str(query_no) + '.txt'
    with open(query_path, 'r') as sqlfile:
        query = sqlfile.read()
    query = query.replace('\n', ' ')
    query = query.replace('\t', ' ')

    if season == 'All':
        query = query.replace(' season_filter_fd',' 1 = 1')
    else:
        query = query.replace(' season_filter_fd',' YEAR(match_date) = ' + str(season))
    if date == 'All':
        query = query.replace(' match_date_filter_fd',' 1 = 1')
    else:
        query = query.replace(' match_date_filter_fd',' match_date = "' + str(date) + '"')
    if hometeam == 'All':
        query = query.replace(' team_filter_fd',' 1 = 1')
    else:
        query = query.replace(' team_filter_fd',' team_name = "' + str(hometeam) + '"')
    if visitteam == 'All':
        query = query.replace(' opposite_team_filter_fd',' 1 = 1')
    else:
        query = query.replace(' opposite_team_filter_fd',' team_name = "' + str(visitteam) + '"')
    if inn == 'All':
        query = query.replace(' innings_filter_fd',' 1 = 1')
    else:
        query = query.replace(' innings_filter_fd',' innings_no = ' + str(inn))
    if bat == 'All':
        query = query.replace(' batter_name_filter_fd',' 1 = 1')
    else:
        query = query.replace(' batter_name_filter_fd',' player_name = "' + str(bat) + '"')
    if bowl == 'All':
        query = query.replace(' bowler_name_filter_fd',' 1 = 1')
    else:
        query = query.replace(' bowler_name_filter_fd',' player_name = "' + str(bowl) + '"')
    
    return query

def page2_get_info(query_no, season, date, team, player, opp_team):
    query_path = 'page_2_query' + str(query_no) + '.txt'
    with open(query_path, 'r') as sqlfile:
        query = sqlfile.read()
    query = query.replace('\n', ' ')
    query = query.replace('\t', ' ')

    if season == 'All':
        query = query.replace(' season_filter_fd',' 1 = 1')
    else:
        query = query.replace(' season_filter_fd',' YEAR(match_date) = ' + str(season))
    if date == 'All':
        query = query.replace(' match_date_filter_fd',' 1 = 1')
    else:
        query = query.replace(' match_date_filter_fd',' match_date = "' + str(date) + '"')
    if team == 'All':
        query = query.replace(' team_filter_fd',' 1 = 1')
    else:
        query = query.replace(' team_filter_fd',' team_name = "' + str(team) + '"')
    if opp_team == 'All':
        query = query.replace(' opposite_team_filter_fd',' 1 = 1')
    else:
        query = query.replace(' opposite_team_filter_fd',' team_name = "' + str(opp_team) + '"')
    if player == 'All':
        query = query.replace(' player_name_filter_fd',' 1 = 1')
    else:
        query = query.replace(' player_name_filter_fd',' player_name = "' + str(player) + '"')
    
    return query
    
    
def page3_get_info(query_no, season, date, team):
    query_path = 'page_3_query' + str(query_no) + '.txt'
    with open(query_path, 'r') as sqlfile:
        query = sqlfile.read()
    query = query.replace('\n', ' ')
    query = query.replace('\t', ' ')

    if season == 'All':
        query = query.replace(' season_filter_fd',' 1 = 1')
    else:
        query = query.replace(' season_filter_fd',' YEAR(match_date) = ' + str(season))
    if date == 'All':
        query = query.replace(' match_date_filter_fd',' 1 = 1')
    else:
        query = query.replace(' match_date_filter_fd',' match_date = "' + str(date) + '"')
    if team == 'All':
        query = query.replace(' team_filter_fd',' 1 = 1')
    else:
        query = query.replace(' team_filter_fd',' team_name = "' + str(team) + '"')
    
    return query
    
    
