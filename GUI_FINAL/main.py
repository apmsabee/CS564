def page1_update_info():
    date = page1_combo_date.value + '-' + page1_combo_season.value
    date = datetime.strptime(date, '%d-%b-%Y')
    date = datetime.strftime(date, '%Y-%m-%d')

    query1 = utils.page1_get_info(page1_combo_season.value, date, page1_combo_hometeam.value,
                    page1_combo_visitteam.value, page1_combo_inn.value, page1_combo_bat.value, page1_combo_bowl.value
                    )
    df = pd.read_sql(query1, db)
    if df.empty:
        n_four = 0
        n_six = 0
    elif 4 not in df['Boundary_Type']:
        n_four = 0
        n_six = df[df['Boundary_Type']==6]['Number_of_Boundaries'].iloc[0]
    elif 6 not in df['Boundary_Type']:
        n_four = df[df['Boundary_Type']==4]['Number_of_Boundaries'].iloc[0]
        n_six = 0
    else:
        n_four = df[df['Boundary_Type']==4]['Number_of_Boundaries'].iloc[0]
        n_six = df[df['Boundary_Type']==6]['Number_of_Boundaries'].iloc[0]
    four_text.value = str(n_four)
    six_text.value = str(n_six)


def page2_update_info():
    leftTeamBox2.text = page2_combo_p1.value
    rightTeamBox2.text = page2_combo_p2.value
    # update attributes using query, catch errors in inputs
    return None


def page3_get_info(season, date, team1, team2):
    #     query = "select count(match_winner_id) from matchinfo where match_winner_id = %s"
    #     val = (str(team_id),)
    #     cursor.execute(query, val)
    #     return cursor.fetchall()[0][0]
    team_id1 = team[team['team_name'] == team1]['team_id'].values[0]
    team_id2 = team[team['team_name'] == team2]['team_id'].values[0]
    #     no_of_wins = match[match['match_winner_id']==int(team_id)].shape[0]
    return [team_id1] * 7, [team_id2] * 7


def page3_update_info():
    team1_info, team2_info = page3_get_info(page3_combo_season.value, page3_combo_date.value,
                                            page3_combo_team1.value, page3_combo_team2.value)

    leftTeamBox.text = page3_combo_team1.value
    rightTeamBox.text = page3_combo_team2.value

    matchcount1_text.value = str(team1_info[0])
    win1_text.value = str(team1_info[1])
    wr1_text.value = str(team1_info[2])
    sr1_text.value = str(team1_info[3])
    eco1_text.value = str(team1_info[4])

    matchcount2_text.value = str(team2_info[0])
    win2_text.value = str(team2_info[1])
    wr2_text.value = str(team2_info[2])
    sr2_text.value = str(team2_info[3])
    eco2_text.value = str(team2_info[4])


def write_to_db():
    #need some way to save the notes taken on players and teams
    return None


# Window Creation

home_page = App(title="Home Page", layout="grid", height=800, width=1200)
page_1 = Window(home_page, title="Match Stats", height=800, width=1200)
page_2 = Window(home_page, title="Player Stats", height=800, width=1200)
page_3 = Window(home_page, title="Team Stats", height=800, width=1200)

# HOME PAGE WIDGETS

introText = Text(home_page, text="Welcome To Cricket Pulse!", grid=[1, 0])
fillerText = Text(home_page, text="", grid=[0, 0])  # needs more formatting to center properly

open_match_button = PushButton(home_page, text="Match Search", command=open_page_1, grid=[0, 1], padx=20)
open_player_button = PushButton(home_page, text="Player Comparison", command=open_page_2, grid=[1, 1])
open_team_button = PushButton(home_page, text="Team Comparison", command=open_page_3, grid=[2, 1])

# PAGE 1 WIDGETS

# Header Widgets

title1_box = Box(page_1, align="top", width="fill", height=50, border=True, layout="grid")
pg1_title_filler1 = Text(title1_box, text="", width=4, grid=[0, 0])
close_match_button = PushButton(title1_box, text="Close current Page", command=return_home, width=12, grid=[1, 0])
pg1_title_filler2 = Text(title1_box, text="", width=34, grid=[2, 0])
title1Text = Text(title1_box, text="Cricket Pulse Match Comparison", grid=[3, 0])

# Search Widgets
seasons, dates, teams, inns, players = get_page1_filters()

match_query_box = TitleBox(page_1, align="top", width="fill", height=120, border=True, text="Search", layout="grid")
pg1_query_filler = Text(match_query_box, text="", width="20", grid=[0, 0])

seasonSel1 = Text(match_query_box, text="Season:", grid=[1, 0], align="right")
page1_combo_season = Combo(match_query_box, options=seasons, grid=[2, 0])

dateSel = Text(match_query_box, text="Match Date:", grid=[3, 0], align="right")
page1_combo_date = Combo(match_query_box, options=dates, grid=[4, 0])

teamText = Text(match_query_box, text="Team:", grid=[5, 0], align="right")
page1_combo_hometeam = Combo(match_query_box, options=teams, grid=[6, 0])
team_sel_buffer = Text(match_query_box, text="Opponent Team: ", grid=[7, 0])
page1_combo_visitteam = Combo(match_query_box, options=teams, grid=[8, 0])

inningSel = Text(match_query_box, text="Inning:", grid=[9, 0], align="right")
page1_combo_inn = Combo(match_query_box, options=inns, grid=[10, 0])

batsmanSel = Text(match_query_box, text="Batsman:", grid=[11, 0], align="right")
page1_combo_bat = Combo(match_query_box, options=players, grid=[12, 0])

bowlerSel = Text(match_query_box, text="Bowler:", grid=[13, 0], align="right")
page1_combo_bowl = Combo(match_query_box, options=players, grid=[14, 0])

row_filler = Text(match_query_box, text="", width=10, grid=[0, 1])
PushButton(match_query_box, text='Search', command=page1_update_info, grid=[6, 2], align="right")

# SEARCH RESULTS
dataBox = TitleBox(page_1, text="Search Results", height=500, width="fill", border=True, align="top", layout="grid")

boundariesBox = TitleBox(dataBox, text="Boundaries", height=160, width=590, border=True, grid=[0, 1])
four_label = Text(boundariesBox, text='No. of Fours: ', grid=[0, 0], width=60, height=5, align="right")
four_text = Text(boundariesBox, text='', grid=[1, 0], align="left")
six_label = Text(boundariesBox, text='No. of Sixes: ', grid=[0, 1], width=60, height=5, align="right")
six_text = Text(boundariesBox, text='', grid=[1, 1], align="left")

runsBox = TitleBox(dataBox, text="Runs by Over", height=160, width=590, border=True, grid=[0, 0])

wicketTypeBox = TitleBox(dataBox, text="Wickets by Type", height=160, width=590, border=True, grid=[1, 1])
wicketOverBox = TitleBox(dataBox, text="Wickets by Over", height=160, width=590, border=True, grid=[1, 0])

battersBox = TitleBox(dataBox, text="Top Batters", height=160, width=590, border=True, grid=[0, 2])
takersBox = TitleBox(dataBox, text="Top Wicket-Takers", height=160, width=590, border=True, grid=[1, 2])

# PAGE 2 WIDGETS

# Header Widgets
title2_box = Box(page_2, align="top", width="fill", height=50, border=True, layout="grid")
pg2_title_filler1 = Text(title2_box, text="", width=4, grid=[0, 0])
close_player_button = PushButton(title2_box, text="Close current Page", command=return_home, width=12, grid=[1, 0])
pg2_title_filler3 = Text(title2_box, text="", width=2, grid=[2, 0])
save_player_button = PushButton(title2_box, text="Save Notes", command=write_to_db, width=12, grid=[3,0])
pg2_title_filler2 = Text(title2_box, text="", width=20, grid=[4, 0])
title2Text = Text(title2_box, text="Cricket Pulse Player Comparison", grid=[5, 0])

match['match_date'] = pd.to_datetime(match['match_date'])

# Search Widgets
player_query_box = TitleBox(page_2, align="top", width="fill", height=140, border=True, text="Search", layout="grid")
pg2_query_filler = Text(player_query_box, text="", width="20", grid=[0, 0])

seasonSel2 = Text(player_query_box, text="Season:", grid=[1, 0], align="right")
page2_combo_season = Combo(player_query_box, options=list(match['match_date'].dt.strftime('%Y').unique()) + ['All'],
                           grid=[2, 0])

dateSel2 = Text(player_query_box, text="Match Date:", grid=[3, 0], align="right")
page2_combo_date = Combo(player_query_box, options=list(
    match[match['match_date'].dt.strftime('%Y') == page1_combo_season.value]['match_date'].dt.strftime(
        '%B %d').unique()) + ['All'], grid=[4, 0])

player1Sel = Text(player_query_box, text="Player 1:", grid=[5, 0], align="right")
page2_combo_p1 = Combo(player_query_box, options=['a', 'b'], grid=[6, 0])

player2Sel = Text(player_query_box, text="Player 2:", grid=[7, 0], align="right")
page2_combo_p2 = Combo(player_query_box, options=['a', 'b'], grid=[8, 0])

team_p1_Text = Text(player_query_box, text="Player 1 Team:", grid=[1, 1], align="right")
page2_combo_p1team = Combo(player_query_box, options=list(team['team_name'].values), grid=[2, 1])

team_p2_Text = Text(player_query_box, text="Player 2 Team:", grid=[3, 1], align="right")
page2_combo_p2team = Combo(player_query_box, options=list(team['team_name'].values), grid=[4, 1])

opp_team_sel_buffer = Text(player_query_box, text="Playing Against: ", grid=[5, 1])
page2_combo_opponent = Combo(player_query_box, options=list(team['team_name'].values), grid=[6, 1])

row_filler_page2 = Text(player_query_box, text="", width=10, grid=[0, 2])
PushButton(player_query_box, text='Search', command=page2_update_info, grid=[4, 3], align="right")

# SEARCH RESULTS

middleBox2 = TitleBox(page_2, text="Search Results", align="top", width="fill", height=500, border=True)

leftTeamBox2 = TitleBox(middleBox2, width=600, height=500, border=True,
                        text="Player 1", layout="grid", align="left")
rightTeamBox2 = TitleBox(middleBox2, height=500, width=600, border=True,
                         text="Player 2", layout="grid")

matchplayed1_label = Text(leftTeamBox2, text='Matches Played: ', grid=[0, 0], width=60, height=5, align="right")
matchplayed1_text = Text(leftTeamBox2, text='', grid=[1, 0], align="left")
runs1_label = Text(leftTeamBox2, text='Runs: ', grid=[0, 1], width=60, height=5, align="right")
runs1_text = Text(leftTeamBox2, text='', grid=[1, 1], align="left")
strikerate1_label = Text(leftTeamBox2, text='Batter Strike Rate: ', grid=[0, 2], width=60, height=5, align="right")
strikerate1_text = Text(leftTeamBox2, text='', grid=[1, 2], align="left")
wickets1_label = Text(leftTeamBox2, text='No. of Wickets: ', grid=[0, 3], width=60, height=5, align="right")
wickets1_text = Text(leftTeamBox2, text='', grid=[1, 3], align="left")
economy1_label = Text(leftTeamBox2, text='Bowler Strike Rate: ', grid=[0, 4], width=60, height=5, align="right")
economy1_text = Text(leftTeamBox2, text='', grid=[1, 4], align="left")
thoughts1_label_player = Text(leftTeamBox2, text='User Thoughts: ', grid=[0,5], width=60, height=5, align="left")
thoughts1_box_player = TextBox(leftTeamBox2, grid=[1,5], align="left", width=200)

matchplayed2_label = Text(rightTeamBox2, text='Matches Played: ', grid=[0, 0], width=60, height=5, align="right")
matchplayed2_text = Text(rightTeamBox2, text='', grid=[1, 0], align="left")
runs2_label = Text(rightTeamBox2, text='Runs: ', grid=[0, 1], width=60, height=5, align="right")
runs2_text = Text(rightTeamBox2, text='', grid=[1, 1], align="left")
strikerate2_label = Text(rightTeamBox2, text='Batter Strike Rate: ', grid=[0, 2], width=60, height=5, align="right")
strikerate2_text = Text(rightTeamBox2, text='', grid=[1, 2], align="left")
wickets2_label = Text(rightTeamBox2, text='No. of Wickets: ', grid=[0, 3], width=60, height=5, align="right")
wickets2_text = Text(rightTeamBox2, text='', grid=[1, 3], align="left")
economy2_label = Text(rightTeamBox2, text='Bowler Strike Rate: ', grid=[0, 4], width=60, height=5, align="right")
economy2_text = Text(rightTeamBox2, text='', grid=[1, 4], align="left")
thoughts2_label_player = Text(rightTeamBox2, text='User Thoughts: ', grid=[0,5], width=60, height=5, align="left")
thoughts2_box_player = TextBox(rightTeamBox2, grid=[1,5], align="left", width=200)

# PAGE 3 WIDGETS
title_box = Box(page_3, align="top", width="fill", height=50, border=True, layout="grid")
pg3_title_filler1 = Text(title_box, text="", width=4, grid=[0, 0])
close_team_button = PushButton(title_box, text="Close current Page", command=return_home, width=12, grid=[1, 0])
pg3_title_filler3 = Text(title_box, text="", width=2, grid=[2, 0])
save_team_button = PushButton(title_box, text="Save Notes", command=write_to_db, width=12, grid=[3,0])
pg3_title_filler2 = Text(title_box, text="", width=20, grid=[4, 0])
titleText = Text(title_box, text="Cricket Pulse Team Comparison", grid=[5, 0])

match['match_date'] = pd.to_datetime(match['match_date'])
# PG3 QUERY WIDGETS
team_query_box = TitleBox(page_3, align="top", width="fill", height=120, border=True, text="Search", layout="grid")

pg3_query_filler = Text(team_query_box, text="", width="50", grid=[0, 0])

seasonSel3 = Text(team_query_box, text="Season:", grid=[1, 0], align="right")
page3_combo_season = Combo(team_query_box, options=list(match['match_date'].dt.strftime('%Y').unique()) + ['All'],
                           grid=[2, 0], align="left")
dateSel = Text(team_query_box, text="Match Date:", grid=[3, 0], align="right")
page3_combo_date = Combo(team_query_box, options=list(
    match[match['match_date'].dt.strftime('%Y') == page3_combo_season.value]['match_date'].dt.strftime(
        '%B %d').unique()) + ['All'], grid=[4, 0], align="left")

teamText = Text(team_query_box, text="Teams:", grid=[5, 0], align="right")
page3_combo_team1 = Combo(team_query_box, options=list(team['team_name'].values), grid=[6, 0])
team_sel_buffer = Text(team_query_box, text="", grid=[7, 0], width=2)
page3_combo_team2 = Combo(team_query_box, options=list(team['team_name'].values), grid=[8, 0])

row_filler = Text(team_query_box, text="", width=10, grid=[0, 1])
search1_filler = Text(team_query_box, text="", grid=[0, 2])
search2_filler = Text(team_query_box, text="", grid=[1, 2])
search3_filler = Text(team_query_box, text="", grid=[2, 2])
search4_filler = Text(team_query_box, text="", grid=[3, 2])
PushButton(team_query_box, text='Search', command=page3_update_info, grid=[4, 2])

# Left-Hand Team Widgets
middleBox = TitleBox(page_3, text="Search Results", align="top", width="fill", height=500, border=True)

leftTeamBox = TitleBox(middleBox, width=600, height=500, border=True,
                       text="Team 1", layout="grid", align="left")

matchcount1_label = Text(leftTeamBox, text='No. of Matches: ', grid=[0, 0], width=60, height=5, align="right")
matchcount1_text = Text(leftTeamBox, text='', grid=[1, 0], align="left")
win1_label = Text(leftTeamBox, text='No. of Wins', grid=[0, 1], width=60, height=5, align="right")
win1_text = Text(leftTeamBox, text='', grid=[1, 1], align="left")
wr1_label = Text(leftTeamBox, text='Win Ratio: ', grid=[0, 2], width=60, height=5, align="right")
wr1_text = Text(leftTeamBox, text='', grid=[1, 2], align="left")
sr1_label = Text(leftTeamBox, text='Batter Strike Rate: ', grid=[0, 3], width=60, height=5, align="right")
sr1_text = Text(leftTeamBox, text='', grid=[1, 3], align="left")
eco1_label = Text(leftTeamBox, text='Bowler Strike Rate: ', grid=[0, 4], width=60, height=5, align="right")
eco1_text = Text(leftTeamBox, text='', grid=[1, 4], align="left")
thoughts1_label = Text(leftTeamBox, text='User Thoughts: ', grid=[0,5], width=60, height=5, align="right")
thoughts1_box = TextBox(leftTeamBox, grid=[1,5], align="left", width=200)

# Right-Hand Team Widgets
rightTeamBox = TitleBox(middleBox, height=500, width=600, border=True,
                        text="Team 2", layout="grid")

matchcount2_label = Text(rightTeamBox, text='No. of Matches: ', grid=[0, 0], width=60, height=5, align="right")
matchcount2_text = Text(rightTeamBox, text='', grid=[1, 0], align="left")
win2_label = Text(rightTeamBox, text='No. of Wins', grid=[0, 1], width=60, height=5, align="right")
win2_text = Text(rightTeamBox, text='', grid=[1, 1], align="left")
wr2_label = Text(rightTeamBox, text='Win Ratio: ', grid=[0, 2], width=60, height=5, align="right")
wr2_text = Text(rightTeamBox, text='', grid=[1, 2], align="left")
sr2_label = Text(rightTeamBox, text='Batter Strike Rate: ', grid=[0, 3], width=60, height=5, align="right")
sr2_text = Text(rightTeamBox, text='', grid=[1, 3], align="left")
eco2_label = Text(rightTeamBox, text='Bowler Strike Rate: ', grid=[0, 4], width=60, height=5, align="right")
eco2_text = Text(rightTeamBox, text='', grid=[1, 4], align="left")
thoughts2_label = Text(rightTeamBox, text='User Thoughts: ', grid=[0,5], width=60, height=5, align="right")
thoughts2_box = TextBox(rightTeamBox, grid=[1,5], align="left", width=200)

page_1.hide()
page_2.hide()
page_3.hide()

############################################################

home_page.display()
