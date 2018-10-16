from configparser import ConfigParser
import os

ProjectPath = os.path.split(os.path.realpath(__file__))[0]  #获取当前项目路径
print(ProjectPath, "ProjectPath")
ConfigPath = os.path.join(ProjectPath, "config.ini")
print(ConfigPath, "ConfigPath")
class ReadConfig:
    def __init__(self):
        self.read_config = ConfigParser()
        self.read_config.read(ConfigPath)




    def getConfig(self, property):
        """通过property获取配置文件的对应值"""
        return self.read_config.get("CONFIG", property)

    def writeConfig(self, property, value):
        """根据key值修改配置文件的对应值"""
        cf = ConfigParser()
        cf.read(ConfigPath)
        cf.set("CONFIG", property, str(value))
        with open(ConfigPath, "w")as f:
            cf.write(f)



