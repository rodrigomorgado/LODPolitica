# -*- coding: utf-8 -*-

import api_transparencia as api
import api_dataTxt as dataTXT

def gera_rdf_estados():

	lista_estados = api.get_estados()

	rdf_resource = ""

	for estado in lista_estados:

		link_dbpedia = dataTXT.get_link_dbpedia(estado["nome"])
				
		if link_dbpedia:
			rdf_resource += "<rdf:Description rdf:about=\"" + link_dbpedia + "\">\n"
		else:
			rdf_resource += "<rdf:Description>\n"

		for chave_json in estado.keys():
			rdf_resource += "\t<politica:"+ chave_json + ">" + estado[chave_json] + "</politica:" + chave_json + ">\n"

		rdf_resource += "</rdf:Description>\n"

	return rdf_resource.encode("utf-8")


def gera_rdf_cargos():
	lista_cargos = api.get_cargos()

	rdf_resource = ""

	for cargo in lista_cargos:
		
		link_dbpedia = dataTXT.get_link_dbpedia(cargo["nome"])
				
		if link_dbpedia:
			rdf_resource += "<rdf:Description rdf:about=\"" + link_dbpedia + "\">\n"
		else:
			rdf_resource += "<rdf:Description>\n"

		for chave_json in cargo.keys():
			rdf_resource += "\t<politica:"+ chave_json + ">" + cargo[chave_json] + "</politica:" + chave_json + ">\n"

		rdf_resource += "</rdf:Description>\n"

	return rdf_resource.encode("utf-8")

def gera_rdf_partidos():
	lista_partidos = api.get_partidos()

	rdf_resource = ""

	for partido in lista_partidos:
		link_dbpedia = dataTXT.get_link_dbpedia(partido["sigla"])
				
		if link_dbpedia:
			rdf_resource += "<rdf:Description rdf:about=\"" + link_dbpedia + "\">\n"
		else:
			rdf_resource += "<rdf:Description>\n"

		for chave_json in partido.keys():
			rdf_resource += "\t<politica:"+ chave_json + ">" + partido[chave_json] + "</politica:" + chave_json + ">\n"

		rdf_resource += "</rdf:Description>\n"

	return rdf_resource.encode("utf-8")

def gera_rdf_candidatos():
	total_cargos = 10
	sigla_estados = [estado["sigla"] for estado in api.get_estados()]

	rdf_resource = ""

	for estado in sigla_estados:
		for id_cargo in range(1,total_cargos+1):
			
			if estado != "BR" and id_cargo == 1:
				continue
			
			print estado, id_cargo

			candidatos = api.get_candidatos_por_estado_e_id_cargos(estado, id_cargo)
			for candidato in candidatos:
				
				link_dbpedia = dataTXT.get_link_dbpedia(candidato["apelido"])
				
				if link_dbpedia:
					rdf_resource += "<rdf:Description rdf:about=\"" + link_dbpedia + "\">\n"
				else:
					rdf_resource += "<rdf:Description>\n"
				
				for chave_json in candidato.keys():
					if(isinstance(candidato[chave_json], bool)):
						candidato[chave_json] = str(candidato[chave_json])

					rdf_resource += "\t<politica:"+ chave_json + ">" + candidato[chave_json] + "</politica:" + chave_json + ">\n"

				#restante dos dados (ver a chave do json pro id do candidato)
				bens_candidato = api.get_bens_candidatos_por_id(candidato["id"])
				for bem in bens_candidato:
					rdf_resource += "\t<rdf:Description>\n"
					
					for chave_json in bem.keys():
						if(isinstance(bem[chave_json], bool)):
							bem[chave_json] = str(bem[chave_json])

						rdf_resource += "\t\t<politica:"+ chave_json + ">" + bem[chave_json] + "</politica:" + chave_json + ">\n"
					
					rdf_resource += "\t</rdf:Description>\n"

				# doadores = api.get_doadores_do_candidato_por_id_em_2014(candidato["id"])
				# for doador in doadores:
				# 	rdf_resource += "\t<rdf:Description>\n"
					
				# 	for chave_json in doador.keys():
				# 		if(isinstance(doador[chave_json], bool)):
				# 			doador[chave_json] = str(doador[chave_json])

				# 		rdf_resource += "\t\t<politica:"+ chave_json + ">" + doador[chave_json] + "</politica:" + chave_json + ">\n"
					
				# 	rdf_resource += "\t</rdf:Description>\n"

				candidaturas_passadas = api.get_candidaturas_passadas_pelo_id_do_candidato(candidato["id"])
				for candidatura in candidaturas_passadas:
					rdf_resource += "\t<rdf:Description>\n"
					
					for chave_json in candidatura.keys():
						if(isinstance(candidatura[chave_json], bool)):
							candidatura[chave_json] = str(candidatura[chave_json])

						rdf_resource += "\t\t<politica:"+ chave_json + ">" + candidatura[chave_json] + "</politica:" + chave_json + ">\n"
					
					rdf_resource += "\t</rdf:Description>\n"

				estatisticas_candidato = api.get_estatisticas_do_candidato(candidato["id"])
				for estatistica in estatisticas_candidato:
					rdf_resource += "\t<rdf:Description>\n"
					
					for chave_json in estatistica.keys():
						if(isinstance(estatistica[chave_json], bool)):
							estatistica[chave_json] = str(estatistica[chave_json])
						elif(estatistica[chave_json] == None):
							estatistica[chave_json] = "Sem informacao"

						rdf_resource += "\t\t<politica:"+ chave_json + ">" + estatistica[chave_json] + "</politica:" + chave_json + ">\n"
					
					rdf_resource += "\t</rdf:Description>\n"

				rdf_resource += "</rdf:Description>\n"


	return rdf_resource.encode("utf-8")
	
def gera_rdf_excelencias():

	lista_excelencias_deputado = api.get_excelencias_por_cargo("deputado")
	lista_excelencias_senado = api.get_excelencias_por_cargo("senado")
	
	rdf_resource = ""
	
	for excelencia in lista_excelencias_deputado:

		link_dbpedia = dataTXT.get_link_dbpedia(excelencia["apelido"])
		
		if link_dbpedia:
			rdf_resource += "<rdf:Description rdf:about=\"" + link_dbpedia + "\">\n"
		else:
			rdf_resource += "<rdf:Description>\n"
		
		for chave_json in excelencia.keys():
			if(isinstance(excelencia[chave_json], bool)):
				excelencia[chave_json] = str(excelencia[chave_json])

			if(chave_json == "processos"):
				excelencia[chave_json] = excelencia[chave_json].replace("a href", "rdf:Description rdf:about").replace("</a>", "</rdf:Description>").replace("<b>", "").replace("</b>", "").replace("target=\"_blank\"", "")
				
			rdf_resource += "\t<politica:" + chave_json + ">" + excelencia[chave_json] + "</politica:" + chave_json + ">\n"
			
		bens_excelencia = api.get_bens_excelencia_por_id(excelencia["id"])
		for bem in bens_excelencia:
			if(isinstance(bem, dict)):
					rdf_resource += "\t<rdf:Description>\n"
					
					for chave_json in bem.keys():
						rdf_resource += "\t\t<politica:"+ chave_json + ">" + bem[chave_json] + "</politica:" + chave_json + ">\n"
					
					rdf_resource += "\t</rdf:Description>\n"
			
		rdf_resource += "</rdf:Description>\n"
		
	for excelencia in lista_excelencias_senado:
		
		link_dbpedia = dataTXT.get_link_dbpedia(excelencia["apelido"])
		
		if link_dbpedia:
			rdf_resource += "<rdf:Description rdf:about=\"" + link_dbpedia + "\">\n"
		else:
			rdf_resource += "<rdf:Description>\n"
		
		for chave_json in excelencia.keys():
			if(isinstance(excelencia[chave_json], bool)):
				excelencia[chave_json] = str(excelencia[chave_json])

			if(chave_json == "processos"):
				excelencia[chave_json] = excelencia[chave_json].replace("a href", "rdf:Description rdf:about").replace("</a>", "</rdf:Description>").replace("<b>", "").replace("</b>", "").replace("target=\"_blank\"", "")
				
			rdf_resource += "\t<politica:" + chave_json + ">" + excelencia[chave_json] + "</politica:" + chave_json + ">\n"
			
		bens_excelencia = api.get_bens_excelencia_por_id(excelencia["id"])
		for bem in bens_excelencia:
			if(isinstance(bem, dict)):
					rdf_resource += "\t<rdf:Description>\n"
					
					for chave_json in bem.keys():
						rdf_resource += "\t\t<politica:"+ chave_json + ">" + bem[chave_json] + "</politica:" + chave_json + ">\n"
					
					rdf_resource += "\t</rdf:Description>\n"
			
		rdf_resource += "</rdf:Description>\n"
		
	return rdf_resource.encode("utf-8")
