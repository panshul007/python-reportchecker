import MySQLdb as mdb

def executeQuery(query):
    db = mdb.connect(host="localhost",port=3306,user="user",passwd="password",db="reportsdb");
    try:
        cur = db.cursor()
        cur.execute(query)
    
        #print "Query executed successfully."
        return cur
    
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1]) 
    
    finally:
        if db:
            db.close()
            
def queryTest():
    query = "Select count(*) from ReportProfile"
    executeQuery(query)
    
