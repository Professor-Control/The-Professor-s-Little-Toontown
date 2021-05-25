from toontown.suit import DistributedFactorySuit
from direct.directnotify import DirectNotifyGlobal

class DistributedMintSuit(DistributedFactorySuit.DistributedFactorySuit):
    
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMintSuit')
    
    def renameBoss(self):
        if self.getStyleDept() == 's':
            name = 'Factory Foreman'
            title = '.ffm'
        elif self.getStyleDept() == 'm':
            name = 'Mint Supervisor'
            title = '.svr'
        elif self.getStyleDept() == 'l':
            name = 'Office Overseer'
            title = '.oo'
        else:
            name = 'Club President'
            title = '.cpr'
        if self.getSkeleRevives() > 0:
            nameInfo = '%(name)s\n%(dept)s\nLevel %(level)s' % {'name': self.name,
             'dept': self.getStyleDept(),
             'level': '%s%s%s' % (self.getActualLevel(), title, '\nVersion 2.0')}
            self.setName(name)
            self.setDisplayName(nameInfo)
        else:
            nameInfo = '%(name)s\n%(dept)s\nLevel %(level)s' % {'name': self.name,
             'dept': self.getStyleDept(),
             'level': str(self.getActualLevel()) + title}
            self.setName(name)
            self.setDisplayName(nameInfo)
        return
