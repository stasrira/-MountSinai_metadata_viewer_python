import pyodbc 
import sys

def printL (m):
	if __name__ == '__main__':
		print (m)

class MetaViewer:
	strConn_prod = "Driver={ODBC Driver 17 for SQL Server};Server=10.160.20.65,51261;Database=dw_motrpac;UID=mt_internal_user;PWD=se@lf0n1nt3rn@l"
	#TODO: Dev connection string should be repointed to a test SQL Server when it becomes available
	strConn_dev = "Driver={ODBC Driver 17 for SQL Server};Server=10.160.20.65,51261;Database=dw_motrpac;UID=mt_internal_user;PWD=se@lf0n1nt3rn@l"
	strConn = ''
	sqlproc_getMetadata = "usp_get_metadata_studies_combined_by_sids"
	sqlproc_getMetaStudies = "select * from vw_get_study_stats"
	#envir = ''
	
	
	def __init__(self, envir = "development", str_conn = ""):
		self.envir = envir
		
		if len(str_conn) > 0:
			self.strConn = str_conn
		else:
			if self.envir == "development":
				self.strConn = self.strConn_dev
			else:
				self.strConn = self.strConn_prod
		
	def getCurConn (self):
		return self.strConn
	
	def getCurrentEnvir (self):
		return self.envir
	
	def setEnvir (self, envir = "development"):
		self.envir = envir
		if self.envir == "development":
			self.strConn = self.strConn_dev
		else:
			self.strConn = self.strConn_prod
	
	def getMetadata (self, sample_ids):
		#open connection and execute SQL query
		conn = pyodbc.connect(self.strConn, autocommit=True)
		cursor = conn.cursor()
		cursor.execute("exec " + self.sqlproc_getMetadata + "'" + sample_ids + "'")
		
		#returned recordsets
		rs_out = []
	
		try:
			#raise pyodbc.ProgrammingError("STAS123")
			while True:
				#print ("Loop---------")
				rows = cursor.fetchall()
				columns = [column[0] for column in cursor.description]
				#printL (columns)
				results = []
				for row in rows:
					results.append(dict(zip(columns, row)))
				rs_out.append (results)
				
				cursor.nextset()

		except Exception as e:

			if hasattr(e, 'message'):
				err_msg = e.message
			else:
				err_msg = e
			
			err_msg_template = "No results.  Previous SQL was not a query."
			if str(err_msg) != err_msg_template:
				raise Exception (e)
				
		return rs_out
		
	def getMetaStudies (self):
		#open connection and execute SQL query
		conn = pyodbc.connect(self.strConn)
		cursor = conn.cursor()
		cursor.execute(self.sqlproc_getMetaStudies)
		
		#returned recordset
		rs_out = []
		rows = cursor.fetchall()
		columns = [column[0] for column in cursor.description]
		#printL (columns)
		results = []
		for row in rows:
			results.append(dict(zip(columns, row)))
		rs_out.append (results)
				
		return rs_out

#if executed by itself, do the following
if __name__ == '__main__':

	#utilization of the MetaViewer class
	mv = MetaViewer ()

	printL (">>>>>>>>>> Metadata >>>>>>>>>>>>>>>>")
	#submit comma delimited list of sample_ids
	#sid example: '99920015501, 99920015801,  80000885507,90001015204, 90001015502'
	meta_out = mv.getMetadata ("99920015501, 99920015801")
	#output results for test purposes
	i = 0
	for rs in meta_out:
		printL ("=============Recordset " + str(i) + "==========")
		for row in rs:
			print (row)
		i=i+1

	printL (">>>>>>>>>> Studies >>>>>>>>>>>>>>>>")
	studies = mv.getMetaStudies()
	for rs in studies:
		for row in rs:
			print (row)
		








