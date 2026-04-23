import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/ndosiWebsite.ini")

class ReadConfig_UserInfo():

    def getUrl(self):
        return config.get("Environment", "dev_url")

    def getUsername(self):
        return config.get("Login Details", "username")

    def getPassword(self):
        return config.get("Login Details", "password")