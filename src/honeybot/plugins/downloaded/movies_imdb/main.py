"""
[movies_imdb.py]
IMDb Movies Plugin

[Author]
Zoi Katsantoni

[About]
Searches a movie then returns certain information

[Commands]

> > > .movies_imdb <<search>> <<movie>> <<information>>
> > > returns the certain information about the movie
> > > .movies_imdb 250movies
> > > returns 250 all-time most popular movies
> > > """

import imdb


class Plugin:
    movies = imdb.IMDb()

    def __init__(self):
        pass

    def search_movie_by_name(movie):
        movies = imdb.IMDb()
        certain_movie = movies.search_movie(movie)
        if not certain_movie:
            print("Could not find this movie")
            return -1
        else:
            ret = certain_movie[0]
            return ret.movieID

    def get_movie_from_id(movie_id):
        movies = imdb.IMDb()
        return movies.get_movie(movie_id)

    def get_movie_cast(movie):
        to_return = "Title: " + str(movie["title"])
        for cast in movie["cast"]:
            to_return += cast["name"] + " " + cast.currentRole + "\n"
        return to_return

    def get_movie_directors(movie):
        to_return = "Title: " + str(movie["title"]) + "\n" + "Directors: \n"
        for director in movie["director"]:
            to_return += director + "\n"
        return to_return

    def get_movie_producers(movie):
        to_return = "Title: " + str(movie["title"]) + "\n" + "Producers: \n"
        for producer in movie["producer"]:
            to_return += producer + "\n"
        return to_return

    def get_movie_rating(movie):
        return str(movie["rating"])

    def get_movie_year(movie):
        return str(movie["year"])

    def get_movie_genre(movie):
        to_return = ""
        for genre in movie["genres"]:
            to_return += genre + "\n"
        return to_return

    def get_movie_runtime(movie):
        return str(movie["runtimes"][0] + " minutes")

    def get_movie_countries(movie):
        to_return = ""
        for country in movie["countries"]:
            to_return += country
        return to_return

    def top_movies(movie2):
        movies = imdb.IMDb()
        top = movies.get_top250_movies()
        i = 1
        all_together = ""
        for movie in top:
            all_together += str(i) + ". " + movie["title"]
            i += 1
        return all_together

    def run(self, incoming, methods, info, bot_info):
        try:
            movies = imdb.IMDb()
            movie2 = ""
            msgs = info["args"][1:][0].split()

            if msgs[0] == ".movies_imdb":
                if info["command"] == "PRIVMSG" and msgs[1] == "250movies":
                    methods["send"](info["address"], self.top_movies(movie2))
                if info["command"] == "PRIVMSG" and msgs[1] == "searchmovie":
                    if len(msgs) > 4:
                        methods["send"](info["address"], "too many messages")
                    elif len(msgs) == 4:
                        movie_to_search = msgs[2]
                        what_to_search = int(msgs[3])

                        if what_to_search == "cast":
                            methods["send"](info["address"], self.get_movie_cast(movie_to_search))
                        elif what_to_search == "directors":
                            methods["send"](
                                info["address"], self.get_movie_directors(movie_to_search)
                            )
                        elif what_to_search == "producers":
                            methods["send"](
                                info["address"], self.get_movie_producers(movie_to_search)
                            )
                        elif what_to_search == "rating":
                            methods["send"](info["address"], self.get_movie_rating(movie_to_search))
                        elif what_to_search == "year":
                            methods["send"](info["address"], self.get_movie_year(movie_to_search))
                        elif what_to_search == "genre":
                            methods["send"](info["address"], self.get_movie_genre(movie_to_search))
                        elif what_to_search == "runtime":
                            methods["send"](
                                info["address"], self.get_movie_runtime(movie_to_search)
                            )
                        elif what_to_search == "countries":
                            methods["send"](
                                info["address"], self.get_movie_countries(movie_to_search)
                            )

        except Exception as e:
            print("imdb plugin error: ", e)
