# from environment import CONF
# PLATFORM = CONF.get("PLATFORM", "DEV")

#
PLATFORM = "DEV"

STATIC_FILES_PATH =  "/home/psygnet/iam-movieDB/iam_movieDB_01/main/static/"

# the Movie DB constants
TMDB_API_KEY_v3 = "be92fc3219373595614a42092b3a2495"
TMDB_API_KEY_v4 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZTkyZmMzMjE5MzczNTk1NjE0YTQyMDkyYjNhMjQ5NSIsInN1YiI6IjVhNzBhNjcyOTI1MTQxMzc1MTAxMGNhMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jR-PM9AMwZOgUXTN0n1CKHKA4kavzTxBRTfBSxr8_Zw"
TMDB_API_URL = "https://api.themoviedb.org/3/"

# API Calls

add_api_request = "?api_key="
get_movie_request = "movie/"

