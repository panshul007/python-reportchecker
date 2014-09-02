import mainpackage.querycreator as qc
import mainpackage.dataaccess as da
import mainpackage.ixdateutils as du
import mainpackage.errorlogcollectionutils as elcu
import mainpackage.emailutil as eu
import mainpackage.mailrecipients as mr
import mainpackage.mailmessageutil as mmu
import logging


padTypeId = 1
enbwTypeId = 2
demandMonitorTypeId = 3
heatMapsTypeId = 4

def getTotalReportCounts():
    padTotal = (da.executeQuery(qc.getTotalReportsActiveCountByReportTypeId(padTypeId))).fetchone()[0]
    enbwTotal = da.executeQuery(qc.getTotalReportsActiveCountByReportTypeId(enbwTypeId)).fetchone()[0]
    dmTotal = da.executeQuery(qc.getTotalReportsActiveCountByReportTypeId(demandMonitorTypeId)).fetchone()[0]
    hmTotal = da.executeQuery(qc.getTotalReportsActiveCountByReportTypeId(heatMapsTypeId)).fetchone()[0]
    return padTotal,enbwTotal, dmTotal,hmTotal

def getSuccessCounts():
    yesterdayTime = du.getFormattedYesterday(False)
    enbwDateRange = du.getEnbwDateRange()
    padSuccess = da.executeQuery(qc.getSuccessfulReportCountForDateByReportTypeId(yesterdayTime, padTypeId)).fetchone()[0]
    enbwSuccess = da.executeQuery(qc.getSuccessfulEnbwReportCountForDateRange(enbwDateRange[0],enbwDateRange[1])).fetchone()[0]
    dmSuccess = da.executeQuery(qc.getSuccessfulReportCountForDateByReportTypeId(yesterdayTime, demandMonitorTypeId)).fetchone()[0]
    hmSuccess = da.executeQuery(qc.getSuccessfulReportCountForDateByReportTypeId(yesterdayTime, heatMapsTypeId)).fetchone()[0]
    return padSuccess,enbwSuccess,dmSuccess,hmSuccess


def execute():
    logging.basicConfig(filename='reportCheckerExecution.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info("Report Checker Execution Started.")
    try:
        successMailMessages = []
        errorMailMessages = []
        
        padTotal,enbwTotal, dmTotal,hmTotal = getTotalReportCounts()
        padSuccess,enbwSuccess,dmSuccess,hmSuccess = getSuccessCounts()
        
        successMailMessages.append(mmu.getSuccessMailHeader(du.getFormattedYesterday(False)))
        
        successMailMessages.append(mmu.getSuccessMailStatusByReportType("Premium Advertisement Reports", padSuccess, padTotal))
        successMailMessages.append(mmu.getSuccessMailStatusByReportType("ENBW Reports",enbwSuccess,enbwTotal))
        successMailMessages.append(mmu.getSuccessMailStatusByReportType("Demand Monitor Reports",dmSuccess,dmTotal))
        successMailMessages.append(mmu.getSuccessMailStatusByReportType("Heat Maps", hmSuccess,hmTotal))
        successMailMessages.append("---------------------------------------------------------------------- <br/>")
        
        if padTotal!=padSuccess:
            logging.info("PAD Error")
            padErrorProfiles = elcu.getErrorProfilesByReportTypeId(du.getFormattedYesterday(True), padTypeId)
            errorMailMessages.extend(mmu.prepareErrorMessagesFromReportProfile(padErrorProfiles,"Premium Advertisement Reports"))
        
        if enbwTotal!=enbwSuccess:
            logging.info("ENBW Error")
            enbwDateRange = du.getEnbwDateRange()
            enbwErrorProfiles = elcu.getErrorProfilesByReportTypeId(enbwDateRange[0],enbwDateRange[1])
            errorMailMessages.extend(mmu.prepareErrorMessagesFromReportProfile(enbwErrorProfiles,"ENBW Reports"))
        
        if dmTotal!=dmSuccess:
            logging.info("DM Error")
            dmErrorProfiles = elcu.getErrorProfilesByReportTypeId(du.getFormattedYesterday(True), demandMonitorTypeId)
            errorMailMessages.extend(mmu.prepareErrorMessagesFromReportProfile(dmErrorProfiles,"Demand Monitor Reports"))
        
        if hmTotal!=hmSuccess:
            logging.info("HM Error")
            hmErrorProfiles = elcu.getErrorProfilesByReportTypeId(du.getFormattedYesterday(True), heatMapsTypeId)
            errorMailMessages.extend(mmu.prepareErrorMessagesFromReportProfile(hmErrorProfiles,"Heat Maps"))
        
        logging.info("PAD: %s/%s",padSuccess,padTotal)
        logging.info("ENBW: %s/%s",enbwSuccess,enbwTotal)
        logging.info("Demand Monitor: %s/%s",dmSuccess,dmTotal)
        logging.info("Heat Maps: %s/%s",hmSuccess,hmTotal)    
        
        if len(errorMailMessages)==0:
            recipients = mr.getSuccessMailRecepients()
        else:
            successMailMessages.append("<br/> <strong>Report Profiles with errors in report generation:</strong> <br/>")
            errorMailMessages.append("<br/> We are working on the errors and will be resolved as soon as possible. You will receive the correct reports by tomorrow.<br/>")
            recipients = mr.getErrorMailRecepients()
        
        eu.sendReportGenerationStatusMail(successMailMessages, errorMailMessages, recipients, du.getFormattedYesterday(False))
        logging.info("Report Checker Execution finished.")
        
    except Exception as e:
        logging.error("Exception in execution: %r", e)
    
execute()