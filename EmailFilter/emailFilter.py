from validate_email import validate_email


class EmailFilter:
    inputFileName = "emails.txt"
    outputFileName = "filteredEmails.txt"
    inputFile = file
    outputFile = file

    def __init__(self, inputFileName, outputFileName):
        self.inputFile = file(inputFileName, "r")
        self.outputFile = file(outputFileName, "a+")
        pass

    def __init__(self):
        self.inputFile = file(self.inputFileName, "r")
        self.outputFile = file(self.outputFileName, "a+")
        pass

    def mailExist(self, mail):
        try:
            return validate_email(mail, verify=True)
        except:
            return False

    def processMails(self):
        fileContent = self.inputFile.read()
        processedMails = set(fileContent.split(","))
        for mail in processedMails:
            if self.mailExist(mail):
               self.outputFile.write(mail + ",")
        return processedMails


def main():
    emailFilter = EmailFilter()
    emailFilter.processMails();
    #or give your parameters
    #customEmailFilter = EmailFilter("inputfile.txt", "outputfile.txt")
    #customEmailFilter.processMails()


main()
