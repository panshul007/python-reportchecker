profile_companyName_index = 3
profile_energysource_index = 15

def getSuccessMailHeader(date):
    return "<h3>Report Generation Status for Date: %s is as follows:</h3>" %(date)

def getSuccessMailStatusByReportType(reportType,successCount,totalCount):
    return format("<strong> %s </strong> -- successfully generated: %d out of %d" %(reportType,successCount,totalCount))

def prepareErrorMessagesFromReportProfile(profiles,reportType):
    errorProfiles = []
    errorProfiles.append(format("<strong>%s</strong>: <br/>" %(reportType)))
    for profile in profiles:
        errorProfiles.append(format("- %s   %s " %(profile[profile_companyName_index],profile[profile_energysource_index])))
    return errorProfiles