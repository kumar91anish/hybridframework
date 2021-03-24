import configparser

conf = configparser.RawConfigParser()
conf.read(".\\Configuration\\config.ini")


class Readconfig:
    @staticmethod
    def ApplicationUrl():
        url = conf.get('common info', 'baseurl')
        return url

    @staticmethod
    def UserName():
        username = conf.get( 'common info','usermail')
        return username

    @staticmethod
    def Password():
        password = conf.get('common info','password')
        return password
