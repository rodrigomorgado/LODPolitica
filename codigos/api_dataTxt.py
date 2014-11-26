# -*- coding: utf-8 -*-

import urllib2
import urllib
import json
from random import randrange

def recuperar_servico(texto):

    if randrange(2) == 0:
        json_parameters = {
        	'lang' : 'pt',
        	'min_confidence': '0.01',
        	'text': texto,
        	'social.parse_hashtag': 'False',
        	'country': '-1',
        	'include': 'lod',
        	'$app_id': 'bb35be37',
        	'$app_key': '4ba9707d6403aeb35114cd9cf224c02d'
        }
    else:
        json_parameters = {
            'lang' : 'pt',
            'min_confidence': '0.01',
            'text': texto,
            'social.parse_hashtag': 'False',
            'country': '-1',
            'include': 'lod',
            '$app_id': 'bb35be37',
            '$app_key': '4ba9707d6403aeb35114cd9cf224c02d'
        }

    parameters = urllib.urlencode(json_parameters)

    full_url = "https://api.dandelion.eu/datatxt/nex/v1/?" + parameters

    print full_url

    request = urllib2.Request(full_url)
    try:
        response = urllib2.urlopen(request)
        return json.loads(response.read())
    except urllib2.HTTPError, e:
        print str(e)
        return {}

def get_link_dbpedia(pessoa):
	pessoa = pessoa.encode("utf-8")
	print pessoa
	json = recuperar_servico(pessoa)
	if(len(json["annotations"]) > 0):
		return json["annotations"][0]["lod"]["dbpedia"]
