import FactorySpecs
from otp.level import LevelSpec
from toontown.toonbase import ToontownGlobals

class FactoryBase:

    def __init__(self):
        pass

    def setFactoryId(self, factoryId):
        self.factoryId = factoryId
        self.factoryType = 'a'
        self.cogTrack = 'a'

    def getCogTrack(self):
        return self.cogTrack

    def getFactoryType(self):
        return self.factoryType

    if __dev__:

        def getEntityTypeReg(self):
            import FactoryEntityTypes
            from otp.level import EntityTypeRegistry
            typeReg = EntityTypeRegistry.EntityTypeRegistry(FactoryEntityTypes)
            return typeReg
