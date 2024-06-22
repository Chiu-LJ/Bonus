import csv

file_name = "pe8_data.csv"

# 嘗試使用 'big5' 編碼來讀取 CSV 文件
with open(file_name, "r", encoding='big5') as myfile:
    reader = csv.DictReader(myfile)
    data = list(reader)

# 將字符串值轉換為適當的數據類型
for row in data:
    row['PCT'] = float(row['PCT'])
    row['PF'] = float(row['PF'])
    row['PA'] = float(row['PA'])

    # 處理 HOME 和 AWAY 欄位，只取最後一部分的數字部分
    try:
        home_record = row['HOME'].split('-')
        away_record = row['AWAY'].split('-')
        row['Home_Wins'] = int(home_record[0])
        row['Home_Losses'] = int(home_record[1])
        row['Away_Wins'] = int(away_record[0])
        row['Away_Losses'] = int(away_record[1])
    except ValueError:
        row['Home_Wins'] = row['Home_Losses'] = 0
        row['Away_Wins'] = row['Away_Losses'] = 0

# 問題1：找出東部聯盟中主場勝率低於客場勝率的球隊
east_teams_home_lower_away = []
for row in data:
    if row['Conference'] == 'Eastern':
        home_games_played = row['Home_Wins'] + row['Home_Losses']
        away_games_played = row['Away_Wins'] + row['Away_Losses']
        if home_games_played > 0 and away_games_played > 0: #避免分母是0
            home_win_rate = row['Home_Wins'] / home_games_played
            away_win_rate = row['Away_Wins'] / away_games_played
            if home_win_rate < away_win_rate:
                east_teams_home_lower_away.append(row['Team'])

# 問題2：計算東部聯盟和西部聯盟中球隊的平均得分減掉失分之差
east_pf_pa_diff_sum = 0
west_pf_pa_diff_sum = 0
east_teams_count = 0
west_teams_count = 0

for row in data:
    pf_pa_diff = row['PF'] - row['PA']
    if row['Conference'] == 'Eastern':
        east_pf_pa_diff_sum += pf_pa_diff
        east_teams_count += 1
    elif row['Conference'] == 'Western':
        west_pf_pa_diff_sum += pf_pa_diff
        west_teams_count += 1

east_avg_pf_pa_diff = east_pf_pa_diff_sum / east_teams_count if east_teams_count > 0 else 0
west_avg_pf_pa_diff = west_pf_pa_diff_sum / west_teams_count if west_teams_count > 0 else 0

# 問題3：根據每支球隊和另一區球隊的對戰記錄來對所有球隊進行排序
team_interconference_wins = {}
for row in data:
    interconference_record = row['CONF'].split('-')
    interconference_wins = int(interconference_record[0])   # 取勝場數
    team_interconference_wins[row['Team']] = interconference_wins

ranking_list = sorted(team_interconference_wins.items(), key=lambda x: x[1], reverse=True)

# 輸出結果
print("(1) 東部聯盟中主場勝率低於客場勝率的球隊:")
for team in east_teams_home_lower_away:
    print(team)

print("\n(2) 哪一區的球隊擁有較高的“平均得分減掉失分”:")

if east_avg_pf_pa_diff > west_avg_pf_pa_diff:
    print("東部聯盟")
elif west_avg_pf_pa_diff > east_avg_pf_pa_diff:
    print("西部聯盟")
else:
    print("東部聯盟和西部聯盟相同")

print("\n(3) 根據每支球隊和另一區球隊的對戰記錄來對所有球隊排序:")
for rank, (team, wins) in enumerate(ranking_list, start=1):
    print(f"{rank}. {team} - {wins} wins")
