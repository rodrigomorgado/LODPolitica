# -*- coding: utf-8 -*-

import json_converter as converter

def gera_RDF():
	arquivo = open('basePolitica.rdf', 'w+')

	abre_tag_rdf = """<?xml version="1.0"?>
<rdf:RDF 
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:politica="Nossa sintaxe"
>
"""
	arquivo.write(abre_tag_rdf)

	arquivo.write(converter.gera_rdf_estados())
	arquivo.write(converter.gera_rdf_cargos())
	arquivo.write(converter.gera_rdf_partidos())
	arquivo.write(converter.gera_rdf_excelencias())
	arquivo.write(converter.gera_rdf_candidatos())

	fecha_tag_rdf = "</rdf:RDF>"
	arquivo.write(fecha_tag_rdf)

	arquivo.close()


if __name__ == '__main__':
	gera_RDF()