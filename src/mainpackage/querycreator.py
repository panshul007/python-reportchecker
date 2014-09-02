
def getTotalReportsActiveCountByReportTypeId(reportTypeId):
    query = "Select count(*) from ReportProfile where reportType_id=%d and status='Active'" % (reportTypeId)
    return query

def getSuccessfulReportCountForDateByReportTypeId(date,reportTypeId):
    query = "Select count(*) from ReportGenerationLog where generatedForDate='%s' and reportType_id=%d and publishedStatus='Success'" % (date,reportTypeId)
    return query

def getSuccessfulEnbwReportCountForDateRange(dateFrom,dateTo):
    query = "Select count(*) from ReportGenerationLog where reportType_id=2 and generatedForDate between '%s' and '%s' and publishedStatus='Success'" %(dateFrom,dateTo)
    return query

def getFailedReportsLogForDateByReportTypeId(date,reportTypeId):
    query = "Select * from ReportGenerationLog where generatedForDate='%s' and reportType_id=%d and (publishedStatus='Failed' or reportGenerationStatus='Failed')" % (date,reportTypeId)
    return query

def getFailedEnbwReportsLogForDateRange(dateFrom,dateTo):
    query = "Select * from ReportGenerationLog where generatedForDate between '%s' and '%s' and reportType_id=2 and (publishedStatus='Failed' or reportGenerationStatus='Failed')" % (dateFrom,dateTo)
    return query

def getErrorLogByReportGenerationLogId(logId):
    query = "Select * from ErrorLog where reportGenerationLog_id=%d" %(logId)
    return query

def getReportPublishingErrorLogByReportPublishingLogId(reportPublishingLogId):
    query = "Select * from ReportPublishingErrorLog where reportPublishingLog_id=%d" %(reportPublishingLogId)
    return query

def getReportPublishingLogIdByReportGenerationLogId(reportGenLogId):
    query = "Select id from ReportPublishingLog where reportGenerationLog_id=%d" %(reportGenLogId)
    return query

def getDataProcessingForDate(date):
    query = ""
    return query

def getProfilesByProfileIds(profileIds):
    queries = []
    for profId in profileIds:
        queries.append("Select * from ReportProfile where id=%d" %(profId))
    return queries
    

