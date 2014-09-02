import MySQLdb as mdb

def executeQuery(query):
    db = mdb.connect(host="46.51.197.62",port=13306,user="root",passwd="yjteER435J",db="verivoxreportsdb");
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
    
