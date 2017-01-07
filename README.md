# spaCy API

REST API for spaCy

The API can be reached under ```http://localhost:20040/api/```.

## Requirements

- Python 3.5: [Instructions](https://www.python.org/downloads/)

- virtualenv: [Instructions](https://virtualenv.pypa.io/en/stable/installation/)

## Installation

Run ```make``` for a local setup and then ```env/bin/start_debug``` to start the API in debug mode.

To start the uWSGI, run ```make start```

## Procedure

First, define your REST API in the configuration under ```/config/api.yml```, 
then add the Python logic for the *operationId* under /spacyapi/api

## SwaggerUI

Go to [here](http://localhost:20040/api/ui) to view the brilliant SwaggerUI documentation of your API.

## Logstash

By default, this project sends request logs and other (e.g. error logs) to different logstash UDP ports.

Configure the logstash input like this:

```
input {
    udp {
        codec => json {}
        type => "spacyapi"
        port => 1740   
    }
    udp {
        codec => json {}
        type => "spacyapi_uwsgi"
        port => 1741   
    }
}

filter {
    if [type] == "spacyapi" {
        json {
            source => "message"
        }
        mutate {
            remove_field => [ 'message' ]
        }
    }
}
```

## Resources
### Connexion
[Documentation](https://connexion.readthedocs.io/en/latest/)
[Github](https://github.com/zalando/connexion)
