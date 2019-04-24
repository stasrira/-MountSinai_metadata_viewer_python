import metaviewer_pyodbc_lnx as mvr 

print ("-----------Start Utilization Example-----------")

#utilization of the MetaViewer class
mv = mvr.MetaViewer("production")

print (">>>>>>>>>> Metadata >>>>>>>>>>>>>>>>")
#submit comma delimited list of sample_ids
#sid example: '99920015501, 99920015801,  80000885507,90001015204, 90001015502'
meta_out = mv.getMetadata ("99920015501, 99920015801,  80000885507,90001015204, 90001015502")
#output results for test purposes
i = 0
for rs in meta_out:
	print ("=============Recordset " + str(i) + "==========")
	for row in rs:
		print (row)
	i=i+1

print (">>>>>>>>>> Studies >>>>>>>>>>>>>>>>")
studies = mv.getMetaStudies()
for rs in studies:
	for row in rs:
		print (row)
		








