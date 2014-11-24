# -*- coding: utf-8 -*-

import urllib2
import json

def recuperar_servico(url):
    full_url = "%s%s" % ("http://api.transparencia.org.br:80/sandbox/v1", url)

    print full_url

    request = urllib2.Request(full_url)
    request.add_header("App-Token", "e3fnCzz6kofS")
    try:
        response = urllib2.urlopen(request)
        return json.loads(response.read())
    except urllib2.HTTPError, e:
        print str(e)
        return {}


def get_cargos():
	return recuperar_servico("/cargos")

def get_estados():
	return recuperar_servico("/estados")

def get_partidos():
	return recuperar_servico("/partidos")

def get_excelencias_por_cargo(cargo="deputado"):
	if cargo.lower() == "senado":
		id_cargo = 2
	else:
		id_cargo = 1

	return recuperar_servico("/excelencias?casa=" + str(id_cargo))

def get_bens_excelencia_por_id(id_candidato):
	return recuperar_servico("/excelencias/" + str(id_candidato) + "/bens")

#id de cargos vai de 1 a 10
def get_candidatos_por_estado_e_id_cargos(sigla_estado, id_cargo):
	return recuperar_servico("/candidatos?estado=" + str(sigla_estado) + "&cargo=" + str(id_cargo))

def get_bens_candidatos_por_id(id_candidato):
	return recuperar_servico("/candidatos/" + str(id_candidato) + "/bens")

def get_doadores_do_candidato_por_id_em_2014(id_candidato):
	return recuperar_servico("/candidatos/" + str(id_candidato) + "/doadores?anoEleitoral=2014")

def get_candidaturas_passadas_pelo_id_do_candidato(id_candidato):
	return recuperar_servico("/candidatos/" + str(id_candidato) + "/candidaturas")

def get_estatisticas_do_candidato(id_candidato):
	return recuperar_servico("/candidatos/" + str(id_candidato) + "/estatisticas")