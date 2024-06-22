import csv
from collections import defaultdict
from datetime import datetime

# 讀取CSV文件
def read_data(filename):
    movies = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)
    return movies

# 1. 2016年評分最高的前三部電影
def top_3_movies_2016(movies):
    movies_2016 = [movie for movie in movies if movie['Year'] == '2016']
    sorted_movies = sorted(movies_2016, key=lambda x: float(x['Rating']), reverse=True)
    print("Top 3 movies with the highest ratings in 2016:")
    for i, movie in enumerate(sorted_movies[:3], 1):
        print(f"Top {i}: {movie['Title']} with rating {movie['Rating']}")

# 2. 參與電影最多的導演
def director_most_movies(movies):
    director_count = defaultdict(int)
    for movie in movies:
        directors = movie['Director'].split(',')
        for director in directors:
            director_count[director.strip()] += 1
    top_director = max(director_count, key=director_count.get)
    print(f"The director involved in the most movies is {top_director} with {director_count[top_director]} movies")

# 3. 產生最高總收入的演員
def actor_highest_total_revenue(movies):
    actor_revenue = defaultdict(int)
    for movie in movies:
        actors = movie['Actors'].split(',')
        revenue = float(movie['Revenue (Millions)']) if movie['Revenue (Millions)'] else 0
        for actor in actors:
            actor_revenue[actor.strip()] += revenue
    top_actor = max(actor_revenue, key=actor_revenue.get)
    print(f"The actor generating the highest total revenue is {top_actor} with ${actor_revenue[top_actor]:,.2f}")

# 4. Emma Watson電影的平均評分
def emma_watson_average_rating(movies):
    total_rating = 0
    count = 0
    for movie in movies:
        if 'Emma Watson' in movie['Actors']:
            total_rating += float(movie['Rating'])
            count += 1
    average_rating = total_rating / count if count != 0 else 0
    print(f"The average rating of Emma Watson's movies is {average_rating:.2f}")

# 5. 出演最多電影的前四位演員
def top_4_actors_most_movies(movies):
    actor_count = defaultdict(int)
    for movie in movies:
        actors = movie['Actors'].split(',')
        for actor in actors:
            actor_count[actor.strip()] += 1
    sorted_actors = sorted(actor_count.items(), key=lambda x: x[1], reverse=True)
    print("Top 4 actors playing the most movies:")
    for i, (actor, count) in enumerate(sorted_actors[:4], 1):
        print(f"Top {i}: {actor} with {count} movies")

# 6. 合作最頻繁的導演與演員組合的前七位
def top_7_director_actor_pairs(movies):
    director_actor_pairs = defaultdict(int)
    for movie in movies:
        directors = movie['Director'].split(',')
        actors = movie['Actors'].split(',')
        for director in directors:
            for actor in actors:
                pair = (director.strip(), actor.strip())
                director_actor_pairs[pair] += 1
    sorted_pairs = sorted(director_actor_pairs.items(), key=lambda x: x[1], reverse=True)
    print("Top 7 frequent collaboration pairs of director & actor:")
    for i, ((director, actor), count) in enumerate(sorted_pairs[:7], 1):
        print(f"Top {i}: Director {director} and Actor {actor} with {count} collaborations")

# 7. 合作演員最多的前三位導演
def top_3_directors_most_collaborations(movies):
    director_actor_collaborations = defaultdict(set)
    for movie in movies:
        directors = movie['Director'].split(',')
        actors = movie['Actors'].split(',')
        for director in directors:
            for actor in actors:
                director_actor_collaborations[director.strip()].add(actor.strip())
    sorted_directors = sorted(director_actor_collaborations.items(), key=lambda x: len(x[1]), reverse=True)
    print("Top 3 directors who collaborate with the most actors:")
    for i, (director, actors) in enumerate(sorted_directors[:3], 1):
        print(f"Top {i}: Director {director} collaborated with {len(actors)} actors")

# 8. 出演最多類型電影的前六位演員
def top_6_actors_most_genres(movies):
    actor_genres = defaultdict(set)
    for movie in movies:
        genres = movie['Genre'].split(',')
        actors = movie['Actors'].split(',')
        for actor in actors:
            for genre in genres:
                actor_genres[actor.strip()].add(genre.strip())
    sorted_actors = sorted(actor_genres.items(), key=lambda x: len(x[1]), reverse=True)
    print("Top 6 actors playing in the most genres of movies:")
    for i, (actor, genres) in enumerate(sorted_actors[:6], 1):
        print(f"Top {i}: Actor {actor} played in {len(genres)} genres")

# 9. 電影年份差距最大的前三位演員
def top_3_actors_largest_year_gap(movies):
    actor_years = defaultdict(list)
    for movie in movies:
        actors = movie['Actors'].split(',')
        year = int(movie['Year'])
        for actor in actors:
            actor_years[actor.strip()].append(year)
    actor_gaps = {actor: max(years) - min(years) for actor, years in actor_years.items() if len(years) > 1}
    sorted_actors = sorted(actor_gaps.items(), key=lambda x: x[1], reverse=True)
    print("Top 3 actors whose movies lead to the largest maximum gap of years:")
    for i, (actor, gap) in enumerate(sorted_actors[:3], 1):
        print(f"Top {i}: Actor {actor} with a gap of {gap} years")

# 主程序
def main():
    data = read_data('IMDB-Movie-Data.csv')

    print("\n--- Question 1 ---")
    top_3_movies_2016(data)
    
    print("\n--- Question 2 ---")
    director_most_movies(data)
    
    print("\n--- Question 3 ---")
    actor_highest_total_revenue(data)
    
    print("\n--- Question 4 ---")
    emma_watson_average_rating(data)
    
    print("\n--- Question 5 ---")
    top_4_actors_most_movies(data)
    
    print("\n--- Question 6 ---")
    top_7_director_actor_pairs(data)
    
    print("\n--- Question 7 ---")
    top_3_directors_most_collaborations(data)
    
    print("\n--- Question 8 ---")
    top_6_actors_most_genres(data)
    
    print("\n--- Question 9 ---")
    top_3_actors_largest_year_gap(data)

if __name__ == "__main__":
    main()