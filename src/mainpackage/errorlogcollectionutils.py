import mainpackage.querycreator as qc
import mainpackage.dataaccess as da

def getErrorProfileIds(cursor):
    rows = cursor.fetchall()
    errorProfiles = []
    for row in rows:
        errorProfiles.append(row[12])
    return errorProfiles

def getErrorProfiles(errorProfileIds):
    profiles = []
    queries = qc.getProfilesByProfileIds(errorProfileIds)
    for query in queries:
        profiles.append(da.executeQuery(query).fetchone())
    return profiles

def getErrorProfilesByReportTypeId(date,reportTypeId):
    failedReportsCursor = da.executeQuery(qc.getFailedReportsLogForDateByReportTypeId(date, reportTypeId))
    errorProfileIds = getErrorProfileIds(failedReportsCursor)
    errorProfiles = getErrorProfiles(errorProfileIds)
    return errorProfiles