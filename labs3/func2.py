from movie import movies

#1 task
def abovefivefive(name):
    for i in range(len(movies)):
        if name == movies[i]["name"] and movies[i]["imdb"] > 5.5:
            return True

#2 task
def score():
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            print(movies[i]["name"])  

#3 task
def categor(category):
    for i in range(len(movies)):
        if category == movies[i]["category"]:
            print(movies[i]["name"])

#4 task
def average():
    sum = 0
    for i in range(len(movies)): sum += movies[i]["imdb"]
    print(sum/len(movies))

#5 task
def categoryAverage(category):
    sum, cnt = 0, 0
    for i in range(len(movies)):
        if category == movies[i]["category"]:
            sum += movies[i]["imdb"]
            cnt+=1
    print(sum/cnt)

# name = input()
# print(abovefivefive(name))
# score()
# category = input()
# average()
# catAverage = input()
# categoryAverage(catAverage)


