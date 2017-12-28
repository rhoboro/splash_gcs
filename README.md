```sh
$ docker pull scrapinghub/splash
$ docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash

$ pip install git+git://github.com/scrapy/scrapy.git
$ pip install scrapy-splash
$ pip install google-cloud-storage

# need to install gcloud sdk
$ export GOOGLE_APPLICATION_CREDENTIALS=`pwd`/credentials.json

# need to edit FILES_STORE and GCS_PROJECT_ID in settings.py
$ scrapy crawl myspider -o result.json
```
