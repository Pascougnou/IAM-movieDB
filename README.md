# IAM-movieDB 0.1
Trying to add a new dimension to film notation through multiple tags 

## For developers

- You should use a *v-env* for your Python environment otherwise you will encounter strange behavior.
- This application will require a *constants.py* file containing at least your tMDb API key, here is an example:

```python
# platform
PLATFORM = "DEV"
FQDN = "[your-test-FQDN-if-you-have-one]"

STATIC_FILES_PATH =  "[your-path-for-static-files]"

# the Movie DB constants
TMDB_API_URL_v3 = "https://api.themoviedb.org/3/"
TMDB_API_URL_v4 = "https://api.themoviedb.org/4/"
TMDB_ADD_API_REQUEST = "?api_key="

# API Keys
TMDB_API_KEY_v3 = "[your-v3-key]"
TMDB_API_KEY_v4 = "[your-v4-key]"

# API Calls
GET_MOVIE_REQUEST = "movie/"
```
