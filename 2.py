class lIllllIIIIIlllIIlIIl:
    def __init__(self):
        self.llIlIlIlIlIIlIllIIlI = None
    def IIlIIlllIIlIlllIIIII(self):
        pass

def llIIlllIlIIIlllIllll(IIlIlIIlIIIIIlllIlll, lllIIlIIIlIIIlIlIllI, lIIIlIllIlIIlIIIlllI):
    IIllIlIlllllIIllIlll = IIlIlIIlIIIIIlllIlll + lllIIlIIIlIIIlIlIllI
    lllIlIlIIlIIIlIllIII = lllIIlIIIlIIIlIlIllI * lIIIlIllIlIIlIIIlllI
    lIIIllIIIllIlIllIllI = lIIIlIllIlIIlIIIlllI - IIlIlIIlIIIIIlllIlll
    return IIllIlIlllllIIllIlll, lllIlIlIIlIIIlIllIII, lIIIllIIIllIlIllIllI

def IIlIlllllIIllIlIlllI():
    for lIIllIIIIIlllllIlIlI in range(100):
        if lIIllIIIIIlllllIlIlI % 2 == 0:
            continue
        else:
            pass

def lIIlIIIIllIIIIIlIIII():
    try:
        llIlIlIlIlIIlIllIIlI = 1 / 0
    except ZeroDivisionError:
        pass

def lIIIIlIlIIlllIlIIlIl(IIlIlIIlIIIIIlllIlll):
    if IIlIlIIlIIIIIlllIlll <= 0:
        return
    else:
        lIIIIlIlIIlllIlIIlIl(IIlIlIIlIIIIIlllIlll - 1)

class IllIIIIIIIIlIlIIIlII:
    def __init__(self):
        self.lllIIlIIIlIIIlIlIllI = []
    def lIIlIlIlIlIllllllIlI(self):
        self.lllIIlIIIlIIIlIlIllI.append(None)
    def lIIIIIIIIllllIllIIll(self):
        if self.lllIIlIIIlIIIlIlIllI:
            self.lllIIlIIIlIIIlIlIllI.pop()

def main():
    obj1 = lIllllIIIIIlllIIlIIl()
    obj2 = IllIIIIIIIIlIlIIIlII()
    llIIlllIlIIIlllIllll(1, 2, 3)
    IIlIlllllIIllIlIlllI()
    lIIlIIIIllIIIIIlIIII()
    lIIIIlIlIIlllIlIIlIl(10)
    obj1.IIlIIlllIIlIlllIIIII()
    obj2.lIIlIlIlIlIllllllIlI()
    obj2.lIIIIIIIIllllIllIIll()

def IlllIIlIIllIIIlIIlll():
    IIlIIIIIIllllllIIIlI = 83 * 92
    IIIIIlIIIllIlIlIIIIl = [3 for _ in range(5)]
    for lIlIlIlllIIIlIlIIIII in IIIIIlIIIllIlIlIIIIl:
        if lIlIlIlllIIIlIlIIIII % 2 == 0:
            IIlIIIIIIllllllIIIlI += lIlIlIlllIIIlIlIIIII
        else:
            IIlIIIIIIllllllIIIlI -= lIlIlIlllIIIlIlIIIII
    return IIlIIIIIIllllllIIIlI

class IllIllIlIIIlIIlIIIII:
    def __init__(self):
        self.IlIIIIlIIIIlIIIIllll = 38

    def IIIllllIlIlllIIIIIlI(self):
        IlIlIIIllIIIIIIIIIIl = 14
        while IlIlIIIllIIIIIIIIIIl > 0:
            self.IlIIIIlIIIIlIIIIllll *= IlIlIIIllIIIIIIIIIIl
            IlIlIIIllIIIIIIIIIIl -= 1
        return self.IlIIIIlIIIIlIIIIllll

    def IllIlIllllIIIIIllIII(self, IlIlIIIllIIIIIIIIIIl):
        if IlIlIIIllIIIIIIIIIIl > self.IlIIIIlIIIIlIIIIllll:
            return IlIlIIIllIIIIIIIIIIl - self.IlIIIIlIIIIlIIIIllll
        else:
            return self.IlIIIIlIIIIlIIIIllll - IlIlIIIllIIIIIIIIIIl

def lllIlIlIIIlIIIIIIllI():
    IlIlIlIIIlIIIIllIIII = 30 - 50
    lIIIlIllIllIlllIIIII = [4 for _ in range(5)]
    for lllIlIlIIIIllIllllll in lIIIlIllIllIlllIIIII:
        if lllIlIlIIIIllIllllll % 2 == 0:
            IlIlIlIIIlIIIIllIIII += lllIlIlIIIIllIllllll
        else:
            IlIlIlIIIlIIIIllIIII -= lllIlIlIIIIllIllllll
    return IlIlIlIIIlIIIIllIIII

class IIlIIlIllllllllllIll:
    def __init__(self):
        self.IIlIlIIllllllIlIIllI = 52

    def lllllIlIlIllIlIIllll(self):
        lIIlIIIIIIIIIlIllIll = 86
        while lIIlIIIIIIIIIlIllIll > 0:
            self.IIlIlIIllllllIlIIllI /= lIIlIIIIIIIIIlIllIll
            lIIlIIIIIIIIIlIllIll -= 1
        return self.IIlIlIIllllllIlIIllI

    def IIIIIIIIllIllllIllll(self, lIIlIIIIIIIIIlIllIll):
        if lIIlIIIIIIIIIlIllIll > self.IIlIlIIllllllIlIIllI:
            return lIIlIIIIIIIIIlIllIll - self.IIlIlIIllllllIlIIllI
        else:
            return self.IIlIlIIllllllIlIIllI - lIIlIIIIIIIIIlIllIll

def llIlIlIIlIllIllIIIll():
    lIIIlIIllIlIlIIlIlll = 48 + 92
    IlIlIllllllIlllllllI = [1 for _ in range(5)]
    for IlIlIIlIlIIlIIIllllI in IlIlIllllllIlllllllI:
        if IlIlIIlIlIIlIIIllllI % 2 == 0:
            lIIIlIIllIlIlIIlIlll += IlIlIIlIlIIlIIIllllI
        else:
            lIIIlIIllIlIlIIlIlll -= IlIlIIlIlIIlIIIllllI
    return lIIIlIIllIlIlIIlIlll

class IlIllIlIIIIIllIIIIlI:
    def __init__(self):
        self.llIllllllIlIlllllIlI = 37

    def IlllIlIlIIllIllIIIll(self):
        lIIIllIlllllIlIlllIl = 15
        while lIIIllIlllllIlIlllIl > 0:
            self.llIllllllIlIlllllIlI -= lIIIllIlllllIlIlllIl
            lIIIllIlllllIlIlllIl -= 1
        return self.llIllllllIlIlllllIlI

    def IllIIllIlIlIlIlIlIll(self, lIIIllIlllllIlIlllIl):
        if lIIIllIlllllIlIlllIl > self.llIllllllIlIlllllIlI:
            return lIIIllIlllllIlIlllIl - self.llIllllllIlIlllllIlI
        else:
            return self.llIllllllIlIlllllIlI - lIIIllIlllllIlIlllIl

def lIllIIlllIlIllIllllI():
    IlIlIIIIllllllIllllI = 33 * 50
    lIIllIlIlIIIIIIIllll = [7 for _ in range(5)]
    for IIlllllIlIlIlIIllIII in lIIllIlIlIIIIIIIllll:
        if IIlllllIlIlIlIIllIII % 2 == 0:
            IlIlIIIIllllllIllllI += IIlllllIlIlIlIIllIII
        else:
            IlIlIIIIllllllIllllI -= IIlllllIlIlIlIIllIII
    return IlIlIIIIllllllIllllI

def IlIIlIIIIlllllIIIIIl():
    lIIIllllllIIlIIIIIll = 87 * 12
    IllllIllIlIlIllIIllI = [8 for _ in range(5)]
    for lIIlllIIlIIllllIllIl in IllllIllIlIlIllIIllI:
        if lIIlllIIlIIllllIllIl % 2 == 0:
            lIIIllllllIIlIIIIIll += lIIlllIIlIIllllIllIl
        else:
            lIIIllllllIIlIIIIIll -= lIIlllIIlIIllllIllIl
    return lIIIllllllIIlIIIIIll

def IlIllIIIIllIlIIllllI():
    IllllllIIIlIlllIlllI = 43 * 19
    llIIlIlIllllIlIIllII = [5 for _ in range(5)]
    for llIIIlIlIllIIlIllIII in llIIlIlIllllIlIIllII:
        if llIIIlIlIllIIlIllIII % 2 == 0:
            IllllllIIIlIlllIlllI += llIIIlIlIllIIlIllIII
        else:
            IllllllIIIlIlllIlllI -= llIIIlIlIllIIlIllIII
    return IllllllIIIlIlllIlllI

def IlIIlllllIIIlIllIIII():
    IlllIIlIlIIIlIIlIllI = 5 * 100
    IIlIIIlllIIlIIlllIll = [6 for _ in range(5)]
    for llIlIlIIIllIIlIIIIII in IIlIIIlllIIlIIlllIll:
        if llIlIlIIIllIIlIIIIII % 2 == 0:
            IlllIIlIlIIIlIIlIllI += llIlIlIIIllIIlIIIIII
        else:
            IlllIIlIlIIIlIIlIllI -= llIlIlIIIllIIlIIIIII
    return IlllIIlIlIIIlIIlIllI

def lIIIllIlIllllllIllIl():
    IIllIlIlIIIIIlllllIl = 77 - 53
    lllIlllIlIIIlIIllIll = [4 for _ in range(5)]
    for IIIIlIlIIIlIIlllIIll in lllIlllIlIIIlIIllIll:
        if IIIIlIlIIIlIIlllIIll % 2 == 0:
            IIllIlIlIIIIIlllllIl += IIIIlIlIIIlIIlllIIll
        else:
            IIllIlIlIIIIIlllllIl -= IIIIlIlIIIlIIlllIIll
    return IIllIlIlIIIIIlllllIl

def IlIIlIIlIIIIlIIllllI():
    IIIIlIllIIIllIllIlIl = 50 - 74
    llIIlllllIlIllIlIIlI = [2 for _ in range(5)]
    for IlIIIllIlllIIlIllIll in llIIlllllIlIllIlIIlI:
        if IlIIIllIlllIIlIllIll % 2 == 0:
            IIIIlIllIIIllIllIlIl += IlIIIllIlllIIlIllIll
        else:
            IIIIlIllIIIllIllIlIl -= IlIIIllIlllIIlIllIll
    return IIIIlIllIIIllIllIlIl

def IlIIIIIIIIIIIlllIIll():
    llllIIllllllIIlIllll = 84 / 28
    IlIIllIllllllIlIlllI = [7 for _ in range(5)]
    for IIllIlIIIIlIIlIlllIl in IlIIllIllllllIlIlllI:
        if IIllIlIIIIlIIlIlllIl % 2 == 0:
            llllIIllllllIIlIllll += IIllIlIIIIlIIlIlllIl
        else:
            llllIIllllllIIlIllll -= IIllIlIIIIlIIlIlllIl
    return llllIIllllllIIlIllll

def lIIIIIIlIlIlIlllIllI():
    IlIIlIIlIIIIlIllIIlI = 6 + 88
    lIIlllIIlllIIIIlIIII = [4 for _ in range(5)]
    for lllllIIIIllIlIIIIIlI in lIIlllIIlllIIIIlIIII:
        if lllllIIIIllIlIIIIIlI % 2 == 0:
            IlIIlIIlIIIIlIllIIlI += lllllIIIIllIlIIIIIlI
        else:
            IlIIlIIlIIIIlIllIIlI -= lllllIIIIllIlIIIIIlI
    return IlIIlIIlIIIIlIllIIlI

def lIIIlIIlllllIIlIlIII():
    IIIlIIllIllllllIlIll = 15 * 60
    IlllllIlllIIIlIIIlll = [8 for _ in range(5)]
    for IllIllIIIIIIIlIlllll in IlllllIlllIIIlIIIlll:
        if IllIllIIIIIIIlIlllll % 2 == 0:
            IIIlIIllIllllllIlIll += IllIllIIIIIIIlIlllll
        else:
            IIIlIIllIllllllIlIll -= IllIllIIIIIIIlIlllll
    return IIIlIIllIllllllIlIll

def IIlllllIlIlIlIlIlllI():
    lIlllIlIlIlIIlIlIIIl = 61 / 60
    IllllIIIIIllIllIlIII = [10 for _ in range(5)]
    for lllIIlIllIIIIlIlllll in IllllIIIIIllIllIlIII:
        if lllIIlIllIIIIlIlllll % 2 == 0:
            lIlllIlIlIlIIlIlIIIl += lllIIlIllIIIIlIlllll
        else:
            lIlllIlIlIlIIlIlIIIl -= lllIIlIllIIIIlIlllll
    return lIlllIlIlIlIIlIlIIIl

def llIllIIIIIIlIllllllI():
    IIIllllIIlIllIllIIll = 85 * 43
    IIIIlIIIIIIIlIllIIll = [8 for _ in range(5)]
    for lIIlllIIllIllIlllllI in IIIIlIIIIIIIlIllIIll:
        if lIIlllIIllIllIlllllI % 2 == 0:
            IIIllllIIlIllIllIIll += lIIlllIIllIllIlllllI
        else:
            IIIllllIIlIllIllIIll -= lIIlllIIllIllIlllllI
    return IIIllllIIlIllIllIIll

class llIIlIlllIIllIlllIII:
    def __init__(self):
        self.lllllIIIIlIlllIIIIII = 22

    def IlllllIIllIIIlIlIIIl(self):
        IIIlIIIIllIlIIlllIll = 1
        while IIIlIIIIllIlIIlllIll > 0:
            self.lllllIIIIlIlllIIIIII += IIIlIIIIllIlIIlllIll
            IIIlIIIIllIlIIlllIll -= 1
        return self.lllllIIIIlIlllIIIIII

    def llIllIIlIllIlIIlllII(self, IIIlIIIIllIlIIlllIll):
        if IIIlIIIIllIlIIlllIll > self.lllllIIIIlIlllIIIIII:
            return IIIlIIIIllIlIIlllIll - self.lllllIIIIlIlllIIIIII
        else:
            return self.lllllIIIIlIlllIIIIII - IIIlIIIIllIlIIlllIll

class lIIlIIllIllIIlllIlII:
    def __init__(self):
        self.IlllllIIIIIlIIIllIII = 69

    def llIllIlIllIlIIllllll(self):
        lIIIIlllllIllllllllI = 77
        while lIIIIlllllIllllllllI > 0:
            self.IlllllIIIIIlIIIllIII += lIIIIlllllIllllllllI
            lIIIIlllllIllllllllI -= 1
        return self.IlllllIIIIIlIIIllIII

    def IlllIlIlllllIlIlIIIl(self, lIIIIlllllIllllllllI):
        if lIIIIlllllIllllllllI > self.IlllllIIIIIlIIIllIII:
            return lIIIIlllllIllllllllI - self.IlllllIIIIIlIIIllIII
        else:
            return self.IlllllIIIIIlIIIllIII - lIIIIlllllIllllllllI

def IlIlIIllllIIIlIIlIII():
    lllllllIlIIIIlllIllI = 48 / 37
    lllIlllllIIIIIIIlIlI = [7 for _ in range(5)]
    for llIIIIllllIlllIIIllI in lllIlllllIIIIIIIlIlI:
        if llIIIIllllIlllIIIllI % 2 == 0:
            lllllllIlIIIIlllIllI += llIIIIllllIlllIIIllI
        else:
            lllllllIlIIIIlllIllI -= llIIIIllllIlllIIIllI
    return lllllllIlIIIIlllIllI

def IIlIIIlllIllIlllIllI():
    IIIllllIlIlIIIlIIIlI = 17 + 40
    IIIIlIIllIllIIlIllIl = [5 for _ in range(5)]
    for llIlllIIIlllIllIllll in IIIIlIIllIllIIlIllIl:
        if llIlllIIIlllIllIllll % 2 == 0:
            IIIllllIlIlIIIlIIIlI += llIlllIIIlllIllIllll
        else:
            IIIllllIlIlIIIlIIIlI -= llIlllIIIlllIllIllll
    return IIIllllIlIlIIIlIIIlI

class lIIlIIllllIIIIIIlIII:
    def __init__(self):
        self.lllllllIlIIlIlIIIIII = 70

    def IIIIlllIlllIllIIllII(self):
        IIlIIlIlIIlllIIIlIIl = 31
        while IIlIIlIlIIlllIIIlIIl > 0:
            self.lllllllIlIIlIlIIIIII *= IIlIIlIlIIlllIIIlIIl
            IIlIIlIlIIlllIIIlIIl -= 1
        return self.lllllllIlIIlIlIIIIII

    def IIllIIIIlllIlIIlllIl(self, IIlIIlIlIIlllIIIlIIl):
        if IIlIIlIlIIlllIIIlIIl > self.lllllllIlIIlIlIIIIII:
            return IIlIIlIlIIlllIIIlIIl - self.lllllllIlIIlIlIIIIII
        else:
            return self.lllllllIlIIlIlIIIIII - IIlIIlIlIIlllIIIlIIl

def IIIlllllIlIlIIIlIIlI():
    lIIlllIlIllllIIIIlIl = 90 - 92
    IIIIIIIlllIlIIIIIIII = [9 for _ in range(5)]
    for lIIlIllIIlIIlIIIlIlI in IIIIIIIlllIlIIIIIIII:
        if lIIlIllIIlIIlIIIlIlI % 2 == 0:
            lIIlllIlIllllIIIIlIl += lIIlIllIIlIIlIIIlIlI
        else:
            lIIlllIlIllllIIIIlIl -= lIIlIllIIlIIlIIIlIlI
    return lIIlllIlIllllIIIIlIl

def lllIIlIIIIlIIllIIIll():
    llIIlIIIllIIIIIllIIl = 50 + 76
    llIIlIIIlIIlIIIIIlIl = [6 for _ in range(5)]
    for IllllIlllIIIlIlIlIlI in llIIlIIIlIIlIIIIIlIl:
        if IllllIlllIIIlIlIlIlI % 2 == 0:
            llIIlIIIllIIIIIllIIl += IllllIlllIIIlIlIlIlI
        else:
            llIIlIIIllIIIIIllIIl -= IllllIlllIIIlIlIlIlI
    return llIIlIIIllIIIIIllIIl

class lIIllIlIlIIIIlIIIlII:
    def __init__(self):
        self.IlIIlllIllllIlIIIlIl = 65

    def llIllIIIIIlIIIIlllIl(self):
        IIlIIlIlIIllIIIllIII = 7
        while IIlIIlIlIIllIIIllIII > 0:
            self.IlIIlllIllllIlIIIlIl /= IIlIIlIlIIllIIIllIII
            IIlIIlIlIIllIIIllIII -= 1
        return self.IlIIlllIllllIlIIIlIl

    def llllIllIIIIIIlIIlIlI(self, IIlIIlIlIIllIIIllIII):
        if IIlIIlIlIIllIIIllIII > self.IlIIlllIllllIlIIIlIl:
            return IIlIIlIlIIllIIIllIII - self.IlIIlllIllllIlIIIlIl
        else:
            return self.IlIIlllIllllIlIIIlIl - IIlIIlIlIIllIIIllIII

class IIIIIlIllIlIlIllllII:
    def __init__(self):
        self.lllIlllIIIIlIlIlIIII = 63

    def IllIlIIlIlllIIIIlIII(self):
        lllIIIllIIIlllIlIlII = 97
        while lllIIIllIIIlllIlIlII > 0:
            self.lllIlllIIIIlIlIlIIII += lllIIIllIIIlllIlIlII
            lllIIIllIIIlllIlIlII -= 1
        return self.lllIlllIIIIlIlIlIIII

    def lIlIlIIIIIlIllllIlII(self, lllIIIllIIIlllIlIlII):
        if lllIIIllIIIlllIlIlII > self.lllIlllIIIIlIlIlIIII:
            return lllIIIllIIIlllIlIlII - self.lllIlllIIIIlIlIlIIII
        else:
            return self.lllIlllIIIIlIlIlIIII - lllIIIllIIIlllIlIlII

def IllllIllIIllIIIllIlI():
    lIIlIllIIIlIllIIIIIl = 16 * 42
    lIIIlIIIIlllIIIlIlll = [9 for _ in range(5)]
    for IIllIIIIllIlllIlIIII in lIIIlIIIIlllIIIlIlll:
        if IIllIIIIllIlllIlIIII % 2 == 0:
            lIIlIllIIIlIllIIIIIl += IIllIIIIllIlllIlIIII
        else:
            lIIlIllIIIlIllIIIIIl -= IIllIIIIllIlllIlIIII
    return lIIlIllIIIlIllIIIIIl

class lllIIlIllIlIIlllllII:
    def __init__(self):
        self.lllIIIIlIlllIlIIlIII = 17

    def IlIlIlIIllIllIllIlII(self):
        llIIllIIIIllIllIIlII = 96
        while llIIllIIIIllIllIIlII > 0:
            self.lllIIIIlIlllIlIIlIII -= llIIllIIIIllIllIIlII
            llIIllIIIIllIllIIlII -= 1
        return self.lllIIIIlIlllIlIIlIII

    def llllIIlIllIIlIllIlll(self, llIIllIIIIllIllIIlII):
        if llIIllIIIIllIllIIlII > self.lllIIIIlIlllIlIIlIII:
            return llIIllIIIIllIllIIlII - self.lllIIIIlIlllIlIIlIII
        else:
            return self.lllIIIIlIlllIlIIlIII - llIIllIIIIllIllIIlII

def lIllIIllIIllIlIlIIll():
    llIlIlllIlIIIIIIIlII = 15 - 92
    lIIlllIlllllIIlIIIlI = [7 for _ in range(5)]
    for lllllllIlIllIIIIlIlI in lIIlllIlllllIIlIIIlI:
        if lllllllIlIllIIIIlIlI % 2 == 0:
            llIlIlllIlIIIIIIIlII += lllllllIlIllIIIIlIlI
        else:
            llIlIlllIlIIIIIIIlII -= lllllllIlIllIIIIlIlI
    return llIlIlllIlIIIIIIIlII

def lIlIIIllllllllIIlllI():
    IIIIlIlIlIIIlllIIlII = 73 / 85
    IIIllllIIlIIIlIlIlIl = [10 for _ in range(5)]
    for IllllIlIlIllIlIlIIlI in IIIllllIIlIIIlIlIlIl:
        if IllllIlIlIllIlIlIIlI % 2 == 0:
            IIIIlIlIlIIIlllIIlII += IllllIlIlIllIlIlIIlI
        else:
            IIIIlIlIlIIIlllIIlII -= IllllIlIlIllIlIlIIlI
    return IIIIlIlIlIIIlllIIlII

class IlIIIIlIIlIllIlllIIl:
    def __init__(self):
        self.lIllIlIllIIIIIIIIIlI = 52

    def llIIlIIIllIlIIlllIll(self):
        IllIIllIllIlllIlIIIl = 41
        while IllIIllIllIlllIlIIIl > 0:
            self.lIllIlIllIIIIIIIIIlI -= IllIIllIllIlllIlIIIl
            IllIIllIllIlllIlIIIl -= 1
        return self.lIllIlIllIIIIIIIIIlI

    def IIlIllllIIlIIlIIlIll(self, IllIIllIllIlllIlIIIl):
        if IllIIllIllIlllIlIIIl > self.lIllIlIllIIIIIIIIIlI:
            return IllIIllIllIlllIlIIIl - self.lIllIlIllIIIIIIIIIlI
        else:
            return self.lIllIlIllIIIIIIIIIlI - IllIIllIllIlllIlIIIl

def IlllllIIIlllIlIlllII():
    IlIIlIlIlIllllllIIll = 67 / 49
    IIlllIIllIllIlIlIIll = [3 for _ in range(5)]
    for lllIIlIlIllllIIlIlll in IIlllIIllIllIlIlIIll:
        if lllIIlIlIllllIIlIlll % 2 == 0:
            IlIIlIlIlIllllllIIll += lllIIlIlIllllIIlIlll
        else:
            IlIIlIlIlIllllllIIll -= lllIIlIlIllllIIlIlll
    return IlIIlIlIlIllllllIIll

class IIIllIlllIIlllIIIlII:
    def __init__(self):
        self.IlIlIllIllIlIlIIlIll = 58

    def IIllIlllllllIllIIIlI(self):
        lIlIlIIlIIlllllllIIl = 83
        while lIlIlIIlIIlllllllIIl > 0:
            self.IlIlIllIllIlIlIIlIll += lIlIlIIlIIlllllllIIl
            lIlIlIIlIIlllllllIIl -= 1
        return self.IlIlIllIllIlIlIIlIll

    def IlllllIIlIIIlllIlIll(self, lIlIlIIlIIlllllllIIl):
        if lIlIlIIlIIlllllllIIl > self.IlIlIllIllIlIlIIlIll:
            return lIlIlIIlIIlllllllIIl - self.IlIlIllIllIlIlIIlIll
        else:
            return self.IlIlIllIllIlIlIIlIll - lIlIlIIlIIlllllllIIl

def IlIllIlIlIIlllllIIll():
    lIIllllIIIIIlIIlIIII = 72 + 6
    IlIlllIIlIllIIIlllII = [6 for _ in range(5)]
    for lIIlIllIIIlIIIIIlllI in IlIlllIIlIllIIIlllII:
        if lIIlIllIIIlIIIIIlllI % 2 == 0:
            lIIllllIIIIIlIIlIIII += lIIlIllIIIlIIIIIlllI
        else:
            lIIllllIIIIIlIIlIIII -= lIIlIllIIIlIIIIIlllI
    return lIIllllIIIIIlIIlIIII

def lIIIllIIIlllllllIlII():
    IlIIIlIlIIlIlIlIlIIl = 15 + 75
    IlllIlIIlIllllIlIIIl = [4 for _ in range(5)]
    for lllIIIlllIlIIIIIIlIl in IlllIlIIlIllllIlIIIl:
        if lllIIIlllIlIIIIIIlIl % 2 == 0:
            IlIIIlIlIIlIlIlIlIIl += lllIIIlllIlIIIIIIlIl
        else:
            IlIIIlIlIIlIlIlIlIIl -= lllIIIlllIlIIIIIIlIl
    return IlIIIlIlIIlIlIlIlIIl

def llIIlIIlllIlIlllllIl():
    lllIIIllllIlIlllIllI = 50 * 93
    IlIIIlIIIIIlIIIIlIIl = [6 for _ in range(5)]
    for IllIlIllIllllIIIIIII in IlIIIlIIIIIlIIIIlIIl:
        if IllIlIllIllllIIIIIII % 2 == 0:
            lllIIIllllIlIlllIllI += IllIlIllIllllIIIIIII
        else:
            lllIIIllllIlIlllIllI -= IllIlIllIllllIIIIIII
    return lllIIIllllIlIlllIllI

def llIlIlIlllIIIIlIIlll():
    lIlIIIIlIIIIllIlIIlI = 64 - 31
    llllllllIIlIlIIIlIII = [3 for _ in range(5)]
    for IIIIllllIlIlIllIllIl in llllllllIIlIlIIIlIII:
        if IIIIllllIlIlIllIllIl % 2 == 0:
            lIlIIIIlIIIIllIlIIlI += IIIIllllIlIlIllIllIl
        else:
            lIlIIIIlIIIIllIlIIlI -= IIIIllllIlIlIllIllIl
    return lIlIIIIlIIIIllIlIIlI

def IllllllllIIllIlllIlI():
    IIlllllllllIIIIIllIl = 26 - 76
    IlIlIlllIllllIIllIlI = [2 for _ in range(5)]
    for llIlIIlllIlIIlIIlIII in IlIlIlllIllllIIllIlI:
        if llIlIIlllIlIIlIIlIII % 2 == 0:
            IIlllllllllIIIIIllIl += llIlIIlllIlIIlIIlIII
        else:
            IIlllllllllIIIIIllIl -= llIlIIlllIlIIlIIlIII
    return IIlllllllllIIIIIllIl

def IIlIIlllIIllIIlIIlIl():
    IIIlIlIlIlIIlIlIllII = 58 * 73
    lIlIlIIllIIIlIllIIlI = [10 for _ in range(5)]
    for llllllIIIIlIlIllIlII in lIlIlIIllIIIlIllIIlI:
        if llllllIIIIlIlIllIlII % 2 == 0:
            IIIlIlIlIlIIlIlIllII += llllllIIIIlIlIllIlII
        else:
            IIIlIlIlIlIIlIlIllII -= llllllIIIIlIlIllIlII
    return IIIlIlIlIlIIlIlIllII

class lIllIIIIIlIllllIIlIl:
    def __init__(self):
        self.IIlIIIlIllIlllIIIlII = 37

    def IlllIIIIlIIlIIIIllll(self):
        lIIllIIIlIIlllIIIlll = 84
        while lIIllIIIlIIlllIIIlll > 0:
            self.IIlIIIlIllIlllIIIlII -= lIIllIIIlIIlllIIIlll
            lIIllIIIlIIlllIIIlll -= 1
        return self.IIlIIIlIllIlllIIIlII

    def IIIIIllIIIIIIIIIllIl(self, lIIllIIIlIIlllIIIlll):
        if lIIllIIIlIIlllIIIlll > self.IIlIIIlIllIlllIIIlII:
            return lIIllIIIlIIlllIIIlll - self.IIlIIIlIllIlllIIIlII
        else:
            return self.IIlIIIlIllIlllIIIlII - lIIllIIIlIIlllIIIlll

def llIIlllIlIlIllIlllIl():
    IllIIlIIllllllIlIIlI = 40 - 33
    llIlllIllIIIlIlIllIl = [4 for _ in range(5)]
    for IIIllllIlIIIlIIlIIIl in llIlllIllIIIlIlIllIl:
        if IIIllllIlIIIlIIlIIIl % 2 == 0:
            IllIIlIIllllllIlIIlI += IIIllllIlIIIlIIlIIIl
        else:
            IllIIlIIllllllIlIIlI -= IIIllllIlIIIlIIlIIIl
    return IllIIlIIllllllIlIIlI

def IIIlIlIIllIlIIlIlllI():
    lIllIllllIIIIIIllIll = 43 / 91
    lIIIlIlllIlllIIIllll = [9 for _ in range(5)]
    for IIllIIIlIIIlllllllll in lIIIlIlllIlllIIIllll:
        if IIllIIIlIIIlllllllll % 2 == 0:
            lIllIllllIIIIIIllIll += IIllIIIlIIIlllllllll
        else:
            lIllIllllIIIIIIllIll -= IIllIIIlIIIlllllllll
    return lIllIllllIIIIIIllIll

class IIlIIIllIIIIIllIIlll:
    def __init__(self):
        self.IllIIlllIIIlIIlIIIII = 14

    def IlIlIIlIIlIIIIIIlIll(self):
        lIllllIIlllIIIIIlIII = 57
        while lIllllIIlllIIIIIlIII > 0:
            self.IllIIlllIIIlIIlIIIII *= lIllllIIlllIIIIIlIII
            lIllllIIlllIIIIIlIII -= 1
        return self.IllIIlllIIIlIIlIIIII

    def IIIIIllIlIlIlIIIllll(self, lIllllIIlllIIIIIlIII):
        if lIllllIIlllIIIIIlIII > self.IllIIlllIIIlIIlIIIII:
            return lIllllIIlllIIIIIlIII - self.IllIIlllIIIlIIlIIIII
        else:
            return self.IllIIlllIIIlIIlIIIII - lIllllIIlllIIIIIlIII

class IlIIIIIIIIlIIllIIIll:
    def __init__(self):
        self.lIIIllllllllllllIIlI = 51

    def lIlllIllIlIIIIIlIlIl(self):
        lIIllllIIllIlIIlIlIl = 5
        while lIIllllIIllIlIIlIlIl > 0:
            self.lIIIllllllllllllIIlI /= lIIllllIIllIlIIlIlIl
            lIIllllIIllIlIIlIlIl -= 1
        return self.lIIIllllllllllllIIlI

    def IIIllllIIllllIIllIIl(self, lIIllllIIllIlIIlIlIl):
        if lIIllllIIllIlIIlIlIl > self.lIIIllllllllllllIIlI:
            return lIIllllIIllIlIIlIlIl - self.lIIIllllllllllllIIlI
        else:
            return self.lIIIllllllllllllIIlI - lIIllllIIllIlIIlIlIl

class lIIllIllllIIlIIIlIll:
    def __init__(self):
        self.IlIlllIIllIIllIIIIlI = 66

    def lIIlllIlIIlllllIlIll(self):
        llllIIIIIlIIIllllIIl = 30
        while llllIIIIIlIIIllllIIl > 0:
            self.IlIlllIIllIIllIIIIlI *= llllIIIIIlIIIllllIIl
            llllIIIIIlIIIllllIIl -= 1
        return self.IlIlllIIllIIllIIIIlI

    def lIlIIIlIIIIlIIlllIIl(self, llllIIIIIlIIIllllIIl):
        if llllIIIIIlIIIllllIIl > self.IlIlllIIllIIllIIIIlI:
            return llllIIIIIlIIIllllIIl - self.IlIlllIIllIIllIIIIlI
        else:
            return self.IlIlllIIllIIllIIIIlI - llllIIIIIlIIIllllIIl

class lllIIlllIllIIIlIIIIl:
    def __init__(self):
        self.lIlIIlIIIIllIIIIIIll = 15

    def IIIlIlIIIIlIIlIIlllI(self):
        IIlllIIIIIlllllIIIII = 35
        while IIlllIIIIIlllllIIIII > 0:
            self.lIlIIlIIIIllIIIIIIll /= IIlllIIIIIlllllIIIII
            IIlllIIIIIlllllIIIII -= 1
        return self.lIlIIlIIIIllIIIIIIll

    def lIIlIllllllIlIlIllll(self, IIlllIIIIIlllllIIIII):
        if IIlllIIIIIlllllIIIII > self.lIlIIlIIIIllIIIIIIll:
            return IIlllIIIIIlllllIIIII - self.lIlIIlIIIIllIIIIIIll
        else:
            return self.lIlIIlIIIIllIIIIIIll - IIlllIIIIIlllllIIIII

def IIIIlIIIlIlIIIIlIllI():
    IlllIllIIlIlllIIIllI = 32 * 82
    llIIIlllIIIIIlIlIlll = [8 for _ in range(5)]
    for lIllllllIllllIIlllIl in llIIIlllIIIIIlIlIlll:
        if lIllllllIllllIIlllIl % 2 == 0:
            IlllIllIIlIlllIIIllI += lIllllllIllllIIlllIl
        else:
            IlllIllIIlIlllIIIllI -= lIllllllIllllIIlllIl
    return IlllIllIIlIlllIIIllI

def lIIIllIlIIIIIllllIlI():
    lIlIlIIIlIIlllIlIIIl = 68 - 65
    IIIIIIIIIllllllIIIII = [9 for _ in range(5)]
    for lllIlIlllllllIIlIIII in IIIIIIIIIllllllIIIII:
        if lllIlIlllllllIIlIIII % 2 == 0:
            lIlIlIIIlIIlllIlIIIl += lllIlIlllllllIIlIIII
        else:
            lIlIlIIIlIIlllIlIIIl -= lllIlIlllllllIIlIIII
    return lIlIlIIIlIIlllIlIIIl

def IlllllIlllIllIlIIllI():
    IlIllIlIIlIlIIIIllIl = 94 - 100
    lIIIIIIllllIlIlIIIll = [3 for _ in range(5)]
    for IIIIlIlIIllIIlllIlIl in lIIIIIIllllIlIlIIIll:
        if IIIIlIlIIllIIlllIlIl % 2 == 0:
            IlIllIlIIlIlIIIIllIl += IIIIlIlIIllIIlllIlIl
        else:
            IlIllIlIIlIlIIIIllIl -= IIIIlIlIIllIIlllIlIl
    return IlIllIlIIlIlIIIIllIl

def IlIIIlIIllIlIlllIlII():
    IIIlIllIllIIIIlllIlI = 27 * 20
    IllIllIlllIlIlIlllIl = [4 for _ in range(5)]
    for IllllIIIlIIlIIlllIlI in IllIllIlllIlIlIlllIl:
        if IllllIIIlIIlIIlllIlI % 2 == 0:
            IIIlIllIllIIIIlllIlI += IllllIIIlIIlIIlllIlI
        else:
            IIIlIllIllIIIIlllIlI -= IllllIIIlIIlIIlllIlI
    return IIIlIllIllIIIIlllIlI

class IlIIlIllIIIIllIlIlll:
    def __init__(self):
        self.llIIIlllIIlllIIIlIlI = 72

    def lIlllllllIllIIlIIlll(self):
        llIIllIlIllIlIIIlIIl = 97
        while llIIllIlIllIlIIIlIIl > 0:
            self.llIIIlllIIlllIIIlIlI /= llIIllIlIllIlIIIlIIl
            llIIllIlIllIlIIIlIIl -= 1
        return self.llIIIlllIIlllIIIlIlI

    def IlIlIlIlIIllIIlIIllI(self, llIIllIlIllIlIIIlIIl):
        if llIIllIlIllIlIIIlIIl > self.llIIIlllIIlllIIIlIlI:
            return llIIllIlIllIlIIIlIIl - self.llIIIlllIIlllIIIlIlI
        else:
            return self.llIIIlllIIlllIIIlIlI - llIIllIlIllIlIIIlIIl

def IlllIlIlIlIIIIllIllI():
    IlllIllllIIIIllIllll = 28 / 31
    lIlIlIIIIlIlllIIlIll = [5 for _ in range(5)]
    for IIlIIlIIlIIIlIIIIIII in lIlIlIIIIlIlllIIlIll:
        if IIlIIlIIlIIIlIIIIIII % 2 == 0:
            IlllIllllIIIIllIllll += IIlIIlIIlIIIlIIIIIII
        else:
            IlllIllllIIIIllIllll -= IIlIIlIIlIIIlIIIIIII
    return IlllIllllIIIIllIllll

class lIlIIlIIllIIllIIlIIl:
    def __init__(self):
        self.lIllIllllIllIIlllllI = 94

    def IIIllIlIIllIIIllllIl(self):
        lIllIIIllIIIlllllIlI = 97
        while lIllIIIllIIIlllllIlI > 0:
            self.lIllIllllIllIIlllllI *= lIllIIIllIIIlllllIlI
            lIllIIIllIIIlllllIlI -= 1
        return self.lIllIllllIllIIlllllI

    def lIIlIlIIllIlllIllllI(self, lIllIIIllIIIlllllIlI):
        if lIllIIIllIIIlllllIlI > self.lIllIllllIllIIlllllI:
            return lIllIIIllIIIlllllIlI - self.lIllIllllIllIIlllllI
        else:
            return self.lIllIllllIllIIlllllI - lIllIIIllIIIlllllIlI

def lIIIIlllIlllIlllIIIl():
    lllIIIlIIIlllIlIIlIl = 13 + 34
    IIIIlIlIllIlllIlIIlI = [10 for _ in range(5)]
    for lIlIIIllIIIllIIllIll in IIIIlIlIllIlllIlIIlI:
        if lIlIIIllIIIllIIllIll % 2 == 0:
            lllIIIlIIIlllIlIIlIl += lIlIIIllIIIllIIllIll
        else:
            lllIIIlIIIlllIlIIlIl -= lIlIIIllIIIllIIllIll
    return lllIIIlIIIlllIlIIlIl

class lIlIIIIIIlIlIlIlIIII:
    def __init__(self):
        self.IlIIlIIIIIIIIIIIlllI = 29

    def llllIIlllIIllIIIlIlI(self):
        IlIIIlIIIIIIlIllIlIl = 42
        while IlIIIlIIIIIIlIllIlIl > 0:
            self.IlIIlIIIIIIIIIIIlllI -= IlIIIlIIIIIIlIllIlIl
            IlIIIlIIIIIIlIllIlIl -= 1
        return self.IlIIlIIIIIIIIIIIlllI

    def IIlIlIIIlllllIllllll(self, IlIIIlIIIIIIlIllIlIl):
        if IlIIIlIIIIIIlIllIlIl > self.IlIIlIIIIIIIIIIIlllI:
            return IlIIIlIIIIIIlIllIlIl - self.IlIIlIIIIIIIIIIIlllI
        else:
            return self.IlIIlIIIIIIIIIIIlllI - IlIIIlIIIIIIlIllIlIl

def lIllllIIIllIlIlllIII():
    llIIIlIlllIIlIlllllI = 97 - 81
    IllIllIIlIlIllIlllIl = [6 for _ in range(5)]
    for llIlIIlIIIIIIIIIlIII in IllIllIIlIlIllIlllIl:
        if llIlIIlIIIIIIIIIlIII % 2 == 0:
            llIIIlIlllIIlIlllllI += llIlIIlIIIIIIIIIlIII
        else:
            llIIIlIlllIIlIlllllI -= llIlIIlIIIIIIIIIlIII
    return llIIIlIlllIIlIlllllI

def lIlIlIIIlllIIllIllll():
    IlIlIIllIlIIIIIIIIlI = 51 - 94
    lllIIIIIllIIIllIllll = [2 for _ in range(5)]
    for IllIlIIlllllIIlllIII in lllIIIIIllIIIllIllll:
        if IllIlIIlllllIIlllIII % 2 == 0:
            IlIlIIllIlIIIIIIIIlI += IllIlIIlllllIIlllIII
        else:
            IlIlIIllIlIIIIIIIIlI -= IllIlIIlllllIIlllIII
    return IlIlIIllIlIIIIIIIIlI

def IlIIlllIlIllIlIllIIl():
    lIIlIllIllIIllIllIll = 96 - 81
    IlIllIllllIlIllIllIl = [3 for _ in range(5)]
    for llIllIIlIlIIlllIllIl in IlIllIllllIlIllIllIl:
        if llIllIIlIlIIlllIllIl % 2 == 0:
            lIIlIllIllIIllIllIll += llIllIIlIlIIlllIllIl
        else:
            lIIlIllIllIIllIllIll -= llIllIIlIlIIlllIllIl
    return lIIlIllIllIIllIllIll

class IlIIIlIllIIIlIllllII:
    def __init__(self):
        self.IlllllIIIIlIIIIllIll = 59

    def lIlIIIlllIllIIlIIIIl(self):
        lllllIIlllllIIllIIll = 4
        while lllllIIlllllIIllIIll > 0:
            self.IlllllIIIIlIIIIllIll /= lllllIIlllllIIllIIll
            lllllIIlllllIIllIIll -= 1
        return self.IlllllIIIIlIIIIllIll

    def lIIlIIIlIlIllIIIllIl(self, lllllIIlllllIIllIIll):
        if lllllIIlllllIIllIIll > self.IlllllIIIIlIIIIllIll:
            return lllllIIlllllIIllIIll - self.IlllllIIIIlIIIIllIll
        else:
            return self.IlllllIIIIlIIIIllIll - lllllIIlllllIIllIIll

def lIllIlIIllIIlIIllllI():
    lllllllIIlIIlIIIlIll = 5 + 75
    IIIlIIIIlIIIIIIlIlll = [4 for _ in range(5)]
    for lIIIlIIIIIIlIIIllIlI in IIIlIIIIlIIIIIIlIlll:
        if lIIIlIIIIIIlIIIllIlI % 2 == 0:
            lllllllIIlIIlIIIlIll += lIIIlIIIIIIlIIIllIlI
        else:
            lllllllIIlIIlIIIlIll -= lIIIlIIIIIIlIIIllIlI
    return lllllllIIlIIlIIIlIll

class lIlIIllIlIIlIIlIllIl:
    def __init__(self):
        self.lllIlIIllIIIIllIlllI = 63

    def IlIIIIIlIIllIllllllI(self):
        lIIIIlIlIIIllIIIlIll = 62
        while lIIIIlIlIIIllIIIlIll > 0:
            self.lllIlIIllIIIIllIlllI += lIIIIlIlIIIllIIIlIll
            lIIIIlIlIIIllIIIlIll -= 1
        return self.lllIlIIllIIIIllIlllI

    def lIIIllllIIIllIlIIlll(self, lIIIIlIlIIIllIIIlIll):
        if lIIIIlIlIIIllIIIlIll > self.lllIlIIllIIIIllIlllI:
            return lIIIIlIlIIIllIIIlIll - self.lllIlIIllIIIIllIlllI
        else:
            return self.lllIlIIllIIIIllIlllI - lIIIIlIlIIIllIIIlIll

def IlIIIIIIIIlIllllIIII():
    llIIIIIllIlIlIlIIIlI = 25 - 100
    IIlllIlIlIlIlIIlllll = [10 for _ in range(5)]
    for llllIllIllllIIIIIllI in IIlllIlIlIlIlIIlllll:
        if llllIllIllllIIIIIllI % 2 == 0:
            llIIIIIllIlIlIlIIIlI += llllIllIllllIIIIIllI
        else:
            llIIIIIllIlIlIlIIIlI -= llllIllIllllIIIIIllI
    return llIIIIIllIlIlIlIIIlI

class lIlIIllIllllIIIIlIII:
    def __init__(self):
        self.llIIlllIIIlllllIIlII = 68

    def llIlIlIIIllIIllIlIlI(self):
        lIIlIllIlIlIlllIlIIl = 84
        while lIIlIllIlIlIlllIlIIl > 0:
            self.llIIlllIIIlllllIIlII /= lIIlIllIlIlIlllIlIIl
            lIIlIllIlIlIlllIlIIl -= 1
        return self.llIIlllIIIlllllIIlII

    def lllIIIlIlIlIlllIIIll(self, lIIlIllIlIlIlllIlIIl):
        if lIIlIllIlIlIlllIlIIl > self.llIIlllIIIlllllIIlII:
            return lIIlIllIlIlIlllIlIIl - self.llIIlllIIIlllllIIlII
        else:
            return self.llIIlllIIIlllllIIlII - lIIlIllIlIlIlllIlIIl

def IlIIIllIIIlllIlIIllI():
    IIIlIIlIIllIlllllllI = 49 / 81
    llIIlIIlIIlllllIllIl = [1 for _ in range(5)]
    for IlIlIllllIlIIIIlIIlI in llIIlIIlIIlllllIllIl:
        if IlIlIllllIlIIIIlIIlI % 2 == 0:
            IIIlIIlIIllIlllllllI += IlIlIllllIlIIIIlIIlI
        else:
            IIIlIIlIIllIlllllllI -= IlIlIllllIlIIIIlIIlI
    return IIIlIIlIIllIlllllllI

class IlIllllllIIlIIllIlIl:
    def __init__(self):
        self.lIlIIlllllIlllllIlII = 12

    def lIIIllllIlIllllIIlII(self):
        lIlIIlIlIIIlIIlllllI = 14
        while lIlIIlIlIIIlIIlllllI > 0:
            self.lIlIIlllllIlllllIlII -= lIlIIlIlIIIlIIlllllI
            lIlIIlIlIIIlIIlllllI -= 1
        return self.lIlIIlllllIlllllIlII

    def IIlIIIllIlllIIIlIIIl(self, lIlIIlIlIIIlIIlllllI):
        if lIlIIlIlIIIlIIlllllI > self.lIlIIlllllIlllllIlII:
            return lIlIIlIlIIIlIIlllllI - self.lIlIIlllllIlllllIlII
        else:
            return self.lIlIIlllllIlllllIlII - lIlIIlIlIIIlIIlllllI

def lIIlIlIllllIIIIIIIII():
    lIllIlIIlIIIIllIIllI = 94 / 94
    llIIIIIIIIlIIlllllIl = [2 for _ in range(5)]
    for lIlIlIIllIlIlllllIlI in llIIIIIIIIlIIlllllIl:
        if lIlIlIIllIlIlllllIlI % 2 == 0:
            lIllIlIIlIIIIllIIllI += lIlIlIIllIlIlllllIlI
        else:
            lIllIlIIlIIIIllIIllI -= lIlIlIIllIlIlllllIlI
    return lIllIlIIlIIIIllIIllI

def IIIlllllllIllIIllIll():
    IlIlIIIllIllllIIIlll = 19 + 97
    lIIIlIllllIIlIIIIllI = [4 for _ in range(5)]
    for IIIlIllllIIlIlIlIIIl in lIIIlIllllIIlIIIIllI:
        if IIIlIllllIIlIlIlIIIl % 2 == 0:
            IlIlIIIllIllllIIIlll += IIIlIllllIIlIlIlIIIl
        else:
            IlIlIIIllIllllIIIlll -= IIIlIllllIIlIlIlIIIl
    return IlIlIIIllIllllIIIlll

def llIIIlIllIllIllIIIIl():
    IIlIIIlIIIIIlIIIIlII = 53 / 76
    IIllIlIIllIllIIIlIlI = [2 for _ in range(5)]
    for IIlIIIllIlllIIlllIII in IIllIlIIllIllIIIlIlI:
        if IIlIIIllIlllIIlllIII % 2 == 0:
            IIlIIIlIIIIIlIIIIlII += IIlIIIllIlllIIlllIII
        else:
            IIlIIIlIIIIIlIIIIlII -= IIlIIIllIlllIIlllIII
    return IIlIIIlIIIIIlIIIIlII

class lIlIIIIIlIIIIIIIIIll:
    def __init__(self):
        self.lllIlIllIIlIllIIllll = 7

    def IlIlIIllIlIIIIlIIlIl(self):
        lIlIIllllllIIlIlIllI = 81
        while lIlIIllllllIIlIlIllI > 0:
            self.lllIlIllIIlIllIIllll *= lIlIIllllllIIlIlIllI
            lIlIIllllllIIlIlIllI -= 1
        return self.lllIlIllIIlIllIIllll

    def lllIIllllIIIlIIIIIIl(self, lIlIIllllllIIlIlIllI):
        if lIlIIllllllIIlIlIllI > self.lllIlIllIIlIllIIllll:
            return lIlIIllllllIIlIlIllI - self.lllIlIllIIlIllIIllll
        else:
            return self.lllIlIllIIlIllIIllll - lIlIIllllllIIlIlIllI

class lllIIIlIIIlIllIIIlIl:
    def __init__(self):
        self.IlIIIlIIIIlIIlllIlIl = 6

    def lIlIIIlIllIIlIIIlIII(self):
        IIllIlIlIIlIllllIlII = 25
        while IIllIlIlIIlIllllIlII > 0:
            self.IlIIIlIIIIlIIlllIlIl *= IIllIlIlIIlIllllIlII
            IIllIlIlIIlIllllIlII -= 1
        return self.IlIIIlIIIIlIIlllIlIl

    def IlIlllIIlIIlllllIlIl(self, IIllIlIlIIlIllllIlII):
        if IIllIlIlIIlIllllIlII > self.IlIIIlIIIIlIIlllIlIl:
            return IIllIlIlIIlIllllIlII - self.IlIIIlIIIIlIIlllIlIl
        else:
            return self.IlIIIlIIIIlIIlllIlIl - IIllIlIlIIlIllllIlII

class lllIlllIIllIIIlIlIll:
    def __init__(self):
        self.IlIIIllIlIIlIlIlIIIl = 69

    def IllllllIIIIlIllIIIlI(self):
        IIlIIIllllIIIllIlllI = 60
        while IIlIIIllllIIIllIlllI > 0:
            self.IlIIIllIlIIlIlIlIIIl /= IIlIIIllllIIIllIlllI
            IIlIIIllllIIIllIlllI -= 1
        return self.IlIIIllIlIIlIlIlIIIl

    def lIllIllIllIllllIlllI(self, IIlIIIllllIIIllIlllI):
        if IIlIIIllllIIIllIlllI > self.IlIIIllIlIIlIlIlIIIl:
            return IIlIIIllllIIIllIlllI - self.IlIIIllIlIIlIlIlIIIl
        else:
            return self.IlIIIllIlIIlIlIlIIIl - IIlIIIllllIIIllIlllI

class IlIIIIIIIIIIIIlIIlII:
    def __init__(self):
        self.IIlIlllIlIIllIIIIIlI = 95

    def lllIIlllllllIIIIlIlI(self):
        lIIllIlIlIIIlIIlllll = 37
        while lIIllIlIlIIIlIIlllll > 0:
            self.IIlIlllIlIIllIIIIIlI -= lIIllIlIlIIIlIIlllll
            lIIllIlIlIIIlIIlllll -= 1
        return self.IIlIlllIlIIllIIIIIlI

    def llllIIlIIIllIlIlllIl(self, lIIllIlIlIIIlIIlllll):
        if lIIllIlIlIIIlIIlllll > self.IIlIlllIlIIllIIIIIlI:
            return lIIllIlIlIIIlIIlllll - self.IIlIlllIlIIllIIIIIlI
        else:
            return self.IIlIlllIlIIllIIIIIlI - lIIllIlIlIIIlIIlllll

def IlIIIlIllllIlIIlIlII():
    lllIIIllIIIIIllIlIll = 20 / 94
    llIIlIIlIIIlIllllIlI = [6 for _ in range(5)]
    for lIlIIIllIlIlIIIIIIII in llIIlIIlIIIlIllllIlI:
        if lIlIIIllIlIlIIIIIIII % 2 == 0:
            lllIIIllIIIIIllIlIll += lIlIIIllIlIlIIIIIIII
        else:
            lllIIIllIIIIIllIlIll -= lIlIIIllIlIlIIIIIIII
    return lllIIIllIIIIIllIlIll

def IIllllIllIllIlllIlII():
    lIlIIIllllllIlIIIlll = 81 * 76
    llIllllIllIIIIIIIIIl = [8 for _ in range(5)]
    for lIIIIlIlIIIIlIIIIIll in llIllllIllIIIIIIIIIl:
        if lIIIIlIlIIIIlIIIIIll % 2 == 0:
            lIlIIIllllllIlIIIlll += lIIIIlIlIIIIlIIIIIll
        else:
            lIlIIIllllllIlIIIlll -= lIIIIlIlIIIIlIIIIIll
    return lIlIIIllllllIlIIIlll

def llIIlIIIIIIlIlIIIllI():
    IIIIIlllIlIlIIIlllll = 51 / 18
    IIllllllIlIlIlllIlIl = [4 for _ in range(5)]
    for lllIIlIIllIIlIIIlllI in IIllllllIlIlIlllIlIl:
        if lllIIlIIllIIlIIIlllI % 2 == 0:
            IIIIIlllIlIlIIIlllll += lllIIlIIllIIlIIIlllI
        else:
            IIIIIlllIlIlIIIlllll -= lllIIlIIllIIlIIIlllI
    return IIIIIlllIlIlIIIlllll

class IllIlIIIIlIlIlIIIlII:
    def __init__(self):
        self.lllllIIIIllIIIIIIIIl = 34

    def IIIllIlIllllIIlllIII(self):
        lIlIlllIIlIllllIllII = 84
        while lIlIlllIIlIllllIllII > 0:
            self.lllllIIIIllIIIIIIIIl *= lIlIlllIIlIllllIllII
            lIlIlllIIlIllllIllII -= 1
        return self.lllllIIIIllIIIIIIIIl

    def IIlIlIIIIlllIlIllIIl(self, lIlIlllIIlIllllIllII):
        if lIlIlllIIlIllllIllII > self.lllllIIIIllIIIIIIIIl:
            return lIlIlllIIlIllllIllII - self.lllllIIIIllIIIIIIIIl
        else:
            return self.lllllIIIIllIIIIIIIIl - lIlIlllIIlIllllIllII

class IIIlllIIlllIllIlIIII:
    def __init__(self):
        self.llllIllllIIIlIIllIIl = 4

    def lIIIIIllllIlIlIIllIl(self):
        lIIIIlIlIIIlIIIIIllI = 52
        while lIIIIlIlIIIlIIIIIllI > 0:
            self.llllIllllIIIlIIllIIl *= lIIIIlIlIIIlIIIIIllI
            lIIIIlIlIIIlIIIIIllI -= 1
        return self.llllIllllIIIlIIllIIl

    def IlIIlIlIIlIlllIIIIlI(self, lIIIIlIlIIIlIIIIIllI):
        if lIIIIlIlIIIlIIIIIllI > self.llllIllllIIIlIIllIIl:
            return lIIIIlIlIIIlIIIIIllI - self.llllIllllIIIlIIllIIl
        else:
            return self.llllIllllIIIlIIllIIl - lIIIIlIlIIIlIIIIIllI
b='E͉͍͐͏͔͓̖͈͉͒̀͂́̔ͯ̈́͆̀͋ͅͅ͏̙͔͖͍͈͚͖͈̘͈̘͔͙̗͈͖̝͓̖̖͒͆̐̈́̈͗̒̌͗̓͑̉ͯ̀̀̀̀͒ͯ̀̀̀̀̀̀̀̀͒͗̔̑͂́̔̎͂̔̈́̓̚̚͘ͅͅ͏̙͔͖͍͈͚̈́̈͗̒̉̎̈́̓ͅͅ͏͕͔̘̈́̈̇͆̍̇̉ͯ̀̀̀̀̀̀̀̀ͅ͏͓͖͍̝͎͖͈̘͈̘͉͊̑͂͗͌̈͗̓͑̉ͯ̀̀̀̀̀̀̀̀ͅ͏̗͖͙̝̑͒̇̇ͯ̀̀̀̀̀̀̀̀͆ͅ͏͒̀͏͉͉͎͎͇͎̗͈͖͉͌̓͂͐̔̐̀̀͒́̈͌̈͒͗̔̑̉̉ͯ̀̀̀̀̀̀̀̀̀̀̀̀͘̚ͅͅ͏̗͖͙̝͈̑͒̋̓͒̈ͅ͏̗͈͖̻͒̈́̈͒͗̔̑͘͏͉͌̓͂͐̔̐̽̉̾͏͖͈̘͈̘̻͒̈́̈͗̓͑͏͉͌̓͂͐̔̐̅͏͓͖͍͔͕͎͉͊̑͂͗̽̉̉ͯ̀̀̀̀̀̀̀̀͒͒̀ͅ͏̗͖͙͔͔͕͎̙͔͖͍͈͚͖͚͔̑͒ͯ̀̀̀̀̓͐ͯ̀̀̀̀̀̀̀̀͒͒̀͗̒ͯ͗͗͆͗͘̚ͅͅͅͅ͏̴̴̴̶̢̢̢̝̯͍͍͉̫͍͔͈̰̦͍̲͚̘̲͎̥̯̦͔̲̯̺̺̘̱̝͖͈̘͈̘̝͓̖̖̇͋́̐̏̓̏͂͊͂̇ͯ͗̓͑͂́̔̎͂̔̈́̓͘ͅͅ͏͖͚͔̈́̈͗͗͆͗ͅ͏̉̎̈́̓ͅ͏̷̴̢̢͕͔̘̘̘̝̦̱̣̘͚̪̮͕͓͙͚̬̰̮̘͚̫̭͈͓͓͚̮̘͙͚̺̤̭͓͙͚̩̬̭͕̭͙̳͚̬̮̘͙͍͚̺͚̭͖̘͚̫͎̮͙̯͚̫̬̮͓͚̺̮̈́̈̇͆̍̇̉ͯ͐̒͒͋͋̐̇̒͌͆͋͑̒̒͂͒͋͊͑̑̓͋̒̓͐̓̓̒̏͆ͅ͏̸̵̷̴̨̨̡̘̤͚̮̘͙͚̮͓͚̺̮͔͓͚̺̰̭͖͓͙͚̩̮͓̭̥͚̬̮̭͙͚̪̮͚̩͎̭͔͓̘͚̮̭͙̖͚͎̭͓̯͚͖̭͍̭̖͚̫̭͓͚̪̭̭͚̮͖͓͙͚̬̭̖͚̗̭͈͓͙͕͚̹̭͙͚̰̭͇͙͉͚̰̮͔̭͙͚̹͚̭̒́͐͊́͒͋̒̋̒͒͌̒͊͋͆͑̓̒̒́̓͌́͐̒́̒͒͑̒̐͂͐̒́͂̓͂͑̓̒͂͑̓͂̓͂̓̕͏̸͓͙͚̬̭͇͙͚̪̭͗̏̓̑͏̸̵̘͚̫̮͕͓͙̣͚̫͎̭͇̘̖͚̬̮͇͓͉͚͖̭̭̙͚̺͚̭͖̘̺͚̩̬̮͈͙͚̹̗̮͓͙͚͚̮͚̗̭̒͌̒͆̒́͑̒̒̓͗͐̒͂͒̓̒́͏̷̭͙͚̺͖̮͙͚͎̭͓̘͚̰̭͈̭͙̐͐̓́̓̒͂͏̸̸̴̴̴̵̷̨̨͚̹̮͖͚̺̭̘͙͚̫̭̭̳͚̬̭͖̘͔͚̹̭͓̭̯͚̭͔͓̘͚̭̘͓͚̤̭͔̘̺͚̭͇͓͇͚̮͓͙͚̫̗̮͓͚̬̭͖̘̦͚̬̭͖̘͕͚̬̭͉̘͚̺̤̭͕̭͙̥͚̫̬̭̭͙͚̫̮̭͙͚̺̮͓̘͙͎͚̫̭͎̭͔͚̪̮͙͕͚͎̮͓̘͙̥͚̫̮̘͚̭͚̭͙͎͚̩̭͓̺͚̭͓͙͚̹̗̮͓͙͚͚̮͚̬̮͙͍͚̹̗̭̭͙͚͚̮͓͓͚̫̭͇͓͙͚̩̭͔̭͙͉͚̩̮͖̘͔͚̭͖̘͙͚͚̮͍̭͙͚̩̮̏̓̒͑͂͒͐͆͐̒̒̒́͂̒́̓͋̒͂̒́̏̒͂͂͐̔͐̒̏̒͆̒͂̒͑͌͊͒̏͂̒͒̓́͊͊̒̔͂̓͌̓̒̒͂͐̓͂̓̒͂͆͑͗͐̒͂͒̓̒͒͑̓͒̈́͂̒͗͊̋̓͂̒́͂͂͑͆͏̵̶̨̨̭͙̰͚̫̮͖͙͚̫̮̘͖͚̫̭͔̭͙͚͎̮͉͙̖͚̬͎̮͎̭͙͚̭͙͚͖̭͔̘͙͚̬̭̭͚̭͓͚̹̮͓͙̱͚̮͎̭͙̘͚̰̮̘̙͚̩̭͖̘͙̙͚̮͎̭͙͚̪̰̮͓͙̓̓͒̏͒̒͊́̓̒͂̏͑̓͂́͒̒̒́͂͊̓̒͂͌͂͂͒̒͂́̏͐̕͏̴̶̴̸͚̬͖̭͇͓̩͚̭̭͙͚̬̮͈͙͚̬̮͓͚̹̮͓͙͚̬͎̭̭͉͚̩̤̮͓͚̫̮͔̭̦͚̫̭͓͚̩̮͇̘͚̫̮̘͈͚̭͍͙͚̩̬̮̘͚̺̮͍̭͙͚̗̮͓̭̥͚̬̮̭͔͚̹̮̒́̏͑̏̏̓̓̏͒̒͗͑͋̒͐̒͒̒̓͑̒̋̒́͒͑̒͂͒̓͌͒̒͒̏̏́̒͊͋̒͘͏͓͙̬͚̬̬̮͏̸̸̴̨̘͙͕͚̫̰̮̭͇͚̭͖͓͙͚̬̭͙͚͚̫̭͓͚̩̭͌̒͂͌̓͊̒̓̓͏͓͙̦͚͖̮̳͚̭͂͑̓̒͂͒͏̴̨͓͚̬̬̮̭͙͚̪̰̮͈̭͙͚̩̭͍̘͚̩̭͖̘͚̭͓̰͚͎̭͉̘͙̹͚̮͓͓̣͚̫͖̭͓̒͐͒̓͂̒̒̔́͊̒́͂͊̒͑̒ͅͅ͏̴̴̸̴̴̴̨̨̡̨̧̨̡̨͚̹͎̮͓͎͚̪̤̮͙͚̪̭̭̥͚̩͎̭͎͓͙̪͚̹̭͉̭͙͚̩̤̮͙͚̫̮͓̭͚̺̭̘͚͚̺̭͔̭̭͚̰̭͖̘͚̫̬̭͇̘͙͎͚̪̮͕͓͙͚̺̭͕̙͚̮̭͙͚̭̘͙͉͚̩̮͔͚̫̗̮͕͓͙͚̫̭̭͓͚̗̮̘͚̫̬̭͎͓͖͚̫̭͓̗͚̩̮͓͚̮̘͙̤͚̬̭̘͚͎̭̘͚̪̭͙̯͚̭͎̭͙͚̗̮͌̒͑̓͐̒͂͌͊̓͌̏̒͑̒̓̒́̒̓͐̓̒͂͊͐͂̓͋̓̒̔̏͋̒͂͑̒̒͊͒̒͒̒́͒͑͒͐̒͐͂͑̒̏͑̓͂͊͂͏̨͚̤̮͓͙͚̬̮͔̭͚̹̮͕͙͚̹̭̘͓͚̫͚̭͈̭͍͚̤̭͎̘͚͎̮͇̭͙͈͚̩̮̓̒͑͂̓̒̏͊̓͒͊̒̒͂̒̒́͆͘͘͏͙̩͚̬̮͓͉͚̰̭͓̘͙͚̗̭̘͙̯͚̪̮͎͙̬͚̪̭͇͙̤͚͖̭͓̫͚͎̮̘͙͚̺̮͓͙̦͚̪̭͎͓͚̹̰̭̓͆͒̒́͂́͐͂̓͒̓͂̓̒͂͒͗̏͐̏̒̑͏̷̢̨͓͚̫̮͇̭͙͚͎̭͈̭͚̫̭͓͙͚̗̭͓͙͚̬̭͉̭͙͚̭͇̘͔͚̬̭̒͐͒̓́̒͊͒͒͌͂͊̏́̏̒͏̸̘͙͚͚̭͚̮͓͙͚̪͚̮̤͚̬̮͎̭͈͚̭͔̘͙̥͚̬̮́͑̓̒͆́͂͑͆͑̓̒̏̒́͒́͏̸̭͙͙͚̮͓͍͚̩̗̭̘̖͚̩̭͎̘͙͚̹̭͓̘͙͚̫̰̮͖͚̬̮͓͍͚̭͎̘͙͚͎̮͇̘͙͈͚̩̮͂͒̒͋̒͊̐͊͑̓̒͂͑̒́̏͂͂͆͘͏̸̸̴̴̡̨̪͚̬̭͈̘͙͚̰̭͓͓͙͕͚̗̮͎͓͙̯͚̩̤̮͎͙̩͚̩̤̭͇̩͚̩̭͓̫͚̮̭͙͚̺̮͓͙͓͚̪̭͎͚̹̰̭͚̫̭͎̘͙͚͚̭͉̭͇͚̬̮͕͚̫̰̭͓͙̲͚̬̭͉̭͙͚̬̮͉̭͚̬̭̓̒͆́́̓̓̒̓̒́͒̑̏͐̏̓̒͌͐̓̒͐͒̓͂̒͐̓̒͊̏͂̒̕͏̸̸̘͙͚̭̭͚̮͔͙͚̭̘̤͚̫̭̘͈͚̭͔̘͕͚̬̮́̏͑̒͑́͂̓͆͂͂͊̒͌̒͂͒̒̏͏̸̭͙͙͚̮͓͙͍͚̩̗̮͕̭͙͚̩͖̭͎̭͙͚̹̮͂͒͊̐͊͏̸͙͚̫̰̭̘͓͚̬̮͓͙͔͚̭͎̘͚͎̮͇̭͙͚̪̮̓͋̒͑́͆̒̑́̋͆͘͏̸̴̧̨͙͚̬̮͖̘͙͚̰̭̭͙͚̫̮͕̘͙̯͚̪̭̘͙̬͚̪̗̭͔̭͙̤͚̩̭͓̫͚̪̰̮̭͙͚̩̭͚̪̭͎̭͚̹̤̭̓͆̓́͒͂͒͂̓̒͒͗͒̓̒͑̏̒͐͏̴̨̨͓͚̫̮͍̘͙͚͎̮͓͚̬̤̮͙͚̭͓͙̱͚̺̭͉̭͙͚̬̭͇̘͙̗͚̬̮͙̒̓͒̓́͑̒͊͐̓͌͂̓͊̈́͊̓͏̸̸̡͚̭͓͚̫̮̘͙͚̭̭͚̫̮͙͚̩͎̭͔̘͕͚̮́̏͑̒͑̓͒͆͂͒̒͑̓͑̒͂͂͏̸̘͙͚̮͓̘͚̩̗̮͕̭͙͎͚̩͖̭͎͓͖͚̹̮͕̭͙͚̹͖̮͖͚̬̤̭͈̭͙͔͚̩̭͎̘͙̮͚̮͇̘͙͈͚̺͚̮͗͂͒̒̒͊͐̓̒̓͂̓͘͏̧͚̬̮̭͚̤̭̭͚̗̭͙̯͚̮͈͙̬͚̪̮͖̘̩͚̭͓͙͇͚͎̮̭͙͚̺̭͙̓̒͆͒̒͑́͒̒͌́͐̓͂͊̓̏̒͂̏̓͂͒̓̏͒̓͏̴̴̢̨͚̪̭͍̘͔͚̹̰̭͓͚̫̮͕͓͙͚͎̭͈̭͇͚̬̭͍̘͕͚̭͓͙̱͚̫̭͉̘͙͚̬̭͇̘͈͚̬̭̏̒͐̒̓͒̓́̒̒͂͊͊͆̒͏̸̸̴̡̨̘͙͚̭͓͓͚̮͓͓͙͚̭̘͚̫̮͈͚̹̰̭͔̘͙͚̮́̏̒͑́͂͆͂͌̒͑̓̒͂͂͏̸̢̭͙͚̫̗̭̫͚̩̗̭̦͚̩͖̭͈͙͚̩̰̮̭͙͚̹̭͈̘͖͚̫̮͓͙͔͚̭͎̘͙̯͚̫̮͇̭͙͚̩̭͓͙̪͚̬̮͓͉͚̤̭͔̭͚̗̭͗͐̓̒͋̓̒̓͒͒̒͊͑͂͊̏͆͑͆͒̒́̒͌́͘͏̨̨̨̘͙̯͚̪̭͖̘͙̬͚̪͖̮͖̘͙̤͚̭͓̫͚̩̮̭͙͚̺̭͙͚̪̮͔͙͚̹̰̭͖̘͙͚̮͕͙͚̩̮́͂̓̒̏͒͑̏͒̓͑̏̓͗́̓̓͆͏̡̨̨̡͓͚̬̤̮͙͚͖̭͓͙͚̗̭͉̭͙͚̩̮͉̭͙͚̬̮͙͚̭͔͙̥͚̮͔͓͙͚̪͖̭̭͚̬͎̮͈͚̹̭͔̘͖͚̬̮̒͊͐̓͌͂͊͂͆̏͊̓͂́̏̓́͂͆͑̒͑̓̒͆̒́͏̸̘͙͈͚̮͓͍͚̩̗̭͓̺͚̩͖̭͍͓͙͚̩̰̭͓͙͚̹̭͉̘͓͚̬̤̮͓͍͚̫̭͎̘͙͚̩͖̮͇̘͙͉͚̪̮͂͒̒͌̒̐͊͒̒͑̒͆̓͆͘͏̸̦͚̬̭͈̘͍͚̰̭͔͓͚̫̮̓̒͆̒́̒̑͏̴̸̨͓͙̯͚̩̤̭͓̘͙̩͚̪̮̘̩͚̭͓̫͚̪͖̮̭͙͚̪̮͓͚̪̭͍̘͙͚̹̤̭̓͒̒́̓̒͒͒͐̒̒̏͏̸̵̨̨̨̨̘͙͚̫̮͇̭͙͚̗̮͓͓͇͚̬̮͔͕͚̭͓͙̲͚̺̭͉̭͙͚̮͉̭͙͚̬̮͉̭͙̬͚̭͙͚̭͉͙͚̪̗̮͓̤͚̫̤̭͈̘͈͚̹̭͔̘͙͚̗̮͒̓́̒̓̒͂̏͊́͂̏̔́̏͑̓́͂̓͆̓̒̒͂͂͏̸̸̴̸̴̷̴̡̨̘͙͚̮͓͙͚̩̗̮͕̭̦͚̩͖̭͎̘͚̹̮͖̘͙͚̫̤̮͕͓͚̬̮͎̘͙͔͚̫̭͎̘͚̮͇̭͙͚̩̭͓͙͚̬̮͓͙͚̰̭͔͓͚̫̭͕̘͙̯͚̪̤̮͎͙̬͚̪̮̘̩͚̰̭͓͙͇͚͎̮̘͙͚̺̮͓͚̪̭͎̭͚̹̰̭͚̫̭͇̘͙͚̩̭͍̭͇͚̬̬̮͙͚̫͚̭͓͙͚̺͎̭͉̘͙̦͚̬̭͇̘͚̬̭͐͂͒͌̒̒̏͊̓̒͆͊̒̒́͊͆͑͆͒́̒̑̓͒͒̒͂̓͂͒̓̏͐̒̏̒͌͐̓̒̓͒̓̒͐̓͌͊̒͐͘͘͏̴̭͚͚̭͓̘͚̮͓̘͙͚̪̮̤͚̫̭͈̘͈͚̹̭͔̘͙̥͚̬̮̒̑́̒͆́͂͆̓͒̓̒̒͂͂͏̢̘͙͙͚̫̗̭͙͚̩̗̮͕̘͙͚͚̩̭͉͙͚̩̰̭͖͓͙͚̹̮͓͚̫͖̭͈̭͙͔͚͖̭͎̘͙͚̩̮͇̘͙͇͚͎̮͐̓̔͊̓̓͐̓̒́͂̏́͘͏̸̴̸̸̨̨̨͚̬̭͈̘͙̩͚̰̭͓͙͚̫̮͖͙̯͚̪̰̮͓͙̬͚̪̗̭͔̭͙̤͚̭͓͙͚̩͖̮̘͙͚͚̩̭͙͚̪̮͔͚̹̰̭͖͓͙͚̫̮͈͓͙͚̭͎̭͇͚̫̭͓͕͚̫̭͓̗͚̹̭͉̭͙̤͚̩̭͇̘͚̬̮͉͓͚͚̭͓͓͚̫̮͔̭͙͚̮͔̤͚̫̬̭͈̘͙͚̪͎̭͔̘͙̥͚̗̮̓̒͌͆́͒͂̓͐͂͊̓͊͒͒̓̒̏̓̒̑͒̓́̏̒͒͒̒͒͊̒̒͒̒͌́̒͆̓͆͂̓̒͑͂͏̸̸̭͙͚̭͙͚̩̗̭̭̦͚̩͖̭͍͓͚̩̰̮͓̘͙͚̹̮͕͖͚̫̭̭͍͚̭͎̘͚̫͚̮͇̘͙͚͎̮̓͂͐̓͊͋̒̒̏͒̓̒̏͌̒͂̒̑̓́͘͏̸̸̨̨̥͚̬̭͈̭͙̹͚̰̭͓͚̫̭͕͓͙̯͚̮͇͙̬͚̩̮͖̘͙̤͚̫̭͓̹͚̮̭͙͚͚̺̭̘͚̪̭͓͙̓̒͆́͑̒͌͂͊̓̓̒͂͒̏͒̓̒̏͊͏̸̷̨͚̹̤̭͓͙͚̫̮͇͓͙͚͎̮͔͓͚̫͖̭͓͙͚̬̭͓͙͚̬̰̭͉̘͙͚̭͇̘̘͚̬̮͉͓͙͐͒̓́̒͊͒͌͆͊͆͂̏̒͏̴̨̨͚̭͓̘͙̥͚̮̭͙͚̪͖̮͖̤͚̫̮͎̭͈͚̭͔̘͙͚̬̮́̏́͂͑͆̓̒̒́͂͏̸̸̭͙͖͚̮͓͙͚̩̗̭͇̭̖͚̩̭͎͓͙͚̩̰̭͖̘͙͚̫̰̮͔͖͚̬̭͈̭͍͚̭͎̘͙͚̮͇̭͙͚͎̮́͒̔̒͊̐̓̒͆̒́̓͂́̏́͘͏̸̸͙͚̬̮̖͚̤̭͚̗̮͈̭͙̯͚̪̭͖̘͙̩͚̩̤̭͇̩͚̩̭͓̫͚̮̭͙͚̺̭͚̪̭͓͙̓̓͆͑̓̒́͒̓̒̑́͂̓̒̓̒́͒̑̏͒̓̒̑̏͊͏͚̹̰̭͏̴̵̨̨̨̘͚̮͇̘͙͚̩̭̘͚̬̰̭͓͙͚͚̭͓̗͚̺̭͉̭͙͚̬̭͇̘͙͚̬̮̙͚͚̭̭͙͚̫̮͓͓͙͚̮̤͚̫̭̘͙͚̗̭͔̘͚̮̒̓́̓͆͐̒͊͒͌͂͊̒͂̏͊̓̒́͒̓͆͂͂͐̓̒͂͌͑͂̒͐͂͂͏̸̭͙͚̮͓͚̩̗̮͕̘͙͚̩̭͍̘͚̹̮͕͙͚̫̤̭̘͓͚̬̬̮͓͙͔͚̭͎̘͚̬̤̮͇̭͙̘͚̩̮͑́͒̒͒͊̒̏͊̓͋̒͑́͊̒̒͆̕͘͏̸̸̸̸̴̨̨̨̩͚̬̭͈̭͚̤̭͓̘͚̫̮͔̭͙̯͚̪̤̮͙̩͚̩̭͔̭͙̤͚̩̭͓͙͚̩͖̮̘͙͖͚̮͓͙͚̪̭͎̭͙͚̹̤̭͕̭͙͚̭͉͓͙͚̭͉̭͚̫͎̮͔͕͚̹̭͓͙̱͚̭͉̘͙̣͚̬̭͇̘͙͚̬̮͉͓̙͚͚̭̭͙̥͚̫̭͉̭͙͚̪̮̤͚̫̮͙͚̺͖̭͔̘͕͚̮̓̒͆̒̋́̒̑͊̓̏̓͊͒́͒͐̏͂́̓͂̏̒͊̓̒͊́͂̒́͒̓͆̓͐̓̒͑̓͑̒́͒̕ͅ͏̸̢̭͙͚̪͖̮͓͙͚̩̗̭͓͙͚̩͖̭͈̘͖͚̹̮͓̘͙͚̫̰̭̭͓͚̫͖̮͓͙͔͚̤̭͎̘͙̮͚̫͚̮͇̘͙͚̪̭͓͚̬̮͖̘͚̤̭͔̭͚̫̭̓͒͑͌͊̒͊͑̒͑͂̋͆͑̒͆̒̋́̒̑͘͏̨͙̯͚̪̭̓͏̸̴̴̴̨̨̨̡̘͙̬͚̩̤̮̘̩͚̫̭͓͙͚̩̮̭͙͙͚̪̭͙͎͚̪̭͎͓͙̰͚̹̰̭̭͙͚̭͙͚̩̮͓͓͇͚̬̭͍̘͙͚̫̭͓͙̤͚̺̭͉̘͙͚̬̮͉̭͚̬̮͉͓͙͚̭͔͚̮̘͙͚̪͚̮͚̫̭͈̘͙͚̪̗̭͔̘͚̬̮͒̒̓͊̏͒͒̓̏͐́͋̓̓͆̒͂͌͒͊̓͆̒͌͂́̏̓̒͆́͂͒͆͒̓̒͑̒͐͂͏̸̴̧̢̧̘͙͚̪͖̭͚̩̗̭̖͚̩̭͈̘͙͚̩̰̭͇͙͚̫̤̮͓͖͚̬̮͓͍͚͚̭͎̘͙͚̮͇̘͙͇͚͎̭͓͚̬̭͈̭͙͚̰̭͓̘͚̗̮͖̭͙̯͚̪̮͖͓͙̬͚̪̮̘͙̤͚̭͓̫͚̩̮̭͙͓͚̩̮͓͕͚̪̭͎̭͚̹̰̭̑͐̓̒͋̓̒͊̓̓̒͑̒́́̓́͑̒͆̏́̒̑́͂̏͒͂͒̓̒̏͒͐̒̏̒͐͘ͅ͏̸̨̢̨̨͙͚̮͙͚̗̭͈̭͇͚̬̬̮͕͚̭͓͚̺̭͉̭͙͚̩̮͉̭͙͈͚̬̭̓́͑̓̓́̒͐̓̒͂͊͊̒̔̓͏̨̡̭͙͚͚̭͔͓͙̥͚̫̮͔̭͙͚̪͖̭̘͚̬͖̮͈͚̹̭͔̘͚̩̮́̓͆͊̒͑̓̒͊̒̏͊͏̸̨̨̘͙͚̮͓͙̗͚̩̗̮͕̭̮͚̩̭͎͙͚̩̰̮͓͙͚̹̭͍̘͖͚̫͎̮͎̘͙͔͚̭͎̘͚̮͇̭͙͚̪̮͐͂͒̒͊̓̐͒͒̒͂̒̑͂͌͆͘͏͙̤͚̬̮͖̘͙̩͚̰̭͓͓͙͚̗̭͖͙̯͚̪̰̭̓͆́͂́̓͏̴̘͙̬͚̩̬̮͖̘̩͚̬̰̭͓͙͚̮̭͙͓͚̩̭͚̪̮͔͓͙̒̓͊́̓͒͒̓̒̏̕͏̴̨̢̨̨͚̹̰̭͕̘͚̮͙͚̮͓͚̬̮͕͚̭͓̗͚̺̭͉̭͙͚̩̮͉̭̖͚̬̭̒̓́͑̓̓͂̏͑̒͊͐̓̒͂͒͊̒̓̒͏̵̭͙͓͚͚̭̭͙͚̫̮̘͙͚̭̭̤͚̬͎̭͈̘͙͚̩͎̭͔̘̘͚̪͚̮́͑̓͐͆͂͂͒̒͑̒͏̭͙͏̸̢͚̭͙͚̩̗̭͓͙̗͚̩͖̭͇̘͙͚̹̮̘͙͚̹̮͖͚̬̤̮͎̘͙͔͚̪̰̭͎̘͙̮͚̫͚̮͇̘͙͚̩̮͂͐̓̔͌͊͑͒͐̓̒͋͆͘͏͚̬̮̘͙̹͚̰̭̓̒̓͆͒́͏̸̸̸̨̨̡͚̗̭̘͙̯͚̪̤̮͖͓͙̩͚̩̮̘̩͚̤̭͓̬͚̮̘͙͚͚̺̭͙̳͚̪̭͙͓͚̹̰̭͕͙͚̭͉͓͙͚͚̮͔͓͇͚̬̭͍̘͙͚̹̭͓̗͚̺͎̭͉̭͙̹͚̭͇̘͙̪͚̬̮͉̘͔͚͚̭͚̫̭͎̭͙͚̮͖͚̬̮͎̭͈͚̪͖̭͔̘͓͚̩̮̓̒͌́͑͆͒̒́̓̒͂͒̏͒̓̏͊̓̓́̓́̒͌͊͊̒́̏̒́͒̓̒͑̓͆͂͂̓̒͆̒̒͊͏̸̸̢̢̢̨̘͙͙͚̮͓̫͚̩̗̮͕̭͚̩̭͇͓͙͚̩̰̮͕̭͙͚̫̤̭̘͓͚̫̭͈̭͍͚̩̭͎̘͙͚̩͖̮͇̘͙͚̪̭͓͚̬̮͖̭͙͚̰̭̘͚̫̭͕͙̯͚̪̭́͒̒̒͊͌̒͊̒͊͌͆͑̒͆͊́͒̒͌̓͘ͅ͏̸̘͙̩͚̩̮̘̩͚̪̭͓̫͚̮̘͙͆͒̒͊̓̒͂͒͏̴̨͚̩̮͓͙̫͚̪̭͎̙͚̹̰̭͔̘͚̫̭͍͙͚̩̭͍̭͚̫̭͓͙͚̹̭͓͙̱͚̹̭͉̭͙̥͚̮͉̭͚̬̮͉͓͙͐̏̓̒̒̓͒̓̓͆̒͊͒͒͌͆͊̓͂̏̒̔͏̡͚͚̭͓͓͚̭͍̭͙͚̩̮͚̫̮͎̭͙͚̩̭͔̘̘͚̮́̒͆́͂͆̓͑̓̒͂͑͂̒́͒͏̸̸̴̢̨̨̨̨̨̭͙͚̪͖̭͙͇͚̩̗̮͕̭͚̩͖̭͈̭͚̩̰̭͍̭͙͚̫̰̮͖͖͚̬̬̭͈̭͙͔͚̪̗̭͎̘͚̩̮͇̘͙̖͚̺͚̭͓͙͚̬̮͖̭͙͚̰̭͔͚̫̮͈̘͙̯͚͖̮͇͙̬͚̩͎̭͇̩͚̬͖̭͓͙͚̫͚̮̭͙͚̺̭͚̪̮͔͓͙͓͚̹̰̭͖̭͙͚̮͕͓͙͚͚̭͖̘͚̫͖̮͔͙͚͚̭͓͙̤͚̺̭͉̘͙͚̩̮͉̭͙͚͚̬̮͙̬͚͚̭͓̭͙̥͚̫̭͉̭͙͚̩̗̭̭̤͚̫̭̘͈͚̰̭͔̘͖͚̪̮͒͐̓̒̒̏̓̒̒̒̏͑͂͆̏́̓̒̑͂̓̓̒̓͊͒̐̏͒̓̒͐̏́̓͂̒͊̓͌͂͊̓͊̓́̓͆͑̒͌̒́̒͘͏̸̭͙͚̭͙͚̩̗̭͇̘̖͚̩̭͇͓͚̩̰̮͕̘͙͚̫̤̭̭͓͚̫̗̮͎̘͙͔͚͎̭͎̘͙͚̪̮͇̘͙͚̩̮̓͂͐̓̒͊̒̏͒̒͂̓͆̔͆̕͘͏̸̴̸͙̣͚̬̮̘͙͚̰̭̭͙͚̫̮͎̭͙̯͚̪̤̮͇͙̩͚̪̮̘̩͚̗̭͓̩͚̩̮̭͙͚̩̭͙͚̪̭͎͙̬͚̹̰̭̭͙͚̫̭̘͙͚̭̓͆͒̓́͒͂̓̓͒̒͂̓̒͆͒͒͒̓̓̏̓͐͒͋̓́̏͏̴̸̵̨̡̨̘͇͚̫̮͙͚̬͖̭͓͙͚̹̭͉̭͙̦͚̭͇̘͈͚̬̮͔͚͚̭̘͙͚̭͎͓͙͚̪͖̭͉̘͚̬̮͎̭͙͚̹̭͔̘͕͚̪͚̮̒̏͐̓͌͊́̏̒͊̓̒́͒́͂͆̒̓͑̒͏̢̭͙͚̪͖̭͙͚̩̗̮͕̭͚̩̭͉͙͚̩̰̮͓̘͙͚̫̰̮͔͖͚̫̭͈̭͍͚̩̭͎̘͚͎̮͇̘͙͚͎̮͐͐̓̒̋͊̓̓̒̏̒͆̒̒͂̔́̕͘͏̷̸̸̴̨̨̨͉͚̬̭͈̘͙͚̰̭͓͚̗̭͖̘͙̯͚̪̰̮͎͙̩͚̩̮͖̘̩͚̗̭͓͙͚̩̮̭͙͚͚̮͓͙͚̪̭͓͙͚̹̤̭͕̭͙͚̫̭͍͙͚͚̭͎̭͇͚̫͚̮͙͚̭͓̗͚̭͉̘͙͚̩̮͉̭͙͚͚̬̮͉͓͔͚̭͔̭͙̥͚̫̭͙͚̭̘̤͚̬̮͎̭͈͚̭͔̘̘͚̪̮̓̒͆͊́͒̒̑́̓͂̒͂̓͊͆͒́͒͐̏͊͗͒̓̓͂̒͐̓͌́͂͊̒́͂̒́̏̓͋̓͆͂͊̒͊̒́͊̒͏̸̸̴̭͙͓͚̭͚̩̗̭͇̘͚̩͖̭͈͖͚̩̰̮̭͙͚̫̤̭̭͖͚̬̭͈̭͍͚̗̭͎̘͙͚͎̮͇̘͙̙͚̩̮͂͐̓̒̒̈́̓̒͒͒̒̒͂͂͆͘ͅ͏̸̴͍͚̬̮͖̭͙͎͚̤̭͔̘͙͚̫̮͖̭͙̯͚̪̮͎͙̬͚̩̰̮͖̘̩͚̭͓͙͚̬̤̮̘͙͚̪̭͙̳͚̪̭͍̘̙͚̹̰̭̓̒͆́͂͂̓̒́͊̓͊͒̐͒̓̏̒͏̸̨̨̨̭͙͚̫̭͉̭͙͚͚̭̘͚̫̮͔͕͚̭͓͚̺̭͉̭͙̪͚̩̮͉̭͇͚̬̮͉̭͙͚̭͔͓͚̫̭̘͙͚̪͚̭̭̤͚̬̭͈̘͙͚̪͚̭͔̘͓͚̮͒̓́͐̒͊̓̓̒͂̏͊̒̔̒͗́̏̒͑̓͊͆͑̒̓͑̒͂͂͏̸̵̸̸̴̸̸̴̴̴̵̸̴̨̨̡̨̡̨̭͙͚̭͚̩̗̭̖͚̩̭͍͓͖͚̹̭͓̘͙͚̫̤̭̘͓͚̫͖̮͎̘͙͔͚̩̭͎̘͚̮͇̭͙͚͎̭͓͙͚̬̮̭͙͚̰̭͔͓͙͕͚̫̮͖͙̯͚̮͍͙̩͚̩̮͖̘͙̤͚̬̭͓̮͚̫͚̮̭͙͚̩̮͓͙̯͚̪̮͔͓͚̹̰̭͓͙͚̫̮͖͓͙͚̭͍̭͇͚̬̮͔͙͚̹̭͓͙͚̫̭͉̭͙͚̬̭͇̘͙͈͚̬̮͉̘͙͚̭͓͙͚̭͓͙͚̮͓͚̫̭͈̘͈͚̬̭͔̘͙͚̪̮̑́͐̓̒̈́͋̓̒͊̒͊͊̒̏̒̒͂͋́͑͆͒̓́̓͂͊̓͒̓̒͒͑͐̏̒͐͒̓͂̏̒̓͌͊̏́̏͒́͂͌͆͂̓̒͂̒͂͘͘͏̘͙͚̪͖̮͓̖͚̩̗̮͕̭̮͚̩̭͇͓͖͚̩̰̭͎̘͙͚̹̮͖͚̫̗̭͈̭͍͚͎̭͎̘͙͚͎̮͇̭͙̗͚̪̭͓͙͚̬̮͖̭͍͚̤̭͓͙͚̗̭͑͒̒̒͊̒͒͒̓̒̒͂͂͂͆͑̓͆̒́͒͂́͘͏͙̯͚̩̰̮͖͓͙̬͚̩͎̭͇͙̤͚̪̗̭͓̫͚̫͚̮̭͙̓̓̓̒͒͏̴͚̪̭͙̳͚̪̭͎͓͔͚̹̤̭͒̓̏̒͏̨̡̨͓͙͚̫̭͇̭͙͚͚̮͓͚̫͎̭͍̘͙͚̫̭͓͙͚̭͉̘͙̣͚̭͇̘͚̬̮͍̘͙͚͚̭̘͚̭͈͙͚̪̗̭̘̤͚̬̭̘͙͚̩̭͔̘̘͚̩̮͒̓͂͑̒͊͌͊͊́͂́̏̒͂́͒̒͑́͂̓͆͋̒̓͌͑͊̒͊̕͏̸̡̭͙͚͚̮͓͚̩̗̮͕̘͙͚̩͖̭͉͚̹̭͈͓͙͚̹̮͖͚̬̮͓͙͔͚̩̭͎̘͙͚̩͖̮͇̘͙͚̪̮́͒̒̏̓̒̏͊͒͐̓̒͂͑͆͂̏͆͘͏̸̵̴̨̨̨̨͙̲͚̬̮̭͙͚̤̭͚̫̮͕̘͙̯͚̮͎͙̩͚̩̤̭͔̭̩͚̭͓͙͇͚̫̮̘͙͚͚̭͙͚̪̭͙͓͚̹̰̭͕̘͙͚̫̮͔̘͙͚̮͔͓͚̬̭͓͕͚̫̭͓̗͚̫̰̭͉̭͙͚̭͇̘͙͚̬̮͙̬͚̭͓͓͙̥͚̫̭͙͚̩̭͓̭̤͚̫̭̘͙͚̪͎̭͔̘͓͚̮̓͆͒͊́͑̓̒͌͂͊̓̒́̓̓͊͒́͒͒̓̏͊̓͒̓́̏̒͊͒̒͊̒̈́͂̏͆͊̓́̏̓͌̓͆̓̒͌͑̒͂͂͏̴̭͙͖͚̫̗̭̙͚̩̗̭̘͙̗͚̩̭͈̭͚̹̭͓͓͙͚̺̭͍̘͖͚̬̭̭͙͔͚̰̭͎̘͙͚̮͇̭͙̙͚̺͚̮͐̓̒͋͊̒̏͊͊̒͌͂͂̓͘ͅ͏̷̸͙͚̬̮͖̭͙̩͚̤̭͔͙͚̫̭̓͆́̓͂͏̴̴̵̨̨̨̨̡͓͙̯͚̪̤̮͎͙̩͚̩̭͇͙̤͚̫̭͓̩͚̩̮̘͙͚̮͓͙̹͚̪̮͔͓͚̹̰̭͕̭͚̭͇̭͙͚̩̭͎̭͚̫̗̭͍̘͙͚̺͖̭͓͙̱͚̫͖̭͉̭͙̥͚̩̭͇̘͙̮͚̬̮͉͓͙͚̭̘͙͚̭͙͚̪͚̭͉̘͚̬̗̭̘͙͚̺͖̭͔̘̘͚̮̓̓̓̒͆͒͐́͒͐̏̒̒̓́̓͆̒͊͌͊́̏͑́͂͋̓͆̒͌͑̒́͂͘͏̸̘͙͚̪͖̮͓͙̙͚̩̗̭͇̘͚̩͖̭͈̘͙͚̹̮͖̘͙͚̹̭͈̘͓͚̫̭̭͙͔͚̩̭͎̘͙͚̮͇̘͙̖͚̺͚̮̒͒̒̋̐͊͒̒̏͌͒̈́͂͘͏̓̒͏̸̸̴̴̨̨̡̨͚̬̮͖̘͉͚̰̭͓̭͚̫̮͎̘͙̯͚̪̭̘͙̬͚̩̭͇͙̤͚̪̭͓̬͚̬̤̮̭͙͚̪̭͙͔͚̪̭͎͓͙̰͚̹̰̭͚̮͓͙͚͚̮͓͓͇͚̬̤̮͔͙͚̬͚̭͓͙͚̬̰̭͉̘͙̤͚̬̭͇̘͙̖͚̬̮͉͓͙͚͚̭͓̭͚̫̭͙͚̩̗̮̤͚̫̤̭̘͈͚͖̭͔̘͓͚̫̮͆̒́̒͌͒̓͒̓̒͒͑͒̓̏͐̓̒͐́̓̓͂̒̓͌͊͂́̒͑̓͊̓͆͒̓̒͌̒͂̒͆͏̸̴̸̢̭͙͚̮͓͙͚̩̗̭͇̭͙͚̩̭͈͓͙͚̩̰̮͓͙͚̫̤̭͈̘͖͚̬̤̭͈̭͙͔͚̪̭͎̘͙̮͚̮͇̘͙͚̩̭͓͎͚̬̮̘͙͚̤̭͔͓͚̗̮̘͙̯͚̪̤̮͕͓͙̩͚̪͚̭͇̩͚͚̭͓͙͇͚̪͖̮̭͙͕͚̩̭͙̯͚̪̮͔̙͚̹̰̭̭͙͚̫̮͓͙͚͚̭̐́͒͒͒͊͒̒͆́̓͆͑̒͆͒̒́̒͌́͌̓̒́̓͒͒̓̏̓̒͐͒͑̓́͘̕͏̴̸̨̨̡̘͚̬̭͍̘͕͚̹̭͓͙̱͚̬̰̭͉̭͙͚̬̮͉̭͚̬̮͍̘͙͚̭̭͚̫̮͔͓͙͚̭͓̭͚̬͚̮͙͚̭͔̘̘͚̬̮̒͊͂̒͒͊̒͒͂́̏͒̒͑̓͆͂̒͑̓͑́͆̒͂͏̢̭͙͚̫̗̭͚̩̗̮͕̭͙͚͚̩̭͇̘͙͚̩̰̮̑͐̓̒̓͊͏̨̭͙͚̹͖̮͓͖͚̫̭̭͍͚̪̭͎̘͚̩̮͇̘͙͚͎̮̓̒͌̒͊̒̑͆̔́͘͏̖͚̬̮̘͉͚̰̭̓̒͆͒̒́͏̸͙͚̫̮͈͓͙̯͚̪̤̮͕͓͙̩͚̩̰̮͖̘͙̤͚̩͚̭͓̮͚̪̮̘͙̓͂̓̒͆͒͏̨̨̨͚̺̮͓͙͚̪̭͓͚̹̰̭͓͚̮͉͙͚̭͇̭͇͚̫͚̮͕͚̹̭͓͚̬͖̭͉̭͙͚̭͇̘͙̪͚̬̭̏͐͂̏͊̒͌͐̒̓́̓̓͂̏̒͐̓̒͊̒̔́̏ͅ͏̘͚̭͓͓͚̫̭͉͓͙͚̪̗̭̭̤͚̬̗̮͈͚͎̭͔̘̘͚̮̒́̏̒͑̓͆͑̒͑̓̒͂̒́͒̕͏̘͙͚̪͖̭͙͐͐̓͏̴̴̴̨̨̨̡͚̩̗̭͚̩͖̭͈̭͙͚̹̭͕̘͙͚̫̰̭̭͖͚̬̬̮͎̘͍͚͎̭͎̘͙͚̪͖̮͇̭͙͚̺͚̭͓͙̩͚̬̮͖̭͙͎͚̤̭͔̘͙͚̗̮͎͙̯͚͖̮͈͙̬͚̩͎̮̘͙̤͚̤̭͓̹͚̫̮̘͙͚̩̮͓͙͚̪̭͔͚̹̤̭͕̘͚̮͓͙͚̮͓͚̫̭͓͕͚̭͓͙͚̬̰̭͉̭͙̣͚̭͇̘̖͚̬̮͉̭͙̬͚͚̭̘͚̫̭̘͙͚̩̮͔͚̫̮͈͚̪̭͔̘͙̥͚̮͋̓̒̈́̐͊͒̒̒͂̏͑͆́͂́̓͂̓͒́̓̒͊͒̓͐͒̏͊̓̒̒̓́͐̓́̏͐̒͊͒̒͂̏͊͂̏̒́͑̒͑̓͊͆̓̓̒͑̓̒͆͂͂͘ͅ͏̸̸̸̴̸̴̨̭͙͚̭͙͚̩̗̭̭͙͚̩̭͍͓͖͚̩̰̭͓͙͚̹̮͓͓͚̫̭̭͙͔͚̪̭͎̘͙͚̪͖̮͇̭͙͚͎̭͓͙͚̬̭͈̭͚̤̭̘͚̗̭̭͙̯͚̪̤̭͖̘͙̩͚̩̭͔̭̩͚̩̭͓̹͚͎̮̭͙͓͚̪̮͓͙̱͚̪̭͎͙͚̹̤̭͔̘͚̫̭͉̭͙͚͚̮͓͇͚̬̮͔͕͚̬̭͓̗͚̫̰̭͉̭͙̪͚̭͇̘̙͚̬̭̓͂͐̓͒͋͒͊̒͋͊̓̒͊͌͊́͑̒͆̒͑́͒̒͌́͑̒̓̒́͒͐̏̓͂̒͐͒̓͂͑̒̓̒͊̒́̏̒͘̕ͅ͏̨̘͙̬͚͚̭͓͓͙̥͚̭͍͓͙͚̪͚̭̭̤͚̬̮͈͚͎̭͔̘͙͚̬̮́́͂͆͒̒͒͑̓̒́́͏̸̴̷̸̴̨̨̨̭͙͚͚̪͖̭̘͚̩̗̭̘͙͎͚̩̭͉͚̹̭͖̭͙͚̹̭̭͓͚̬̤̮͓͍͚̭͎̘͙̮͚̮͇̭͙͚̩̭͓͙̤͚̬̮͚̰̭͔͓͙͕͚̫̮͕̭͙̯͚͖̮͎͙̩͚̪̗̮͖̘̩͚̭͓̹͚͎̮̘͙͙͚̪̮͓͚̪̭͎͓͔͚̹̰̭͕̭͚̭͙͚͚̭͎̭͚̬̬̭͍̘͕͚̬̭͓͙͚̹̭͉̘͙̦͚̬̮͉̭͈͚̬̭͐̓̒͋͊̓̒̏͊͒͒̒͑̒͂̓͂͆͑͆͑̓̒̋́͂̓̒͂̏̓̒͂͒͐̒̑̏̒̒͐́͋̓̓͂̒͊̒́͊̒͘̕͏̸̴̘͙͚̭͓̭͙̥͚̮͕͓͙͚̪̗̮͖̤͚̬̭͈̘͙͚̪̭͔̘̘͚̩̮́̏́͂͆̓̒͆͑͒̒͏̸̴̧̭͙͚̮͓̺͚̩̗̮͕̘͙͖͚̩͖̭͈͙͚̹̮̭͙͚̫̰̭̭͓͚̫͖̭̭͙͔͚̗̭͎̘͙̮͚̫̮͇̭͙͚͎̭͓̣͚̬̮̭͚̰̭͓͚̗̮͈̭͙̯͚̭͓̘͙̩͚̩̭͔̭͙̤͚̗̭͓̬͚̩͖̮̭͙͖͚̩̭͙͚̪̭͍̘͙̒́͒̒̓̐͊͑͑̒͌͂͊́͑̒͆͒̒͑́͑̒͌́͂͊͆́̓̒͒͒̓̏͘̕͏̸̨̨͚̹̰̭͔̘͙͚̮͈̭͙͚͚̮͓͚̫͚̭͍̘͙͚̫̭͓͙̱͚̫̭͉̭͙͚̭͇̘͙̮͚̬̭́̓́͐̒͊͌̏͊͆͂͂̏͏̸̡̭͚͚̭͓͙̥͚̫̭͙͚̪̗̮͕͚̫̮͙͚̭͔̘͓͚̮̒͐́͑̓͋̓͆̓̒͑̓͑́͒̒͂͒͏̸̸̴̵̢̨̨̨̨̡̭͙͚̮͓̤͚̩̗̭̭͚̩͖̭͍̘͙͚̹̭̭͙͚̫̤̭͍̘͓͚̫̭͈̭͍͚̪̰̭͎̘͚̫͚̮͇̭͙͚̺͚̭͓͚̬̮͖̭͙̩͚̤̭͓͓͚̫̭̘͙̯͚̪̮͈͙̬͚̪͚̮͖̘͙̤͚̤̭͓̫͚̪̮̭͙͚̩̮͓͙͚̪̮͔͓͚̹̤̭͖͙͚̫̮͈̭͙͚̩̮͔͓͚̫̗̭͍̘͕͚̬̭͓̗͚̬̭͉̭͙̥͚̩̮͉̭̗͚̬̮̙͚͚̭͙͚̫̮͙͚̩̮͚̬͎̭̘͙͚̩͎̭͔̘͚̗̮͑́͒̒͋̒̋͊͋̒͒̒̒̒͌͑̒͆́̒̑͑̓͂̓̒͆͒͗͐́̏̒̓͒̓͆̒͊̒́͊̒̏̒͊̓̒́͑̓̓͒̓͆̓͐̓̒͌͑̒͐͂͘̕͘͏̸̴̡̭͙͚̪͖̭͚̩̗̭͇̭̺͚̩͖̭͈͚̹̮͓̘͙͚̺̮͖͚̫̮͓͍͚̭͎̘͙͚̮͇̘͙͈͚͎̭͓͙͚̬̮͖̘͚̤̭̭͚̫̮̘͙̯͚̪̮͎͙̬͚̩̮͖̘̩͚̭͓̩͚̩͖̮̭͙͚̪̭͙͖͚̪̭͙͗͐̓̒̐̒̓̒̏͊͊͐̓̒̏͑̒͂͂̓́̓́͑͆̒͑́͒̒͌͌͂̓͆̒͂̓̓̒͒͒͒̓̏͊̓͘͏̷̵̴̨̨̨̨̡͚̹̰̭͚̮͔͙͚͚̮͔͓͇͚̬̮͙͚̭͓͙͚̭͉̘͙͚̩̭͇̘͍͚̬̮͉͓͚̭͔͙͚̫̭͈̘͙͚̪͖̮͚̬͎̮͙͚̩̭͔̘͖͚̩̤̮͐̓̒͐́̓̓͂̒͂͐̓͌͂̏͊́͂̒̒͌́̏̓̓͆͑̓̒͑̓͑̒͏̸̘͙͙͚̭͍͚̩̗̮͕̭͙̗͚̩̭͈̘͚̩̰̮̘͙͚̫̤̭͈̘͖͚̬̤̮͎̘͙͔͚̪̭͎̘͙͚̩̮͇̭͙͚̺͚̮͂͐̓̒͊̒̏͑̒̓͂̏͋͘͏͙͚̬̮̭͚̤̭͔͓͙͕͚̗̭̓̈́͆͒̒̒́́͏̴̴̨̨̨͙̯͚̪̭͖̘͙̩͚̪̭͇͙̤͚̩̗̭͓̩͚̮̭͙͖͚̪̭͙̰͚̪̮͔͚̹̤̭͕̭͚̫̮͙͚͚̮͖͓͚̫͎̭͍̘͕͚̭͓͙͚̹̭͉̘͙̹͚̮͉̭͖͚̬̭̓̓̓̓̒́̓͒͒̓̏̓̒̑̒͐͒͑̓̓́̒͊̒́͂͊͂̏̒͏̴̡̭͚̭͔͙̥͚̭͈͙͚̭̭͚̬̮͙͚̹̤̭͔̘͚̩̮̒̑́̏̓́͂̓͆͂͂͑̒̓͑̓͑̒̏͏̸̨̘͙͓͚̭͙͚̩̗̮͕̘͚̩̭͇̘͙͚̹̮̭͙͚̫̰̭͉̘͖͚̬̮͎̘͍͚̩͖̭͎̘͚̮͇̘͙̙͚͎̮́͐̓͒̒̈́͊̐͊͒̒͂̒̒̑͂́͘͏̢͙͚̬̭͈̭͙̩͚̰̭̓͆́͏̸͙͕͚̫̮͖͙̯͚̪̭͓̘͙̩͚̩̮̘͙̤͚̪̭͓̮͚̮̭͙͙͚̺̮͓͙͚̪̭͍̘͙̬͚̹̤̭̓̓͂͂͒̏̓̒͂̓͒̏͐̈́̏͏̸̵̢̨̨̘͙͚̫̮͈͙͚̭͈̭͚̬̬̭͍̘͙͚̭͓͙̱͚̗̭͉̭͙͚̩̭͇̘͙͚̬̮͉͓͚̭͔̭͙͚̫̮͕̘͙͚̪̗̭̭̤͚̬̮͎̭͈͚̪̰̭͔̘̘͚̫̮͒̓̓͂̏̒͊͌͂̏͊͂̒́̏̓͆͒̒͊̒̒͆͘ͅ͏̸̢̘͙͚̭͙͈͚̩̗̭͓͙͎͚̩̭͇͙͚̹̮͕͓͙͚̹͖̮͓͚̫͖̭͈̭͙͔͚̭͎̘͙͚̩̮͇̘͙̘͚̩̮̑́͐̓͌͊̓͊͑̓̒́͆̏͆͘ͅ͏̨͙̳͚̬̮͖̭͙̹͚̤̭͓̘͚̗̮͖͙̯͚̩̤̭̘͙̩͚̪͚̭͇̩͚̩̭͓̹͚̫̮̭͙̓͆́̒͌́̓͐̓̒̓̒͊͒͏̨̨̨̨̡͚̮͓͙͚̪̭͍̘͙͚̹̤̭͔̘͚̮͖̭͙͚͚̭͉̭͚̫̗̭͓͙͚̬͚̭͓͚̬͖̭͉̭͙͚̭͇̘͕͚̬̮͉̘͚̭͓̭͚̫̭͈͓͙͚̪͖̭̘͚̬̮͎̭͙͚̭͔̘͙̥͚̮́͒͐̐̏̒͐́̓́̒͊͒͌͊̒̔́̏̒̒͐́̏̒͑̓͆͌̒̏͑́͒͂͂͏̸̢̭͙͚̮͓͙͚̩̗̭̘͙͚̩̭͎͙͚̹̭͓͓͙͚̹͖̮͓͓͚̫̗̮͓͙͔͚̪̬̭͎̘͙̮͚̫͚̮͇̘͙͚̪̮̓͂͒͋͋̏͊̓͊̓̒͑͋͆͘͏̴̸̴̢̨͚̬̮̭͙͚̰̭͔̘͚̗̮͖̘͙̯͚͖̮͎͙̩͚̩̰̭͇͙̤͚̬̭͓̮͚̫̮̭͙͖͚̩̮͓͙͚̪̭͎͓͚̹̤̭͕͚̫̭͈͙͚͚̭͍̭͇͚̬̬̭͓͙͚̺͚̭͓͚̺͎̭͉̭͙̪͚̮͉̭͙͚̬̭̓̒͆͒͊́̒̑́͂̓̓͒̓̒͊͒͐̏̒̓̒̓͒̓̓͂̒͒͌͊̒̔́̏̕͏̸̨̘͚̭͓͚̭͉̭͙͚̭͉̘̤͚̬̮͎̭͈͚̩̤̭͔̘͙͚̮̒́̏͒̒͆́͂͆͂̒͒̒͂͂̕͏̨̭͙͚̫̗̮͓͙͎͚̩̗̭̭͙͚̩̭͇̘͚̩̰̭͙͚̹̭̘͓͚̬̬̮͎̘͍͚̗̭͎̘͙̮͚̮͇̭͙͚̪̭͓͙̺͚̬̮͖̘̖͚̤̭̘͚̗̭̐͒͋͒͊̒̏͊̓̓͋̒̒͂͂͆͑͆̒́͑̒̑́͘̕͏͙̯͚̮͖͓͙̬͚̩̭͇͙̤͚̪̭͓̮͚̮̘͙͚̭͙̳͚̪̮͔͓͙̓͂͊͂̓̏̓̒́̓͒̒́͒͒̓̏͏̸̷̨̨͚̹̰̭͕͓͚̮͔͙͚͚̭͍̭͚̬̭͓͙͚̺̗̭͓͙͚̫̰̭͉̘͙̪͚̭͇̘͚̬̮͉̭͚͚̭͚̮͕̘͙͚̩̭̭̤͚̬̭̘͈͚̭͔̘͕͚̩̮̒͐́̓̓͂̒͊͒͌͊́̏̒̋̒͌́͑̓̒͆́͂͆̓͑̒̓͌̒͂͆̒͊͏̭͙͏̸͚̮͓͚̩̗̭͇̭͙̗͚̩͖̭͇̭͙͚̹̭͓̘͙͚̹̭̘͓͚̫͎̮͓͍͚̫͖̭͎̘͙̮͚̫̮͇̭͙͈͚̩̮́͒̒̓̐͊̓͊̒͑̒͊͆͘͏̵̸̴̴̨̨̨͚̬̮̘͙͚̤̭͔̭͚̫̮͔̭͙̯͚̪̰̮͓͙̩͚̩̬̭͇͙̤͚͚̭͓̬͚̬̤̮̭͙͚̪̮͓͚̪̭͍̘͙̰͚̹̰̭͖̘͙͚̮͉͙͚͚̭͈̭͇͚̬̮͔͕͚̺̭͓͚̫̰̭͉̭͙͚̬̭͇̘͙̰͚̬̭̓̒͊͆͒́̒͌͐̓́̓̒͒͐͐̒͑̏́̓̓́̒͆̓̒͆͊̒̔́͏̴̘͙͚̭͔̘͚̫̭͓͙͚̮̤͚̫̭̘͈͚̪͎̭͔̘͙̥͚̮͗́̏̒͆̓͋͆͂͂͒̓̒͌̒́͂͏̭͙͏̸̴̴̴̴̴̧̢̨̨̨̨͚̪͖̮͓͚̩̗̮͕̭̦͚̩̭͈̘͖͚̹̮̘͙͚̺̭̘͖͚̫̮͎̘͍͚̩̭͎̘͙͚̩͖̮͇̘͙͉͚̩̭͓͙͚̬̮͖̭͙͎͚̤̭͙͕͚̫̭͕͙̯͚̪̮͇͙̩͚̩͎̭͇̩͚̩̭͓̩͚̮̘͙͚̮͓͙̳͚̪̭͎̙͚̹̰̭͔̘͚̭̘͙͚̩̮͖͓͇͚̬̭͍̘͕͚̭͓͙͚̺̭͉̭͙̦͚̮͉̭͙͚̬̮͚͚̭͔͓͚̭͙͚̪͚̮͓̤͚̫̰̮͈͚̹̭͔̘͚̩̮͒̒̒͊̒͊͑͊͊̒̓̒̓͆͑͆́͑̓̓̓̓̒̓̒͂͒͑́͒͐̏̓̒̒̓́͋̓̒̒͂͒͊̓́̏̔͊̓̒́̒͑́͂͋̓͆̓̒͑̓̒͆̒̏͘͘ͅ͏̸̸̴̨̘͙͙͚̪͖̭͍͚̩̗̮͕̘͙͚̩̭͎͓͚̹̮͖͓͙͚̺̭͉̘͖͚̫̗̭͈̭͙͔͚̪̭͎̘͚̫̮͇̘͙͇͚̩̭͓͙̪͚̬̮͖̭͙͎͚̰̭͓͓͙͚̗̭̘͙̯͚̪̭̘͙̬͚̩̭͔̭͙̤͚̭͓̬͚͎̮̘͙͚̪̭͙͐̓̒͒͊̒̏͊͊̒̒̑͊͆͑͆́͂́͐͐͂̏̓̒́͒̓͒̓͘͏̸̸̸̴̨̨͚̪̭͎͓͙̬͚̹̰̭͕̭͙͚̫̮͈͓͙͚͚̮͖͓͇͚̫̭͓͕͚̬̭͓̗͚̹̭͉̘͙̪͚̮͉̭͚̬̮͙̬͚͚̭͚̫̭̭͙͚̭̭̤͚̫̭̘͙͚̹͎̭͔̘͖͚̩̮̏͒̓͂̒͊͒̒͊̒͂̏̒͐͊̓́͑̓̒͑̓͋͆͂͒̒͌͑̒͊͏̸̴̢̭͙͚̭͚̩̗̮͕̘͙͚̩̭͉͙͚̹̮͓̭͙͚̹̮͖͚̬̮͎̘͙͔͚̪̗̭͎̘͙̮͚͎̮͇̘͙͇͚͎̭͓͙͚̬̮̭͙͚̰̭͔̭͚̗̮͎̭͙̯͚̮͍͙̩͚̪̭͔̭͙̤͚̩̬̭͓̩͚̫͚̮̭͙͈͚̪̭͙̪͚̪̮͔͙͚̹̰̭͐́͐̓̒̏̏͊̓͊͊͐̓̒͂́́͑͂͆͒̒́̒͌́͂͊̓͒̓̒͒͒̓̏̓͗͘͏̨̨̨̭͙͚̫̭͙͚͚̭͖̘͚̬̭͓͙͚̫̭͓͚̭͉̘͙͚̩̮͉̭͓͚̬̭͒͌̓̓́̒͊͂͒͌͒͊̒̔́͂͂̒͏̴̭͚̭̘͚̭͙͚̪̗̭̘̤͚̫̬̭͈̘͙͚̪͖̭͔̘̘͚̪̮̒̑́̏͒̒͑́͂͋̓͆͌̒͑̒͏̸̸̶̢̨̨̭͙͚̭͙͚̩̗̭̭͚̩̭͈͙͚̩̰̮͖̘͙͚̫̤̭̘͓͚̬̤̭̭͍͚̩̗̭͎̘͙͚̮͇̭͙͉͚̩̭͓͙̣͚̬̭͈̘͙͚̤̭̭͚̫̭̭͙̯͚̭͖̘͙̩͚̩̮͖̘͙̤͚̪̭͓͙͚̮̘͙͚̺̮͓͙͚̪̭͎̭͚̹̰̭̐́͐̓͒͋̒̋͊̓͊̒͌̒͂͆͑͆͊́͑̒͌͑͂͊͂̏̓͊͂͒͑̏͐̏̒͘͘ͅ͏̴̸̧̨͚̫̭͍͓͙͚̭͍̭͚̬̬̭͍̘͕͚̺̭͓͙̤͚̺̭͉̘͙͚̬̭͇̘͙͚̬̮͉͓͚̭͓̘͚̫̭̭͙͚̭̘̤͚̬̗̮͈͚̪̭͔̘̘͚̗̮̓̒͐͒̓͂̏̒͊̒͊͊̓̔̒́̏̒͑̓͌͆͂͊̒͑̓̒͆̒͂͘͏̸̢̘͙͚̫̗̭̫͚̩̗̭͇̭͍͚̩͖̭͈͓͙͚̹̮͖͙͚̫̤̮͓͖͚̬̰̮͓͍͚̩̭͎̘͙͚̩͖̮͇̘͙̙͚̩̮̑͐̓̒̒͊̓̓̒͑̒͆͘ͅ͏̸̴̨̩͚̬̮͖̭͚̤̭͔̘͚̫̭͔͙̯͚̪̮͎͙̬͚̩̮̘̩͚̪̭͓͚̪̰̮̘͙͚̺̭͙̫͚̪̭͎̭͚̹̤̭̓̒͆̒̒́̒͌̓̓͒̒͒̓̒͂͒͐̏͒̓̏̒͐͏̨̨̭͙͚̫̭͎̭͙͚͚̮͕͓͚̫̗̭͍̘͕͚̭͓͚̫̰̭͉̭͙̥͚̮͉̭͚̬̭͒̓́̒͊̒͂̏͊̒̔́̏̒͗͏̭͙͏̡͚͚̭͔̘͙̥͚̫̭͙͚̩̭̭͚̫̮͎̭͙͚̪̬̭͔̘͓͚̬̮́̓͌̓͆̓͒̒͂͑̒͂͏̵̸̘͙͚̫̗̭͚̩̗̭̖͚̩̭͎͓͖͚̩̰̭͓͙͚̫̰̭͓̭͓͚̫̮͎̘͙͔͚̪̤̭͎̘͚̮͇̭͙͚̺͚̭͓̗͚̬̮̭͙̥͚̤̭̘͙͚̗̮̐͐̓̒͋̓̒͊̒͋̒͊̒̑͂̔͑̒͆͒́͒͂́͘͏̸̴̴͓͙̯͚͖̭̘͙̩͚̩̤̮̘̩͚̩̭͓̹͚̪͖̮̘͙͔͚̺̮͓͙͚̪̮͔͓͙͚̹̰̭͂͐͒̒̓̒͒̏͐̏͏̨̨̧̨̨̨̭͙͚̮͔͙͚͚̮͓͇͚̫͎̭͓͕͚̭͓͙̲͚̫̭͉̭͙͚̩̮͉̭͕͚̬̮͉̭͙͚͚̭͔͚̮͖͓͙͚̮͖̤͚̬̮͈͚̪̭͔̘͖͚̫̮́̓̓͂͐̒͒̒͂͊͊̏̒́̓̒͆́͂͆͂͂̓̒͒͑̓̒̏̒͆͏̨̧̘͙͈͚̫̗̭̘͚̩̗̭̘͚̩͖̭͇͖͚̹̮͕͙͚̹̮͖͖͚̫̮͎̘͍͚̪̰̭͎̘͙̯͚̮͇̘͙͈͚͎̭͓͚̬̮͖̘͙̹͚̰̭͔͓͚̗̭͙̯͚̪̰̮͙̩͚̪̗̭͔̭͙̤͚̪̗̭͓͙͚̫̮̭͙͐̓̒͋̒̈́̓̒͊̓̓̓̒̒́̓́͑̒͆́̒͌́͐̓͋̓̓͊͊͒͘͏͚̺̭͙̬͚̪̭͎͔͚̹̤̭̏͒̓̏̓̒͏̸̨̨̨̨̘͙͚̭̭͙͚̮͓͇͚̬̮͔͕͚̭͓̗͚̹̭͉̭͙͚̭͇̘͙̥͚̬̮͉̘͚͚̭͚̫̭͓͙͚̮͓̤͚̬͚̭͈̘͈͚̭͔̘̘͚̬̮́͌̓͂̏͑̒͆̓̒͂̓͊̒̓͂̏̒̑́͒̓̒͆̓͐͆͂̓̒̒͂̒͂ͅ͏̸̴̸̨̨̭͙͚̭͙̘͚̩̗̭͇̭͙͚͚̩͖̭͇̘͙͚̩̰̭͕͓͙͚̹̭͍̘͓͚̬̤̮͓͙͔͚̩̭͎̘͙̯͚̮͇̘͙͈͚̩̭͓͚̬̮̘͙̩͚̰̭̭͚̗̮͕̘͙̯͚͖̮͓͙̩͚̩̭͇̩͚̤̭͓̬͚͎̮̘͙͚̪̭͙͚̪̭͍̘͙͚̹̰̭͖͓͙͚̫̭͙͚̮͕͓͚̫͖̮͕͚̫̤̭͓͙̲͚̫̰̭͉̭͙͚̮͉̭͖͚̬̭͗͂͐̓̐͒̒͑̓́̓͆͑̒̒͆͒́͒̒̑́͂͐͂̓̒͂̓̒́͒͗͒̓͂̏͒͌̓̓́̏̒͊͐̓̒͊͂͂̏̒͘͏̡̭͙̬͚̭͔̘͚̫̭̘͙͚̪̮͓͚̬͖̮͈͚̹̭͔̘͖͚̬̮́̏̒͆̓͌͆̓̓̒͑̓̒͆̒́͏̸̸̢̨̭͙͖͚̭̙͚̩̗̭͓͙͚̩̭͇͓͙͚̩̰̮͓͙͚̹̭͈̘͖͚̬̤̭̭͙͔͚̭͎̘͚̮͇̘͙͚̪̭͓͙͚̬̮͖̭͙̩͚̤̭͙͕͚̗̮͓͙̯͚̪̤̮͍͙̩͚̩̮͖̘̩͚̭͓͙͇͚̪͖̮̘͙͕͚̭͚̪̮͔͚̹̤̭́͐̓̒͌̏͊͐͒̒͌͂͂̒̒́͌͆͑͆́͑̓́͐̓͂̒͂͊̓͒́͒͒̓̒̐̏̓̒͘͘͏̨̨͓͙͚̮́͏̸̧̨͙͚̩̭͎̭͇͚̬̮͙͚̺̭͓̗͚̹̭͉̭͙͚̭͇̘͙̱͚̬̭̓̓͆̒͆͐̓͌͆͊̒́̏͏̴̘͙̬͚͚̭͓͓͚̭̘͙͚̩̮͓̤͚̫̮͎̭͈͚͖̭͔̘͚̬̮́̒͑́͂͌͆̓̓̒̒͂̒͐̏͏̸̸̸̷̨̨̨̨̨̭͙͚̭͙͇͚̩̗̭͇̘͍͚̩͖̭͈̭͚̩̰̭͎͙͚̹̭̭͓͚̫͚̮͎̘͙͔͚̪̤̭͎̘͙͚̮͇̘͙͚͎̭͓͙͚̬̮͖̘͙͚̰̭͙͚̫̮͈̘͙̯͚̪̮͙̬͚̩̭͇̩͚̤̭͓͚̮̘͙͙͚̺̮͓͚̪̭͎͓̙͚̹̰̭͖͙͚̭̘͙͚͚̮͔͓͚̫̗̮͕͚̹̭͓͙͚̗̭͉̘͙̪͚̮͉̭͓͚̬̮͉͓͚͚̭͓̘͚̫̭͉͙͚̩̭͓̭̤͚̫̭̘͙͚̹̰̭͔̘͓͚̮͗͂͐̓̒̒̏̓̓͒̒̓́̓̋́͑͆̏́͑̓͂͊̓͂̓̒͂̓̒͂͂͒̏͐̒̏̒̓́͋̓͂̒͊͐̓̒͊͂͂̏̒̒̑́̒͑̓̓͆̓̒͂͌͑̒͂͂͘̕ͅ͏̭͙͚̪͖̭͙͚̩̗̮͕̘͍͚̩͖̭͇͙͚̩̰̭̘͙͚̹̮͕͓͚̫̮͓͍͚̭͎̘͙̯͚̫͚̮͇̘͙͚̪̮̓͐̓̒̓̐͋͊̓̒̏͑̒́̓͆̕͘̕͏̶̸̴̴̴̵̨̨̡̨͙̺͚̬̮̭͙͎͚̤̭͓͓͙͚̗̭͙̯͚̭̘͙̬͚̩̤̭͔̭̩͚͎̭͓̬͚̫͚̮̘͙͚̭͙͚̪̮͔͔͚̹̰̭͖̘͙͚̭͎̭͙͚̭̘͇͚̫̭͍̘͕͚̹̭͓͙͚̬̰̭͉̭͙̦͚̬̮͉̭͙̦͚̬̮͉͓͙͚̭͔̭͙͚̭̭͙͚̮͚̬̮͙͚̹̭͔̘͕͚̩̮̓͆͒́͂́͐̓͂͊͒̒͂̓̒͒̒́͒͒̓̏̓̒́̓́̏͐̒͊̒͒͊́̏́͂͌͆͂͂͑̓̒͊͑̓͑̒͊͏̸̢̘͙͚̮͓͙͈͚̩̗̭͙͚̩̭͇̭͙͚̹̭͈͙͚̹͖̭̘͓͚̬̤̮͓͍͚̩̭͎̘͙͚̮͇̭͙͉͚̪̮̓́͒͋̓͊͊͊̓͋̒͑̒͒́̓͆͘ͅ͏̸̸̸̨̨̘͚̬̭͈̭͙͚̤̭͔̘͚̫̮͖̭͙̯͚̪̰̮͙̩͚̩̮͖̘̩͚̬͚̭͓͚̩͖̮̘͙͚̺̮͓͚̪̭͙͓͚̹̤̭͕͓͙͚̮͍̘͙͚̭͉̭͇͚̫̮͙͚͖̭͓͙̱͚̬͖̭͉̭͙͚̭͇̘͙̬͚̬̮͙͓͚̭͓̘͙̥͚̮͓̘͙͚̭̘̤͚̬̮͙͚̹̭͔̘̘͚̬̮̓̒͆̏́̒̑͊̓͆̒̓̒͂͒͐̏͐̒̏͊̓́̓͂̏̒̏͐̓͌͂͊͂̏͊̓́̏́͂͆͂͊̒͊͑̓͑͊̒̏̕ͅ͏̸̸̸̢̭͙͓͚̮͓͙͚̩̗̭͇̭͙̗͚̩͖̭͇͓͙͚̩̰̮͙͚̺͖̭͍̘͓͚̬̮͓͙͔͚̭͎̘͙͚͎̮͇̘͙͚̪̮͂͒͑͑̓̒͑́̈́͂͆͘̕͏̵̸̨͍͚̬̮͓͙͚̤̭͓̭͙͚̫̭̭͙̯͚̩̤̮͎͙̬͚̩͎̮̘͙̤͚̰̭͓͙͚̬̤̮̭͙͓͚̺̭̖͚̪̭͎̭͙͚̹̤̭͖͓͚̮͙͚͚̭̓̒͆͒́͂͐̓͒́̓͊͒̏͒̓̒̏͂̒͐́͑̓̓́͏̨̨̘͚̫̮͔͙͚͖̭͓͚̬̰̭͉̭͙̦͚̩̭͇̘͖͚̬̭̒͊̓̓͌͂͊̒̔̒͏̸̘͙͚͚̭͓͚̫̭͙͚̩̗̭̘̤͚̫̤̮͈͚̩̭͔̘͖͚̬̮́͑̒͑̓͊̓͆͌̒͑̓̒͒̒́͏̸̸̨̘͙͚̫̗̭̦͚̩̗̭͚̩̭͍͓͖͚̩̰̭͎̘͙͚̫̰̭͓̭͓͚̫̮͓͙͔͚̪̤̭͎̘͚̮͇̭͙̙͚̺͚̭͓͚̬̮̘͙͚̤̭̭͚̫̭͕͓͙̯͚̪̭̐͐̓̒͋̓̒̋͊̒̒͑̒̒́͑̒͑͆͒̓́͑̒̑͂͘͏̘͙̩͚̩̭͔̭̩͚̬̰̭͓͙͇͚̩͖̮̭͙͖͚̺̮͓͚̪̭͎͙͚̹̰̭͆̒̓͒̏͐̒̋̏̓͂͏̴̨̨̨̡̨͙͚̫̮͔͓͙͚̭͍̭͚̫̭͓͕͚͖̭͓͙͚̫̭͉̘͙͚̮͉̭͙͚̬̮͉̭͙͚̭͚̭͓͙͚̪̗̮͓͚̫̬̭̘͙͚̹̭͔̘͙͚̮̓͒̓͂̏̒͊͊͒̒͂͊̏͆͂̏́́̏͒̓̒͆́͂͊͆̓̒͌͑͊͂͂͏̸̸̸̴̸̴̨̨̭͙͚̮͓͙͍͚̩̗̭̭͙̗͚̩̭͈̭͖͚̩̰̭͉̘͙͚̹̭̭͖͚̫̮͎̘͍͚̩̭͎̘͙̮͚̫͚̮͇̭͙͚̩̭͓͙̺͚̬̮͖̘͙̹͚̰̭͔͓͙͚̫̮͓͙̯͚̭̘͙̬͚̩̮͖̘̩͚̬̰̭͓͚̩͖̮̘͙͚͚̩̮͓͚̪̭͎͙͚̹̰̭͖̭͚̭͍͓͙͚̭̭͇͚̫̮͔͙͚̫͎̭͓͙̤͚̬̭͉̘͙̤͚̬̭͇̘͚̬̭͗͂͒͋͊̒͒͑̒͊̒͂̓͆͑͆́͂͐͂͊͐̒̓̒͂͒͐̒̓̏̓̒̓́̓͂̏͌̒̓̓͌͊̏̒͘̕͏̭̙͚̭͔͚̫̮͔̭͙͚̪̗̭͍̘̤͚̫̮͙͚̹̬̭͔̘͚̪͚̮̒́̏̓̒͑̓͆̒͂͑̓͑̒̏͏̸̸̴̴̢̡̘͙͚̮͓̫͚̩̗̭͇̭͚̩͖̭͍̘͚̹̭͇͓͙͚̹̭̘͓͚̫͖̭͈̭͍͚̭͎̘͙̯͚̪̰̮͇̭͙̘͚̪̭͓͙͚̬̮͙͚̤̭͔͓͙͕͚̫̮͔͙̯͚͖̮͓͙̬͚̪̮̘̩͚̬͖̭͓̬͚͎̮̭͙͖͚̩̭͙͚̪̭͓͙͚̹̰̭͕͚̫̮͓͙͚̩̭͒́͒̒̒̒̏͊͒͌̒̒́͊͆͑̓͆͑̓́̓͂͐̓͒̒̓̒͂͒͒̓͒̏͊͂̓̒͐͒̓̓͘͏̴̨̨̘͇͚̬̮͕͚̬̭͓͙͚̗̭͉̭͙̥͚̩̭͇̘͙͚̬̭̒͆͐̓̒̏͊͂́͏̭͙͏͚͚̭́͏̵̡͙͚̮͔̭͙͚̪̮͚̬̭̘͙͚̹͎̭͔̘͚̬̮̓́͂͆̓͒̓̒͊͌͑̒͐́͏̸̢̭͙͚̫̗̭͙͚̩̗̭̭͙͎͚̩͖̭͍͓͙͚̹̭͕̘͙͚̺͖̮͖͖͚̬̭͈̭͍͚̪̭͎̘͙͚̮͇̭͙̖͚̩̮͑͐̓͋͊̓̒͆̒̓͂́͆̕͘͏̴̨̨̨̨̡͚̬̭͈̘͚̤̭͓̘͙͚̗̭͖̘͙̯͚̪̰̮͍͙̬͚̪͖̮͖̘̩͚̭͓̬͚͎̮̭͙͚̺̮͓͍͚̪̭͎͙͚̹̤̭͕̭͚̮͕͓͙͚͚̭͖̘͚̫͖̮͙͚̺̭͓͙̱͚̭͉̭͙͚̬̭͇̘͙͚̬̮͚̭͔͓͚̭͙͚̪͚̭͓̭͚̬͖̮͎̭͈͚̭͔̘͚̪̮̓̒̔͆̒̒́͂́̓̒́̓̓̒͂͒̒̏͐̒̏̓̒̓́̓́̒͊͐̓͌̓͊́͂̈́͊̓̒́̏̒͆́͂͑̓͆̒̒́͒̒͐͊͘͏̴̸̘͙͚͚̪͖̮͓͚̩̗̮͕̭͚̩͖̭͎͙͚̹̮̭͙͚̹̮͖͚̬̮͎̘͍͚̭͎̘͙͚̪͖̮͇̘͙̙͚̪̭͓̥͚̬̮͓͉͚̤̭͙͚̫̮͙̯͚̩̰̭̘͙̬͚̪̮͖̘͙̤͚̩̭͓̩͚̩͖̮̘͙͚̭͙͒̒̒̈́̓̐͊͐̓͐̓̒̒́̏̓͆͑̒͆͒̒́͑̓͂͌̓͒̓̏̓̒͒͗́͒͒̓͘ͅ͏̷̸̨̨̨̨̡͚̪̮͔͙͚̹̰̭͕͙͚̮͕͓͙͚̭͇̭͚̫̮͔͕͚̬̭͓͙͚̫͖̭͉̘͙̪͚̩̭͇̘͇͚̬̮͍̭͙͓͚͚̭͚̫̭͙͚̩̗̭͉̘͚̫̭̘͙͚̩̭͔̘͙̥͚̫̰̮̏̓͗̓́̓͂̏̒͊̏̓̒͒͊̒́͑̓̒͑̓͌̓͆̒͂͌͑͏̴̸̴̸̨̧̨̡̘͙͖͚̫̗̮͓̤͚̩̗̭̭͚̩̭͍͓͙͚̩̰̭͉̘͙͚̫̤̮͓͓͚̬̭̭͙͔͚̪̰̭͎̘͙̯͚̫͚̮͇̭͙͚̺͚̭͓͍͚̬̮̭̖͚̤̭͔͚̗̭͕̭͙̯͚̪̤̮͇͙̩͚̪̭͔̭͙̤͚̩̤̭͓̬͚̮̭͙͔͚̩̭͙͚̪̮͔͚̹̤̭͕̭͚̫̭͓͙͚̭̭͚̬̰̮͔͕͚̭͓͙͚̬̰̭͉̭͙̦͚̩̮͉̭͙͚̬̮̙͚͚̭͚̭͓͙͚̭͍̘͚̬̭͈̘͙͚̩̬̭͔̘͕͚̮͒̒͋̒̋͊̐̓̒͂͌͋͑̒͆͒̒́̓̒͌́̓͒̓̒͂̓͒͒̓̏̓̒͌̒̓͒͌̓́̏͌̒͊̓̒͂̏͊͊̓̒́͒̓̒͆́͂͊͆͂̒͊͑̒͂͒͘͏̸̸̘͙͚̮͓͙̗͚̩̗̭̘̺͚̩͖̭͍̘͙͚̹̭͓͙͚̹͖̭̘͓͚̬̮͓͍͚̭͎̘͙͚̩͖̮͇̭͙̙͚̺͚̮̓́͒͋̒̐͊͋͊̒͑̒́͂̈́͘͏̖͚̬̮̭͙͚̰̭̓̒͆͒̏́͏̸̴̵̨̨̨̡͙͕͚̫̭̘͙̯͚̪̰̮͇͙̬͚̪̭͔̭͙̤͚͖̭͓̹͚̮̭͙͚̺̮͓͙͚̪̭͓͙͚̹̤̭͕̘͚̮͓͙͚̗̮͓͚̬̰̭͍̘͕͚̺̭͓͚̹̭͉̘͙͚̬̭͇̘͙͚̬̮͍̘͚͚̭͓͙͚̮͔̭͙͚̪̗̭̭͚̫̰̭̘͙͚̪̭͔̘͚̫̰̮̓͐̓̏́̓̒͂̓͒͐̏͐͐̏͊̒̓́͑̓́͐̒͊̒͒͊̒̔̓̈́́̒͌́͑́͂͆͒̒͌͑͒̒̏͏̭͙͏̴̴̴̴̴̨̨͚̫̗̮͓͉͚̩̗̮͕̘̺͚̩͖̭͇͓͙͚̩̰̭͍͓͙͚̫̤̭͈̘͖͚̬̰̮͓͙͔͚̤̭͎̘͚̫͚̮͇̘͙͚̩̭͓͚̬̮͓͙̹͚̤̭͓̘͙͕͚̗̮͈͙̯͚̩̰̮͇͙̬͚̩̭͇̩͚̩̭͓̫͚̩͖̮̭͙͓͚̩̭̖͚̪̭͎̭͙͚̹̤̭͔̘͚̫̭͈͙͚̭͍̭͇͚̬̭͓͕͚̺̭͓͙̱͚̺͎̭͉̭͙̣͚̬̭͇̘͚̬̭͒̒̒̐̒͑͂̒̑̋͆͑̒͆͒́́̓̓͂̓̒̓̒͒͒̓̒̏̒͐͒̓̓́̏̒͒̒̓͊̒͌͘͏̵̨̡̨̭͙͚̭͙͚̫̮͖̭͙͚̩̗̮͚̫̤̮͎̭͙͚̭͔̘͓͚̮́̏͑̓̓͆͑̓̒͑́̒́͂͏̸̸̸̴̸̨̨̭͙͙͚̫̗̮͓͚̩̗̭͓͚̩̭͍̭͙͚̹̮͕̘͙͚̫̰̮͓͚̫̮͎̘͙͔͚̩̗̭͎̘͙͚̪͖̮͇̭͙͚͎̭͓̗͚̬̮̘͙͚̤̭̘͚̗̭̭͙̯͚̪̮͎͙̩͚̩̮̘̩͚̭͓͙͇͚̮̘͙͚͚̪̮͓͚̪̭͎͙̬͚̹̤̭͓͙͚̮͒̒͌̒̈́͊̐͊͐̓̒̏̔́͑̒͆͒͊́͑̒͌́͑̓͒̒́̏̓͂͒͐̒̋̏̓͐́͘ͅ͏̨̨͓͙͚͚̮͓͚̫̭͍̘͕͚͖̭͓͚̗̭͉̭͙̤͚̩̮͉̭͙̤͚̬̭̓͂͑̒͊͊̒͂͊̒̔͂͏̸̸̡̨̘͙̬͚͚̭͓͓͚̭͎͙͚̮͕͚̫̭͈̘͙͚̹̬̭͔̘͙͚̮́̒͑́͂̓͆͂̓̒͑́͂͏̢̘͙͕͚̪͖̮͓͙͚̩̗̭̭͚̩̭͇͓͖͚̹̭͙͚̺̮͓͚̫͎̭̭͍͚̪̭͎̘͙͚̩͖̮͇̭͙͍͚̺͚̮͒̏͋̒͊̒͊͐̓͊͐̓̒͌̒͒͂͘͏̸͉͚̬̮͉͚̰̭͔͓͙͚̫̭͔̭͙̯͚̭̘͙̬͚̩̬̮͖̘̩͚̬̬̭͓͙͚͎̮̘͙͖͚̮͓͚̪̭͎͚̹̤̭̓̒͆͑̓̒́͂͂͊͐̒̓͊͂͒́͒͐̒̑̏̓̒̑͏̸̸̴̴̡̨͓͙͚̫̮͇̘͙͚͚̮͔͓͚̬̭͓͕͚̫̰̭͓͙͚̫̭͉̘͙̪͚̬̭͇̘͕͚̬̮͍̘͚͚̭͔̘͚̫̭͓͙͚̩̭͓̭̤͚̫̭͈̘͈͚̪̗̭͔̘̘͚̬̮͒̓͂̒͊͒̒͊͆̒̒̑́̒͑̓͐͆̓̒̒̒̏͏̸̸̭͙͚͚̪͖̮͓͙͚̩̗̭͇̘͙͖͚̩͖̭͈͓͚̹̮͙͚̫̰̭͓̭͖͚̬̭̭͙͔͚͎̭͎̘͙̮͚̮͇̭͙̙͚̺͚̭͓̦͚̬̮̭͙͚̰̭͓͙͕͚̫̮͓͙̯͚̪̤̭̘͙̬͚̪̗̭͇͙̤͚̭͓̬͚͎̮̘͙͚͚̭͙͚̪̭͙͒̑̒̏͊͑̓̒͂͌͂͂͑̒͆͒͊́͑͐͒̓͂͒̓̒́͒́͒͒̓̏͊̓͘ͅ͏͚̹̰̭͏̴̨̨̨̨̭͚̫̭͇̭͙͚̩̭͈̭͚̫̮͔͕͚̫̤̭͓͙̱͚̺̭͉̭͙͚̩̭͇̘͙̳͚̬̮͉̘͙͚͚̭͓̘͚̮͓͙͚̪̮͖̤͚̫̬̭̘͈͚̺̭͔̘͙̥͚̫̮̒͐͒̓̒͊͊̓̒͊͂́̒͑́͂̓͆̓̓̒͌̒̏͆͏̭͙͏̸̸̴̴̴̢̨̨͚̮͓͚̩̗̮͕̭͙͚̩̭͇͓͖͚̩̰̮̘͙͚̺̮͕͖͚̬̤̭͈̭͍͚̪͚̭͎̘͙͚͎̮͇̭͙͚̪̭͓͚̬̮͓͙̥͚̤̭͔͙͚̫̭͓͙̯͚͖̮͙̩͚̩̮̘̩͚̩̭͓̬͚̮̘͙͚̮͓͙͚̪̮͔͙͚̹̰̭͕͚̫̮͇̘͙͚̩̭͈̭͚̫̭͍̘͕͚̬̭͓͙̱͚̫͖̭͉̘͙͚̬̮͉̭͚̬̮͍̘͙̰͚̭͂͒̒̏͊̒͐͊̓̒̒͂͂͌͆͑̒͆͒́̓͂͒͂͋̓͒̒͆̓̒́̓͒̒́͒͐̏̓̓̒̓͒̓͆̒͊͒̒́͊̒͐́̏͘ͅͅ͏̡͚̭͙͚̩̮͔͚̬̭͈̘͈͚̭͔̘͚̬̮̓̒͑́͂͋̓͆̓̓̒͒̒͂̏̒̏́͏̭͙͖͚̪͖̭͙͈͚̩̗̭̭͚̩͖̭͈̘͖͚̹̭͓̘͙͚̹̭͈̘͓͚̫̭͈̭͙͔͚̪̤̭͎̘͙͚̮͇̘͙̗͚͎̮͐̓͋̒̈́̒͊͒̒̓̈́́̓́͘͏̸̴͚͚̬̮͖̭͙̹͚̤̭͔̘͚̗̭͓͙̯͚̪̮͙̬͚̩̮͖̘͙̤͚̗̭͓̬͚̬̤̮̭͙͚̪̭͙͚̪̮͔͔͚̹̤̭̓̒͆́̒̑́͑͂͋̓́̓̒͒͐͒̓͑̏̓̒͏̷̨̨̨̨̭͚̮͙͚̗̭͍̭͚̫̭͍̘͙͚̫̤̭͓͙͚̫̭͉̘͙͚̩̭͇̘͙͚̬̭̒͐́͑̓̓́̒͊͒͌͊̏̏͏̴̡̘͙̰͚̭͚̫̮͕͙͚̩̭͉̘͚̬̮͙͚̭͔̘͓͚̩̮́̏͑̓̒͆̓̓͆̓̒̏͑̓͑́̒͊͏̘͙͏̸̸͚̭͙͈͚̩̗̭͇̘͚̩͖̭͇͖͚̩̰̭͉̭͙͚̹̮͔͖͚̬̭͈̭͙͔͚̪̤̭͎̘͙̯͚̮͇̘͙̘͚̩̮͂͐̓̒̈́̓̒͊̓̒͂͂͆͘͏̵̸̨͙͚̬̮̘͙͚̰̭̘͚̫̮͇͙̯͚̮͓͙̩͚̪̮͖̘͙̤͚̪̭͓̩͚̮̭͙̓̓͆͒́͒̒̑̓͂͊͐͒̏̓̒͂͒͏͚̭͙̲͚̪̮͔͚̹̰̭́͒͒̓̏̓̒͘͏̸̡̨̘͙͚̫̭͙͚͚̮͕͓͚̬̬̮͕͚̹̭͓̗͚̺̭͉̭͙͚̭͇̘͚̬̭͒͋̓̓́̒͊͐̓̒͂͊̒̓͂̏̒̔͏̡̭͙͚̭͓̘͙̥͚̭͎̭͙͚̪̭̘͚̬̗̮͎̭͈͚̭͔̘͚̮͂́̏́͂͆̓͌̒̒͂͒̒̏͂͂͏̸̸̭͙͚̮͓͙͚̩̗̭̺͚̩̭͈͖͚̩̰̭͕͓͙͚̹͖̮͓͓͚̬̮͓͍͚̩̭͎̘͙͚̬̤̮͇̘͙͚͎̮͗́͒̔͋̓̒͊̓̒̓̒͑̒͒̈́̔́͘͏̸̸̸̴̵̨̨̨͎͚̬̭͈̭͙͚̰̭̘͚̗̭̘͙̯͚̪̮͎͙̩͚̩̭͔̭̩͚̫̭͓̫͚̮̘͙͖͚̮͓͙͚̪̭͓͔͚̹̰̭͖̘͚̭͓͙͚͚̮͓͇͚̬̤̮͙͚̫̭͓͚̺͎̭͉̘͙̤͚̬̭͇̘͙̹͚̬̮͚͚̭̭͙͚̫̭͈̘͙͚̪̗̮̤͚̬̮͈͚̪͚̭͔̘͚̮̓̒͆͊́͒̒̑́͐̓̒̓̒́̓͒́͒͐̈́̏͊̒̒̓́͋̓͂͑̒͐̓͌͊̒̔͊̓̒́͒̓͆͑̓̒̓͑̓̒̒̏́͂͘͏̘͙͙͚̪͖̮͓͙͚̩̗̮͕̘̺͚̩͖̭͉͙͚̹̭͖̘͙͚̫̤̭̭͓͚̫̮͎̘͙͔͚̫͚̭͎̘͚̬̤̮͇̘͙͚̪̮͒͊̒̓̐͊͒̒͊̒̒̓͆͘͏͙͚̬̮͖̘͙͚̰̭͓͙͕͚̗̮͖͙̯͚̩̰̮͈͙̬͚̩͎̮͖̘͙̤͚̭͓͙͚̪̰̮̭͙̓̓͆̓́͒́̓̓́͂̓͊͒͏̴̨̢̨͚̺̭͚̪̭͎̭͙͚̹̤̭͖͚̫̮͈͙͚͚̭͖̘͚̫̮͔͕͚̺̭͓͙̱͚̬̭͉̭͙̪͚̩̭͇̘͙͚̬̭̏͒̓̒̋̏̓̒͐͒̓̓́̒͊̓̓̒̓͊̏͏̘͙͏̵͚̭͓͓͙͚̮͓͙͚̩̭͓̭̤͚̬͎̭̘͙͚̪̭͔̘͖͚̮́̏́͂͒͆̓̒͌͑͆̒́͂͏̸̸̸̴̵̨̧̨̨̨̘͙͚̮͓͙͚̩̗̭̭͚̩̭͎͖͚̹̭͙͚̹͖̮͖͓͚̫̭͈̭͙͔͚̪̰̭͎̘͚̮͇̘͙͉͚̩̭͓͙̹͚̬̮̭͚̤̭̘͚̫̭͕͓͙̯͚͖̭͕̘͙̩͚̩̭͇̩͚̬̰̭͓͚̩̮̘͙͚̩̮͓͙̬͚̪̭͎͓͙͚̹̤̭͕͚̮͙͚̗̭͉̭͚̫͚̭͍̘͙͚̺͚̭͓͙̱͚̹̭͉̭͙͚̩̭͇̘͚̬̮͉̭͚̭͓̘͙͚̭͎͙͚̪̭̭̤͚̬̗̮͎̭͈͚̩̰̭͔̘͙͚̮̐͂͒̑͋̒̋͊̓̒͊͐̓̓̒͊̒̒́̓͆͑͆͒̒̋́͒̒̑͂̓̒̓̒͂̏͒̑͐̏͂̓̒͐́͑̓̓́̒͊͌͊̓̒͗̒́̏́͂̓͆̓͒̒̒͂͒͘͘͏̸̢̭͙͚͚̭̬͚̩̗̮͕̭͙̗͚̩̭͈͙͚̩̰̭͓͙͚̺̭͓̭͖͚̬̮͎̘͍͚̪͎̭͎̘͙̯͚̫͚̮͇̘͙͉͚͎̮́͐̓̒͊̓͊͊̒͂̒́͘͏̸̨̡̢͚̬̮͖̘͙͚̤̭̭͚̗̭͓͙̯͚̭̘͙̬͚̩͎̭͇̩͚͚̭͓̹͚̮̘͙͓͚̺̮͓͚̪̮͔͓͙͚̹̰̭͖͚̭͎̭͙͚̗̮͓͇͚̬̭͓͕͚̫̭͓͙͚̬̰̭͉̭͙͚̭͇̘̓̒̐͆̒́͒̒̑́͑͂͊͒̓̒͂̓̒́͒̏͐̒̐̏͂̓̒͐́̓́͑̒͆͒̒͆͊́̏̒͏̨͚̬̭͏̘͚͚̭͓͚̫̮͓͓͙͚̪̗̮͕̤͚̬͚̭͈̘͈͚̪̰̭͔̘̘͚̮̒́͑̒͑̓͆̓̒̒̒͂͂͘͏̸̶̵̴̸̨̨̧̨̭͙͚̮͓͚̩̗̭͇̘͙͚̩͖̭͈̭͙͚̹̭͎͙͚̺̮͓͓͚̫̮͓͙͔͚̪̬̭͎̘͚̬̤̮͇̘͙͚̩̭͓̪͚̬̮̘͙͚̰̭͓͙͚̗̮͙̯͚̩̰̭͓̘͙̬͚̩̭͔̭̩͚̰̭͓̬͚̪͖̮̭͙͚̩̭͙͚̪̭͓͚̹̰̭͔̘͙͚̫̮͓͙͚͚̭͇̭͚̫̮͔͕͚̫͎̭͓͚̹̭͉̭͙̹͚̭͇̘͙̬͚̬̮͉̭͙͓͚͚̭̘͙̥͚̮͔̘͙͚̮͖̤͚̫̰̭̘͙͚̰̭͔̘͖͚̫̰̮͗͂͒̒̏̐͊̓͊̓̒͑̒̑̏͆͑̒͆͒́͒͂́͌̓̒͂̓̒͒͒͒̓̏͊̒͌͒͑̓́̒͊̏̓̒͊̒̔̓́̏́͑́͂͆͂͂̓̒͌͑͂̒͘͏̭͙͏͚̫̗̭͙͎͚̩̗̭̘͙͎͚̩̭͇̭͙͚̹̭͇̘͙͚̺͖̮͔͖͚̫̗̭͈̭͍͚̪̭͎̘͙͚̩͖̮͇̭͙͚̺͚̮͐̓͋͊̐͊̓̒̒͆̈́͌͘͏̸̡͚̬̮͖̭͙͚̰̭̘͙͚̫̮͇̭͙̯͚̪̰̭̓̒͆́͒͂̕͏̴̴̴̨̘͙̩͚̩͎̭͔̭̩͚̩̰̭͓͙͚̩͖̮̭͙͚͚̩̮͓͙̰͚̪̭͎͔͚̹̰̭͖͓͚̫̮͇͙͚̩̮͓͇͚̬̬̮͙͚̺̭͓̗͚̫͖̭͉̭͙̥͚̬̭͇̘͙̬͚̬̮͉͓͙̒̓͊͒͐̏̓̒̒͐͒̓̓͑̒͐̓͌͒͊̒͏̡͚̭͓̘͙̥͚̭͎͓͙͚̪͚̭͉̘͚̬̭̘͈͚̰̭͔̘͚̬̮́̏́͂͆̒͒͌̒͂̒̏͂͏̴̴̴̨̨̧̨̘͙͚̫̗̭͍͚̩̗̮͕̭͙͎͚̩͖̭͈͓͚̹̭͓̘͙͚̹̮͖͚̬̭͈̭͙͔͚̪̗̭͎̘͚̩̮͇̭͙͇͚̩̭͓͙̺͚̬̮͖̘͙͎͚̤̭̭͚̗̭̘͙̯͚̪̮͙̬͚̩̭͔̭͙̤͚̪̭͓̩͚͎̮̭͙͈͚̩̭͕͚̪̮͔͚̹̰̭͖͓͙͚̫̭͎͙͚͚̭͈̭͇͚̫̭͓͙͚̬̭͓͙̲͚̺̭͉̘͙͚̬̮͉̭͙̱͚̬̮͍̭͙͚̭͙̥͚̫̭͉͙͚̪͚̮̤͚̬̭͈̘͈͚̭͔̘͖͚̩̤̮̒͐̓̒̒̏͊̓͒̓̒͂̒̒̏͆͑͆́͒̒̑́͐͂͊̓͂̓̓̒͂͒͒̓̒̏̓̒͌͒̓̓͂̒͊͒͌͊͊́̏͑̓̓̓͆͑̓̒̏̒́͆̒͘͏̸̴̢̭͙͚̭͙̘͚̩̗̭͇̘͍͚̩̭͉͙͚̩̰̭͈̘͙͚̹͖̮͔͓͚̫͎̭̭͙͔͚͚̭͎̘͙̯͚̬̤̮͇̭͙͚̺͚̭͓͎͚̬̮̘͙̹͚̤̭͓͓͚̗̭͕̭͙̯͚̪̰̭͖̘͙̩͚̪͚̮̘͙̤͚̩̭͓͙͇͚̩̮̭͙͚̪̭͙̬͚̪̮͔͚̹̰̭͗͂͐̓̒͊̓̓̒͌͂̏͑̒͆͒́̒͌́͒̏̓̏͒̒͒̓̏̓̒͌͘͏̸̴̸̨̡͓͙͚̫̮͓͙͚͚̮͔͓͚̫͎̭͍̘͕͚̹̭͓͚̭͉̭͙̪͚̬̭͇̘͉͚̬̮͍̘͙̬͚͚̭̘͚̭͍͙͚̭͓̭͚̬͚̮͎̭͙͚̤̭͔̘̘͚̗̮͒͐̓́̒͊̒͂͊̒̔́͂̒́͒̒͑́͂̓͆͂̒͑́̒͂͏̸̸̡̨̭͙͚̭͚̩̗̭͙͖͚̩̭͈̭͚̩̰̮͖̘͙͚̫̰̮͖͚̫̮͓͍͚̪̭͎̘͙͚̮͇̘͙̙͚̺͚̭͓͙̤͚̬̭͈̘͍͚̤̭͓̭͚̗̭͗́͐̓̒͋̓͊̒̏͑̓̒͑̒́̓͑͆̒́̒̑́͘ͅ͏̸̴̨̨͓͙̯͚̭͖̘͙̩͚̩̭͇͙̤͚̪̭͓̫͚̩̮̘͙͈͚̪̮͓͙̰͚̪̮͔͙͚̹̤̭͕͙͚̮͙͚̮͂͊̓̏̓̒͆͒͐̏̓͗̓́͑̓̓͂̏͏̴̴̨̨͓͇͚̫͚̮͔͕͚̫̗̭͓͙͚̫̰̭͉̘͙͚̬̭͇̘͙͚̬̭̒̓̒͊͆͏̡̘̙͚͚̭͚̫̭͓͙͚̭̘͚̫̬̭͈̘͙͚̹̰̭͔̘͕͚̗̮̒́͒̓̒͑̓͋͆͂͂͌̒͑̒͂͏̸̨̭͙͚̪͖̭͚̩̗̭͇̘͙͚̩͖̭͇̘͙͚̩̰̭͇̭͙͚̹͖̮͓͚̬̮͎̘͙͔͚̫̭͎̘͚̮͇̘͙͚̩̮̓͐̓̒͊̐͐̓̒͆̓̒̒͂̔͆͘͏̸̨͙̳͚̬̮͖̘͙͚̰̭̘͚̫̭͕̭͙̯͚̪̮͙̬͚̩̮̘͙̤͚̬͎̭͓̹͚̫͚̮̭͙͓͚̺̭͙̭͚̪̭͚̹̰̭̓͆̒́͑̒̑͊̓͂͒̓̒͒̏͒̓̏͊̓̒͘͏̸̨̨̨̡̨̡͙͚̭͙͚͚̮͓͚̫̭͓͕͚̹̭͓̗͚̬̭͉̭͙͚̭͇̘̖͚̬̮͉̘͙͚͚̭̭͙̥͚̫̭͍̭͙͚̩̗̮͚̫̤̮͎̭͙͚̭͔̘͓͚̬̮̓́͌̓̓́͑̒͊͒̒͊̒̏͂̏̒͂́͑̓͆͒̓̒͑́͒̒͂͏̸̘͙͓͚̮͓͚̩̗̭̘͙͎͚̩̭͍̭͙͚̩̰̭͇̭͙͚̹̭͈̘͓͚̬̮͎̘͙͔͚̪̭͎̘͚͎̮͇̭͙͚̩̮͂͒̒̐͋͊̐͊̒͆̓̒̒́͌͆͘͏̨̩͚̬̭͈̭͍͚̰̭͙͚̗̭͔̭͙̯͚̪̰̮͖͓͙̬͚̪͖̮̘̩͚͖̭͓͚̪͖̮̘͙͚̺̮͓͙̯͚̪̭͎͓͚̹̤̭͕͓͚̮̭͙͚͚̭̓̒͆̒́͑̓͂́͒̒́̓̒͂͒̑̏͐̏̒̒͐́͑̓͂̕͏̸̴̨̘͇͚̬̤̮͙͚̹̤̭͓̗͚̹̭͉̭͙̤͚̬̭͇̘͚͚̬̭̒͐̓͌͊̒̒͏̡̘͙̰͚͚̭͙̥͚̭͉̘͙͚̮͓͚̫̤̭͈̘͈͚͎̭͔̘͖͚̬̮́͑̓́͂͆͂͂̓̒̒͂̒̏͏̘͙͕͚̪͖̭̬͚̩̗̭̘͙͖͚̩̭͈̘͙͚̹̭͓̘͙͚̹̮͓͖͚̫̮͓͙͔͚̭͎̘͙̮͚̮͇̭͙̗͚̪̮͐̓̒͋͊̐͊̓̓̒̓͑́̓͂̓͆͘͏̸̴̸̷̸̨̧̨̨̡͚̬̮͖̭̖͚̰̭͔͓͚̗̭͙̯͚̮͙̬͚̩̮̘͙̤͚̩̭͓̹͚͎̮̘͙͖͚̪̭͙͚̪̮͔͓͙͚̹̰̭͖͚̫̭͍͙͚̮͓͚̬̬̭͍̘͙͚̫͎̭͓͙͚̬͖̭͉̘͙͚̩̭͇̘͓͚̬̮͉̘͙͚͚̭̭͙̥͚̫̮͓͙͚̮͓͚̫̮͎̭͈͚̭͔̘͕͚̪̮̓̒͂͆̒́̒̑́͐̓͂͊͊̓͒̓̓̒́͒͒̓̏̓̒͐͒̓̓͂̏͐̒͊͌͊̒͗́͒̓͑͆͂̓̒͂̒́͂̒͊͏̸̭͙͚̮͓̺͚̩̗̭͇̘̮͚̩͖̭͈̭͖͚̹̭̘͙͚̺̭̭͓͚̫̮͓͙͔͚̩͖̭͎̘͙̯͚̬̤̮͇̘͙͇͚̪̮̓͂͒̒̒̒͊͋͊͒̒̏͑͆͘͏̸͚̬̮̭͙̥͚̰̭͓͓͚̫̭͕͙̯͚̭̓̒̋͆͒́̒̑̓͂͊͏̴̴̴̨̨̘͙̩͚̩͎̭͇͙̤͚̩̭͓͙͚̫̮̘͙͚̩̭͙͚̪̭͍̘͙͚̹̤̭͓͚̫̮͓͙͚̩̭̭͇͚̬̬̮͕͚̭͓͚̺͎̭͉̭͙͚̭͇̘͙͚̬̭̓̓͊͊͒͗͒̓̏͐̒̓͒͐̓͌̒͐̓̒́͂͊̒̔̈́́̏͆ͅ͏̭͙̰͚͚̭́͏̵̸̴͙͚̮͕̭͙͚̮̤͚̫̭̘͙͚̪̭͔̘͓͚̪̮̓́͂͆͂͐̓̒͌͑͊̒͊͏̢̨̨̘͙͙͚̪͖̭͙̖͚̩̗̭̘̦͚̩̭͇̘͙͚̹̭͓̘͙͚̺͖̭̘͖͚̬̭͈̭͍͚̪̭͎̘͚̮͇̭͙͚̺͚̮͐̓͋̒͊͊͊̒͂̒̒̒͂̋͘͏̸̴͚̬̮͖̘͙͚̰̭̭͙͚̫̮͍̭͙̯͚̪̤̭͓̘͙̩͚̩̮̘͙̤͚̭͓̬͚̩̮̘͙͚̪̮͓͙̬͚̪̭͎͓͙͓͚̹̤̭̓̒͑͆̏́͒͂͂͒́̓̓̒͆͒͗͐̏͏̷̴̨̨̧̨̭͙͚̭͈̭͙͚̩̮͖͓͇͚̬̤̭͓͕͚̬͖̭͓͙͚̬̰̭͉̭͙͚̮͉̭͙͚̬̮͍̘͙͚̭͚̭͎̭͙͚̩̮̤͚̬̮͈͚̭͔̘͚̩̮́̓͆̒͒̒͊͂̏͌͂́̏͑̓̒͑́͂͆̓͒̓̒̏͑̓̒́̒̏͊͏̸̘͙͚͚̫̗̮͓̦͚̩̗̮͕̘͙̗͚̩͖̭͈̭͙͚̩̰̭͙͚̹̮͖͚̫͚̮͎̘͍͚̭͎̘͚̪͖̮͇̘͙͈͚͎̮͒̒̐͊̓̓͒̓̒̒͂̒̑́͘͏̸̴͙͚̬̮͖̘͙̹͚̰̭͓͓͙͚̫̭̭͙̯͚̭͕̘͙̬͚̩̮͖̘͙̤͚͚̭͓̬͚̪͖̮̘͙͚̩̭͙̓̓͆́͂͒͂͊͂͂̓̒͒͐͒̓͏̴̸̴̸̡̨̡̨͚̪̭͎͓͙͚̹̰̭͖͓͙͚̫̭̘͙͚̗̭͉̭͇͚̬̰̭͍̘͙͚̭͓͙͚̺̭͉̘͙̪͚̬̭͇̘͙̖͚̬̮͉͓͚͚̭̘͙̥͚̫̭͈͙͚̪͖̮͖͚̫̭͈̘͙͚̩̭͔̘͓͚̪̮̏͒͌̓́̒͌͂͊͊̓̒̑́͑̓̓͆̓̒͑̒͊͏̸̘͙͈͚̭͙͚̩̗̭͇̘͙̗͚̩̭͇͓͙͚̩̰̭͈͓͙͚̹͖̮͔͓͚̬̮͓͙͔͚͚̭͎̘͙̮͚̫̮͇̭͙͈͚͎̮͂͐̓͊̐̓̒͂͑͂͊́̕͘͏̴̨̨͙͚̬̭͈̭͙͚̤̭͔͓͙͚̗̮̭͙̯͚̭̘͙̩͚̪͖̮͖̘̩͚͖̭͓̩͚̮̘͙͚̩̭͙͚̪̮͔̙͚̹̰̭̓͆̒́͂́͌͂͊͒̒͂̓̒͂̓͒̑͒̓̏̓̒͏̴̨̨̡̭͙͚̫̮̭͙͚͚̮͖͓͇͚̫͖̭͓͕͚̬̭͓͙̱͚̭͉̭͙̤͚̮͉̭͙͚̬̮͍̭͙͚͚̭̘͙̥͚̭̭͙͚̪̭͍̘͚̬̮͎̭͈͚̭͔̘̘͚̮͒͑̓́̒͒̒͊́͂͂̏͌͂́͑́͂͊͆̓̒̓̒́͊̒͂͒͏̸̵̢̭͙͚̭͚̩̗̭̭͙͎͚̩̭͇̘͙͚̩̰̮̑͂͐̓̒͋͊͏͓͙͚̹͖̭͈̘͖͚̫̮͓͍͚̪̬̭͎̘͚̩͖̮͇̘͙̙͚̺͚̮̒͒͑̒̒̒͘͏̴̸̢̨̨͙̺͚̬̭͈̘͚̤̭͓̘͚̗̭͓͙̯͚̪̤̮͖͓͙̬͚̪̗̭͔̭̩͚̬̗̭͓̮͚̪̮̘͙͚̩̮͓͙̱͚̪̭͎̭͙͚̹̤̭̭͙͚̫̭͎̘͙͚͎̮͕͓͚̬̭͓͙͚̫̤̭͓͚̫̭͉̭͙͚̩̭͇̘͙̣͚̬̭̓͆̒̋́̒͌́͑̒̓̒͆͒͐͐̏͂͐͒̓́̒͊͆͒͌͊̒̔̏͏̘͙͏͚̭͓͙̥͚̫̭͍̭͙͚̪̗̭͓̭̤͚̬̗̮͎̭͈͚̭͔̘̘͚̪͚̮́̏͒̓͆̒̒́͒̒͏̸̸̸̸̡̧̨̘͙͚̭̯͚̩̗̭͇̭͙͚̩͖̭͈̘͚̹̮̭͙͚̫̤̭̭͖͚̬̭̭͙͔͚̫̭͎̘͚̮͇̘͙͚̪̭͓͚̬̮͖̘͙͚̰̭͓͚̗̮͈̭͙̯͚̩̤̭͓̘͙̬͚̩̰̮͖̘̩͚̬̬̭͓͙͚̮̭͙͚̭͙̲͚̪̭͎̭͙͚̹̤̭͖̘͚̫̮͎̘͙͚͚̭̭͇͚̬̤̭͓͙͚̬̭͓͙̤͚̬͖̭͉̭͙̥͚̭͇̘͙͚̬̭̐́͐̓̒͒̒̏͊͐͒̒͌̏̒̑́̔͆͑̒͆̒́͒̒͌́̒̓͊͂̓͒͐́͒͒̓̏̒͐͒̓́͌̒͒͌̓͊͂̏͘͏̸̘͙͚͚̭͔͓͙̥͚̮͙͚̪͖̭̭̤͚̬̗̭̘͙͚̹̭͔̘͓͚̩̤̮́́͂͒̓͆͑̒͌͑͂̒͏̸̢̨̘͙͕͚̭̦͚̩̗̭͙̗͚̩̭͎̭͙͚̩̰̭͎͙͚̹̮͓͖͚̬̭̭͙͔͚̪̭͎̘͙͚̪̰̮͇̭͙͚̺͚̮́͐̓̒͋̓͊̓͊̓̒͂͌͘̕ͅ͏̸̴̨̨̧̨̡̥͚̬̮̘͚̤̭̘͙͕͚̫̭̘͙̯͚͖̮͍͙̩͚̩̬̮̘͙̤͚̬̭͓̮͚̪̰̮̘͙͚̪̮͓̙͚̪̮͔͓͚̹̰̭͙͚̮͔͙͚͚̮͓͇͚̬̤̮͕͚̭͓̗͚̫̭͉̭͙͚̮͉̭̖͚̬̮͉͓͙̬͚͚̭͓͓͙̥͚̭̭͙͚̮͖͚̬̭͈̘͙͚̺̭͔̘͙̥͚̫̮̓̒͆͒̒̋́͑͐͂̓͒́̓̒͒͗͐̒̏̒͌͐̓́̓̓͂͑̒͐̓̒͂͊͊̒͆́̏̒́́͂͌͆͂͂̓̒̏͑̏͆͏̸̨̧̭͙͚͚̮͓͙͍͚̩̗̭̘͙̗͚̩̭͇͓͙͚̹̭͖̭͙͚̺͖̮͖͚̫̭̭͍͚̪͚̭͎̘͙̮͚͎̮͇̭͙̗͚̩̭͓͙͚̬̮͖̭͙͚̤̭͓͙͚̗̭́͒͋͊̐͊͑̓̒͌̒́͆͑͆̏́͑͂́͘͏̴̴̸͙̯͚̭̘͙̬͚̩̭͔̭̩͚͚̭͓̹͚̩̮̘͙͚̪̭͙͚̪̮͔͙̰͚̹̤̭̭͙͚̫̭͍̘͙͚̗̮̓͂͊͒̒͂̓̒̏͒͗͒̓́̏̓͐͒̓́͏̸̷̴̸̴̸̧̨͓͚̬̭͍̘͙͚̺̗̭͓͙͚̫̰̭͉̘͙͚̬̭͇̘͙͚̬̮͍̘͙͚̭͔̭͚̫̮͙͚̮͖̤͚̫̭͈̘͈͚̭͔̘͚̩̮̒͊͌͊̈́́̏̒͆̓͒̓͆͂͂̓̒̒́̒̏͊͏̸̸̸̸̴̸̢̧̨̨̨̘͙͕͚̮͓̦͚̩̗̭͚̩͖̭͈͓͙͚̩̰̮̭͙͚̹̭͉̘͓͚̬̮͎̘͍͚̬̤̭͎̘͙̮͚̩͖̮͇̭͙͚͎̭͓͙̩͚̬̮̭͙͚̤̭͔̘͙͕͚̫̭͕͙̯͚̭͖̘͙̩͚̩̭͇͙̤͚͚̭͓̫͚̫͚̮̘͙͙͚̺̭͙͚̪̭͍̘͙̬͚̹̰̭͖̘͙͚̫̮̭͙͚̭̭͚̫̮͕͚̭͓͙̲͚̹̭͉̭͙͚̩̮͉̭͙͚͚̬̭͂͒̒͋̓̒̐͐͒̒̒̏́͑͆͒̒́̓͂͊̓́̓̒͒̏͒̓̏͒͐̓́̏͌̒͊̏͐̓̒͂͊͂͘͏̨̭͚͚̭͙̥͚̫̭͎̭͙͚̩̭͓̭̤͚̫̭̘͈͚̹̭͔̘͓͚̪͚̮̒͐́͑̓̓͆̓̒͌̒͂̒͏̭͙͏̸̸̴̸̸̵̨̨̨̡͚̭͙͉͚̩̗̭̘͙͚͚̩̭͇͓͙͚̹̮͓͙͚̹̭͈̘͖͚̬̭̭͍͚̩̭͎̘͚̫͚̮͇̭͙͚̺͚̭͓͚̬̮͓͙͚̤̭͔͙͕͚̗̭͕͙̯͚̪̮͖͓͙̩͚̩̭͇̩͚̩̭͓͙͚̬̤̮̭͙͙͚̪̮͓͙̫͚̪̮͔̙͚̹̤̭͓͙͚̮͖̭͙͚̩̮͓͇͚̬̮͙͚̹͖̭͓͙̲͚̹̭͉̭͙͚̮͉̭͙͚͚̬̮̙͚͚̭͓̭͙͚̭̭͙͚̩̗̮͓͚̬̗̭̘͙͚̩̰̭͔̘̘͚̮͂͐̓͋͊̐͊͒͒̒͆͌̒͆̒̒͌͑̒̏͆͒̒́̓́̓͂̓̒͆̓͊͒͐̏̓̒͐́̓͆͐̒͆͐̓͌͊͂̏͊̓̒́́͂͋͆̓̒͌͑̒́͒͘͏̸̸̴̨̘͙͙͚̮͓͙̙͚̩̗̮͕̘͚̩͖̭͇͓͙͚̹̮͓̘͙͚̹̭̘͓͚̫̮͓͙͔͚̪̰̭͎̘͚̫̮͇̭͙͍͚̪̭͓͙͚̬̮͖̭͚̤̭͔̘͚̫̮̘͙̯͚̩̤̮͍͙̬͚̩̮̘͙̤͚̩̭͓͙͇͚̫͚̮̘͙͚̩̭͖͚̪̮͔͓͙͚̹̤̭͂͒̒̋̐͊͒͌̒̏͑̒̑͊͆͑́͆̒̒́̒̑͌̓͆͒̓͒̑͒̓̒̏͗͘͏̨̡̨͓͚̮͖̭͙͚͚̭͍̭͇͚̬̤̭͍̘͙͚̫̤̭͓͙͚̬̭͉̘͙̤͚̮͉̭͙͈͚̬̮͙͚͚̭̭͚̫̭͈͓͙͚̪͖̮̤͚̫̤̭̘͙͚̭͔̘͓͚̪̮̒̓́̓͂̒͌͊̏͂̏͊̓͗́͑̒͆̓͆͑̓̒͌͑͂͂̒͊͏̸̸̸̴̷̴̴̢̨̨̡̭͙͚̭͙͚̩̗̭̭͚̩̭͇͓͙͚̩̰̭͈͓͙͚̫̤̭̭͖͚̬̰̮͎̘͙͔͚̪̭͎̘͙̯͚̮͇̭͙͍͚͎̭͓͙͚̬̮̭͙͚̰̭͔̭͙͚̫̭̘͙̯͚͖̮͖͓͙̩͚̪̮͖̘͙̤͚̩̭͓͙͇͚͎̮̭͙͈͚̪̭̙͚̪̭͎͓͚̹̤̭͕͓͚̫̮͈͙͚͚̮͓͓͇͚̫͖̮͔͙͚̬̭͓͙͚̫̭͉̭͙̣͚̮͉̭͚̬̮͙͚̭͔̭͙̥͚̭̘͙͚̪̭̘͚̫̭̘͙͚̹̭͔̘͚̪̮̑́͐̓͌͋̒͊̐͑̒͊͂́͑̒͆͒͊́͂͑͂͊̏̓́͒͒̓̒̏̒̒͐͒̓̓́̒̓͌͒͊͆́̏̒͒͊̓́̏́͂͊͆̓͊̒͌͑͊̒̏͘͘͏̢̘͙͓͚̪͖̭͚̩̗̭̭̖͚̩̭͈̭͚̹̭̘͙͚̹̭͉̘͓͚̬̤̮͓͍͚̪̤̭͎̘͙͚̬̤̮͇̘͙͚̺͚̮͐̓̒͋̒͊̒̏͊͋͒̒͑̒̋͘ͅ͏̓̒͏̸̸̴̸͚̬̭͈̭͙͎͚̤̭͔̭͙͕͚̫̮͇̘͙̯͚͖̭̘͙̩͚̩̭͔̭̩͚̭͓͙͚̩̮̭͙͚̩̮͓͙͚̪̭͎̭͚̹̰̭͆́͂͐͂̒́̓͊͆͒͐͐̏̒̕͏̴̴̨̨̨̨͚̮͔̭͙͚͎̮͕͓͇͚̫̭͓͕͚̺͎̭͓͙͚̬̭͉̘͙̦͚̬̭͇̘͙̰͚̬̮͉͓͙͚͚̭̭͚̮͔̘͙͚̪̗̮͔̤͚̫̭͈̘͈͚̪̭͔̘͚̬̮̓̒͐́̓́̒͊͒̒͊̏́͑̒͑́͂͆̓̒̒͒̒̏́͏̸̸̢̭͙͚̭͙͍͚̩̗̮͕̘͙͎͚̩͖̭͇͓͙͚̩̰̭͇̘͙͚̺͖̭̭͖͚̬̮͓͍͚̩̭͎̘͚̫͚̮͇̭͙͚̺͚̮̓͂͐̓͒̒͆͑̒̒̑͌͘͏̸̴̨͚̬̮͖̭͙̥͚̰̭͓͙͕͚̗̭͔͙̯͚͖̮͙̩͚̪̭͔̭̩͚̩̭͓̫͚̮̭͙͖͚̩̭̘͚̪̭͙͚̹̤̭̓̒͆́͑́̓͂͋̓̏̒̓̒́͒͒̓̒̏͊̓͗͘͏̴̴̨̨̨̡̨̭͙͚̭͙͚̭͈̭͇͚̬̭͓͕͚̺̭͓͙͚̺̭͉̭͙͚̭͇̘͙̥͚̬̭́͌̓̓́̏̒͒̒̓͊͂̏͏̭͔͚̭͓͓͚̫̭͍̘͙͚̪͖̭͉̘̤͚̬̗̭͈̘͙͚̺͖̭͔̘͓͚̬̮̒́̏̒͑̓͆̒͑̒́͏̸̢̨̭͙͚̪͖̭͚̩̗̭̭͙͚̩̭͎̘͚̩̰̭͇̭͙͚̹̭̘͓͚̫̭̭͍͚̭͎̘͚̫͚̮͇̘͙͉͚̩̭͓͎͚̬̮̭͙͚̰̭͙͕͚̫̮̑͐̓̒͋͒͊̒̏͊͌̒͌̒͂͊̒̑͆͑̒͆͒̓́͑̓͘͏̴̴̸̨̨̧̨͓͙̯͚̪̰̮͖͓͙̩͚̩̰̭͇͙̤͚̭͓͙͇͚̮̭͙͓͚̩̮͓͙͚̪̮͔͙͓͚̹̰̭͖̘͙͚̫̭͎̘͙͚͚̭̘͚̫̭͍̘͙͚̺͚̭͓͙͚̹̭͉̭͙͚̮͉̭͚̬̭̓́͆̓͂͒͐́̏̓͒̓͂͐̒͊̏͌͊͂̏̒͐͏̡̨̭͚̭̘͚̭̘͙͚̪̮͚̫̬̭͈̘͈͚̩̰̭͔̘͙͚̮̒̑́̏͒̒͑́͂͊͆̓͒̓̒̒͂͒͏̸̢̢̭͙͚̭̙͚̩̗̭̭͚̩̭͈͓͙͚̩̰̭͇̭͙͚̺͖̭͍̘͓͚̬̮͎̘͍͚̪̭͎̘͙̯͚̫͚̮͇̭͙̗͚̪̮͗͂͐̓̒͋̒͊̒͆̒͆͆͘͏̶̸͙͚̬̮͖̘͙͚̰̭͙͚̫̭̓͆̒́͑̓͂͏̴͙̯͚̮͈͙̩͚̪̗̭͔̭͙̤͚̬͎̭͓͚̬̤̮̘͙͔͚̪̮͓͚̪̭͎̭͔͚̹̤̭̓͂͊̓̓̒͂͒͐̒̐̏̒͏̨̧̨͓͙͚̫̮͇̭͙͚͚̭̭͇͚̫͚̮͙͚̺͖̭͓͙̲͚̫̭͉̘͙͚̭͇̘͚̬̭͒̓͂͌̒͐̓͌͊̏͂̏̒͒͏̵̸̡̘͚̭͓̘͙͚̫̭͔̭͙͚̪̮͖͚̫̮͎̭͈͚̹̭͔̘̘͚̮̒́̏̓͆̓̓̒̒͊̒͂͂͘͏̸̴̴̴̡̢̨̨̨̡̭͙͚̮͓͚̩̗̮͕̘̲͚̩͖̭͉͙͚̹̭͈̭͙͚̺̮͖͓͚̫͚̮͓͙͔͚̩̭͎̘͙͚͎̮͇̭͙͚̺͚̭͓͙͚̬̮̭͙̥͚̤̭͔̭͙͕͚̗̭̘͙̯͚̪̰̭͕̘͙̬͚̩̮̘̩͚̭͓͙͇͚̮̘͙͚̪̭͚̪̭͓͚̹̤̭͓͚̮͇͓͙͚̭͈̭͇͚̬̬̮͕͚̭͓͙͚̬̭͉̭͙̹͚̬̭͇̘͙͚̬̮͚̭͙̥͚̫̭͙͚̪̗̮͓͚̬̮͈͚̹̬̭͔̘͓͚̩̮̓͂͒̒̒̓͊͊̓̒͑͊̓́̔͑͆͆͒́́͑͒̒͂̏̓́̓͒̒͒̓̒̏͊̒͌͐̒̓́̓́̏̒͐̓̒́͂͊̏͆͊̓̒̑́̏͑̓̓͌̓͆̓̒̓͑̓̒̒͊͘̕͏̸̸̴̴̴̸̧̡̨̭͙͚̮͓͙͚̩̗̭̘̲͚̩̭͇̘͖͚̹̭̘͙͚̺̭͍̘͓͚̫͚̭͈̭͙͔͚̭͎̘͚̫͚̮͇̘͙͍͚̩̭͓͚̬̮͖̭͙͚̤̭͙͕͚̫̭̘͙̯͚͖̭͖̘͙̩͚̩̮̘̩͚̭͓̫͚̩͖̮̭͙͙͚̩̮͓͙̱͚̪̮͔͓͚̹̰̭͕͚̫̭͉͓͙͚̩̭͖̘͇͚̬̮͙͚̹̭͓͙͚̹̭͉̘͙͚̭͇̘͙͚̬̭͒́͒̓͋̒͊̒͊͊͊̒͂͂̒̑͆͑̒͆̒́͑̓͒͂͒̒͂͒̓̒͒͐̏̒̓̒̓͒̓͆̒͆͐̓͌͆͊͂̏͘̕ͅ͏̵̨̘͙̬͚͚̭͙͚̭͍̘͙͚̪͚̭͍̘̤͚̬̮͙͚̩̭͔̘͚̫̮́͑̓́͂͆̒̏͑̓͑̒̏͆͏̸̘͙͚̮͓̩͚̩̗̭̭͚̩͖̭͈̘͙͚̩̰̭͇͓͙͚̺̭͓̭͓͚̫̭̭͙͔͚̪̬̭͎̘͚̪̮͇̭͙͈͚̩̮̒́͒̒͋̒̈́̐͊̒̏͌̒̒͆͆͘͏̸̘͚̬̮͖̭͙͎͚̰̭͔͙͕͚̫̭̭͙̯͚͖̭̘͙̬͚̩̮̘̩͚̬̭͓̬͚͎̮̭͙͚̺̭͔͚̪̮͔͓͙͓͚̹̤̭̓̒͆́̓͒͂͐͂͒̒̏̓̒́͒͑̏͒̓̒̏͏̴̷̵̨̧̨͚̭̭͙͚̭̭͇͚̬̤̭͓͙͚̫̭͓͙͚̬̭͉̘͙͚̭͇̘͈͚̬̮͍̘̙͚̭͔̭͙͚̭͓͙͚̩̗̭͉̘̤͚̬̭͈̘͈͚̭͔̘͓͚̩̮̓̒̓́͌̓͂̏͌̒͒͌͊̏͂̏̒̒́̏́͂͑͆̒̏̒͂̓̒͊͏̷̸̴̴̸̸̨̨̨̡̭͙͚̫̗̮͓͙͚̩̗̭͇̘̖͚̩̭͉͚̩̰̮̭͙͚̹̮͔͓͚̫̮͎̘͙͔͚̪͚̭͎̘͙̯͚̫͚̮͇̘͙͈͚͎̭͓͙͚̬̮̭͙̩͚̤̭͔͙͕͚̗̭͓͙̯͚̮͖͓͙̩͚̪̮͖̘͙̤͚̪̭͓̮͚̮̭͙͕͚̪̭͙̲͚̪̭͎͓͙̰͚̹̤̭͙͚̫̭͙͚̩̮͓͚̬̭͍̘͙͚̫̭͓̗͚̭͉̭͙̣͚̮͉̭͖͚̬̮͍̘͙̰͚͚̭̘͙̥͚̭͎̭͙͚̭͓̭͚̫̭̘͈͚̭͔̘͕͚̪̮̓͒͒̒͊̓̒̏͒͊̓̒́͑͆͒́̓́͒͂͊͒̏̓̒͂͒͒̓̏͐̓͒͋̓̓͐̒͊͂͌͒͊̒́͂͂̏̒́͑́͂͆͂̒͌̒͂͒̒͊͘͏̭͙͚̪͖̮͓͚̩̗̭̘͙͖͚̩͖̭͎̘͙͚̹̭͈͙͚̫̤̮͕͓͚̬̬̭͈̭͍͚̪̭͎̘͚͎̮͇̭͙̙͚͎̮͐͒̒̏͋̐͊̓̓̒̒͊̒̒͂́͘͏͚̬̮̘̖͚̤̭̭͚̗̮̓̒͋͆͒̒́͑̒͌́͏̸̴̸̵̸̨̨̨͓͙̯͚̮͇͙̩͚̩̭͇͙̤͚̩̭͓̮͚̮̘͙͚̺̮͓͙̹͚̪̭͍̘͚̹̤̭͕̘͙͚̮͔͓͙͚̮͓͇͚̫̮͕͚̫̗̭͓͚̹̭͉̘͙̣͚̬̭͇̘͙̩͚̬̮͉͓͙͚͚̭̘͙͚̫̭̭͙͚̭̘̤͚̬͎̮͙͚̪̭͔̘̘͚̮͂͊̓͆̓̓̓̒͂̓͒̓̏͐̏̒́̓͂̏͑̒͊͐̓̒͊̒̔́͒̓͋͆͂͌̒͑̓͑͒̒́͒̕͏̭͙͓͚̪͖̮͓͚̩̗̭͓̲͚̩̭͎͓͚̩̰̭͈̭͙͚̹͖̭͓̭͓͚̬̮͎̘͙͔͚̫̭͎̘͙͚̩͖̮͇̘͙̘͚̪̮͒̒̋͌̒͊̒̏̒͆̏͆͘ͅ͏̸̸̴̴̴̨͙̳͚̬̮͖̘͚̰̭͓͙͚̫̮͖̘͙̯͚̪̮͙̬͚̩̭͇̩͚̫̭͓͚̪̮̭͙͔͚̪̭̖͚̪̭͙͚̹̤̭͕̭͚̫̮̭͙͚͚̮͔͓͚̫̭͓͙͚̭͓͙͚̫̰̭͉̭͙̪͚̬̭͇̘͚̬̭̓͆̒̒́͒͂͂͊̓͆̓̒̓̒͂͆͒͒̓̒̏͊̓͗̒͐͒͐̓́̒͊͒͒͌́͂͊̒͒͏̘͙͏̡͚͚̭͔͓͙̥͚̫̭̭͙͚̪͖̭͈̘͚̫̮͈͚̪̭͔̘͙̥͚̮́̓͋͆̒͂͑̓̒͒͂͂͏̸̷̸̴̴̨̨̧̭͙͚̮͓͙͚̩̗̮͕̭͙͚͚̩̭͍̘͙͚̩̰̭͇͓͙͚̫̤̮͕͓͚̫̭͈̭͙͔͚̩͎̭͎̘͚̬̤̮͇̘͙͚̪̭͓͙̳͚̬̮̭͙̥͚̰̭͓͓͙͚̗̮͎͓͙̯͚̪̮͖͓͙̩͚̩̬̭͔̭̩͚̭͓͙͇͚̪͖̮̘͙͙͚̺̮͓͙͚̪̭͍̘͙͚̹̤̭̭͙͚̮͙͚̭̭͚̬̭͓͙͚̹̭͓͙̱͚̬̰̭͉̭͙͚̬̮͉̭̓͂͒͊̐̓̒̓̒̑̏͆͑͆͒́͂́͂̒́͊̓͒̏͐̏͐́͑̓̓͂̏͌̒͊͆͒͌͊̒̕͘͏̨͚̬̭͏̵̴̡̨̘͚̭͓͙͚̭͎͙͚̪̮͚̬̭͈̘͙͚̩̬̭͔̘͙͚̩̮̒̑́̏͑́͂̓͆̓͒̓̒̏͑͏̸̴̴̸̨̧̨̨̡̭͙͚̫̗̭͚̩̗̮͕̘̦͚̩̭͉͖͚̹̮̭͙͚̹̭̭͓͚̬̤̭͈̭͍͚̪̭͎̘͙̮͚̮͇̘͙͚͎̭͓͙͚̬̮͖̘͙͚̤̭̭͚̗̮͍͙̯͚̪̤̭̘͙̬͚̩͎̮͖̘̩͚̫̭͓͙͚̮̭͙͖͚̩̮͓͚̪̮͔͓͙͚̹̰̭͖͚̮͓̘͙͚̗̮͖͓͇͚̫̮͔͙͚̺͖̭͓͙̤͚̹̭͉̘͙̤͚̬̮͉̭͚͚̬̮͉̘͙͚̭͓̭͙̥͚̫̮̘͙͚̪̗̮͖͚̫̮͎̭͙͚̪̭͔̘̘͚̮̐͐̓̒̒͊̓̒͊͒͒͒̒̒́̓̏́͑͆̒́͑̒͌́̓͐̒̓͊́̓͒͐̒̓̏͂̓̒͐́̓́̒̓̓͌͊̓̒͂́̏̓͑͆̓̒͑͆̒͂͒̕͘͏̸̘͙͕͚̭̘͚̩̗̭͇̭͙̗͚̩͖̭͈̭͙͚̹̭͍͓͙͚̺̭̘͖͚̫͎̮͎̘͙͔͚̩̭͎̘͙̮͚̫͚̮͇̭͙͇͚̩̮́͐̓̒̐͊͊͋̒͒͆͘͏̴͚̬̭͈̭͙͚̰̭̭͚̗̮͓͙̯͚̩̰̭͓̘͙̩͚̩̮̘̩͚̬̭͓͙͚̪̰̮̘͙͚̺̭͙͚̪̭͓͙͚̹̤̭̓̒͊͆̒́͒̒̑́͐͒̒͂̓͊͒͐̏͒̓̏͊͗ͅ͏̨̨̘͚̫̮͔̘͙͚͚̮͖͓͚̫̮͕͚̬̭͓͚̭͉̭͙͚̩̮͉̭͙͙͚̬̮͉̘͔͚̭͔͓͚̮͔͓͙͚̪̗̮͓̤͚̫̰̭̘͙͚̰̭͔̘͓͚̬̮̒̓͒̓́̒͊͒͐̓̒̓͊̒̔́͂̓̒́̏̒͆́͂͆̓̒͌͑͂̒͂͏̭͙͏̢͚̫̗̭͙͎͚̩̗̭͓͙͚̩̭͈̘͙͚̩̰̭͕͓͙͚̫̤̮͓͓͚̫͖̮͎̘͍͚̪̭͎̘͚̫͚̮͇̭͙͚̪̮͐̓͌͊͊̓̒̒̓̒̒͋͆͘͏̴͉͚̬̮͖̘͚̰̭̘͙͕͚̗̭͖̭͙̯͚̭͕̘͙̩͚̩̮̘͙̤͚̭͓̩͚̮̘͙͚͚̪̮͓͙̲͚̪̮͔̙͚̹̤̭̓̒͆̒̒́͑́͂͊͂͒͂̏̓̒́̓͒͐̏̓̒͏̨̨̨̡͓͙͚̭͇̘͙͚̩̭̘͚̫̗̭͍̘͙͚̺͖̭͓͙̱͚̫̰̭͉̭͙̦͚̮͉̭͚̬̮͍̭͙͚͚̭͔̘͚̭͍͙͚̪͚̮͓͚̬̗̭͈̘͈͚̤̭͔̘͚̬̮́̓͆͐̒͊͌͊͂̏̒̋͂́̒͆́͂̓͆̓̒̒́̒̏͂͏̸̸̭͙͖͚̭͙͈͚̩̗̮͕̭̦͚̩͖̭͈̭͙͚̩̰̭͎͓͙͚̫̰̮͖͖͚̬̤̮͓͙͔͚̩̗̭͎̘͙͚̮͇̭͙͉͚̪̮́͐̓̒̐̓̒͑͂͆͘ͅ͏̸̴̨͚͚̬̮͖̭͙͚̤̭̘͚̫̮͍̘͙̯͚̪̮͈͙̬͚̩̭͔̭͙̤͚͖̭͓͙͇͚̮̘͙͚̩̭͙̓̒͆̒́͒̒͌͂̓͂́̓͂͒̓͒̓͏͚̪̭͙͚̹̤̭̏͊̓͗͏̴̵̨̨̡̭͚̮͕̘͙͚͚̭͖̘͇͚̬̰̮͔͕͚̺̭͓͙̤͚̫̰̭͉̭͙͚̬̮͉̭͚̬̮͉͓͙͚̭͔̘͙͚̫̮͖̭͙͚̩̗̭̭͚̬͚̮͎̭͙͚̪̭͔̘͓͚̫̮̒̓́̓͂̒̓̒͊͊̓̒͐͗́̏̓͆͒̒͑̏̒͆͏̸̘͙͕͚̮͓̗͚̩̗̭̘͚̩̭͈̭͚̹̮͖̘͙͚̫̰̮͖͚̫͎̭̭͙͔͚̭͎̘͙͚̩͖̮͇̘͙͇͚͎̮́͒̒͋̒̋͊̒̏͊͒̓̒͌͂̓͂́͘͏͙͚̬̮̘͙̹͚̰̭̭͙͚̗̭̓́͆͒́͒͂́͏̴̭͙̯͚̪̰̮͇͙̩͚̪͚̮͖̘̩͚̬̬̭͓̬͚̮̘͙͚̪̭͙̬͚̪̮͔͙͚̹̤̭̓̒̓̒͂̓͒̓͒̓̏̓͗͏̸̴̵̸̨̨̡̨̘͙͚̭͉͓͙͚͚̭͈̭͇͚̫̮͙͚̫̭͓͙̱͚̹̭͉̭͙͚̭͇̘͉͚̬̮͙͚̭͔̘͙͚̭̭͙͚̭͓̭̤͚̫̭͈̘͙͚̤̭͔̘̘͚̗̮́̓́̒̏͐̓͌͂͊͂̏̒͊̓́̏́͂͊͆͂̒͂͑́̒͂͏̸̡̭͙͚̭͚̩̗̭͙͖͚̩̭͈̭͚̩̰̮͖̘͙͚̫̰̮͖͚̬̭̭͍͚̪͎̭͎̘͚̮͇̭͙͈͚̩̮͗́͐̓̒͋̓͊̒̏͑̓̒͂͌̒̒̑͂̓͆͘͏̸̴̴̨̨̨̧̨̡̨͚̬̭͈̘͙̩͚̤̭͓̭͙͕͚̗̭͕̘͙̯͚̪̤̮͙̬͚̩̮͖̘̩͚̬̭͓̫͚̩̮̭͙͚̺̮͓͙͚̪̮͔͙͚̹̤̭͓͙͚̮̭͙͚̮͕͓͇͚̫̮͙͚̭͓͙̤͚̺̭͉̘͙͚̬̭͇̘͙͚̬̮̙͚͚̭̘͚̫̭̘͙͚̭̘͚̫̰̭̘͈͚̭͔̘̘͚̩̮̓̒̋͆́́͋̓̒͊̓̒͆͒͐̏͐̓̏̓͗͐́͐̓͂̏̒͊͐̓͌́͂͊͆͊̓̒́͒̒͑̓͋͆͂͂͌̒͌̒͂̒͏̸̘͙͚̮͓͙͍͚̩̗̭͓̮͚̩͖̭͈̭͙͚̩̰̮̘͙͚̫̤̭̭͖͚̫͎̭̭͙͔͚̭͎̘͙͚͎̮͇̭͙͈͚̺͚̮̑͂͒͌̒̐͑͑̒͌́͊̈́͂͘͏̵̵̸̴̴̨̨̨̨̨͙͚̬̮͖̘͙͚̤̭͓̭͙͕͚̫̭̭͙̯͚̪̭͖̘͙̬͚̩̮͖̘͙̤͚̭͓͚̮̘͙͚̪̮͓͙͚̪̭͓͙̬͚̹̤̭͕͚̮͔͓͙͚͚̭͉̭͇͚̬̭͍̘͕͚̫̭͓͙͚̺̭͉̘͙͚̩̭͇̘͖͚̬̭̓͆́͐͂͂́̓̒͂͂̓͒̐͐͑̏͊̓̒̓́̓́̒͆̒̏͊̒ͅ͏̭͚̭͓͓͚̫̭̘͙͚̪͖̮͕̤͚̬̭͈̘͈͚̹̰̭͔̘͓͚̩̤̮̒́̏̒͑̓͊͆̓̒̓̒̒͘͏̘͙͏̸͚̮͓͙͕͚̩̗̭̖͚̩̭͍̘͖͚̹̭͙͚̫̤̭͓̭͓͚̬̤̮͓͙͔͚̪̭͎̘͚̬̤̮͇̭͙̗͚͎̮͂͒͋̓̒͊̒͊͐̓̒͑͊̒̑́͘͏̴̸̨̡̨̡̣͚̬̮̭͍͚̰̭͓̘͚̗̮͓͙̯͚̭͓̘͙̩͚̩̤̮͖̘͙̤͚̬͖̭͓͚̩͖̮̘͙͚̮͓͙̫͚̪̮͔͓͚̹̤̭͕͓͚̭͓͙͚̗̭͍̭͇͚̫͎̭͍̘͙͚̺̭͓̗͚̫̰̭͉̭͙͚̬̮͉̭͚̬̮͉̘͙͚̭̘͚̭͉͓͙͚̪̮͚̬͖̭͈̘͙͚̹͎̭͔̘͙̥͚̗̮̓̒͆͒̒́̒̑́͊͂͊̓̒͂͒̐́͒͐̏̒̑̒̓́͋̓́̒͌͊͊̒̒͌́̏͑̒͆́͂͆̓͐̓̒͑͂͏̸̢̘͙͚̭͚̩̗̮͕̘̲͚̩̭͈͓͙͚̩̰̭̭͙͚̹̭̘͖͚̫̭͈̭͍͚̪̗̭͎̘͙̮͚̫͚̮͇̭͙͚̩̮͑́͐̓̒͂̒͊͋͒͋̒̓̒̔͆͘͏̷̗͚̬̮͖̘͙͚̤̭͓͙͚̗̮̭͙̯͚̪̤̮͙̬͚̩̬̭͔̭̩͚̬̬̭͓̹͚͎̮̘͙͚̺̭͙͚̪̮͔͙̓̒͆̓́͒͂́͊͊̓̒̓̒́͒͗̏͒̓̏̓͏̴̡̨̡̨͚̹̰̭͕̭͚̫̭͎̭͙͚͚̮͖͓͇͚̫͚̭͍̘͕͚̭͓͙͚̫̭͉̘͙̪͚̮͉̭͚̬̮͉̘͙͚͚̭͔͚̫̭̘͙͚̪̗̮͕͚̫̮͈͚̪̭͔̘͚̮̒͐͒̓͂̒̒͂͒͊͆́̏̒͋͗́̓̒͑̓͑͆̓̒͑̓̒̒̏͂͂͏̸̸̸̭͙͙͚̮͓̩͚̩̗̭͇̘̦͚̩͖̭͈͚̹̭͍͓͙͚̺͖̮͖͖͚̬̭̭͙͔͚̩̭͎̘͙͚̩̮͇̘͙͚̪̭͓͚̬̮̭͙̥͚̰̭͓͙͚̫̮͕̭͙̯͚̪̰̭̘͙̩͚̩̤̮͖̘͙̤͚̪̰̭͓͙͚̪̰̮̭͙́͒̒̒̓̒̏͊̓̒͆͌̓͆͋͆͑̒̏͆͒́͒͂͒̓͊͒͘͏̴̴̨̨̡͚̪̭͙͚̪̭͚̹̤̭̭͚̫̭̘͙͚̩̭͈̭͚̫͚̭͓͕͚͖̭͓͚̫͖̭͉̭͙͚̩̮͉̭͙͚̬̮͉̘͙͓͚̭͓̭͙̥͚̫̭͍͓͙͚̪̗̮͓͚̬͖̮͈͚̩̬̭͔̘͓͚̮͒̓͂̏͊̓̒̑͐̒͐͒͋̓̒͊͒̒͂͊̒̔̏́̏̓͆̓̒͑̓̒̒͂͂ͅ͏̸̸̨̭͙͓͚̮͓͚̩̗̭̭͚̩̭͇͓͚̩̰̮͙͚̹̭͈̘͖͚̬̭̭͙͔͚̭͎̘͙͚͎̮͇̭͙͚̺͚̮͂͒̒͋̒̋͊̒̏͒̓͒̒͌͂͂͂̔͘ͅ͏̸̨̨͚̬̮͓͙̥͚̰̭͔̘͙͕͚̫̮͇̭͙̯͚̭̘͙̬͚̪͚̭͇̩͚̪̭͓̫͚̮̘͙͔͚̺̮͓͙͚̪̮͔͚̹̤̭̓̒͋͆͒́͂͊͐̓̒͊̓̒͂͒̏͐̏̓̒͘͏̸̨̡͓͙͚̫̮͉̭͙͚̩̭̭͚̫̮͙͚̹͖̭͓̗͚̫͖̭͉̭͙̥͚̭͇̘͙̭͚̬̮͍̘͙̬͚̭͓̘͙̥͚̭͎͓͙͚̪͖̮͕͚̬̭̘͈͚̩͎̭͔̘͚̬̮͒̓͆͌̒͊͒͐̓͌͊̒́̏́̏́͂͆̓̒͆͌̒̒̏͂͏̭͙͏̸̸̸̴̨̨͚̮͓͙͖͚̩̗̮͕̭̲͚̩͖̭͉͚̩̰̭͍̭͙͚̺͖̮͕͖͚̫̭̭͙͔͚̪̭͎̘͙͚̮͇̘͙̖͚͎̭͓͙͚̬̮͖̘͙͚̤̭̘͙͕͚̫̮͈̘͙̯͚̪̭̘͙̬͚̩͎̮̘̩͚̬͖̭͓͙͇͚̫͚̮̭͙͖͚̪̮͓͚̪̭͎͓͙͚̹̤̭͖̘͚̫̭̘͙͚̮͂͒̒̓̒̏̓̒̓͌͂́͑̓͆͊́͑͂͒͒̒̓͒͐̒̏̒͐͒͌̓͂̏͘̕ͅ͏̴̷̧̨͓͚̫͖̮͔͙͚̬̭͓͙͚̫͖̭͉̘͙͚̮͉̭͚̬̭̒͊̓͌͊́̏̒͒͏̡̘͙̰͚͚̭͓͙̥͚̫̭͈͙͚̩̗̭͉̘͚̬̮͙͚̹͎̭͔̘͖͚̬̮́͒̓̓͆̒͆͑̓͑̒͂͏̸̸̢̭͙͚̪͖̭͙͚̩̗̭̭̺͚̩̭͈̭͙͚̩̰̭͍͓͙͚̫̤̮͖͚̬̭̭͙͔͚͚̭͎̘͙̯͚̮͇̘͙͇͚̩̭͓͚̬̮̭͙̥͚̤̭͔͙͕͚̗̭͗͐̓͋̒͊͒̓̒͌͂͂͆͑̒͐͆͒́̓́̕͘͏̸͙̯͚͖̮͈͙̩͚̪͖̭͔̭̩͚̬͚̭͓͙͚̮̭͙̓͂̓̒̓͊͂͒͏͚̭͙̫͚̪̭͎͚̹̰̭́͒͒̓̏̓̒̕͏̸̴̸̨͓͙͚̫̭͓͙͚͚̭͖̘͇͚̬̤̮͕͚̬̭͓͙̱͚̭͉̭͙̤͚̮͉̭͙͚̬̮̙͚͚̭̭͙̥͚̭͙͚̭̭̤͚̬̭͈̘͙͚̗̭͔̘͚̮͒͋̓́̒͐̓̒͊́͂́̏́͊̓̒́͒́͂͋̓͆͂͒̒̏͑͂̒̏͂͂͏̵̸̸̴̢̨̘͙͚̪͖̭͚̩̗̭̘͙͚̩̭͇̘͙͚̹̭͈̭͙͚̹̭̘͖͚̫͖̮͓͍͚̪̰̭͎̘͙͚̫͚̮͇̭͙͚̩̭͓͙̣͚̬̭͈̘͚̤̭͓̭͚̫̮͔̭͙̯͚̪̤̮͖͓͙̩͚̩̰̮̘̩͚̭͓͙͚̪̮̭͙͚̪̮͓͚̪̭͍̘͙̬͚̹̤̭̭͚̮͒͐̓̒͋̏͊͊͒͌̒͑̒̈́͌͆͑͆̒̋́̒̑͒̒́̓͊͆͒̒͐̒̋̏͐̒̓́͘͏̴̵̧̨̨̘͙͚̭͍̭͚̬̬̭͍̘͙͚̬̭͓͚̬͖̭͉̘͙͚̩̭͇̘͙̰͚̬̮͉͓͚̭̭͙͚̫̭͓͙͚̪̗̮̤͚̬͚̮͙͚̩̤̭͔̘̘͚̩̮̓͂̏̒͊͌͊̒̔̒́̏͒̓͊͆͐̓̒͑̓͑̒͊͘͏̸̴̴̢̨̢̢̨̡̘͙͚̪͖̭̰͚̩̗̭͇̭͍͚̩͖̭͉͙͚̹̮͕͓͙͚̹̭̘͖͚̬̤̮͓͙͔͚̫͖̭͎̘͙͚̮͇̭͙͈͚̺͚̭͓̩͚̬̮͖̭͚̤̭̭͚̫̭͔̭͙̯͚̪̭͕̘͙̬͚̩͎̮̘͙̤͚̬͎̭͓̹͚̮̘͙͚̪̮͓͙͚̪̭͍̘͙͚̹̤̭͖͚̫̭͈̘͙͚̭͎̭͇͚̬̭͓͙͚̬͎̭͓̗͚̫̭͉̘͙͚̭͇̘͙͚̬̮͉͓͚̭͔͓͚̫̭͓͙͚̩̗̮͚̫̮͎̭͈͚̹̬̭͔̘͖͚̩̮͐͐̓̒̒̓͊͊͊̒͑͂̓͑̒͆̒̒́͑̒͌͂͒̓̒͂̓͒̓͐͗̏̓̒͐͒̓́̏̒͆͒͌͊̒͆́̏̒̑́̏̒͑̓͊͆͐̓̒͂̒̒͘ͅ͏̸̴̵̴̸̨̨̨̭͙͙͚̮͓͍͚̩̗̭̘͙͚̩̭͍̘͙͚̹̮͖̭͙͚̫̤̭͓̭͖͚̬̤̮͎̘͙͔͚̩͖̭͎̘͚̬̤̮͇̭͙͚̩̭͓͚͚̬̭͈̭͍͚̤̭̭͙͕͚̗̮͖̘͙̯͚̪̰̭̘͙̩͚̩͎̭͔̭͙̤͚̭͓͚̩̮̭͙͓͚̪̮͓͙͚̪̭͍̘͙̬͚̹̰̭͙͚̮͓͙͚͚̭̘͇͚̫͎̮͔͙͚̹̭͓̗͚̹̭͉̭͙̥͚̭͇̘͚̬̭́͒̒͋̏͊̐͊̒̒̑͊͆͑̒͆̒́͒́͐́̓̓̒͂̏͒͐̏͐̓́͐̓͂͐̒̓͌͊̒͂̏̒̏͘͏̵̡̨̘͙̰͚͚̭͓͓͙͚̫̮͔̘͙͚̭͉̘͚̬̮͙͚̹̰̭͔̘͙͚̬̮́̓͆͂͂̒̓͑̓͑́͏̸̢̭͙͚̭̫͚̩̗̮͕̭͚̩̭͇͓͙͚̹̭͕̭͙͚̹̭͈̘͖͚̫͎̮͎̘͍͚̪̭͎̘͙̯͚͎̮͇̭͙͚̪̮̓́͐̓̒̒͊̐͊͒̒̒͂́͊͆͘͏̸̴̸̴̴̨̡̢̨͇͚̬̮͖̘͚̰̭͔͓͚̫̮͖̘͙̯͚̩̰̭͕̘͙̬͚̩̭͇̩͚̰̭͓̮͚̮̭͙͓͚̩̮͓͚̪̭͎͙͓͚̹̤̭͓͙͚̮͔̭͙͚͚̭͉̭͚̬̮͕͚̭͓͙͚̫͖̭͉̘͙̥͚̬̭͇̘͙͚̬̭̓̒͆̒̋́̒̑͂̓̒́̓̒͂̓͒͐̒̑̏̓͐́̓͂̒͊͐̓̒͂̓͊͏̵̸̸̭͙͓͚͚̭̘͙͚̫̮͙͚̭͓̭̤͚̬̗̭̘͈͚̪̭͔̘͚̮́͒̓͑̓͆͂̒͌̒̒̏́͂͏̴̭͙͚̪͖̮͓̹͚̩̗̭͓̖͚̩͖̭͈͓͙͚̹̮̘͙͚̹̭͍̘͓͚̫̭̭͙͔͚̩̭͎̘͚̫͚̮͇̭͙͚͎̭͓͙̣͚̬̭͈̭͙͚̰̭͓͓͚̗̮͙̯͚͖̮͎͙̩͚̩̭͇͙̤͚͎̭͓̬͚̬̤̮̭͙͚̩̮͓͔͚̪̭͙͗͒̒͌̒̐͊͑͒̒̏͌͒̒̑̔́͑͆̒́̒͌́͌̓͂̓͂̓́̓̒͒͒͐̒̏͊̓͘͏͚̹̰̭͏̴̸̨̨̨̨͙͚̫̭͙͚͚̭̭͚̫͖̮͙͚̹̭͓͙̱͚̭͉̭͙̹͚̬̮͉̭͙͚͚̬̮͉̭͙͚͚̭̭͙̥͚̫̭̭͙͚̮͖̤͚̫̭̘͙͚̪̗̭͔̘͓͚̮̓͒͋̓̓́͌̒͊͐̓͌͊͂͒́͑̓͌͆͂͂̓̒͌͑̒́͂͏̴̸̴̴̨̧̨̨̘͙͙͚̪͖̭͙͚̩̗̭̘̲͚̩̭͇̘͖͚̩̰̮͕̭͙͚̺͖̭͓̭͖͚̫̮͎̘͍͚̪̭͎̘͚͎̮͇̘͙͚̪̭͓͚̬̮͓͙̹͚̰̭̘͙͕͚̗̭͔̭͙̯͚͖̮͍͙̩͚̩̤̮̘̩͚͎̭͓͙͚̬̤̮̭͙͙͚̪̮͓͙̫͚̪̮͔̙͚̹̤̭͓͙͚̮͖̭͙͚̩̮͓͇͚̬̮͔͕͚̫̰̭͓͙̱͚̗̭͉̭͙͚̩̮͉̭͙͚͚̬̮͉͓͙͚͚̭͓͓͙̥͚̭͓͙͚̩̗̮͓̤͚̬̮͎̭͈͚̭͔̘̘͚̩̤̮͐̓̋͋̒͊̒̒̓̒͊̒̒́̏͆͑̒̏͆͒́͒́͂̓͒̒́̓͊͒͐̏̓̒͐́̓͆͐̒̓̒͊͂́́͂͌͆̓̒̏̒͂̏̒͘͏̸̢̘͙͙͚̮͓͚̩̗̮͕̭͙͎͚̩͖̭͇͓͙͚̩̰̭͍̭͙͚̹̭̘͓͚̫͚̮͎̘͙͔͚̪̤̭͎̘͚̫̮͇̘͙͉͚̩̮͂͒̒̓͒͌̒̒̑͊͆͘͏̸̨͙̹͚̬̮͖̘͚̤̭̘͙͚̫̮͉̘͙̯͚̪̭̓͆̒͑́͑͂͏̴̸̴̴̴̨̨̡̡̨̨̘͙̬͚̩̭͔̭̩͚̤̭͓͚̮̭͙͔͚̪̭͙͓͚̪̭͎͓͚̹̰̭͖͙͚̮̭͙͚͚̭͎̭͇͚̫̮͔͙͚̬̭͓͙͚̫̭͉̘͙͚̬̮͉̭͙͚̬̭̒͂̓̒͂́͒͒̓̏̒̓́͑̓͂̒͊̓͌͊͆̕͏̴̵̡̘͙͚͚̭͓̘͙͚̫̭̘͙͚̩̗̮͔͚̬͖̮͈͚̰̭͔̘͓͚̮́̓͋͆̓̒͑̓̒́̒́͒͏̸̴̢̘͙͚̮͓͚̩̗̭͇̘̖͚̩̭͈̘͖͚̩̰̮͓͙͚̹̭͈̘͓͚̬̰̭̭͙͔͚̪̰̭͎̘͙͚̫̮͇̭͙͍͚͎̭͓͚̬̮̘̖͚̤̭͔͓͚̗̭͕͙̯͚̪̤̭͕̘͙̩͚̪̮͖̘͙̤͚̩͖̭͓̬͚̮̭͙͚̪̭͙̩͚̪̮͔͓͚̹̰̭͑́͒̒̒͊̒͒͒̒͌̓͊́͑̒͌͆͒̒́̒͌́̓̏̓̒͂̓͒͒͒̓̏̒͌͘͏̸̨͓͙͚̫̭͍͓͙͚͚̭͍̭͚̬̭͓͙͚̫̭͓̗͚̭͉̭͙̦͚̮͉̭͙͙͚̬̭͒̓́̒͊͂͒͌͒͊̒́͂́̏͏̸̡̭͙͚̭͔̭͙̥͚̭̘͙͚̪̭̭͚̬͎̮͎̭͙͚̰̭͔̘͕͚̩̮́̏́͂͋͆̓͒̒͑́̒͊͏̶̸̴̸̸̸̴̧̨̨̨̡̭͙͙͚̫̗̭͚̩̗̭̭͙͚͚̩̭͈̘͖͚̹̭͈̘͙͚̹̮͖͓͚̬̰̭͈̭͍͚̭͎̘͙͚͎̮͇̘͙͚̺͚̭͓͚̬̭͈̭͉͚̤̭͓̭͙͚̫̭͙̯͚͖̭̘͙̩͚̩̭͇̩͚͚̭͓̫͚̫̮̭͙͚̩̮͓͙͚̪̭͚̹̤̭͔̘͙͚̮̭͙͚͚̮͓͚̬̭͍̘͙͚͚̭͓̗͚̫̰̭͉̘͙̣͚̩̮͉̭͙͚͚̬̮͍̘͙̬͚͚̭͓͚̫̭̭͙͚̭̘͚̫̭̘͈͚̪̭͔̘͚̮͐̓̒͋͊̒͊͊̓̒̒͂̓̈́́̓͑̒͆̒́͂͑̓͂͑͂̓̒́̓̒͊͒̒͐̏͊̓̒́͐̓͂͐̒͊͂͌͂͊̒́͒̒͑̓͌͆͂͌̒͌̒̓̒̏́͒͘͘͏̸̘͙͙͚̮͓͙͎͚̩̗̭̮͚̩͖̭͉͖͚̩̰̮͓͙͚̫̤̮͖͚̫͎̭͈̭͍͚̗̭͎̘͙͚͎̮͇̭͙͍͚̺͚̮͂͒͋̓̒̓̒͒͒̓̒̒͂̈́͂͘͏̵̸̴̴̸̵̨̨͙̲͚̬̮͖̭͙͚̰̭͓͙͚̫̭͔͙̯͚̩̤̮͙̬͚̩̭͔̭̩͚̬̬̭͓̫͚̩̮̭͙͖͚̩̭͙̳͚̪̭͚̹̰̭͙͚̫̭͉͙͚̭͍̭͚̫̗̮͕͚̹̭͓͙̱͚̺͎̭͉̭͙̥͚̭͇̘͙̤͚̬̮͉̘͚̭͙͚̫̮͖͙͚̪͖̮͕̤͚̬̭͈̘͈͚̩̭͔̘͖͚̪͚̮̓͆́͒͂̓͊̓̒̓̒̏͒͒̓̏͊̓̒̑͐̓͒̓̓́̏̒͊͐̓̒͊͂̏̒͌́̏͑̓̓̓͆̓̒͆̒͆̒͏̘͙͚̪͖̮͓͚̩̗̭̘͙͚͚̩̭͎̘͖͚̹̮͕̘͙͚̹͖̮͓͚̫̮͎̘͙͔͚̩̭͎̘͚̫͚̮͇̭͙͚͎̮̐͒̒̐͋͊̒͊͒̓̒̏͊̒̒͊́͘͏̸̴̸̡̨̢̨̡̨͚̬̮̭͍͚̤̭̘͙͚̫̭͖̘͙̯͚̪̰̮͕͓͙̩͚̩̭͇͙̤͚̬̭͓͚̪͖̮̭͙͚̪̮͓͙̬͚̪̮͔͙͚̹̰̭͖̘͙͚̫̭͎̘͙͚͚̭͖̘͚̫̭͍̘͙͚̫͖̭͓͚̺̭͉̭͙̦͚̮͉̭͙͚̬̮͉̘͙͓͚̭͓͚̭͍͓͙͚̮͕͚̬̮͙͚̩̭͔̘͙͚̫̰̮̓̒͆͒̒́͒͂͆̓͒̓̒͂͒͒͐̏̓͗͒̓͂̒͊͊͌͊̒̔̓́̏́̏͑̒͑́͂͆͂̓̒̓͑̓͑͒͏̨̘͙͕͚̪͖̮͓͙͎͚̩̗̭̘͚̩̭͇͓͚̩̰̭͓͙͚̺̭͍̘͓͚̬̮͎̘͍͚̪͎̭͎̘͙͚̮͇̭͙̗͚̪̮͒͋̒̈́͊̒̏͋͊̒͆̒̓͂͆͘͏̸̴̴̨͚̬̮͖̘͙͎͚̤̭̘͚̫̭͙̯͚̮͇͙̬͚̩̮͖̘͙̤͚̩͖̭͓̫͚̮̘͙͚̩̮͓͚͚̪̭͎̭͚̹̰̭̓̒͆́͑̒̑͐̓͂͊̓̓̒͂͒̒͐̒̏̒̑̕͏̨̨̨̨̭͙͚̮̭͙͚͚̮͓͇͚̬̭͓͕͚̬̭͓̗͚̫̭͉̘͙̦͚̩̭͇̘͙̥͚̬̭́͐̓͂͐̒͆͒̒͆͊̒͆͏̸̨̡̭͙͚͚̭͔̭͙̥͚̫̭͓͙͚̭͓̭͚̫̬̮͎̭͈͚̹̭͔̘̘͚̬̮́̓͑͆͂̒̒͊̒͂͏̢̨̭͙͚̫̗̮͓͚̩̗̮͕̘͚̩͖̭͈͓͖͚̩̰̭͕͓͙͚̫̰̮͕͓͚̫͖̭͈̭͙͔͚̩̭͎̘͙̮͚̮͇̘͙͈͚̩̮͗͒̒̓̒̒̓̒͒͂͆͘͏̴̸̸̴̵̨̨̨͙̳͚̬̮̘͙̥͚̤̭͔̘͙͕͚̗̮͉̭͙̯͚̪̤̮͇͙̩͚̩̭͔̭͙̤͚̭͓̬͚̮̭͙͚̺̭͙̲͚̪̭͚̹̤̭̭͚̫̭͎̭͙͚̭͍̭͇͚̬̰̮͔͕͚̭͓͙͚̹̭͉̭͙͚̩̮͉̭͙̘͚̬̮͉̭̙͚̭͔̘͙͚̫̭͎̭͙͚̪̮͓̤͚̬̭̘͙͚̭͔̘͓͚̩̤̮̓͆͒́́̓́̓̒́͒͑̏͒̓̏͊̓̒͌͐̒̓͒̓́̏̒̓̒́͂͊͂̒́̏̓͆̓̓̒̏͌͑́͒̒͏̭͙͏̸͚̮͓̣͚̩̗̮͕̭͚̩̭͇̘͖͚̹̭̘͙͚̫̤̮͓͖͚̬̬̮͓͍͚̪͚̭͎̘͚̫͚̮͇̭͙͚͎̮͂͒̒̒̋͊̒͊͋̓̒͑̒̒̒̔́͘͏͇͚̬̮͖̘͙̩͚̰̭̓̒͆́͏̸̸̴͚̫̭͖͓͙̯͚̪̰̭̘͙̩͚̩̮̘̩͚̪̭͓̫͚̮̘͙͈͚̮͓͙̭͚̪̮͔͚̹̤̭͖͓͚̫̮͇̘͙͚̩̮̓̒̑͑͆͒̒͒̓̒͂͒́͒͐̏̓̒̒͐͒̓̕͏̧̨̨͓͚̫͖̮͔͕͚̭͓͙̱͚̫̭͉̭͙͚̩̮͉̭͙͚̬̭̒͊̓̒͂͒͊̏̔͏̨̡̘͙͚͚̭͙̥͚̫̮͙͚̩̮͚̬͖̭͈̘͙͚̪̭͔̘̘͚̮́͑̓̓͑̓͆̓͒̓̒͑͊̒́͒͏̸̭͙͖͚̪͖̭͙͚̩̗̭̘͙͚̩͖̭͈͓͚̹̭͓͓͙͚̺̭̘͖͚̫̗̮͓͍͚̭͎̘͙͚͎̮͇̘͙̗͚͎̮͐̓͌͋͊̒̏͊͊͊̒͑̒͂̈́́́͘͏̨̨͙͚̬̮͖̭͙͚̤̭͔̘͙͚̗̮͕͙̯͚̩̰̮͍͙̬͚̩̮̘͙̤͚̩̭͓͚̪̮̘͙͚̺̭͚̪̭͎͚̹̰̭͓͚̮̓͂͆̓́͂́̓̓͂͒̓̒͂͆͒̐̏͒̓̒͗̏̓̒͐̒͐́̕͏̴̸̴̴̸̧̨̡͓͙͚̮͓͓͚̫͖̮͔͕͚̺̭͓͙̲͚̹̭͉̘͙͚̬̮͉̭͙̮͚̬̮͍̭͙͚͚̭̭͙̥͚̫̭̭͙͚̮͚̬̮͙͚̩̬̭͔̘͓͚̫̰̮̓͂̏̒͊̓̒͊́͒̓͊͆͂͐̓̒̏͑̓͑̒͏̘͙͔͚̪͖̮͓͚̩̗̮͕̘͚̩̭͉͚̹̮͓̘͙͚̹̮͔͓͚̫̮͎̘͙͔͚̩̭͎̘͙̯͚̪̮͇̘͙͚̩̮͒̒̏̒̋͊̓̒̏͊͊̓̒͊͂͆̏͆͘͏̸̴̸̢̨̨̡͚̬̮̘͉͚̰̭͔̭͙͚̫̮͎͙̯͚̭̘͙̩͚̪͚̮͖̘͙̤͚̩̭͓̩͚̩̮̭͙͚̺̭͙͚̪̮͔͚̹̤̭͖̭͚̭͇͙͚͚̭̭͇͚̬̤̭͍̘͙͚̫̭͓̗͚̭͉̘͙̹͚̬̭͇̘͚̬̮͉͓͙͚̭͔̭͚̭͍͙͚̮͚̬̮͎̭͙͚͚̭͔̘̘͚̮̓̒͆͒̒́͂̓͂͊͐̓̓̒͆͒͐̏͒̓̓̏̓̒͐̒͐́̓̓́͌̒͌͆͊̒́͂̒͋́̏̒͑́͂̓͆͂͂͐̓̒͆͑͂̒͂͒͏̢̘͙͚̪͖̮͓͙͚̩̗̮͕̭͍͚̩̭͇̭͙͚̹̭͈̘͙͚̫̤̭͍̘͓͚̬̭͈̭͍͚̪̭͎̘͙͚̫͚̮͇̘͙͚̺͚̮͒͒̐̒͊͊̒͆̒͊̓̔͘͏̸̸̢͙͚̬̮̘̖͚̰̭͓͙͕͚̫̮͍͓͙̯͚̪̰̮͎͙̩͚̩̮̘͙̤͚̩̤̭͓̮͚̮̘͙̓͆͒̒́͒̓͒̓̒͂̓͒͏͚̺̮͓͙͚̪̭͎̭͙̰͚̹̤̭̏͐̏ͅ͏̴̸̵̸̨̨̨̡̘͚̮͈̭͙͚̮͖͓͇͚̫̭͍̘͕͚̬̭͓͚̹̭͉̘͙̣͚̬̮͉̭͚̬̮͉͓͙͚͚̭͓͙͚̫̭͙͚̭̘͚̫̰̭̘͈͚̪͚̭͔̘̘͚̗̮̒̓́̓͂̏̒̏̒̓͊̒̔̒͊́͑̓͋̓͆͂͌̒͌̒̒͂͏̨̭͙͓͚̫̗̭̬͚̩̗̭͇̭̲͚̩͖̭͈̘͖͚̩̰̭͇͙͚̹̮͓͚̬̬̮͓͙͔͚̫̭͎̘͚̮͇̭͙͚̺͚̮͐̓̒̒̒̓͊͑̓̒͑͊̒̑͂̏͘͏̴̴̨̨̨̘͚̬̮͖̭͙̹͚̤̭͔̘͙͚̗̮͇̭͙̯͚̪̮͎͙̩͚̪͚̭͔̭̩͚̭͓̫͚̬̤̮̭͙͓͚̪̭͙̬͚̪̭͓͚̹̤̭͕͚̫̭͉͓͙͚̭͉̭͚̫̮͙͚͖̭͓͙͚̫̰̭͉̭͙̪͚̭͇̘͙̤͚̬̮͉͓͙͚͚̭̓̒͆́͂́̓̒́͊̓̒͒͒̓̏͊̒͐̓̒͐͒̓́̏̒͊͒͐̓͌͂͊͂̏́͏̵͙͚̫̭͍͓͙͚̪͖̭̘̤͚̬̭͈̘͙͚̪̰̭͔̘͖͚̪͚̮̓̓͆͊̒̏͑̒͏̘͙͏̸̸̸̴̨̨̨̡̨͚̭͙͚̩̗̮͕̭͚̩̭͍̘͖͚̹̭͓̘͙͚̹̮͓͚̫̗̭̭͙͔͚̩͎̭͎̘͚̮͇̘͙͉͚̪̭͓͙͚̬̮̭͙̹͚̰̭͙͚̫̭͖̘͙̯͚̪̰̮͖͓͙̬͚̪̮͖̘̩͚̪̭͓͙͇͚̪̮̘͙͚͚̮͓͙̰͚̪̭͎͓͙̰͚̹̤̭͖͓͚̭͙͚̭͎̭͚̫̭͓͙͚̫̭͓͙̱͚̫̭͉̘͙͚̬̭͇̘͚̬̮͉͓͙͚̭̭͚̭͍͙͚̪̮͚̫̭͈̘͙͚̩̤̭͔̘͙͚̮͂͐̓͒̒̈́͊̒͊̓͐̓̒͌̒̑́͆͑́͆͒́͑̓͂͊̒̏̓͆͒́͒͐̏̒̓́͌̓̓͂̏̒͊͊͒͌͊͆͆̒͗͂́̏͑̒͆́͂̓͆̓͒̓̒͂͑́͂͘͏̸̘͙͚̭̯͚̩̗̭̺͚̩̭͈̭͚̹̮͕̭͙͚̫̰̮͓͓͚̬̰̭͈̭͍͚̪̭͎̘͙͚͎̮͇̘͙͈͚͎̮͒͂͐̓̒͋̓̒͊̒̏͊̓̒̒͒͂͂́͘͏̵̸͚̬̮͖̘͙͚̤̭͓̭͙͚̫̭͖͙̯͚̪̤̭̓̒̐͆́͂̓͏̴̷̨̨̨̘͙̬͚̩̮̘͙̤͚̪̭͓̫͚̮̭͙͕͚̩̭͙͚̪̭͎͚̹̰̭͖͓͚̭͎͙͚̭̘͇͚̫̭͓͙͚̹̭͓̗͚̫͖̭͉̭͙͚̮͉̭͙͚̬̭͂͒̓̓̒͂͒͒̓̏̓̒̑̒͐́̓̓͂̏͐̒̏͒͌͂͊̒͂̏̕ͅ͏̘͔͚͚̭̒́͏̵̸͙͚̮͕͙͚̪̗̮͕̤͚̫̮͈͚̪̭͔̘͕͚̬̮̓́͂̓͆̓̒͑̓̒͆̒͂͏̸̘͙͖͚̮͓͚̩̗̮͕̘͙͚̩͖̭͈͓͖͚̹̮͙͚̹̭͉̘͓͚̫͚̭̭͙͔͚̩̭͎̘͙͚̩͖̮͇̘͙͚̪̮͂͒̒̓͒̒͊͑̓̓̒͌͊̓͋͆͘͏̵̸̴̸̘͚̬̮̘͙͚̤̭͓̭͚̫̭͙̯͚̮͓͙̩͚̩͎̭͇̩͚̤̭͓͙͇͚̫̮̭͙͕͚̩̭͙͚̪̮͔͓͔͚̹̰̭͖͙͚̫̮̓̒͆͒́̒̑͐̓͂͊͐̓̒͂̓͊͒͒̓̓̏̒̓͒͏̸̴̸̴̨͙͚͚̮͓͓͚̫͚̭͍̘͙͚̹̭͓͙͚̹̭͉̭͙͚̬̭͇̘͙͚̬̭̓̓́̒͊͌͊̈́̈́͏̴̭͙̬͚͚̭͓̭͚̫̭͎͙͚̪̗̭͉̘̤͚̫̤̭͈̘͈͚̪̭͔̘͓͚̩̮́̒͑̓̓͆̒̒̓̒͏̸̴̭͙͚̫̗̭̙͚̩̗̭̘͙͖͚̩̭͈̘͖͚̹̭͙͚̺͖̭̘͓͚̫̭̭͍͚̩̗̭͎̘͚̬̤̮͇̘͙͚̩̭͓̦͚̬̮͓͙͚̰̭̭͚̫̮͍̭͙̯͚̪̤̮͙̩͚̩̮̘̩͚̪̰̭͓̫͚̩̮̭͙͚̺̮͓͙̺͚̪̭͎͓͙͓͚̹̤̭͒͐̓̒͋͊̒͊͐̓͊̒̏͌̒̒̒͌͆͑̒͆͒̓́͒̒̑͋̓͒̒̓̒͆͒͐̏͐̏͘͏̴̨̨͓͙͚̭͈͓͙͚̩̭́̓͏̨̨̘͇͚̬̤̭͍̘͙͚̺̭͓͚̭͉̭͙̦͚̩̭͇̘͙̰͚̬̭̒͌͆͊̒̔́͂͏̸̴̡̘͙̬͚̭͔͓͚̫̮͓͙͚̭̭͚̫̮͎̭͈͚̬̭͔̘͚̪͚̮́̏̒͆̓͑͆͂͒̒̒͂̒̏͏̸̭͙͚̪͖̭͙͚̩̗̭̭͙̗͚̩͖̭͇̘͖͚̩̰̭͉̘͙͚̹̮͓͖͚̬̰̭͈̭͙͔͚̩͚̭͎̘͙͚̮͇̭͙͚̩̮͗͐̓͌͋̒̓̓̒̓͂͋͆͘͏̵͙͚̬̮͖̭͚̤̭̭͚̗̮̓͆̒̒́͑̒̑́͏̴̵̸̨̨̨̨͓͙̯͚̩̤̭̘͙̬͚̩̮̘͙̤͚̩̭͓͙͇͚̮̘͙͙͚̪̭͙͚̪̭͙͚̹̰̭͕͓͙͚̭͇͓͙͚̭͍̭͇͚̬̤̭͍̘͕͚̹͚̭͓͙̤͚̫̭͉̘͙̤͚̮͉̭͙͙͚̬̮͍̘͙͓͚̭͔̘͙͚̫̭͉͓͙͚̪͚̮̤͚̬̭͈̘͙͚̹̭͔̘͓͚̮͒͂͒̓͂̓͒͒̓͑̏͊̓͗́̓͂̏̒̒͊̏͂̏́̏̓͆͑̓̒̏͑̒́͂͏̸̴̡̘͙͈͚̮͓͚̩̗̭͇̘͙̗͚̩͖̭͇͚̩̰̭͈̘͙͚̹̭͓̭͖͚̬̮͓͙͔͚̭͎̘͙͚̩̮͇̭͙͚̺͚̭͓͙͚̬̮̘͙͚̤̭͓͓͚̗̮͓͙̯͚̪̤̮͎͙̩͚̪͚̮͖̘̩͚̬̗̭͓͙͇͚͎̮̘͙͚̩̮͓͚̪̮͔͓͔͚̹̤̭͂͒̒̏̓̒̏͊̒͂͑͂͒͂͆̏͑̓͆͒́̒͌́͐̓̒̓́͒͗͐̒̒̏̒͘͏̴̨̨̨̘͙͚̭͉͓͙͚͚̭̭͇͚̫͖̮͙͚̬̭͓͙͚̭͉̭͙̣͚̭͇̘͎͚̬̭́̓́͌̒͐̓͌́͊͂͒́̏̒͏̸̡̭͙͚̭͓͓͚̭͙͚̪̗̮͖͚̬͎̮͈͚̬̭͔̘͕͚̩̤̮́̏̒͑́͂͊̓͆̓̒͑̓̒́̒͏̸̘͙͖͚̪͖̭͙̙͚̩̗̭͚̩̭͈̭͚̹̮͕͓͙͚̫̰̮͕͓͚̬̮͓͍͚̪̬̭͎̘͚͎̮͇̘͙͚̺͚̮͐̓͋̓̒̈́͊̒̏͊̓̒͑̒̒̑͂͘̕͏̸̴̴̸̨̨͙̥͚̬̭͈̭͙͎͚̤̭͓̘͚̫̮͇͓͙̯͚̪̮͙̩͚̩̬̮̘͙̤͚̩̬̭͓̮͚̪̮̘͙͔͚̩̮͓͙̺͚̪̭͎̭͙͚̹̤̭͖͓͙͚̮͖͙͚̭̓͆́̒̑͊̓͒̓̒͆͒͐̏́̓̓͂̏͏̨̨̘͇͚̫͚̮͙͚̭͓̗͚̫͖̭͉̘͙̣͚̩̭͇̘͙̮͚̬̭̒͐̓͌́͂͊̒͏̵̸̘͔͚͚̭͓͙͚̫̭̭͙͚̭͍̘̤͚̬̮͙͚̹͎̭͔̘̘͚̫̰̮̒́͑̓͋͆͂̒̓͑̓͑̒͏̴̸̨̘͙͚̫̗̭͚̩̗̭͇̭̦͚̩͖̭͈̭͙͚̹̮͕͓͙͚̫̤̮͓͖͚̬̤̭̭͙͔͚̬̭͎̘͙͚̩͖̮͇̘͙͍͚͎̭͓͚̬̮͖̘͉͚̰̭̘͚̫̭͔̭͙̯͚̪̭̑͐̓̒̒̐͊̓̒͌̈́́͑̒͆̒́͑̒̑͂͘ͅ͏̴̘͙̬͚̩͎̮͖̘̩͚͎̭͓̹͚̫̮̘͙͚̩̭̖͚̪̭͙̬͚̹̤̭̒́̓̒͊͒͗͒̓̒̏͊̓͏̴̴̸̨̨͚̫̭͎̘͙͚͚̭̘͚̫̮͙͚̭͓͙͚̺̭͉̘͙͚̭͇̘͙̤͚̬̮͉̘͙͚͚̭͓͙̥͚̫̭̭͙͚̩̗̮̤͚̫̤̮͈͚̹̭͔̘͓͚̗̮̓̒͐͒̓́͐̒͊̓͐̓͌͂͊́̏͂́͒̓͌͆͑̓̒͑̓̒̒͂ͅ͏̸̸̨̭͙͚̮͓͙͚̩̗̮͕̭̦͚̩̭͍͓͚̩̰̭̭͙͚̫̤̭͓̭͓͚̬̭̭͙͔͚̪̭͎̘͙͚̮͇̭͙͚̩̭͓͚̬̮̭͙͚̤̭̭͚̫̭͓͙̯͚͖̭̒́͒̒͊̒̏͊̒͂͌͂̓͌͆͑̒̒͆͒̏́͒̒̑͑͂̕͘ͅ͏̴̸̨̨̘͙̬͚̪͖̮͖̘͙̤͚̬͖̭͓͚͎̮̭͙͚̩̮͓͙̹͚̪̭͎͓͙̬͚̹̰̭͓͙͚̫̮͕͓͙͚͚̮͖͓͇͚̬̭͍̘͕͚̭͓͚̺͎̭͉̘͙͚̮͉̭͚̬̭̓̒͂͂͒͑͐̏͐͒̓͂̒̒́͂͊̒̔͆͂̏̒̔͏̸̡̭͙̰͚̭̭͙̥͚̫̮͔͙͚̪̗̮͚̬̭̘͈͚̪̭͔̘͖͚̫̮́̏͑̓̓͆͐̓̒̏͌̒̒͆͏̸̸̨̘͙͚̭̙͚̩̗̮͕̭̦͚̩̭͈̭͖͚̩̰̭̭͙͚̺͖̭͍̘͖͚̫͖̭͈̭͍͚̪̗̭͎̘͙̯͚̮͇̭͙͍͚̺͚̭͓͚̬̮͖̘͙̩͚̤̭̭͚̫̮͖̘͙̯͚̪̰̮͕͓͙̬͚̩̮͖̘̩͚̗̭͓̹͚͎̮̘͙͚̺̭͙̱͚̪̭͎̭͚̹̰̭͒͂͐̓̒̒͊̒͋̒̒͂̓͑̒͆́͑̒͌͂̒͂̓̒͂͒̓̏͒̓̏̒͘͘͏̨̨̨͓͙͚̮͖̭͙͚͚̭͇̭͚̬̬̮͔͙͚̺̭͓̗͚̫̭͉̘͙̥͚̭͇̘͚̬̮͍̘͚̭͓͓͚̫̭̘͙͚̪̗̮͓̤͚̬̗̭̘͙͚̹͎̭͔̘͕͚̪̮́̓͂̒͊̓͌̏͊̒̏͂̏̒͐̒̑́̏̒͑̓͑͆̓̒͌͑̒͊͏̸̴̸̸̢̨̨̨̨̨̨̭͙͚͚̮͓͙̖͚̩̗̭͓͙̗͚̩͖̭͉͙͚̹̭͓͓͙͚̫̰̮͕͓͚̫͚̮͓͙͔͚̩͚̭͎̘͙̯͚̫͚̮͇̘͙͚̪̭͓͚̬̮̭͚̤̭͔̭͙͕͚̗̮͇͙̯͚̭̘͙̩͚̩̮̘̩͚̭͓͙͚̮̘͙͚̪̭͙͚̪̭͎̭͙͚̹̰̭͕̘͙͚̮͇͓͙͚͚̮͔͓͚̫̭͓͙͚̫͖̭͓͙̱͚̺͎̭͉̭͙͚̩̮͉̭͙͚̬̮͚̭͔͓͚̫̭͈͙͚̪̗̮͕̤͚̫̭̘͙͚̩̭͔̘͓͚̫̰̮͂͒͌̓͊̓̒͑͌͆͑̒̋͆͒̒̋́́̓͂͊͒͆͒̒͂̏̓͊͂͒̑͒̓̏͂́̓́̒͊͊͒͌͊̈́̏͊̓̒͌́̏̒͆̓̓͆̓̒͌͑̒͘͏̸̸̘͙͚̮͓͙͚̩̗̭̭̖͚̩̭͇̘͖͚̹̮̭͙͚̺̮͓͚̫͚̭̭͍͚̪̭͎̘͙͚̩̮͇̘͙͚̩̭͓͚̬̮͓͙͚̰̭͔̘͚̫̭̓͂͒͐͋̒͊̒͊͑͊͑̓̒͌̒͆̏͌͆͑̒͆͒̓́̒͌͘̕ͅ͏̴̴̨̨͙̯͚͖̭̘͙̩͚̩̮͖̘͙̤͚̭͓͙͚͎̮̘͙͈͚̩̮͓͙̱͚̪̭͎͙͚̹̰̭͕͓͚̭͇͓͙͚̩̭͉̭͚̫̗̮͕͚̫̰̭͓͙̱͚̭͉̭͙̪͚̮͉̭͙͚̬̭̓͂͑͂̓̓͊͂͒͐̏̓͗̒̓́̓͆̒͊͐̓̒͊͂͒́̏̔͏̵̴̡̘͚̭͓͙͚̭͓͙͚̩̭̭͚̬͎̭̘͙͚̩̭͔̘͚̩̤̮̒́̏͒́͂͋͆̓͒̒͌͑̒̏͘͏̸̧̨̭͙͓͚̫̗̮͓͙͉͚̩̗̭͇̘͙͚͚̩͖̭͉͖͚̩̰̭͙͚̹̮͓͓͚̫̮͎̘͙͔͚̪̬̭͎̘͙͚̬̤̮͇̘͙͉͚̩̭͓͚̬̮͓͉͚̤̭̭͙͕͚̫̭͙̯͚̪̭͒̓̒͊̓̓̓̒͊̈́͆͑̒͆͒̒́͒͑̓͘͏̨̘͙̩͚̩̮̘̩͚̬̭͓͙͚̫̮̘͙͚̮͓͙̦͚̪̭͎͚̹̤̭͒̒͒̓͊͊͒̑́͒͐̏̓̒͘͏̷̨̨̨̨̨̡͚̭̘͙͚͚̮͔͓͚̫̮͙͚̭͓͙͚̫̰̭͉̘͙͚̩̭͇̘͙̖͚̬̮͍̘͙͓͚͚̭̘͙̥͚̫̮͕͓͙͚̩̗̭̭͚̬̗̮͈͚̗̭͔̘͖͚̬̮̓̒̓́͋̓͂̒͊͐̓͌͂̏͊́͑̓͆͒̒͑̓̒͂̒́͏̴̘͙͕͚̫̗̮͓͍͚̩̗̭̭͙͚͚̩̭͉͙͚̹̮͓̭͙͚̫̰̭̘͖͚̬̰̮͓͙͔͚̗̭͎̘͙͚̫̮͇̭͙͇͚͎̭͓͚̬̭͈̭͚̰̭̘͚̗̭͕͙̯͚̭̘͙̩͚̪̭͔̭͙̤͚̩̤̭͓̮͚̫͚̮̘͙͚̩̮͓͙͚̪̮͔͓͙͓͚̹̤̭͒̒͋͊̓̐͊͌̒͑͂͂͊́͑̒̒͆̒̒́͒̒͌́̓͂͊͒͊̓̒͒̒͐̒̏͘͏̸̧̨̡̘͚̫̮͕̭͙͚̮͓͇͚̬̤̭͍̘͕͚̺͖̭͓͙̱͚̗̭͉̭͙̥͚̮͉̭͙͚̬̮͔͚̭͓̭͙̥͚̮͖͙͚̭̘͚̬̮͈͚̭͔̘͚̫̰̮̒͐͒̓́̏͐̒̒͊͂́̏͊̓̒́̏́͂̓͆͂͂͋̒͊͑̓̒́̒̏͏̸̸̸̴̨̨̨̘͙͚̭͚̩̗̭̘̮͚̩̭͈̭͙͚̹̭͇̘͙͚̹̭̘͖͚̫̮͓͍͚̪̰̭͎̘͙͚̫͚̮͇̘͙͚̺͚̭͓͙̫͚̬̭͈̘͙͚̤̭͔͓͚̫̮͉̘͙̯͚͖̮͎͙̩͚̩̰̭͔̭͙̤͚̩̤̭͓̹͚̮̘͙͚͚̩̭͚̪̭͚̹̰̭̭͚̮̭͙͚̭͍̭͇͚̫̮͔͕͚̫̭͓̗͚̗̭͉̘͙̥͚̭͇̘͙̬͚̬̮͙͓͚̭͓͓͚̫̭͙͚̭̘̤͚̫̮͈͚̭͔̘̘͚̬̮̓͂͐̓̒̈́͋̒͊̐͊͒͌̒͒͑̒͑͆͊́̒͌͂̓̓̒́͒͒̓̒͐̏͊̓̒͐̒͐́͐̓͂̏̒̏̓̒͒͊̒͂͂̏͊̓́̏̒͆̓͊̓͆͂͂͌̒͑̓̒́͒̒̏͘̕͘ͅ͏̸̭͙͚̭̰͚̩̗̭͙͎͚̩͖̭͈͚̩̰̮̭͙͚̫̤̭̭͓͚̬̮͎̘͙͔͚̭͎̘͚̬̤̮͇̘͙̖͚̩̮͒́͐̓̒͋̓̓̒̏͒͒̒͆́̓̒̒͆͘͏̴̵̴̨̨̨̨̨̨͚̬̮͖̭͙͚̰̭͓͚̗̮͕̭͙̯͚̪̭͕̘͙̬͚̩̮̘͙̤͚̬͎̭͓̹͚̮̭͙͖͚̪̭͙̦͚̪̭͍̘͙͚̹̤̭͖̘͙͚̫̭͍̘͙͚͚̮͓͚̫̮͔͕͚̭͓͚̺̭͉̭͙̥͚̮͉̭͙̗͚̬̮͉̘͙͚͚̭͓̭͙͚̫̭͎͓͙͚̩̮̤͚̬̭̘͙͚̪͖̭͔̘͓͚̪̮̓̒̓͆͊́͒̒͌́͆͒̓̒͂͒͒̓̏͒̓́͐̒͊̓̒͂̏͊̒̔̓́̏͗́̓͆̓͑̓̒̓͌͑̒͏̘͙͏͚̪͖̮͓͚̩̗̭̭̮͚̩̭͎̘͖͚̩̰̭͇̭͙͚̫̤̭̘͓͚̫͖̭̭͙͔͚̪̰̭͎̘͚̮͇̘͙͚̪̮͒̒̓͋̒͊̒͊̒͌̒̒́̓͋͆͘͏̴̥͚̬̭͈̭͙͎͚̤̭̭͙͕͚̗̮͈̘͙̯͚̪̤̮͈͙̩͚̩̭͔̭͙̤͚̬̭͓͚̬̤̮̭͙̓̒͆́͒́̓͒̓̒͂͒͏̴̴̸̨͚̪̮͓͙̫͚̪̭͎͓͙͚̹̰̭̭͙͚̭͙͚̭͐̏͐́͋̓̓͂̏͏̸̴̨̨̨̡̨̘͇͚̬̤̮͕͚̬̭͓̗͚̬̭͉̭͙͚̬̮͉̭͙͚̬̮͉̘͚̭̘͙̥͚̭̘͙͚̭͉̘͚̫̬̭͈̘͈͚̩̭͔̘͙̥͚̗̮̒͐̓̒͊̒̏̒́̏͑́͂͊͆͂͂̒̒͂͘͏̸̢̭͙͚̭͙͓͚̩̗̮͕̘͙͚̩͖̭͇͙͚̹̭͙͚̹̭̘͓͚̬̮͎̘͍͚͚̭͎̘͙͚̮͇̭͙̗͚̪̮̓͂͐̓͒̓͊͐̓̓͌̒͆̒͂͂͂̓͆͘͏͚̬̮͖̘͙͎͚̤̭̭͙͕͚̗̭̓̒̒͆́͒́͏͙̯͚̪̤̭̘͙̬͚̩͎̮̘͙̤͚̩̭͓̹͚̬̤̮̭͙͚̭̖͚̪̭͎͚̹̤̭̓͑͒̏̓̒͒͑́͒͒̓̒̏̓̒͐͏̸̨̨̨̨̨̘͙͚̮͓̘͙͚͚̭͇̭͚̫͎̮͔͕͚̭͓͙̤͚̹̭͉̘͙͚̩̮͉̭͙̖͚̬̭́̓͂̒͊̓̒͂̓͊͏̴̸̴̨̘͙͚̭͔͚̫̭͓͙͚̭̭̤͚̫̮͈͚̪̭͔̘͚̪̮́̏̓̒͆̓͐͆͂͒̒͂͑̓̒̒̏͏̡̭͙͚̫̗̮͓͚̩̗̮͕̭͙͎͚̩͖̭͈͓͙͚̹̭͙͚̹̮͖͚̬̤̭̭͍͚̫̭͎̘͙͚͎̮͇̘͙͚̩̭͓͙͚̬̮̭͙͚̰̭̐͒̒̐͊͊̓͒͐̓̒͌̒͒̓͂̏͆͑͂͆͒͊́͘͏̸͙͚̗̮͉͙̯͚̪̤̭͖̘͙̩͚̩̬̭͇͙̤͚̩̭͓̬͚͎̮̭͙͖͚̮͓͕͚̪̭͓͙͚̹̰̭̓͂́̓̓͆̓̒͂͒́͒͐̒̏͊͏̴̵̨̨̨͙͚̫̮̭͙͚̮͓͚̬̮͙͚̹̭͓͙̱͚̺͎̭͉̭͙͚̩̮͉̭͙͚̬̮͙̬͚͚̭͔͓͙͚̫̭͎͙͚̩̭͓̭̤͚̫̬̭̘͈͚̹̭͔̘͙̥͚̬̮̓͒͐̓́̏͐̒͊͐̓͌͊͊͂͌͊̓́̓̓͆̓̒͌̒͂̏͏̸̭͙͖͚̮͓͉͚̩̗̭̭̖͚̩̭͇͓͙͚̹̭͈͙͚̹̭̘͓͚̫̮͓͙͔͚̬̭͎̘͚̫͚̮͇̘͙͍͚̩̮́͒̒͋̒͊̐͊̓̓͋̒̏͑͂̒̒͆͘͏̵̸̸̸̸̨͚̬̮͖̘͙͚̰̭͔̘͙͕͚̫̮͇̭͙̯͚̭͓̘͙̩͚̩̤̭͔̭̩͚̭͓͙͚̮̘͙͚̭͚̪̭͎͓͚̹̤̭͙͚̮̓̒͑͆́͂͊̒́̓͊͂͒̒́͒͒̓̒̏̒͌͐̓́͘͏̴̭͙͚̩̭̓͏̨̨̘͇͚̬̤̭͓͕͚̬̭͓̗͚̺̭͉̭͙͚̮͉̭̘͚̬̮͉͓͔͚̭̭͚̭͎̭͙͚̪͖̮͕̤͚̬̮͈͚̭͔̘͚̮̒͒̒́͊̒̓͂̏̒̒́̏͑̒͑́͂͆̓̒̏͑̓̒͂͒̒̏́͒͏̸̸̘͙͙͚̮͓͙͉͚̩̗̮͕̭͙͖͚̩͖̭͉͚̩̰̭͕͙͚̫̰̮͕͖͚̬̬̮͓͙͔͚̩͎̭͎̘͚͎̮͇̘͙͉͚̩̭͓͙͚̬̮͖̭͙͎͚̰̭͓͓͚̫̭́͒̓̒̏̓̓̒͑̒̑͂͆͑́͆́̒̑͘͏̸̴̴̸̨̡̨̨͙̯͚̩̤̭͖̘͙̬͚̩̬̭͔̭͙̤͚̩̰̭͓̩͚̮̭͙͈͚̪̭͙͚̪̮͔͓͚̹̤̭͖̘͚̮̭͙͚̭̭͚̫̗̭͍̘͙͚̭͓͙͚̗̭͉̘͙͚̬̮͉̭͙̤͚̬̮͚̭͔̭͙̥͚̫̭͈͓͙͚̩̮͔̤͚̫̭͈̘͈͚̭͔̘͓͚̮̓̓̒́͒͒̓̒̏̒͌̒̓́͑̓͂̏͌̒͊͌͂͊͊͂͊̓̒́̏̓͆̓̓̒͂̒́̒͂͂̕͏̸̢̭͙͚̭͚̩̗̭͇̘̖͚̩̭͈̘͙͚̹̭̑́͐̓̒̔̒͊͊͏̸̸̴̴̨̨̨̨̡͙͚̹̭̭͖͚̬̮͓͙͔͚̪͖̭͎̘͙͚̫̮͇̘͙͚̪̭͓͍͚̬̮̭̖͚̰̭͔̭͙͚̫̮̭͙̯͚̭̘͙̩͚̪̭͇͙̤͚̪̭͓̮͚̮̭͙͖͚̩̭͙̯͚̪̮͔͓͙͚̹̤̭͔̘͚̫̭͍͓͙͚͚̮͓͓͚̬̭͍̘͕͚̹̭͓͙̱͚̹̭͉̭͙̦͚̩̭͇̘͈͚̬̮͍̘͙̰͚̭͔̘͙̥͚̭͙͚̭̭͚̫̭̘͈͚͎̭͔̘̘͚̪̮̓͒͒̒͑͂͊͆͑̒͆͒̒́͂͌͂͊͑̏̓̓̓̒͂͒͒̓̏͗̒̓͒̓́̒͊͂̒͒͊̒́̏́͂͋̓͆͂͂͑̒͌̒́̒͊͘̕͏̘͙͏̸̸̸̴̶̸̨̨̨͚̭͙͉͚̩̗̭̭͙͚̩̭͉͚̩̰̮͖͙͚̫̰̮͓͚̬̮͎̘͍͚̪̗̭͎̘͚͎̮͇̘͙͚̺͚̭͓͙̩͚̬̭͈̘͚̤̭͓̭͙͚̗̮͖͙̯͚͖̭͕̘͙̩͚̩̮͖̘̩͚̭͓̹͚̪͖̮̘͙͚̩̮͓͙͚̪̭͍̘͚̹̤̭͕̘͙͚̮͎̘͙͚̮͕͓͇͚̫̮͕͚̺͎̭͓͚̺̭͉̘͙̥͚̭͇̘͙̩͚̬̮͚̭͔̭͙̥͚̫̭͙͚̪̮̤͚̬̮͙͚̪̭͔̘͚̪͚̮́͐̓͋̏͊̓̒̏̓͑̓̒̒̒̑͂̓͑͆̒̋́͂́̓͂̒͂͒̓̒͒͑͐̏̒́̓͂̏̒͊͐̓̒͊̒̔͂̏͊̓̒́̏̓͋̓͆̓͒̓̒̓͑̓͑͊̒̏͘̕͘͏̸̸̸̢̨̨̨̭͙͔͚̮͓͙͚̩̗̭͇̘͚̩͖̭͇͓͚̹̭͕̭͙͚̹̭͍̘͖͚̬̤̭̭͍͚̗̭͎̘͚̫͚̮͇̭͙͈͚͎̭͓̩͚̬̮͖̭͉͚̤̭͔̘͙͕͚̫̭͔͙̯͚̩̤̮͎͙̬͚̩̭͔̭̩͚̩̤̭͓̮͚̪͖̮̭͙͕͚̭͙̫͚̪̭͎̭͙̬͚̹̤̭͖̘͙͚̮͖͓͙͚͚̮͓͓͇͚̬̭͍̘͕͚̭͓͙̤͚̬̭͉̭͙̥͚̭͇̘͕͚̬̭͂͒͊̒̒̏͊͊̒͌̒͂̒̒́͑̒͆̒́̓̓̒̓̒͒́͒͒̓̏́̓́̒͆̒́͂͊̏́̏̒͘͏̨̘̙͚͚̭͓͚̫̮͕̘͙͚̩̗̮̤͚̬̭̘͙͚̪̭͔̘͓͚̬̮̒́͒̒͑̓͆͑̓̒͊͌͑̒̏͏̸̸̢̨̘͙͓͚̭͙͖͚̩̗̭̘͙̗͚̩̭͎̘͙͚̹̮͙͚̫̰̭͓̭͓͚̫̮͎̘͙͔͚̪̭͎̘͚̮͇̭͙͚͎̮͂͐̓͋͊͊͑̓̒̏̒̒͂̓́͘͏̸͙͚̬̭͈̭͙͚̤̭̘͙͚̗̮͎̘͙̯͚̪̤̭͕̘͙̩͚̩̮̘̩͚̪̰̭͓͚̮̘͙͕͚̮͓͙̮͚̪̮͔͓͙͓͚̹̰̭̓͂͆̏́͑͂́͆͒̒̓̒͂́͒́͒͐̏͏̴̨̨̨̨̭͙͚̮͓͙͚͚̮͕͓͇͚̬̤̮͙͚̫͖̭͓͙͚̬̭͉̭͙̤͚̩̭͇̘͉͚̬̭́͐̓͂̒͐̓͌͊̏̒͏̸̴̡̭͙͚̭͓͙̥͚̭͓͙͚̭͉̘͚̫̰̭͈̘͈͚̪̭͔̘͙̥͚̩̮͂́̏͑́͂͌͆͂̒̒͒͏̭͙͚̪͖̭͚̩̗̭̭̖͚̩̭͈̘͙͚̹̭͓͓͙͚̹̮͖͓͚̬̤̭͈̭͙͔͚̭͎̘͙̯͚̫͚̮͇̭͙͚̪̮̐͐̓̒̔͋̒͊̐͊̓̓̒́̏͆͘̕͏̸̴͚͚̬̮͖̘͚̤̭͓̭͚̗̮͙̯͚̮͙̬͚̩̭͔̭͙̤͚̩̭͓͙͚̮̭͙͕͚̩̭͙͚̪̭͎͓͙͓͚̹̤̭̓̒͆̒̒́̒̑́͌̓͂͊͋̓̏̓͊́̓͒͒̓̈́̏͏̨̨̨̡̨̭͙͚̫̭͍͙͚̭̘͇͚̫͚̭͍̘͙͚̹̭͓͙̲͚̺͎̭͉̘͙̣͚̩̭͇̘͚̬̮͉̭͚̭͓͓͚̫̭̭͙͚̪̮͖͚̫̮͎̭͙͚̩̤̭͔̘̘͚̮͒̓̓͂̏͐̒͌͆͊̒͒̒́̏̒͑̓͑͆̓̓̒͑̒͂͂̕͏̭͙͏̡͚̫̗̮͓͚̩̗̮͕̭͙͎͚̩̭͎̘͙͚̩̰̮͒̒͊̐͏̭͙͚̫̰̮͕͖͚̫͎̮͓͙͔͚̩̭͎̘͙͚͎̮͇̭͙̗͚̺͚̮̓̒͑͂͂́͘͏͎͚̬̮̭͚̰̭̓̒͆͒̒͑́͏̴̴̴̨̨̨̨̡͚̗̮͇̭͙̯͚̪̰̮͓͙̩͚̩̬̭͔̭͙̤͚̩̭͓͙͇͚̮̭͙͚̪̮͓͖͚̪̮͔͓͚̹̰̭͖͙͚̭͉͙͚̮͕͓͚̫̮͔͕͚̫̭͓͚̭͉̘͙̤͚̮͉̭͙͚͚̬̮͉̘͙͚͚̭̘͙̥͚̫̭͎̭͙͚̭̭͚̬͖̮͈͚̪̭͔̘͓͚̮̓̒̑́͐̓́̓͒̒͐̒̏̒̑̓́̓̓́̏̒͊͊̓̒͊̒̔́͂́̏́͑̓͆͂͂͒̒͑̓̒͒̒́͒͏̸̸̭͙͚̮͓͚̩̗̭̮͚̩̭͇͓͚̩̰̭͕͓͙͚̺͖̮͖͚̫͚̮͓͙͔͚̭͎̘͙͚͎̮͇̭͙͚͎̭͓̘͚̬̮͖̭͙͎͚̰̭̭͚̫̭͑́͒̒̋͋̓̒͊̒̏͐̓̒͑͂͊͂̋́͑̒͆́͒̒̑͘ͅ͏̴̴̨̨͙̯͚̮͙̩͚̩̮̘͙̤͚̬̭͓͙͇͚̪͖̮̘͙͈͚̺̭͙͚̪̭͎̭͙͓͚̹̤̭͖͓͙͚̫̭͍̭͙͚̩̭͇̭͇͚̬̭͓͙͚̹̭͓͙̱͚̫̭͉̭͙̤͚̮͉̭͚̬̭̓͂͊͊̓͒́̓͒̏͒̓̒̏͒̓͆̒͒͌͆͊͆́̏̒̋͏̴̡̘͙͚͚̭͙̥͚̭͎̭͙͚̩̗̮͖͚̫̭̘͈͚̹͎̭͔̘͚̗̮͂́͑̓́͂͆̓̒͌̒̒̏͂͏̸̨̡̘͙͚̭͙͈͚̩̗̭͇̘͙̗͚̩͖̭͈̘͚̹̮͕͙͚̹̮͓͓͚̫̭͈̭͙͔͚̪̭͎̘͙͚̮͇̭͙͉͚̩̭͓͚̬̮͖̘͙̹͚̤̭̘͚̗̮̒͂͐̓̒̏͊̓͒̓̒̏͊̓͂͆͑̒͆́͒̒͌́͘͏̴̨͓͙̯͚̩̰̭̘͙̬͚̩̭͔̭͙̤͚͖̭͓͙͇͚̮̘͙͚̩̭͙͐͆́̓͂͒̑͒̓͏̨̨̧̨͚̪̮͔͓͔͚̹̰̭͖̭͙͚̮͙͚͚̭̭͇͚̬̤̭͓͕͚̹̭͓͚̫̭͉̘͙͚̭͇̘͙͚̬̮͍̘̙͚͚̭̏̒́͐̓̓͂͌̒͒̒͊͊̒̔͆͂̏̒́̕͏̵̴̴͙͚̫̭͉̭͙͚̩̮͓̤͚̫̭̘͙͚̩̭͔̘͓͚̪̮̓̓͆̓̓̒͂͌͑̒͏̸̢̘͙͙͚̮͓̪͚̩̗̮͕̭͍͚̩̭͇͓͙͚̩̰̭͍͓͙͚̹͖̭͍̘͓͚̫̗̭̭͙͔͚̪͖̭͎̘͙̮͚̫̮͇̭͙͚̺͚̮͂͒̒̒͊̒͌͊͊͘͏̵̸͙͚̬̮̘͙͚̰̭̭͚̫̮͎͙̯͚͖̭̘͙̩͚̪̭͔̭̩͚̬̬̭͓̩͚̪̮̭͙͚̭͙̹͚̪̮͔͓͚̹̰̭̓́͆͒́͒̒̑̓͂͐͊̒̓̒͆͒͗́͒͒̓̏̒̑͏̴̵̨̨̨͓͙͚̮͉͙͚͚̭͉̭͇͚̫͖̮͔͙͚̫̭͓̗͚̺͎̭͉̭͙̣͚̬̮͉̭͙̥͚̬̮͍̘͚̭͔̘͙͚̮͖͙͚̭̭̤͚̬̭͈̘͙͚͎̭͔̘̘͚̗̮́̓̓́̒̓͌͒͊̒̒́̏́͂̓͆͂͂͒̒̏͑͂̒͂̕͏̘͙͚̪͖̭͚̩̗̭̺͚̩̭͈̭͙͚̹̭͇̘͙͚̹̭̘͓͚̬̰̮͎̘͍͚̩͖̭͎̘͙͚̬̤̮͇̭͙͇͚̪̮͒͐̓̒̓͋̓̒͊̐͊͊͌̒̒̈́͆͘͏͇͚̬̭͈̭͙̥͚̰̭̘͚̗̭͖̘͙̯͚̮͓͙̩͚̩̮̘̩͚̭͓̹͚̩̮̘͙̓̒͆́͑̒̑́͂͊͐͆͒̒͂͊̓̒̏͒͏̴̶̸̨̧̨̨͚̪̮͓͙͚̪̭͙͓͚̹̤̭͖͓͙͚̫̭͇̭͙͚̭̘͚̬̬̭͍̘͕͚̺͚̭͓͚̺̭͉̘͙͚̩̮͉̭͚̬̮͍̘͙͚̭͓̘͚̫̭͎͓͙͚̪̗̮̤͚̬̮͈͚͎̭͔̘̘͚̗̮͐̏͊̓͒̓͂̏͐̒͊̒͊̒̔̒͗́̏̒͑̓͆͐̓̒͒͑̓̒͂̒͂̕͏̭͙͏̴͚̪͖̮͓͙͎͚̩̗̮͕̘͙͖͚̩͖̭͉͖͚̩̰̭͈̘͙͚̫̰̭̘͓͚̫̮͎̘͙͔͚̬̭͎̘͚̫͚̮͇̘͙͚̪̮͒̓̒͌̒͊̒̑̋͆͘͏̸͙̣͚̬̮͓͙̹͚̰̭͓͙͕͚̫̭͔͙̯͚̩̤̭̘͙̬͚̩̭͇̩͚̪̭͓̫͚̬̤̮̭͙͕͚̭͙̬͚̪̭͙̓͆͒́͑̓͒͂̓̒̓̓̒͒́͒͒̓̏͊̓͏͚̹̤̭͏̴̸̨̨͙͚̫̭͉̭͙͚͚̮͕͓͇͚̬̭͓͙͚̫̭͓͚̭͉̭͙̥͚̮͉̭͚̬̮͉̘͚͚̭͔͓͚̫̭̘͙͚̪͚̭̘̤͚̬̗̭͈̘͈͚̹̰̭͔̘͓͚̮̓͒̓́̒͒͌͊̒̔́͂͂̏̒̏̒͌́̒͆̓͊͆͊̒̒̒́͂͏̸̢̭͙͚̭͙͖͚̩̗̮͕̭͚̩̭͎̭͙͚̹̭͓͓͙͚̹̮͓͚̫͎̭̭͙͔͚̩̗̭͎̘͙͚̩͖̮͇̭͙͚͎̮̒́͐̓̒̋͊͊̓͐̓̒͌̈́͊́͘͏̸̴̴̴̨̧̨͙͚̬̮̘͉͚̤̭̭͙͕͚̗̮͎̘͙̯͚̪̤̮͈͙̩͚̩̰̮͖̘̩͚̭͓̫͚̮̘͙͚̪̮͓͙̱͚̪̭͎͚̹̤̭͕̭͚̫̮͖͙͚̗̭͎̭͚̫͚̭͓͙͚̹̭͓͙̲͚̹̭͉̭͙͚̬̭͇̘̙͚̬̭̓͆͒̒́͑́̓̒́͊̓̒͂͒̒͐̏̓̒̒̓͒̓̓́̒͊͒͌͊̓̒̕͏̸̡̨̘͚͚̭͓̘͚̭̘͙͚̪̮͚̫̬̭͈̘͙͚̹̭͔̘͙͚̩̤̮̒́̒͑́͂͊͆̓͐̓̒͑̕͏̢̘͙͕͚̪͖̮͓͙͚̩̗̭͙͖͚̩̭͈͓͙͚̩̰̭͉̘͙͚̺̮͖͚̬̤̭͈̭͍͚̪̭͎̘͙̯͚̮͇̘͙͇͚͎̮͒̏͋̓͊͊͐̓̒̒͂́̓́͘͏̴͚̬̮͖̭͍͚̤̭̭͚̗̮͎̭͙̯͚͖̭͖̘͙̬͚̩̮͖̘̩͚̗̭͓̫͚̩̮̭͙̓̒͊͆̒́͒̒̑́͂̒͂̓̒͆͒͏̴̷̴̨̨̨͚̪̭͙͚̪̭͎͓͙͚̹̰̭͕͚̮̭͙͚̗̮͖͓͇͚̫͚̭͓͙͚̫͚̭͓͙͚̫͖̭͉̘͙̤͚̬̭͇̘͚̬̮͍̘͙͓͚͚̭͓͚̮͖͓͙͚̪̮͖̤͚̬̭͈̘͙͚̹̭͔̘̘͚̫̰̮͒̓̏͗̓̒͐́͑̓́̒͒͌͊̒͒́͑̒͆́͂͆̓̓̒͊͑̒ͅ͏̸̘͙͖͚̭͙͚̩̗̭͚̩͖̭͈̭͖͚̹̮͙͚̫̰̮͖͖͚̬̮͓͙͔͚̩̭͎̘͙̯͚̫͚̮͇̭͙͚̩̮͂͐̓̐͋̓̒̈́̒͊͑̓̓̒͆͑͊̏͆͘͏̴̴͚̬̮̭͙̥͚̤̭͔̭͚̗̮͎͙̯͚͖̮͙̩͚̩̮̘͙̤͚̩̭͓͙͚̪̰̮̭͙͚̩̭͙͚̪̭͓͙͚̹̰̭̓̒̓͆͒́̒̑́̓͂͋̓͆͒̓͊͒͒͒̓́̏͊͗͏̴̴̨̨̭͚̭͉͙͚̩̭͍̭͚̫͖̮͕͚̺͚̭͓͙͚̭͉̭͙͚̭͇̘͙̱͚̬̭̒͐́̓̓̒͊͐̓̒͊́͂́͂̏͏̡̭͚̭͔͓͚̮͓͙͚̪̗̮͓͚̬̮͙͚̭͔̘͓͚̩̮̒̑́̏̒͑́͂̓͆̓̒͆͑̓͑͂͊̒͊͏̸̭͙͚̮͓͚̩̗̮͕̭͙͚̩̭͇̘͚̩̰̮͑́͒̒̏͊͊̒̏͏̵̸̴̴̨̡͙͚̹̮͖͖͚̬̭͈̭͍͚̩̭͎̘͙͚̮͇̭͙͚̪̭͓͙͚̬̮͖̭͙͚̤̭͙͕͚̫̭͕͙̯͚̪̤̮͓͙̩͚̩̮̘͙̤͚̭͓̩͚̮̭͙͚͚̺̮͓͙͚̪̭͎͙͚̹̰̭͕͓͚̫̮͇̭͙͚̩̮͖͓͚̫̮͕͚̫̭͓̗͚̹̭͉̭͙̤͚̬̮͉̭͙̘͚̬̮͉͓͔͚̭͚̭͙͚̩̮͚̬̗̭̘͈͚̺̭͔̘͚̗̮̓̓̓̒͂̒͊͂̓͌͆͑͂͆́͑̓̓͐͒́̓̓̒͂̓͒̏͐͂̏̓͗̒̓͒̓͆̒͊͒͐̓̒͆͊̒̓̒́̏͑̓̒͆́͂͌̓͆̓͒̓̒͌̒̏̒̏͂͘ͅ͏̨̭͙͖͚̫̗̭͚̩̗̮͕̘͍͚̩͖̭͈̭͚̹̮͙͚̺͖̮͖͚̫̭̭͍͚̰̭͎̘͙͚̮͇̘͙̙͚͎̮͐̓̒̐̒̒̏͊͐̓͑̓̒̏͌̒͂̓͂́͘͏̸͚͚̬̮͖̭͙͚̤̭̭͚̫̮͈͓͙̯͚̩̰̭̓̒͆̏́͒̒̑͏̴̴̴̨̨̨̘͙̬͚̩̮͖̘̩͚̭͓͙͇͚̩̮̘͙͚̩̭͙͍͚̪̭͎͚̹̰̭͔̘͙͚̫̮͇͙͚͚̮͓͚̫̭͓͙͚̫̭͓̗͚̫͖̭͉̘͙̥͚̬̮͉̭͙͚̬̭͂̒́͆̓͆͒̑͒̓̏̓̒͒̓̓͂͑̒͊͒͌͊̒́̕͏̴̵̴̡̨̘͙͚͚̭̘͙͚̫̮͕̘͙͚̩̭͓̭͚̬̗̮͎̭͈͚̪̭͔̘͖͚̪̮́͒̓͆̓̒̒̒͏̴̢̨̨̭͙͚̫̗̭͚̩̗̮͕̭̲͚̩̭͉͙͚̩̰̭͇͙͚̫̰̭̭͓͚̫͖̭̭͙͔͚̩͚̭͎̘͙͚͎̮͇̘͙͈͚͎̭͓͚̬̮̭͙̩͚̰̭͔̭͙͕͚̗̭͙̯͚̪̰̭͕̘͙̩͚̪͖̮͖̘͙̤͚̩͚̭͓͙͇͚̬̤̮̘͙͚̩̭͙̳͚̪̭͎͚̹̤̭͙͚̮͎̘͙͚͚̭͖̘͇͚̫̭͓͙͚̫̭͓̗͚̫̰̭͉̭͙̤͚̮͉̭̐͐̓̒̔̒͊̓̓͑̒͌͂͂́͑̒̑͆͒́́͐̓̓͒̓͒̓̏̓̒͐̓́̓́̒͊͒͌͒͊̒́̏̒͘͘͏̵̨̡͚̬̮͔͚̭̘͙͚̭͓͙͚̪̗̭̘͚̬̗̮͙͚̭͔̘̘͚̬̮͊̓̒́̏͒́͂͊͆͋̒͑̓͑͂̏̒͂͏̘͙͏̢͚̪͖̭̹͚̩̗̭͚̩̭͇̘͚̩̰̭͐̓̒͋̓̒͊̒̏͏͙͚̹̭͉̘͖͚̫̭̭͙͔͚̭͎̘͚̪̰̮͇̭͙͚̪̮̓͒̒͊͌͂͆̒̑͌͆͘͏͚͚̬̭͈̭͙͚̤̭͔̘͙͕͚̗̮͕͙̯͚̪̤̭̘͙̩͚̩̬̮̘͙̤͚̪̬̭͓͙͚̪͖̮̘͙̓̒͆̒́́̓͐͒̓͊͒͏̴͚̩̮͓͚̪̭͓͚̹̰̭͐̒̏͊̒͐̕͏̴̨̨̨̨̡͚̮͖̘͙͚̮͕͓͇͚̫͖̭͍̘͕͚̺͚̭͓͙̱͚̹̭͉̘͙̪͚̩̮͉̭͚̬̮͉͓͙͓͚͚̭͓͚̫̭͓͙͚̭̘͚̫̭̘͈͚̰̭͔̘͚̮̓̒̓́̓͂̏̒̒͊̒̏́͒̒͑̓͋͆͂͂͌̒͌̒́̒̏͂͒͏̸̘͙͚̭͚̩̗̭͓͚̩̭͎͓͙͚̹̮͐͂͐̓̒́͌̒̈́͊̐͊͏͙͚̹̮͓͚̫͎̭̭͙͔͚̫̭͎̘͚̮͇̘͙̖͚̩̮̓͊͑̓̒͌͊̒̒́̓͆͘͏̨͚̬̮͖̘͙͚̰̭͓͚̗̭͕͓͙̯͚̪̭̓̒̓͆̓́͒̒͌́͏̴̴̘͙̬͚̩̭͇͙̤͚̭͓̫͚̪͖̮̭͙͕͚̪̭͙̩͚̪̭͙̓́̓̓̒͒͒̓̏͊̓͏͚̹̤̭͏̭͚̫̮̒͐͒͏̭͙͚̮̓́̏͏̵̨̨͓͇͚̬̤̭͍̘͙͚̭͓͙̤͚̫̰̭͉̭͙͚̭͇̘͙̥͚̬̮͉͓͙̬͚̭͙͚̫̭͍̘͙͚̪͚̭͍̘̤͚̬͎̭͈̘͈͚̩͎̭͔̘͓͚̩̤̮̒͌͂̏͊́̏́̏͑̓̓͆̒̒̒͏̸̵̸̸̴̨̨̨̘͙͖͚̮͓͙̙͚̩̗̮͕̭̺͚̩̭͍̘͙͚̹̮͕͙͚̹̭͈̘͓͚̫͎̮͎̘͙͔͚̩̗̭͎̘͙͚̩̮͇̘͙͚̩̭͓͙͚̬̮̘͙͚̤̭̘͚̫̭͓͙̯͚̪̤̭͓̘͙̬͚̪̮͖̘̩͚̩̤̭͓͙͇͚̪͖̮̘͙͚͚̺̮͓͙͚̪̭͎͓͙͓͚̹̰̭͓͙͚̫̭͎̘͙͚̗̮͓͓͇͚̫͎̭͍̘͕͚̭͓̗͚̹̭͉̭͙̤͚̬̮͉̭͙͚̬̭͂͒̒͊̐͊̓͊̒̏͋͆͑͆͒́͑̒͌͑͊̒̓͒̏͐̓̏͐͒̓́̒̒͂͊͊̒͘ͅͅ͏̵̸̡̭͚͚̭͔͓͙͚̭͈̘͙͚̮͖͚̫̭͈̘͈͚̭͔̘͖͚̬̮̒́́͂͆͂̓̒͂̒͂̏̒́̕͏̭͙͏̸̢̨͚̮͓͉͚̩̗̮͕̘͙͚̩̭͈̘͙͚̩̰̭͇̭͙͚̹̮͖͚̫̮͓͙͔͚̭͎̘͙̯͚̮͇̘͙͚̺͚̮́͒̒͒͊͒͒̓̒͊͑́̓͂̏͘͏̷̖͚̬̮͙͚̤̭̘͚̗̭̘͙̯͚̪̰̮͖͓͙̬͚̩̮͖̘̩͚̬̬̭͓̫͚̫͚̮̭͙͔͚̺̭͙͚̪̮͔͓͙̓̒͆͑̓͊́͑̒͌́͑͆̒̓̒͒̏͒̓̏͏̨͚̹̰̭͖͚̫̭͎̭͙͚͚̮͓͚̬̤̮͕͚̬̭͓͙̲͚̫̰̭͉̭͙͚̮͉̭̖͚̬̭̓̒͐͒̓͂͐̒͊͐̓̒͆͊͂̏̒ͅ͏̴̸̡̘͙͚̭͓̘͙̥͚̫̮͓͓͙͚̮͚̫̮͙͚̩̭͔̘͚̪̮́̏̓͆͂͂͑̓̒͑̓͑͊̒̏͊͏̸̘͙͕͚̪͖̭͙͚̩̗̭͇̭͙͚̩͖̭͈̘͙͚̹̭͈͓͙͚̹̭͍̘͓͚̫̗̭̭͙͔͚͖̭͎̘͙͚̮͇̘͙͚̪̭͓̘͚̬̮̭͍͚̰̭͓͙͕͚̫̮͔̭͙̯͚̪̰̭͐̓̑͒̐͊͒̒͌͂͂͂̓͌͆͑̒͆͒̒́͑͘͏̨̨̘͙̬͚̪̗̮̘̩͚̭͓͙͇͚̩̮̘͙͚̺̭͙͚̪̭͍̘͙̬͚̹̤̭̭͚̮͈̘͙͚͚̭͈̭͚̫͚̭͓͕͚̬̭͓͙̱͚̭͉̘͙̤͚̮͉̭͙̘͚̬̭͒̒͂̓̓͆͒̑̏͒̓̏͐̒̓́̓́̒͊͒̒͊͊͂͒͂̏ͅ͏̸̡̘͙͚͚̭͙̥͚̫̭̭͙͚̮͔͚̬̮͙͚̭͔̘͓͚̬̮͗́͒̓̓͊͆͂̓̒͒͑̓͑́͊̒͂͏̸̭͙͓͚̮͓͚̩̗̭̘͍͚̩̭͈͙͚̹̭̭͙͚̹̭̭͖͚̬̮͓͍͚̩̭͎̘͙͚̪͖̮͇̭͙͚̪̮͂͒̒́͋̒͊̓̐͊͋̓͒̒͂͑̒̏̈́͌͆͘͏̸̴̵̴̨̨̨̧̨͙̳͚̬̮͖̘͙̥͚̰̭̭͙͚̫̮͍̭͙̯͚̪̭̘͙̩͚̩̰̭͇̩͚̩̭͓͙͇͚̩̮̘͙͚̺̮͓͙͚̪̭͎͙͓͚̹̤̭͖͓͙͚̫̮͇͓͙͚̩̭͈̭͇͚̬̭͍̘͙͚̹͖̭͓͙̲͚̹̭͉̭͙͚̭͇̘͙̬͚̬̮͍̘͙̬͚͚̭͓̭͙͚̭͍̘͙͚̪͖̭͉̘̤͚̫̮͙͚̪̭͔̘͚̮̓͆́͒͂͒̓̒̓̏͒͑̏͐͂̏̓͒̓͆̒͌͊̓͂̏́́͂͆̒͑̓͑̏̒͐͂͒͏̸̸̸̴̴̴̸̴̡̧̢̨̘͙͙͚̪͖̮͓̺͚̩̗̮͕̭͍͚̩͖̭͈̘͙͚̹̮͕͙͚̹̭̭͖͚̬̤̮͎̘͙͔͚̪̭͎̘͙͚̮͇̘͙̖͚͎̭͓͙͚̬̮͖̭͙͎͚̰̭͔̭͚̫̮͓͙̯͚̩̰̮͙̬͚̩̮͖̘͙̤͚̗̭͓̩͚̩͖̮̭͙͔͚̪̭͚̪̮͔͓͚̹̤̭̭͚̫̮͍̘͙͚̭͇̭͇͚̬̭͍̘͕͚̬̭͓͙͚̗̭͉̘͙͚̬̮͉̭͙͚̬̮͙͚͚̭͒̒̒̐͊̓̓͒̒͂́͑̈́͆́̒͌͊͋̓͂̓̒͒͒̓̒͑̏̒͌͐̒͐͒̓͂̏̒̒͊͂͊̓͂́͘ͅ͏̸̴̡̨͚̫̮͕̘͙͚̩̗̮͔͚̫̭͈̘͙͚̩̭͔̘͖͚̩̮̓̒͆̓͆̓̒͑̒͏̘͙͏̸͚̭͚̩̗̮͕̘͚̩̭͈̭͚̩̰̭̘͙͚̹̮͓͚̬̮͎̘͙͔͚̪̰̭͎̘͙͚̫̮͇̘͙͈͚͎̮͂͐̓̒̐̒̋͊̒̏͋͊͐̓̒͂͂͊́͘͏̸̨͚̬̮̭͙͎͚̤̭͔͓͙͚̫̭̘͙̯͚̪̮͍͙̩͚̪̭͇̩͚̬̬̭͓̮͚̫͚̮̭͙̓̒͂͆͒́͂͒̓͒̓̒̓̒͒͏͚̭̙͚̪̭͎͚̹̤̭́͒͒̓̒̏̓̒̕͏̸̡̨̘͚̫̭̭͙͚͚̮͓͓͇͚̫̭͍̘͕͚̹͖̭͓͙̱͚̭͉̭͙͚̭͇̘͎͚̬̮͚͚̭͓͙̥͚̭̘͙͚̪̗̭͉̘̤͚̫̭͈̘͈͚̭͔̘͚̮̒͐͒͌̓́̒͊̒͊͂͒͂̏̒͊̓̒́͒́͂͋͆̒̒͂͒̒̏͂͂͘͏̭͙͚̫̗̮͓͍͚̩̗̭̘̲͚̩̭͈͓͖͚̩̰̮̑͒̒͋̒͊̒͏̢͓͙͚̹͖̭̘͖͚̫̭̭͍͚̪̬̭͎̘͚̩͖̮͇̭͙͈͚̩̭͓͙͚̬̭͈̘͉͚̤̭͓̭͚̗̮͌̒͒͌̒̒̑͆͑͆̒́̒̑́͘͏̸̸̸̸̴̸̴̨̨̡͓͙̯͚̪̤̮͕͓͙̩͚̩̭͇̩͚͎̭͓͙͚̪̮̘͙͚̺̮͓͙͚̪̭͎̭͙̬͚̹̤̭͕̭͙͚̮͓͙͚̮͓͓͇͚̫̮͔͕͚̫͖̭͓͚̹̭͉̘͙̥͚̬̭͇̘͙̬͚̬̮͍̘͙͚̭͓̭͚̫̭͉̘͙͚̭͈̘͚̫̭̘͈͚̭͔̘̘͚̮̓̒͂̓͊͆͒̓̏͐̏́̓̓͂̏̒͊̓̒͊̒̔͗́̏̒͑̓͆͂̒͌̒́͆̒͂͂͏̸̢̭͙͓͚̮͓͙͚̩̗̭͓̺͚̩͖̭͈͙͚̹̮͕͓͙͚̫̤̭͈̘͖͚̬̰̮͓͙͔͚̭͎̘͚̮͇̘͙̘͚̩̮͂͒͊͌̒̓͊̒͑́͊̒̑́̓͆͘͏̴̴̴̴̨̨̨̨͙͚̬̮͖̭͚̤̭̭͚̗̮͍̭͙̯͚̪̮͙̬͚̩̮͖̘̩͚͎̭͓̹͚̮̘͙͚̩̭̗͚̪̭͎̭͙͚̹̰̭͖̘͙͚̮̘͙͚̭͇̭͚̫̗̭͍̘͙͚̭͓͙͚̺̭͉̭͙̥͚̮͉̭͙͚̬̭̓͆̒̋́͑̒̑́͂͊̓̒́̓̒͂̓͒͐͒̓̒̏́͐̓́̏̒͊͌͂̏͊̓͂̏̒͏̡̘̙͚̭͓̭͚̫̮͕̘͙͚̩̗̮͚̬̮͎̭͈͚̪͚̭͔̘͓͚̩̮̒́̏̒͑̓͆͐̓̒̏̒̒͊͏̸̴̷̸̵̴̢̨̨̨̭͙͚̮͓͙͇͚̩̗̭̭͚̩̭͎̘͚̹̮͕͙͚̹͖̮͓͖͚̬̭̭͙͔͚̪̭͎̘͚̬̤̮͇̘͙͚̪̭͓͙͚̬̮̭͚̰̭͓͓͙͚̗̮͖̘͙̯͚̪̰̭͓̘͙̩͚̩̬̮͖̘͙̤͚̬̭͓͙͇͚̮̘͙͓͚̮͓͙̦͚̪̭͎͓͙̬͚̹̤̭͕͓͚̫̭͉͙͚͚̮͓͓͚̬̭͍̘͕͚͖̭͓̗͚̹̭͉̭͙̥͚̮͉̭͚̬̮͉̘͙͓͚̭͓͙͚̭͙͚̪̗̭̭̤͚̬͖̮͙͚̪̭͔̘͙͚̩̮̓͂͒͋̒͊̒̏͊̓̓̒͂͌̒̒͊͆͑͆͒̒̒́͂́͒̓͂͒́͒͐̏̒̓͒̓̓͂̒͊͆̒͂͊̒́̏̒͐́̏͒́͂͌̓͆͒̒͑̓͑̏͘͏̘͙͕͚̪͖̮͓͙͉͚̩̗̮͕̭̮͚̩̭͇͓͙͚̩̰̭͇͓͙͚̹̭͈̘͖͚̫͖̮͓͍͚̩̭͎̘͚̬̤̮͇̘͙͈͚̺͚̮͒̒͊̐̓̒͑̒̏̒̑͘͏̴̴̷̨̨̡͚̬̮͖̘͙͚̰̭͚̗̮̭͙̯͚̮͙̬͚̩̭͔̭͙̤͚̪̭͓͙͚̮̘͙͚̪̭͙͚̪̮͔͓͙͚̹̰̭͕͓͚̭͎͙͚̗̮͓͇͚̬̭͓͕͚̗̭͓͙͚̬̭͉̘͙̤͚̭͇̘͕͚̬̮͉̭͚͚̭͔̘͚̫̭͙͚̪̭͉̘͚̬̮͎̭͈͚̭͔̘͚̬̮̓̒̋͆͊́͑̓̒͌́͌͂͊͊̓͊̓͊͂̓͒̑͒̓̏͂̒͐́̓̓́͐̒͆͒̒͂͊̏͂̏̒̒͐́̒͑̓͑̓͆̓̒̏̒͂͆̒̏͂ͅ͏̭͙͏̸̴̸͚̭͙̘͚̩̗̭̮͚̩͖̭͇̘͚̩̰̭͕͙͚̺̭̭͖͚̬̭̭͙͔͚̪̭͎̘͙̯͚̮͇̘͙͚̩̭͓́͐̓͋̓̒̒̏̓͊͑̒͌͂͂͋͆͑̒͘͏̸͚̬̮̭͙̥͚̤̭͔̭͙͚̫̮͖̘͙̯͚̩̰̭͆͒́͂͏̸̴̴̸̨̨̨̡̘͙̩͚̩̭͇͙̤͚͚̭͓̬͚̪͖̮̭͙͚̩̮͓͚̪̭͚̹̰̭͕̘͙͚̫̭͓͙͚͚̮͔͓͚̫͚̮͔͕͚̭͓̗͚̭͉̭͙͚̩̮͉̭͙͚̬̮͉̭͙͚͚̭͓̭͚̫̭͓͙͚̪̗̮͓͚̬̮͎̭͈͚̪͖̭͔̘͖͚̗̮̓́̓̒͒͑͐̒͑̏͊̓̒͐͒͌̓́̒͊̓̒͂͊̒́͂́͌́̒͑̓͊͆̓̒͒̒̒͂͏̢̭͙͖͚̫̗̮͓͙͚̩̗̭͓̦͚̩̭͇̭͙͚̹̮̘͙͚̹̭̭͓͚̫͖̮͓͍͚̪͎̭͎̘͙͚̮͇̘͙͈͚̩̮͒͐͌̒͊͊͑̓͒̒͑̒̈́͂̓͆͘͏̸̴̴̴̵̴̨̨̨̡̨͚̬̮͖̭̖͚̰̭̘͙͚̫̭͓͙̯͚̪̭̘͙̩͚̩̤̮͖̘̩͚̩̭͓̩͚̮̘͙͚̪̭͚̪̮͔̙͚̹̰̭͔̘͚̭͍͙͚̩̭̘͇͚̬̤̮͔͙͚̫͎̭͓͙͚̺͎̭͉̘͙͚̮͉̭͓͚̬̮͍̘͚̭̭͙͚̫̮͓̭͙͚̩̗̮͓͚̫̰̭̘͈͚̭͔̘͚̩̮̓̒̒͆̒́͑͂͒͑̒͂̓̒́̓͒̒͒̓̒̑̏̓̒̒͐́̓̓͐̒̓͌͊͂̏̒̒́̏͑̓͆̓̒͌̒͂̒̏̕ͅ͏̸̴̷̨̨̨̨̡̭͙͖͚̪͖̭̗͚̩̗̭̘͙͚̩͖̭͈͚̹̮͖͓͙͚̺̭͉̘͖͚̫͚̮͎̘͙͔͚̪̭͎̘͚̩̮͇̘͙͈͚͎̭͓͙͚̬̮͖̘͙͚̤̭̭͙͕͚̫̮͎̘͙̯͚͖̭̘͙̬͚̩̮͖̘͙̤͚̩̭͓̩͚͎̮̭͙͚̺̭͚̪̮͔͚̹̰̭͕͓͙͚̮͖̭͙͚͚̭͍̭͇͚̬̤̭͍̘͕͚͚̭͓͙͚̹̭͉̘͙͚̭͇̘͚̬̮͚͚̭̭͙̥͚̫̭͈͓͙͚̪͚̮͖͚̬̮͈͚̭͔̘͓͚̬̮͐̓̒͋͊̓̒̏͊͊̒̓̒̒̏́͑́͆͊́͑͂͒͆̓̒́͒͐̏͒̓̒͌̏̓̒́̓͂̒̒͂͊̓́̏̒͊͊̓̒́͒̓͆̓̒͊͑̓̒́͂̒͂͘͘̕͏̘͙͚̪͖̮͓̩͚̩̗̭̭̦͚̩͖̭͎͓͖͚̩̰̮͓͙͚̫̤̮͓͚̫͎̮͎̘͙͔͚̪̰̭͎̘͙͚̫̮͇̘͙͚̪̮͑͒̒͋̒̒͒͒̓̒̓͊̔͆͘͏̸̸̴̨̨͙͚̬̮̭͚̤̭͔̘͚̫̭̘͙̯͚̪̰̮͍͙̩͚̪͖̮̘̩͚̬̬̭͓̮͚̮̭͙͚̺̭͙͚̪̮͔͓͚̹̤̭͕̭͚̫̭͍̭͙͚̩̮͓͚̫͎̭͍̘͕͚̹̭͓͙̱͚̗̭͉̭͙̣͚̭͇̘͚̬̮̙͚̭͔͚̭͓͙͚̪͖̭͈̘̤͚̫̬̭͈̘͈͚̬̭͔̘͚̪̮̓̓͆͒̒̒́̒̑͑̓͒̒̓̒͂͒͒̏͒̓̏̒̑̒̓͒̓͑̒͊̒͆͊͂͂̏̒͊͊̓̒́̏̓̒͑́͂͋͆̒̒́̒̏͊͏̸̢̨̨̘͙͚̮͓͍͚̩̗̮͕̘͙͚̩̭͈͓͙͚̩̰̮͙͚̹̭͈̘͖͚̫̮͎̘͍͚̪̭͎̘͙͚̫͚̮͇̘͙͚̺͚̮̓́͒̒̏͊͒̓͒̒̒̋͘ͅ͏͙̦͚̬̭͈̭͙͚̰̭̓͆̏́͏̸̨̨̨̨̨͚̫̮͕̭͙̯͚̭͖̘͙̩͚̩̮͖̘̩͚̬̬̭͓̫͚̪̰̮̘͙͈͚̮͓͙̦͚̪̭͓͚̹̤̭͖͓͙͚̭͉͙͚̭̭͚̬̬̭͍̘͕͚̹̭͓͙̱͚̫̭͉̘͙̦͚̩̭͇̘͙͚̬̮͍̭͚̭͔͓͙̥͚̫̭͓͙͚̪̭̭̤͚̬̮͈͚̭͔̘̘͚̫̰̮̓̒͌͂͊͆̒̓̒͒́͒͐̏͊̒͐́̓̓͂̏͌̒͊̒͊͆̒̑́̏̓͊͆̓͑̒͒͑̓̒́͂̒ͅ͏̸̸̴̵̢̨̨̘͙͙͚̫̗̮͓͙͍͚̩̗̭͓͙̗͚̩͖̭͇̘͙͚̩̰̭̘͙͚̺͖̭̭͖͚̬̭͈̭͙͔͚̭͎̘͙͚̮͇̭͙͚̺͚̭͓͙̹͚̬̮͖̭͉͚̤̭͓̭͙͕͚̗̮͎̭͙̯͚̩̤̮͙̬͚̩͎̭͔̭̩͚̗̭͓̫͚̮̭͙͚͚̭̖͚̪̭͚̹̤̭͖͓͚̫̭͉͓͙͚̮͔͓͚̬̬̮͕͚̬̭͓͙͚̭͉̭͙̣͚̭͇̘͙̩͚̬̮͉͓͚͚̭͓͙͚̮͓͙͚̩̗̮̤͚̫̤̮͙͚̭͔̘͙̥͚̮͒͌͋͒̒́̏͂̏͑͆̒́́͋̓̒́̓̒͂͒́͒͒̓̒̏͊̓̒̑̒͐͒̓́̏̒͊͐̓̒́͊́͂́̏̒͌́͒́͂͒͆͐̓̒͑̓͑͂͊͂͂͘ͅ͏̸̴̨̨̨̡̨̭͙͚̪͖̮͓͙̙͚̩̗̭͓̮͚̩̭͍̘͙͚̹̭͖̘͙͚̹̮͖͓͚̬̤̮͓͙͔͚̪̭͎̘͚̫͚̮͇̘͙͚̩̭͓͎͚̬̮̭̖͚̤̭̘͙͕͚̫̭͖̘͙̯͚̪̰̮͖͓͙̩͚̩̰̭͇̩͚̬̰̭͓̹͚͎̮̘͙͚͚̺̮͓͚̪̭͎͙͚̹̤̭͕͓͚̫̮͇̭͙͚̗̭͈̭͚̬̮͔͙͚̫̭͓͙̲͚̺͎̭͉̭͙̤͚̩̭͇̘͙͈͚̬̮͉̭͚̭̘͙̥͚̭͍͙͚̪̮͚̬̭͈̘͙͚̹͎̭͔̘͙͚̫̮̒͒͌̒͊̐͊͊̓̒͑̓̒̒͋͆͑̒͆͒̒́͒̓̒̓̒́͒̏͐̒̋̏̓̒̓͒̓́̒͊͆̓͌͊̒́̏͑́͂̓͆̓͒̓̒̏͑͆͘͘͏̘͙͕͚̪͖̮͓͙͎͚̩̗̭̭̮͚̩̭͈͚̩̰̭͇̭͙͚̺̭͉̘͖͚̬̰̭͈̭͍͚̪̭͎̘͙̯͚̮͇̭͙̖͚̪̮͒͋̒͊̓̒̏͊̒̒͆́̓͆͘͏͚͚̬̮͖̭͙͚̰̭͔͓͙͚̗̭̘͙̯͚̩̰̭͖̘͙̬͚̩̮͖̘͙̤͚̪͖̭͓͚͎̮̭͙̓̒͆̓́͂́͑͆̓̒͂́͒͏̴̨̨̨͚̪̭͙̫͚̪̭͎͓͚̹̰̭͕͚̭̘͙͚͚̭͉̭͚̫͎̭͍̘͙͚̺͖̭͓̗͚̺̭͉̘͙̪͚̭͇̘͚̬̭͒̓̏̒͌̓̒͐́͋̓͂̒͊͌͊̒́̏̒͒͏̵̘͚̭͓͓͙͚̫̮͙͚̮̤͚̬̗̭̘͙͚̹̤̭͔̘͚̩̤̮̒́̏̓͑̓͆͂͂͒̓̒͌͑̒̏͘͏̨̡̘͙͈͚̪͖̮͓͙͖͚̩̗̭͙͚̩̭͎̭͙͚̹̮̭͙͚̺͖̭̭͓͚̫̭͈̭͙͔͚̪̰̭͎̘͙̮͚̫͚̮͇̭͙͚̺͚̭͓͙͚̬̮̭͙̩͚̤̭͔̘͙͚̗̮͒͋̓̏͊̐͊͒͒̒̔͑͆͒́͂́͘͏̴̴̴̸̵̸̨̨̨̡̨͓͙̯͚̪̰̭͓̘͙̬͚̩̮̘̩͚̭͓̫͚̩͖̮̭͙͚̩̭͙͚̪̭͍̘͙͚̹̤̭͖̘͚̫̭͍͙͚̭̭͚̫͚̭͍̘͕͚̺̭͓͙͚̹̭͉̭͙͚̮͉̭͖͚̬̮͚͚̭͓͙͚̫̮͖͓͙͚̭͓̭͚̫̰̭͈̘͙͚̪̭͔̘͓͚̩̤̮͒̒͂̏̓̒͒͐͒̓̏̒̓͒̓̓́̏͌̒͊̒̏͊͆́̏̒͊̓̒͌́͒̓͆͂̒͑̒͏̘͙͙͚̫̗̮͓̯͚̩̗̭̘͙͚̩̭͇̭͚̩̰̮͒̒͋͒͊̒̏͏̘͙͚̺͖̮͔͓͚̫̮͓͍͚̪͚̭͎̘͙͚̮͇̘͙͚̪̮̓̒̓͑̒͂͂̓͋͆͘͏̸̴̴̨̨͚̬̮͖̭͚̤̭͚̫̮̭͙̯͚̪̭̘͙̩͚̩̭͔̭̩͚̭͓̬͚̫͚̮̘͙͕͚̪̭͚̪̮͔͓̙͚̹̰̭͔̘͚̭͈͓͙͚̩̮̓̒̏͆̒͑́͑̓̒̑͌͐͆̒͂͒̓̒͒͒̓̒̓̏̒̒͐́̓͏̴̨̨̨̡͓͚̫̮͔͕͚̬̭͓͙̱͚̫̭͉̭͙̣͚̩̮͉̭͎͚̬̮͙͚̭͚̭͓͙͚̩̗̮͔͚̫̭̘͈͚̭͔̘͚̫̮̒͊̏̓̒̏͊̏̒͊̓́̏͑̓̒͆́͂͌͆̓̒͌̒͂̏̒̏͆͏̢̭͙͚̪͖̮͓̹͚̩̗̭̭͙̗͚̩͖̭͈͓͙͚̹̮͑͒̒͋͊͏̘͙͚̺͖̮͕͓͚̫̮͎̘͙͔͚̪̬̭͎̘͚̪̮͇̭͙͉͚̪̮̓̒͒̒̒͆͆͘͏̸̸̸̴̵̨̨̨̨̡͚̬̮͓͙͚̰̭͔͚̫̭͖͙̯͚̪̮͈͙̬͚̩̮͖̘͙̤͚̗̭͓͚̮̘͙͚̪̭͙͔͚̪̮͔͓͔͚̹̰̭͚̮͓̘͙͚̮͔͓͇͚̫̭͓͕͚̺̭͓̗͚̬͖̭͉̘͙̪͚̩̮͉̭͚̬̮͍̭̙͚͚̭̘͙͚̫̭͎͙͚̩̭̭͚̫̤̭͈̘͙͚̪̭͔̘͓͚̮̓̒͌͆͒͊́̓̒͌̓̓́̓̒͂́͒̓͒̓̏̒͐̓̒͐́̓͂̏̒͊͒̒̓͊̒̒͐̒́͑̓̓͆̓͑̒͑̏̒͂͂͏̸̭͙͚̭͙͈͚̩̗̮͕̭͚̩̭͈͖͚̩̰̮͙͚̹̭͈̘͓͚̫̭͈̭͙͔͚̪̭͎̘͙͚̫̮͇̭͙͚̺͚̭͓͚̬̮̭͙̩͚̤̭͔͓͙͕͚̗̮͔̭͙̯͚͖̮͓͙̩͚̪̭͇̩͚͎̭͓͙͇͚͎̮̘͙͚̭͙͚̪̭͎͚̹̰̭̐́͐̓̒̋͊̓̒͐̓͒̒͊͆̓͊̏͑̒͋͆͒́́͂͐͒̓̒͂̓́͒͗́͒͒̓́̏̓̒͘͘͏̴̨̨̨̡̨̡̘͙͚̭͇͓͙͚͚̭͉̭͇͚̫̭͓͙͚̫̬̭͓͙͚̹̭͉̘͙̹͚̮͉̭͙͚̬̮͍̭͙͚̭͓͓͚̭͙͚̪̗̭̘͚̬̮͎̭͈͚͖̭͔̘̘͚̗̮́̓́̒͊͒͌͊͂̏͂́̏̒͆́͂͌̓͆͌̒͊̒͂̒͂͏̴̨̘͙͖͚̪͖̭̹͚̩̗̭̮͚̩͖̭͎̘͚̹̭͈̘͙͚̫̰̭͓̭͓͚̬̬̭̭͍͚̩̭͎̘͚̮͇̭͙͍͚̩̭͓̥͚̬̮̘͉͚̰̭̘͚̗̮͕͓͙̯͚̪̭̘͙̩͚̩̭͇͙̤͚̪̤̭͓͙͚̪̮̘͙͚̪̭͚̪̮͔͚̹̤̭͐̓̒͋̓̒̒̏͊̒͌̒̓̒̑͂̓͆͑̒͆͒̒́͒̒̑́͒͆̓̓͊͆͒͒͒̓̒͐̏̓̒͌͘͏̨̘͚̮͉̭͙͚̮̒̓́̓͂̏͏̴̴̵̨̡͓͚̬̬̮͙͚̫̭͓̗͚̭͉̘͙̤͚̬̮͉̭͚̬̮͉͓͚̭͔̭͙͚̫̭͈̘͙͚̪̗̮͚̫̬̭̘͈͚̩̤̭͔̘̘͚̗̮̒͊͐̓͌͊̒͂͒̒̔̒́̏̓͆͑̓̒͌̒̒͂͘͏̴̸̴̴̴̴̨̨̨̭͙͓͚̫̗̭̰͚̩̗̭͇̭̮͚̩̭͎͓͙͚̩̰̮͖͓͙͚̫̤̭͈̘͓͚̫̮͎̘͙͔͚̬̭͎̘͚̫͚̮͇̘͙͚̩̭͓͙̩͚̬̮͓͙̹͚̰̭͓͙͚̫̭͖͙̯͚̩̰̮͇͙̬͚̩̮̘̩͚̩̭͓̮͚̪͖̮̭͙͚̩̭̗͚̪̭͚̹̤̭͖͓͚̫̮͕͙͚͚̮͔͓͚̫̭͓͙͚̭͓͙͚̫̭͉̭͙̥͚̮͉̭͙͈͚̬̮͉͓͙͓͚̭͔͚̫̭͍̭͙͚̪͖̭̘̤͚̬̭͈̘͙͚̪̭͔̘͙̥͚̮͐̓̒̒͊̐̒̒̒͌͆͑͆͒́͒͂̓̓͒̒͆̓̒͒͒͒̓̒̏͊̓̒̑̒͐͒̓̓́̒͊͒͒͌͂͊̏́̏́̏̓̒͆̓͆͋̒͊͑͂͂͘͏̘͙͏͚̫̗̮͓͙͈͚̩̗̭̦͚̩̭͍̘͖͚̩̰̭͓͙͚̫̤̭̘͓͚̫͖̭͈̭͙͔͚̩͚̭͎̘͙͚̮͇̭͙͚̩̮͒͋̓̒͊̒͋͊̒͂̓͊͆͘ͅ͏̸̴̴̨̨͙͚̬̮̭͙͚̰̭͔͓͙͚̫̭͓͙̯͚͖̮͖͓͙̩͚̩̬̮̘͙̤͚̭͓͙͇͚̩̮̘͙͚̪̭͚̪̭͎͓͙͓͚̹̤̭͕͚̫̭͎͓͙͚̭͎̭͇͚̬̬̮͔͙͚̺̭͓͙̱͚̬͖̭͉̭͙̪͚̬̭͇̘͉͚̬̭̓͂͆͒̏́͂͑͂͒́̓͆͒̒͒̓̒̏̓̒̓͒̓͂̏̒̓͌͊͊̒͘͏̵̭͚͚̭͔͙͚̭̘͙͚̪̭̭̤͚̬̗̮͎̭͙͚̩̤̭͔̘͙̥͚̬̮̒́̓́͂͌͆̓͒̒͑̏̕͏̸̨̭͙͚̭̙͚̩̗̮͕̘͙͎͚̩̭͉͖͚̩̰̭̭͙͚̫̰̭͈̘͓͚̬̭͈̭͍͚̪̭͎̘͙̯͚̮͇̭͙͍͚̪̮̓́͐̓̒͊̓̒͊̒͂̒͊͂͆͘͏̸̷͉͚̬̮͖̘͚̰̭͔͓͙͚̫̭͖͙̯͚̮͓͙̬͚̩̮͖̘͙̤͚̩̭͓͙͚̮̭͙͓͚̭͙͚̪̭͎͚̹̰̭͖̭͚̫̭͍͙͚̗̮̓̒͆̒͑́͂̓͂͊͐͂̓̓͊́̓͒́͒͒̓̏̓̒̑̒͐͒̓̓́͏̨͓͚̬̬̮͔͙͚̺͖̭͓̗͚̹̭͉̘͙̣͚̮͉̭͎͚̬̭̒͊̓͌͊̒̓͂̏̒͏̡̭̙͚͚̭̭͙̥͚̫̭͙͚̪̗̮͕͚̫̬̮͎̭͙͚̺̭͔̘͚̩̤̮̒́͑̓͑̓͆̓̒͑̏̒̏͏̸̴̴̴̴̡̨̘͙͚̭͙̘͚̩̗̭͓̺͚̩͖̭͈͓͙͚̹̭͓͓͙͚̫̰̭̘͓͚̫͚̭͈̭͙͔͚̩̭͎̘͙͚̮͇̭͙͚͎̭͓͚̬̮̘͙̹͚̰̭͚̗̮͇͙̯͚̪̤̮͍͙̩͚̩̭͇̩͚̤̭͓͙͚̫̮̘͙͚̪̭͙͚̪̭͓͚̹̤̭͓͚̫̮͓̘͙͚͚̮͓͚̫̮͙͚̺̭͓̗͚̺͎̭͉̭͙͚̭͇̘͙͚̬̭͒͂͐̓͌̒̐͊͋̒͊̓͂̓̓́͑̒͂͆͒́͒̓̒̑́̓̓̓̒́̓͊͊͒̒͒̓̏͊̒͌͐̒̓͒̓́͑̒͊̏͐̓͌͊̒͂͂̏͘͏̸̸̴̨̘͚͚̭͓͚̫̭͍͓͙͚̮͖̤͚̫̭̘͙͚̪̭͔̘͓͚̪̮̒̑́͑̒͆̓͆͂̓̒͌͑̒͏̸̴̨̭͙͚̫̗̮͓͚̩̗̭̭̦͚̩̭͇̘͚̹̭̘͙͚̺͖̮͖͚̫̮͓͍͚̪̬̭͎̘͚̫͚̮͇̭͙͍͚̪̭͓͚̬̮͖̭͙͎͚̤̭͓̭͚̫̭͖͓͙̯͚̪̰̭̘͙̩͚̩̮̘͙̤͚̫̭͓͙͇͚̩͖̮̘͙͗͒̒͆͋̒͊̒̏͊͋͐̓̒̏͑̒̒̑͆͑̒͆́̒͌͐͒̓͒͘̕͏̴̴͚̪̮͓͙̰͚̪̭͎͓͙͓͚̹̰̭͕͚̫̭͉͓͙͚̩̮͐̏̓̒̓͒̓͏̨̨̧̨̨̡͓͚̫̭͓͙͚̫͎̭͓̗͚̺̭͉̭͙͚̩̭͇̘͙̮͚̬̮͍̭͙̬͚̭͔͓͚̭͍̭͙͚̩̮͚̬͚̭͈̘͙͚̩̤̭͔̘͚̬̮̒͊͒͌͊̒́̏̒͑́͂͆̓͒̓̒͑̒͐̏͏̘͙͚̪͖̮͓̺͚̩̗̭̭͍͚̩̭͇͖͚̹̭͓̘͙͚̺̮͕͖͚̬̮͎̘͙͔͚̩͚̭͎̘͚̩̮͇̘͙͚͎̮̒͒̒͋̒͊̓̒͊͊̓̒͆̒̑͆́͘̕͏̸̴̨̨̨̨̨̡͙̲͚̬̮͖̭͚̤̭̘͚̗̭͓͙̯͚̩̤̮͙̬͚̩̭͔̭͙̤͚͎̭͓͚̮̘͙͚̩̭͙͚̪̭͎͓̙͚̹̰̭͖͓͙͚̭͍͙͚͚̭͍̭͚̫̗̮͔͕͚͎̭͓̗͚̬̭͉̘͙͚̩̮͉̭͙̱͚̬̮͍̘͙͓͚̭͔̭͚̭̘͙͚̩̭̭͚̬͖̮͎̭͙͚̺̭͔̘͓͚̬̮̓͆̒̒́͑̒͌́͑͊̓͆͂̓̒͂́͒̓͒̓̐̏̒́̓̓͂̒͊̓̒͂͊̒̏́̏̒͆́͂͑͆̓͒̒͑̏̒͂͏̸̘͙͈͚̮͓͙͚̩̗̭͇̘͙͚̩̭͈̘͖͚̩̰̮͙͚̹̮͔͓͚̫̮͓͙͔͚̪̤̭͎̘͙͚̫̮͇̘͙͚̩̭͓͚̬̮̭͙̩͚̤̭͔͓͚̗̭͂͒͒̏͊̒͑̓͊̓̒͒͑̓͊̔͆͑̒̔͆͒́̒͌́͘͏̴̴̴̨̨̡̨̨̡̭͙̯͚̪̤̮͈͙̩͚̪̭͇͙̤͚̪̭͓̬͚̮̭͙͚̪̭͙̬͚̪̮͔͓͚̹̤̭͖͚̮͇̘͙͚͚̭͍̭͇͚̫̮͔͕͚̹̭͓͙͚̫͖̭͉̭͙͚̩̭͇̘͙͚̬̮͍̭͚̭͔͙̥͚̭͉͓͙͚̪̭̘͚̫̭̘͈͚̭͔̘̘͚̫̮̓̏̓̓̓̒͂͒̒͒̓̏̒͐̓̒͐́̓́̒͊̓̒͒͊̔̒͐́̏̓́͂͆̓͌̒͂͌̒́̒͆͏̸̭͙͚̮͓̘͚̩̗̮͕̘̦͚̩̭͇̭͚̩̰̭͐͂͒̒̒͊̒̏͏͙͚̫̰̮͓͚̬̬̭̭͍͚̩̭͎̘͚̩͖̮͇̘͙̙͚̺͚̮̓͑̓̒͌̒̏̒̒͘͏͙̺͚̬̭͈̘͙͚̤̭͓̭͙͕͚̗̭̓͆͊́́͏̴̷͓͙̯͚̪̤̮͎͙̩͚̩̬̭͇͙̤͚̪̭͓̮͚̪̮̘͙͕͚̪̮͓͙͚̪̭͓͚̹̰̭̓̓̏̓̒͆͒͐̏͊̒̑͏̴̴̸̨̡͚̫̭͍͓͙͚͚̭͖̘͇͚̫̮͕͚̫̬̭͓͙̱͚̫͖̭͉̘͙̣͚̬̮͉̭͙͚͚̬̮͙͓͚̭̭͚̫̭̭͙͚̪̮͔͚̫̭̘͈͚̭͔̘͕͚̫̮̓̒̓͒̓͂̒͊͐̓̒͊͊̓́̏͒̒͑̓͋͆̓̓̒͌̒́̒͆͏̴̢̭͙͓͚̪͖̭͙͍͚̩̗̭͇̭͍͚̩͖̭͈̘͙͚̩̰̭͈̭͙͚̺͖̮͔͓͚̬̮͎̘͙͔͚̫̭͎̘͚̫͚̮͇̘͙͍͚͎̮͐̓̒̓̒͒̒̑́͘͏̴̘͚̬̮͖̘͚̰̭͓͚̗̮̭͙̯͚͖̮͇͙̬͚̩̭͔̭͙̤͚̭͓͚̫͚̮̭͙͖͚̩̭͙̮͚̪̭͓͙̓̒͆̒̒́͑̒͌́͌͂̓͂́̓̓̒͂͒͒̓̏͊͏͚̹̰̭͏̸̴̨̨̭͙͚̫̭͎̘͙͚͚̮͔͓͇͚̬̮͕͚̭͓͙̱͚̫̰̭͉̭͙̦͚̩̭͇̘͓͚̬̭͒̓́̒͐̓̒͂̏͊̒͏̘̙͚͚̭̒́͏̵̴̴̡͙͚̫̭͓͙͚̪͚̭̘͚̬̮͎̭͙͚̭͔̘͓͚̪̮̓̓͋͆͊̒̏͑͂̒͏̸̸̴̸̴̸̵̴̡̡̨̘͙͓͚̮͓͍͚̩̗̮͕̘͚̩̭͍͓͖͚̹̮͕͙͚̹̮͔͓͚̬̰̮͓͙͔͚̪̭͎̘͙͚̩̮͇̭͙͚̩̭͓͙͚̬̮̘͙͚̰̭͙͕͚̗̮͇͓͙̯͚̮͍͙̩͚̩̮̘͙̤͚̬̭͓͚͎̮̘͙͚͚̩̮͓͙͚̪̮͔͓͚̹̤̭̭͙͚̫̮͖̘͙͚̮͔͓͇͚̬̤̮͙͚̺͚̭͓͙͚̹̭͉̭͙͚̮͉̭͙͚̬̮͉̘͚͚̭͔͓͙͚̭͓͙͚̪̗̭͓̭̤͚̬̮͎̭͙͚̹̭͔̘͖͚̮͂͒̒̒̋͊̒͊̓̓̓̒͑̓͆͌͆͑̓͆͒́͑̓́͂͊̓͒̓̓̒͂͂͒͐̈́̏̒͌͐͒̓͂̏̒͐̓͌͊́̏́̒́́͂͊͆̒͆͑̒͂͒͘͘ͅ͏̸̸̨̭͙͚̪͖̮͓̖͚̩̗̮͕̘̮͚̩̭͈̭͙͚̩̰̭͙͚̹̭̘͓͚̬̮͎̘͍͚̩͖̭͎̘͙̯͚̮͇̭͙͚̪̭͓͚̬̮͖̘͚̤̭̘͙͚̫̮͕̘͙̯͚̮͈͙̬͚̩̬̭͔̭̩͚͚̭͓̹͚̬̤̮̭͙͔͚̭͙͚̪̭͎͚̹̤̭̐͒̒̒͊̐͊̓̓͋̒̒͂͆͑̒͆͆̒͑́͑͂͂͊̓̒͂̓̒͒́͒͒̓͂̏̓̒͐͘̕͏̸̷̵̴̨̨͓͙͚̫̭͎̘͙͚͚̮͓͇͚̫͚̭͍̘͙͚̹̭͓͙͚̺̭͉̘͙̦͚̭͇̘͚̬̮͍̘͚̭͔̘͙͚̫̭͙͚̪̗̭͉̘̤͚̫̮͙͚̩̭͔̘̘͚̬̮͒̓͂͐̒͌͆͊͂̏̒̋̒͌́̏̓͒̓͆̒͑̓͑͆̒͂͏̸̸̴̴̴̨̨̨̘͙͕͚̭͙͚̩̗̭͇̭͙͎͚̩͖̭͇̘͙͚̹̭͈̘͙͚̺͖̭̘͓͚̬̮͎̘͍͚̫̭͎̘͙̯͚̮͇̭͙͚̺͚̭͓͚̬̮̭͙͚̰̭͓͙͚̗̮͖͓͙̯͚̪̤̭͕̘͙̩͚̩̮͖̘̩͚̬͖̭͓̩͚̬̤̮̭͙͚̪̮͓͖͚̪̭͓͙͚̹̰̭͕̘͙͚̫̮͓͙͚͚̭͈̭͚̬̭͍̘͙͚̫͖̭͓͙͚̬͖̭͉̭͙̹͚̭͇̘͙̣͚̬̭́͐̓̔̐͊͋̒̒͒́̓̔͑̒͆͒̓́͑͂́͂̒̓̒͒͒͐̒̏͊͗͒̓̓́̒͊͌͊͂̏͘͏̡̭͙̰͚͚̭̘͚̮͓͓͙͚̭͓̭͚̬͖̮͈͚̩̬̭͔̘͓͚̪̮́͑̒͑́͂͆͂͂̒͑̓̒̒͊͏̘͙͚̪͖̭͙͚̩̗̭̘͙͚̩̭͇͓͖͚̹̭͓͓͙͚̹̭̘͓͚̫̮͓͍͚̪̬̭͎̘͙͚̪͖̮͇̭͙͚̺͚̮̒͐̓̋͋͊͊̒͊͒͌̒͒͑̒̔͘ͅ͏̸̴̴̨̨͚̬̮͖̘͙̹͚̰̭̭͙͕͚̗̮͖̭͙̯͚̪̤̮͓͙̩͚̩͎̭͇̩͚̩̭͓̬͚̫͚̮̭͙͚̩̮͓͙̬͚̪̭͎͚̹̰̭͖͚̮̭͙͚̩̭͉̭͇͚̬̤̭͍̘͙͚̹͖̭͓͚̬͖̭͉̭͙̪͚̮͉̭͙̙͚̬̭̓̒͑͆́͒́͐̓̒̓̒͒̒͐̏̓̒͐̓̒͐́͐̓̒͌͊̒̔͂̏͏̵̸̡̘͚͚̭͓̭͙͚̭͍͓͙͚̪͚̭͍̘͚̬͖̭̘͈͚̹̭͔̘͚̮̒́́͂͆̒͌̒̒͐͂͒͘͏̨̭͙͚̪͖̭͙͈͚̩̗̮͕̘͙̗͚̩͖̭͉͖͚̹̮͖̭͙͚̺͖̮͖͚̬̤̮͎̘͙͔͚̪̭͎̘͚̫̮͇̘͙̖͚͎̮͒͐̓̓̒͊͑̓̒̒̑͊́͘͏̸̨͙͚̬̮͖̘͙͎͚̰̭͓͓͚̫̮͍̘͙̯͚̪̮͈͙̬͚̩̬̭͔̭̩͚̬͎̭͓͚̪̮̘͙͚̺̭͖͚̪̭͎͓͚̹̤̭̓́͆́̒̑̓̒̓̒͂͆͒͗̏͒̓̒̏̒͘͏̨͚̭͍͙͚͚̮̓̒̓́̓̓͂͏̷̨̨̨͓͇͚̬̰̭͓͕͚̹͚̭͓͙͚̭͉̭͙͚̩̮͉̭͙͚̬̮͙̰͚͚̭̘͙̥͚̫̭͉̘͙͚̪͚̮͖̤͚̫̭͈̘͙͚̺̭͔̘͙̥͚̪͚̮̒͒̒͊͂͒͆́͊̓́͒̓͆̓̒͑̏͏̸̘͙͙͚̮͓͙͖͚̩̗̭̭̺͚̩̭͈̭͚̹̮͖̘͙͚̫̰̭̭͓͚̬̮͎̘͙͔͚̗̭͎̘͙̮͚̫̮͇̘͙͚̪̭͓͙͚̬̮̘͚̤̭͓͓͚̗̭͓͙̯͚̪̰̭́͒͋̒͊̒̏͊͑̒͂͂͊̓͆͑͂͆͒̒̒́̒͌́͒͘͏̸̴̴̴̨̨̨̡̘͙̩͚̪̗̮͖̘̩͚̭͓͙͚̮̘͙͚̪̭͙̫͚̪̭͎͙̬͚̹̤̭͙͚̫̮͓͙͚͚̮͓͓͇͚̬̤̮͕͚̬̭͓͙͚̭͉̭͙̤͚̩̮͉̭͙͚̬̮͍̭͙̰͚͚̭͙̥͚̭͉̭͙͚̮͔͚̬̮͙͚̹̰̭͔̘͚̩̮̒́̏̓͊͂͒̑͒̓̏̓͐̓͒͐̓́̒͐̓̒͊́͂͌́͒̓́͂͆͂͂̓̒͆͑̓͑̒̏͊͏̨̨̭͙͚̪͖̮͓͙͚̩̗̭̘͙͚̩̭͈̘͚̹̭͈͓͙͚̹͖̮͖͖͚̫̭͈̭͍͚̪̭͎̘͚͎̮͇̭͙͚̩̮͐͒͋̏͊̒̏͊̓̒̒̒̒͂͊͆̕͘͏̸̗͚̬̭͈̘͚̰̭͓͙͚̫̮͍̘͙̯͚̪̤̭̓̒͆̒̋́͒͂͏̸̸̴̸̨̢̨̨̘͙̩͚̩̮͖̘̩͚͎̭͓͚̮̭͙͚̪̮͓͙̹͚̪̭͎̭͚̹̤̭͕͙͚̮͖̘͙͚̮͔͓͇͚̫̮͔͙͚̭͓̗͚̬̭͉̭͙͚̩̭͇̘͙̣͚̬̭̒͂̓̒͂͂͒͐͐̏̒̓́̓͂̏̒̏̓͌́͂͊̒̏̕͏̘͙͏̸̴̡̨͚͚̭͓͚̫̭͎̭͙͚̭͉̘͚̫̭̘͈͚̭͔̘̘͚̪͚̮́͒̒͑̓͆͂̒͌̒́̒͏̸̸̭͙͚̮͓͉͚̩̗̭͇̭̖͚̩͖̭͈̘͚̩̰̮̘͙͚̫̰̮͓͖͚̬̭͈̭͙͔͚͖̭͎̘͚̮͇̘͙͚̩̮͒́͒̒̒̒̏͑̓̒͆́̒̒͂͌͆͘͏̸̴͚͚̬̮͓͙͚̤̭̭͙͚̫̭͕̭͙̯͚̩̰̮͙̬͚̩̰̮̘̩͚̩̭͓͚̫̮̭͙͚̪̭͙̫͚̪̭͎̭͚̹̤̭͖͚̫̮͇̭͙͚͚̮̓̒͆͒̓́͑͂͋̓͒̒͂̓̒͂͊͒͒͒̓̏̒͐̓̒͐͒̓́͏̸̡̨͓͚̫̗̮͕͚̭͓͙͚̹̭͉̭͙̥͚̮͉̭͉͚̬̭̒͊͐̓̒͂̏͊͂̏̒͏̸̘͙͚̭͚̫̭̭͙͚̪͚̭̭̤͚̬̭̘͙͚̭͔̘͓͚̫̮́̏͑̓̒͑̓͋͆͑̒͆͌͑͂͂̒͆͏̸̸̸̨̨̘͙͚̭̩͚̩̗̭͓̮͚̩̭͍̘͙͚̹̮͕̘͙͚̫̤̭̘͓͚̬̤̮͓͙͔͚̪̭͎̘͙͚̮͇̭͙͚̩̭͓͚̬̮̭͙̹͚̰̭͓͓͚̗̮͓͙̯͚͖̮͕͓͙̩͚̩̭͔̭͙̤͚̭͓̹͚̪͖̮̘͙͚͚̺̮͓͙̮͚̪̭͎̙͚̹̤̭͕̭͚̮͔͓͙͚̭̐͂͐̓̒͌̒͊̐͊͊̒͑̈́͂͊͆͑̒͑͆͒́̒͌́͊͂́͆̓̒͒̏͐̏̓̒̒̓́̓͂̏͘͏̸̨̡̨̨̘͚̬̭͍̘͙͚̬̗̭͓͚̬͖̭͉̭͙̥͚̮͉̭͚̬̮͉͓͚̭͚̭̭͙͚̭͉̘͚̬͖̮͈͚̩̭͔̘͙͚̫̮̒͊͆͌͊̒̔́̏̒͐̒̑́̏͒̓̒͆́͂͊͆͂̒͑̓̒͆͏̸̭͙͚̮͓̙͚̩̗̭̘͙͎͚̩̭͈͓͚̹̮͖̭͙͚̫̰̭͍̘͖͚̫̭͈̭͍͚̪̰̭͎̘͙͚̪̰̮͇̘͙͈͚̺͚̮̐͂͒̒͋͊̒̏͊̒͊̒̓͘͏̸͚̬̮͖̘͉͚̤̭͓͙͚̗̮̭͙̯͚̩̰̭͖̘͙̬͚̩͎̭͇͙̤͚̪̬̭͓̮͚̫͚̮̭͙͔͚̺̭͙̳͚̪̮͔͓͙͚̹̤̭̓̒͋͆̒́͑͂́͊̓̓̒͒̏͒̓̏͏̨̨̨̨̨̡̭͙͚̭͙͚͚̭͖̘͇͚̫̭͍̘͕͚̫̬̭͓̗͚̹̭͉̘͙͚̩̮͉̭͈͚̬̮͉̭͚̭͔͚̫̮͙͚̮͚̫̮͎̭͈͚̭͔̘͚̪͚̮́͋̓̓͂̒͊̒͊̒̓̒̒͐́̏̓̒͆̓͒̓͆͂͂͒̓̒͂̒́͂̒̏͏̸̨̘͙͕͚̮͓̘͚̩̗̮͕̘̦͚̩͖̭͈͓͙͚̹̭͇̭͙͚̹̭͍̘͓͚̬̤̭̭͙͔͚̩̭͎̘͙̯͚̮͇̘͙͇͚̩̮́͒̒̒̐͊̓̒͌͊͂͆͘͏̶̵̸̴͙͚̬̭͈̭͙͚̰̭͓͙͚̫̭͖͙̯͚̭̘͙̩͚̩̬̭͇͙̤͚͚̭͓͙͚̫̮̭͙͖͚̩̭͙͚̪̭͙̓͆́͒͂̓͂͊͐̓́̓͊͊͒͒̓͂̏͊̓͏̴̴̸̴̨̡͚̹̤̭̭͚̫̮̭͙͚̮͓͇͚̬̮͔͕͚̫̭͓͚̬̰̭͉̭͙͚̬̭͇̘͙̱͚̬̮͉̭͙͚͚̭͔͓͚̫̭͍̭͙͚̮͔͚̫̮͙͚̩̬̭͔̘͙̥͚̮͐̒͐͒͐̓́̏͐̒͆̓̒͊̒̔̈́́̒͑̓͆͂͂̓̒͑̓͑́͂͏̸̭͙͚̮͓͚̩̗̮͕̘̲͚̩̭͈͖͚̩̰̮͗́͒̒̒͊̓̒ͅ͏͙͚̹̭͈̘͖͚̬̮͓͍͚̪͎̭͎̘͚̬̤̮͇̭͙̘͚͎̮̓̓̒͆͑̒̒̒́͘͏̸̸̸̴̴̵̨̨̡̨̗͚̬̮͖̭͙͚̤̭͓̭͚̫̮̭͙̯͚̮͓͙̩͚̩̭͇̩͚̭͓͙͇͚̮̭͙͚̩̮͓͙̹͚̪̭͎̭͙͓͚̹̰̭͖͚̫̭͈̭͙͚̩̮͕͓͚̫̮͙͚̺͖̭͓͚̬̰̭͉̭͙͚̩̭͇̘͙͚̬̮͍̘͚̭̘͙͚̭͓͙͚̩̗̭̭̤͚̫̤̮͙͚̪̭͔̘͚̮̓̒͆̓́̒͌͌͂͊͐̓̒͂͒̓͂͒̓͐̏̓̒͐͒̓̒͊͒͐̓͌͊̒̔̒́̏͑́͂͋͆͒̒͑̓͑̏̒̏́͒̕͏̸̵̘͙͙͚̮͓͙͉͚̩̗̮͕̭͙͖͚̩͖̭͇͓͚̩̰̭͉̭͙͚̺̭̘͓͚̫̗̭͈̭͙͔͚̪̤̭͎̘͙͚͎̮͇̘͙͉͚̩̭͓͙͚̬̮͖̭͙͚̤̭̭͙͚̗̭́͒̒̏͊͊̒̈́́͆͑͆͆́͒͂́͘͏̴̨͓͙̯͚̪̮͍͙̩͚̪̗̭͔̭͙̤͚̩̭͓͙͇͚̮̭͙͚̩̭͂̓͆̓͂͒̐͒̓̒͏̵̨̨̡̧̨̨̨͚̪̮͔͓͙͓͚̹̰̭͓͙͚̭͇͓͙͚̗̭͉̭͇͚̬̮͔͕͚̬̭͓͙͚̹̭͉̘͙͚̩̭͇̘͇͚̬̮͚̭͔̘͙͚̫̭͈̘͙͚̪͖̮̤͚̬̭̘͈͚̭͔̘͓͚̮̏͐́̓́̒͆̓̒͒͊̓̒͊̓̒́̏̓͆͑̓̒̏͌̒́̒͂͂̕͏̸̸̢̭͙͚̭͙͚̩̗̮͕̘͙͎͚̩̭͈͓͙͚̹̮͖̘͙͚̫̰̭̭͓͚̬̭̭͙͔͚̪̭͎̘͙͚̫̮͇̭͙͚͎̮̑́͐̓͌͊͊͑̒͂͌͂͊̏́͘͏̸̴̴̸̨̨̡͙͚̬̮̭͙̩͚̰̭̘͚̗̭͖̭͙̯͚̮͇͙̩͚̪̮͖̘̩͚̭͓̮͚̮̘͙͙͚̺̭͙͚̪̭͎͚̹̤̭͕͚̫̭͓͙͚͚̮͓͓͚̬̮͕͚̬̭͓͙͚̫̭͉̭͙̣͚̩̮͉̭͙͚͚̬̮͉͓͙͚̭͓̘͙̥͚̭̭͙͚̪̭̘͚̬̮͙͚̹̭͔̘̘͚̩̤̮̓̈́͆͒́͒̒̑́͂͊̓̏̒́͆̓̒́͒̏͒̓̏̓̒̓̒͐͒͌̓́̒͊͂͐̓̒͆͊̏́̏́͂͌͆̓͊̒̓͑̓͑͊̒̕͏̸̘͙͚̭͙͉͚̩̗̭̘͙͖͚̩͖̭͎̭͚̩̰̭͕͓͙͚̹̮͖͚̫̮͎̘͍͚̭͎̘͚͎̮͇̭͙͉͚̩̮̓͂͐̓͋̒̏͊͒̓̒̓̒͂̓̒̒͂͆͘͏̸̸̸̨͙̺͚̬̭͈̘͙͚̰̭͓͚̫̮͕͙̯͚͖̭̘͙̩͚̩̭͔̭̩͚̬̭͓̮͚̪̰̮̭͙͚̮͓͙͚̪̭͎̭͙̰͚̹̤̭͓͙͚̮͓͓͙͚͎̭̓͆̏́͑̒͌̓͂͐̒̓̓̒͒͗́͒͐́̏͐́̓́͏̴̴̴̴̨̘͚̬̬̭͍̘͕͚̹̭͓͚̬͖̭͉̘͙̣͚̭͇̘͕͚̬̮͉͓͙͚̭͔̘͚̮͔̭͙͚̪̗̮̤͚̫̬̮͙͚̹̭͔̘̘͚̪̮̒͊̒͊̒̔͂̏̒́̏̒͑́͂͆͐̓̒͑̓͑̒͏̸̨̘͙͚̭͚̩̗̮͕̘͙͚̩͖̭͉͙͚̹̮͓̘͙͚̫̰̮͓͓͚̫̭̭͙͔͚̫̭͎̘͙͚̩̮͇̘͙͚̪̮̑͂͐̓̒́͊̓̐͊̓̒͌͒͆͆͘̕ͅ͏̸͙̣͚̬̮͓͙̹͚̤̭̭͚̫̭̓͆͒́͑̒͌͏̸̴̴̴̵̴̨̡͙̯͚̩̤̭͓̘͙̬͚̩̭͇̩͚̩̤̭͓͙͚̪̰̮̭͙͈͚̪̭͙̲͚̪̮͔͙͚̹̤̭͕̭͚̫̮͈̘͙͚͚̮͔͓͇͚̬̭͓͕͚̺̭͓͙͚̫̭͉̘͙͚̭͇̘͚̬̮͉̘͙͚͚̭͓̭͙͚̫̮͖͓͙͚̩̮͔͚̫̮͙͚̭͔̘͙̥͚̮̓̓̒̓͊͒͒̓̏̓͗̒̓͒̓́̒͆͒̒͊͆͂̏̒͌͗́̓͆̓̓̒͑̓͑͂͂͂͂ͅ͏̸̸̨̘͙͚̮͓͙͚̩̗̭͙̗͚̩̭͎̭͙͚̹̭͖̘͙͚̹̭͈̘͓͚̫̭͈̭͙͔͚̪̭͎̘͙͚̪͖̮͇̭͙͚̩̭͓͉͚̬̮̘͚̤̭̭͙͚̫̭͓͙̯͚̪̤̭̐͂͒̔͋̓͊̐͊͊̒͒͊͆͑̒͆͒̒͑́͒͂͑͘ͅ͏̸̴̵̨̨̨̨̡̘͙̩͚̩̮̘̩͚̪̭͓̫͚̮̭͙͚̺̮͓͙͚̪̭͎͓͙͚̹̤̭͓͚̭͙͚̗̭͉̭͇͚̬̮͕͚͚̭͓͙͚̫̰̭͉̘͙͚̭͇̘͚͚̬̮͉̭͚̭̘͙͚̫̮͓͓͙͚̪̗̮͓͚̬̭͈̘͙͚̩̤̭͔̘͙̥͚̗̮͆͒̒̏̓̒͂͒͒̏͐̏͂͐̒̓́͋̓̓́̒͐̓̒͂͊̓͂̏̒̒́̏͑̓͆̓̒̓͑͂͘͏̸̭͙͚̮͓͚̩̗̭̭̦͚̩̭͉͚̹̮̭͙͚̹̭͈̘͖͚̬̭͈̭͙͔͚͚̭͎̘͙͚̪͖̮͇̭͙͚̩̮̒́͒̒͋̒͊̓̒̏͊͒͒̒͂́̓̓͆̕͘͏̸̶̸̴̨̡̨̨̡̨͚̬̮͖̭͙̹͚̰̭͔͓͙͚̫̮͓͙̯͚̪̤̮͕͓͙̩͚̪̗̮̘͙̤͚̪̭͓̹͚̩͖̮̘͙͚̭͙͚̪̮͔͙͚̹̰̭͕̭͚̮̭͙͚̗̭̘͇͚̫̮͙͚̺̗̭͓͙͚̬̰̭͉̘͙̣͚̭͇̘͙͚̬̮͍̘͙͚͚̭̘͙̥͚̫̮͙͚̮͔͚̫̮͈͚̹̭͔̘͚̪̮̓̒͆́͂͐͒̏̓̒͒̓́͒͒̓̏̓̒̓́͑̓́͐̒͊͐̓͌͊͂̏͂́͒̓͑̓͆͂͂̓̒͑̓̒̒̏͊̕͏̸̢̘͙͈͚̮͓͙͖͚̩̗̮͕̘̺͚̩͖̭͈͙͚̩̰̮́͒̒̓͏̸̸̸̡̭͙͚̹̭̘͓͚̫̭̭͍͚̫̭͎̘͚̮͇̘͙͚̪̭͓͚̬̮̘͙̩͚̰̭͓͓͚̗̮͖̘͙̯͚̪̤̮͎͙̬͚̪̗̭͇͙̤͚̩̭͓̫͚̮̘͙͚̭͙̰͚̪̭͍̘͙͚̹̰̭̓͊̒͊͌̒͂̒̑́̏͆͑̒͆͒́̒͌́̓̓͆̓̒́͒͗́͒͒̓̏͘͏̸̴̸̨̨̭͙͚̫̭͍̘͙͚͚̭̭͇͚̬̮͕͚̺͚̭͓͙͚̹̭͉̭͙͚̭͇̘͙̭͚̬̭͒̓́͌̒͐̓̒͊͂́̏͏̴̘͚̭͔̘͙̥͚̮͔͓͙͚̩̭̭̤͚̫̭̘͙͚̪̭͔̘͓͚̪͚̮̒͌́̏́͂͆̓͑̒͌͑͆̒͏̭͙͚̪͖̮͓͙͚̩̗̭̘̦͚̩̭͈̭͚̹̭͙͚̫̤̭͈̘͓͚̫͖̭͈̭͍͚̪̗̭͎̘͚͎̮͇̭͙͚͎̮͗͒̐͋̒͊̒̏͊͐̓̒̒̒̒́́͘̕͏̸̴͈͚̬̮͓͙͚̰̭͔̘͙͚̫̮͇̭͙̯͚̭͖̘͙̩͚̩̰̮͖̘̩͚̪̰̭͓̬͚̫̮̘͙͖͚̩̭͚̪̭͎̭͙͓͚̹̤̭̓̒͆͒̒́͂͂͊̒̓̒͊͒͒̓̒̏͘͏̸̴̴̴̨̨̨͓͙͚̭͇͙͚̩̭͖̘͇͚̬̤̭͍̘͙͚̭͓͚̬̭͉̭͙͚̬̭͇̘͙̬͚̬̮͉͓͔͚̭͙̥͚̮͖̭͙͚̩̗̮̤͚̫̰̮͈͚̬̭͔̘̘͚̬̮́̓̓̒͌͂͊̒̔̏̒́̏͒̓́͂͆͐̓̒͑̓̒́̒́͏̭͙͚̪͖̭͚̩̗̮͕̘̖͚̩͖̭͈̭͖͚̩̰̭͕̘͙͚̹̭̘͓͚̫͖̭̭͍͚̬̭͎̘͚̪̰̮͇̭͙͇͚̩̮͑͐̓̒̏̒̒͒͋̒͌̒͂̒̑͆͘͏̸̴̴̸̸̨̨̨͙͚̬̮͓͙͚̰̭͔͚̫̭̭͙̯͚̩̰̭̘͙̩͚̪̗̮͖̘͙̤͚̩̤̭͓͙͚̪̰̮̘͙͚̩̭͕͚̪̮͔͓̙͚̹̰̭̭͚̭͎͓͙͚͚̭͍̭͇͚̫̭͓͙͚̫̭͓͚̭͉̘͙̪͚̬̭͇̘͔͚̬̮͍̭͙͚͚̭͓͙̥͚̫̭͎͙͚̪͚̭͉̘̤͚̫̭̘͙͚̩̭͔̘͙̥͚̬̮̓͆͆͒͊́̓̒͌͒͑̓͊͒̓͒̓̒̏̒͐̒͐́̓͂̒͊͒͌͊̒̔͂͒̒́͒̓̓͆̒͂͌͑͂͏̘͙͚̪͖̮͓̩͚̩̗̮͕̘͙͚̩̭͉͚̹̮͑͒̒͊͊̓̒̏͊͏̴̸̴̴͓͙͚̹̭͉̘͓͚̬̮͓͍͚̭͎̘͙̮͚̫̮͇̘͙͈͚̩̭͓͙͚̬̮̘͙͚̰̭̘͚̗̭͖̭͙̯͚̮͍͙̩͚̪̭͇̩͚̭͓̩͚̪̰̮̭͙͚̪̭͙͚̪̭͎͓͚̹̰̭͊̒͂͑̒́͒͊͆͑͆͒̒́͒̒̑́͂͊̓̏̓̒́̓̒͒͐͒̓̏̒͘͘͏̨̨̨̨̨̘͙͚̭͇͙͚̭̭͚̫͎̭͓͕͚̭͓͙̱͚̗̭͉̭͙̤͚̭͇̘͙͚̬̮͉͓͙͚̭̘͚̮͖͙͚̪̗̮͖̤͚̫̭̘͙͚̭͔̘͕͚̩̤̮́̓̓́̏͌̒͊͒̒́͂͊͂͂̏̔́̏͒̒͑́͂̓͆̓̒͌͑́͆̒͏̘͙͓͚̪͖̮͓͙͚̩̗̮͕̭͙͚͚̩̭͈̭͙͚̩̰̮͓̘͙͚̹͖̮͖͚̬̮͓͍͚̪͖̭͎̘͚̪̰̮͇̭͙͚̪̮͒̑͊̐͒̓̒͂͑̒̒̑͌͆͘͏̸̸̴̨̨̨̧̨̡̨͙̲͚̬̭͈̘͉͚̰̭͓͚̫̮͈͓͙̯͚̪̭̘͙̬͚̩̮̘̩͚̭͓̫͚̮̘͙͚̺̮͓͙̬͚̪̭͓͚̹̰̭̭͚̮͔̘͙͚̮͕͓͇͚̬̤̭͓͙͚̫̭͓͚̬̭͉̘͙͚̬̮͉̭͚̬̮͍̘͚͚̭͓͚̫̭͎̭͙͚̭͍̘͚̫̬̭̘͈͚̭͔̘͚̮̓͆̒́͒̒̑͒͒̒́̏̓̒͂̓͒͐̏͐̏͊̒͐̒̓́̓͂̏̒͒͌͊̒̔̏̒̔̒̑́͑̒͑̓͆͂͂̒͌̒́̒̏́͂͘͏̨̘͙͚̪͖̭͙͚̩̗̭͇̘̲͚̩̭͎͓͙͚̹̮̭͙͚̫̤̭̘͖͚̫͎̮͎̘͙͔͚͎̭͎̘͚̮͇̘͙̘͚̩̭͓̣͚̬̮͖̭͍͚̰̭͓͙͕͚̗̮͍̭͙̯͚̩̤̮͙̬͚̩̤̭͇̩͚̩̭͓̫͚̪͖̮̭͙͐͐̓͌̒͊̐͊͐͋̒́̒̑͂͆͑̒͆̒́͒́͋̓̓̒͆̓̒͒͘͏͚̭͙̫͚̪̭͙̬͚̹̰̭́͒͒̓̏͊̓͏̨̨̨̨͙͚̮͕̘͙͚̮͔͓͚̫̭͍̘͕͚̬̭͓͙̱͚̫͖̭͉̘͙͚̮͉̭͚͚̬̭̓́̓́̏̒͊̒́͊͂̏̒ͅ͏̘͚͚̭̘͙̥͚̮̘͙͚̪͖̭̘̤͚̬̭̘͙͚̪̭͔̘͙̥͚̬̮̒́͒́͂͑͆͋̒̓͌͑͒͂͘͏̸̸̘͙͖͚̮͓͙͚̩̗̮͕̘͙͎͚̩̭͎̘͖͚̹̮̘͙͚̫̰̮͔͓͚̫̭̭͙͔͚̪̗̭͎̘͚̮͇̭͙̖͚͎̮͂͒͋͊̒͊͐̓̒̓͌̒̒͂́͘͏̨̩͚̬̭͈̭͚̰̭͙͚̗̮̘͙̯͚̪̰̮͇͙̩͚̩͎̮̘͙̤͚̭͓̮͚̫̮̭͙̓̒͆̒͑́͑̓͂́͊̓͒́̓̒͊͒͏̴̸̨̡̨̨͚̩̭͚͚̪̭͎͙̬͚̹̤̭͕̭͚̫̭͇̘͙͚̮͓͓͚̫͖̭͓͙͚̹̭͓͙̱͚̺͎̭͉̘͙͚̮͉̭͖͚̬̮͉͓͚̭̭͚̭͉̭͙͚̪̗̮͓͚̫̭̘͙͚̩̭͔̘͙̥͚̮͒̓̒̏̓̒͐͒̓͂̏̒͊͒͌͊̓́̏̒̒́̏͑̒͑́͂͆̓̒͌͑͂͒͘͏̭͙͚̫̗̮͓͚̩̗̭̲͚̩̭͈͖͚̩̰̭͇̭͙͚̫̰̭͉̘͖͚̫͎̮͎̘͍͚̩͖̭͎̘͙͚̩͖̮͇̭͙͚̩̮̐͒̒͋̓̒͊̓̒̒̒̓͆̕͘̕͏̶͙͚̬̮͙͎͚̤̭͓̭͙͚̗̮͍͙̯͚̪̤̮͖͓͙̬͚̩̬̮͖̘͙̤͚̬̭͓̮͚̮̘͙͖͚̺̮͓͚̪̭͎͓͚̹̤̭̓͆͑̓́͂́̓͊̓̒́̓͒̏͐̒̑̏̒͌͏̸̨̨̨̨̘͙͚̫̮͉̭͙͚͚̭͖̘͚̬̮͔͕͚̫̭͓͙̤͚̺̭͉̘͙̪͚̩̮͉̭͚͚̬̭͒̓͂̒͊̓̒͒͊̒͏̵̭͔͚͚̭̘͙͚̫̭͙͚̪̗̭͈̘̤͚̬͎̭̘͈͚̪̗̭͔̘͕͚̪̮̒́͑̓͑̓͆̒͌̒̒͊͏̭͙͏̸̨͚̭͙͇͚̩̗̭͇̘͚̩͖̭͈͙͚̹̭͇̭͙͚̹̮͕͓͚̫̗̭̭͙͔͚̪̭͎̘͚̬̤̮͇̘͙͚̩̮́͐̓̒̈́̓̐͊̓̓̒͌̒̑̏͆͘͏̷̸̴̴̴̵̸̨̨̨̨͙͚̬̮̭͚̤̭͔̘͙͕͚̗̮͈̭͙̯͚̪̤̮͎͙̬͚̪̗̮̘͙̤͚̭͓̬͚̬̤̮̭͙͚̪̭͚̪̭͚̹̤̭̭͚̫̮͔͓͙͚̩̮͔͓͇͚̬̮͔͕͚̫̭͓̗͚̺͎̭͉̭͙͚̩̮͉̭͙͚̬̮͉̘͙͚̭͔͙͚̫̭͍̭͙͚̮͖̤͚̫̭̘͙͚̭͔̘͖͚̬̮̓͆͒̒̒́́̓͒́̓̒͒̒͒̓̒̋̏͊̓̒̑͐̒͐͒̓̒͆̓̒͊̒͆̏́̏̓̓͆͂̓̒͌͑́͂̒̏͏̸̴̢̭͙͖͚̮͓̬͚̩̗̮͕̭͙͚̩̭͇͓͙͚̩̰̮͕̭͙͚̺͖̮͖͚̬̭͈̭͍͚̩̗̭͎̘͙͚̪͖̮͇̘͙͚̪̮͂͒̒̏͊͐̓̒̒̏͆͘ͅ͏̸̴̨͎͚̬̮͓͙͚̤̭͔͚̫̮͎͙̯͚̪̰̭̘͙̬͚̪͚̮͖̘͙̤͚̰̭͓̩͚̮̘͙͚̪̭͙͚̪̭͎͓͚̹̤̭̓̒͆͒̒́̓̒̑̓͐͂̓̒͂͒͒͒̓̒̏̒͘͏̸̴̴̨̨̡̘͙͚̫̭͇̭͙͚̩̮͖͓͇͚̬̮͕͚̬̭͓͙͚̬͖̭͉̭͙̪͚̮͉̭͓͚̬̮͉͓͙͚̭͓̭͙̥͚̫̮̭͙͚̪͚̭͍̘͚̬̭̘͈͚̭͔̘̘͚̪͚̮͒̓̒͂͐̓̒́͊́̏̒́̏̓͒͆̒͆͌̒́͒̒͏̘͙͚̪͖̭͍͚̩̗̭̭̖͚̩̭͎͓͚̩̰̮͓͙͚̹̭̘͓͚̫̮͎̘͙͔͚̭͎̘͙͚͎̮͇̭͙͚̪̮̒͐̓̒͋̒͊̒̏͒͒͌̒̏͂͒̓́͋͆͘͏̸̸̴̴̵̸̨̨̡͙͚̬̮͓͙͎͚̤̭̭͚̫̭͖͙̯͚̩̤̭͓̘͙̬͚̩̬̮͖̘͙̤͚̩̭͓̬͚̮̘͙͚̪̭͚̪̮͔͓͙͚̹̤̭͚̭͎̭͙͚̭͍̭͚̫̮͔͕͚̭͓̗͚̺͎̭͉̘͙̦͚̬̭͇̘͈͚̬̮͍̭͚͚̭̭͙͚̭͔̭͙͚̮͚̬͖̮͙͚̹̤̭͔̘͖͚̮̓͆͒́͑̒͌̓͂̓̒͂͒̐͒̓̒͐̏͗͐̓̒͐́̓͂̏̒͊̏̓̒͂̓͊̒̒̒́͑́͂͆͂͐̓̒͑̓͑̒́͂͘ͅ͏̸̵̘͙͓͚̮͓͚̩̗̭͇̘͙͚̩͖̭͇͖͚̹̮͓̭͙͚̹͖̮͖͚̬̰̮͓͙͔͚̪̗̭͎̘͙͚̪̮͇̭͙͚͎̭͓͙͚̬̮̭͙͚̤̭͔͚̗̭͖͙̯͚̭͂͒̒̋̏̓̒͊͑̓̒͑͂͆̏́͑͆͆͒́̓̒͌́̓͂͊͘͏̘͙̩͚̪͖̮͖̘͙̤͚̩̭͓͙͇͚̪͖̮̭͙͚̺̮͓͚̪̭͙̓̓͒̓̏͐̒̒̏͊̓͏̴̴̸̨̨̨͚̹̰̭͙͚̫̮͙͚̭͇̭͇͚̫̮͔͕͚̬̭͓͙͚̹̭͉̭͙̥͚̩̮͉̭͙̰͚̬̭͐̓͒͑̓̓́̏̒̏̓̒͊͏̡̭͙̬͚̭͓̘͚̭͎͓͙͚̮͚̬̮͎̭͈͚͎̭͔̘͕͚̩̮́̏̒͆́͂͆͂͂͑̓̒̓̒́̒͊͏̴̸̴̴̴̨̨̨̘͙͚̪͖̭͙͚̩̗̭͙͚̩̭͈̭͙͚̹̭̘͙͚̫̰̭͉̘͖͚̫̭͈̭͙͔͚̭͎̘͚̮͇̭͙͚̪̭͓͙͚̬̭͈̭̖͚̤̭͓̘͚̫̮͍̘͙̯͚̮͈͙̩͚̩̭͇͙̤͚̩̬̭͓͚̩͖̮̘͙͚̩̮͓̘͚̪̭͓͚̹̰̭͖̘͚̭̘͙͚͚̮͖͓͇͚̫̭͓͕͚̺͎̭͓͙͚̬͖̭͉̘͙̣͚̬̭͇̘͙̬͚̬̭̓͐̓͒͋̓͒͊̐͊͋̒̏͂̒̒͂̏͆͑́͆̒́̒̑͂͊̓͂̓̓̒͂͒͑͐̒̏͊̒͌̒͐́͋̓͂̒͊͒̒͊͘͏̵̡̘͙͚͚̭̘͙͚̫̮͕͓͙͚̪̗̮͚̫̤̭͈̘͈͚̭͔̘͕͚̫̰̮͗́͑̓͆͐̓̒̒͂͂̒͏̸̘͙͚̭͙͓͚̩̗̮͕̘̺͚̩̭͎͓͚̩̰̭͇̭͙͚̫̰̭̘͖͚̬̭͈̭͍͚̗̭͎̘͙͚̪͖̮͇̘͙͚̩̮̑́͐̓̒͊̒̏͋̒͆̒͂͋͆͘ͅ͏̴̸̴̨̨͎͚̬̮͖̘͙̥͚̤̭̭͙͕͚̗̮͎͙̯͚͖̮͙̩͚̪͚̭͔̭͙̤͚̭͓͚̪̮̭͙͈͚̩̭͙͚̪̭͎̭͙̬͚̹̰̭͓͙͚̭̭͙͚̩̮͔͓͇͚̬̮͔͙͚̭͓̗͚̬̰̭͉̭͙̪͚̩̭͇̘̓̒͆́͑́̓͂͋̓́̓̓̒͂͆͒͒̓̈́̏͐́͌̓̒͆̓͌́͂͊̒̒͏̨͚̬̮͉̘͚͚̭͓͚̮͓͙͚̩̮̤͚̬̗̭̘͙͚͎̭͔̘͖͚̬̮̒́͑̒͆́͂͑͆̓͑̓̒͌͑́̒͂̕͏̸̨̘͙͖͚̮͓̗͚̩̗̮͕̘͚̩̭͎̭͙͚̹̮͙͚̫̤̮͔͓͚̬̭͈̭͙͔͚̪̰̭͎̘͙͚̮͇̘͙͚̩̮͂͒̒̒̋͊̐͊͐̓̓̒͂͂͊͆͘ͅ͏̵̸̴̸̸̢̨̨̡̨͙͚̬̮̘͙͚̰̭͙͕͚̗̮͓͙̯͚̪̤̮͖͓͙̬͚̪̮̘͙̤͚̬̭͓̮͚̮̘͙͙͚̮͓͙̩͚̪̭͍̘̙͚̹̤̭̭͚̫̮͖̭͙͚̗̭͇̭͚̫͚̭͍̘͕͚̬̭͓͚̬̰̭͉̭͙̥͚̬̭͇̘͙͚̬̮͉̘͙͚͚̭͓̭͙̥͚̭͎͓͙͚̭̘͚̫̭͈̘͈͚̰̭͔̘͙͚̬̮̓͆͒́͑̓́͐͊͒͒̓̒͂̓͒́͒͐̏̒͐̒̓͒̓́̒͊̒͊̒̔̒́́͂͆͂͋̒̒͂́͏̨̘͙͕͚̪͖̮͓͙͚̩̗̭͙͚̩͖̭͇͖͚̹̮̘͙͚̹̮͓͖͚̫̮͓͍͚̗̭͎̘͙̯͚̮͇̭͙͚̪̮͒͑͋̓̏̓̒͊͒̓̓̒͊͑̒͂͂͊͆͘͏̸̨̨͚͚̬̮͖̭͙͎͚̤̭͓̭͙͕͚̗̭͓͙̯͚̭͖̘͙̬͚̩̭͔̭̩͚̭͓̹͚̮̭͙͔͚̭̖͚̪̭͎͚̹̤̭̭͙͚̮͍̘͙͚̮̓̒͆́́͐͂͊͂̒͂͊̓̒͂͒́͒͒̓̒̏̓̒̑͐́̓͂̏͏̵̸̨̨͓͇͚̫͖̭͍̘͙͚̫̭͓͙̤͚̫̭͉̭͙͚̩̭͇̘͚̬̮͉̘͚͚̭͔̘͙͚̫̮͙͚̮͓̤͚̫̮͈͚̪̭͔̘̘͚̮̒͌͊͊͆̒̋̒̑́̓͑̓͆͂̓̒͂͑̓̒͒̒́͂ͅ͏̴̴̴̴̵̨̨̨̡̘͙͈͚̪͖̭͙̘͚̩̗̭͇̭̲͚̩͖̭͈͓͚̹̭͇̭͙͚̺̮͓͖͚̬̰̮͎̘͙͔͚̩̭͎̘͙͚͎̮͇̭͙͚͎̭͓͙̥͚̬̮̭͙͚̰̭͓͓͚̗̮͍̭͙̯͚̪̤̭͕̘͙̩͚̩̮͖̘̩͚̤̭͓͙͚̫̮̘͙͚̪̮͓͓͚̪̭͓͚̹̰̭͖͙͚̫̭͙͚͚̮͖͓͚̫͚̭͍̘͕͚̺̭͓͙͚̬͖̭͉̭͙͚̬̮͉̭͕͚̬̮͙͚͚̭͓͙͚̫̭͎͙͚̩̭͓̭͚̬̮͈͚̹̭͔̘͓͚̮͐̓̒̒̏͊͊̓̒͒̓́̋́͑͆͒͊́̒̑́͆̒͂̓͊͊͒͗͐̒̏͊̒͌̓͒͋̓̓́̒͊̒͊͆̒͊̓́͑̓̓͆̓̒͒͑̓̒͊̒́͂͘͏̭͙͏͚̫̗̮͓͙͚̩̗̭̘͙͚̩̭͉͚̩̰̮͒̐͋͊͊̓̒̏͏͙͚̫̤̭͈̘͓͚̫͖̭͈̭͙͔͚̬̭͎̘͙͚̫͚̮͇̘͙͚̩̮̓̒͂̈́̏͆͘͏̴̸̨̨̨̨̡̘͚̬̮͖̘͙͎͚̰̭͔̘͙͕͚̗̮͖̘͙̯͚̪̭̘͙̩͚̩̮̘͙̤͚̬̭͓̬͚̪̰̮̘͙͚̩̮͓͙̮͚̪̭͎͓͔͚̹̰̭͖͓͚̮͕͓͙͚̩̭͎̭͇͚̫̭͓͕͚̫̭͓͙̲͚̺̭͉̭͙̦͚̭͇̘͙̬͚̬̮͍̘͚̭̘͙̥͚̭͎̭͙͚̩̮͓͚̬̭͈̘͈͚̪̭͔̘͚̬̮̓̒͆́́͒͆͒́̓̒͒͒͐̏̒̒̓́̓͆̒͊͒̒͂͊͂̏̒̑́̏͑́͂͆̓̓̒͊̒̒̏́͏̸̵̸̴̴̸̴̡̨̘͙͙͚̭͙͈͚̩̗̭͇̘͙͚̩͖̭͈̭͙͚̩̰̭̘͙͚̺͖̭͓̭͖͚̬̤̮͎̘͙͔͚̪͖̭͎̘͚̪̰̮͇̘͙̘͚̺͚̭͓̥͚̬̮͖̭͙͚̰̭͓͓͙͚̫̮̘͙̯͚̩̤̭̘͙̩͚̪̗̭͔̭͙̤͚̩̭͓͚̪̮̘͙͚̩̮͓̗͚̪̮͔͔͚̹̤̭͓͚̫̭͇̭͙͚̭͍̭͇͚̬̰̭͓͙͚̬̭͓͙͚̗̭͉̘͙̦͚̬̭͇̘͍͚̬̮͍̘̙͚͚̭̘͙̥͚̫̮͖̭͙͚̩̮͔̤͚̫̤̭̘͙͚̩͎̭͔̘͙̥͚̮́͐̓͊̐͊̒̒̑͑̒͆́͂͌͑̓̒͂͆͒̑͐̒̏̓̒͐̒͐͒̓͂̏̒͒͌͊͂̒̒́͒̓͆̓̓̒͌͑͂͂͘͏̸̸̢̘͙͚̮͓͚̩̗̭̭̺͚̩̭͈̘͖͚̹̮͖̘͙͚̹͖̭͓̭͖͚̬̰̮͓͙͔͚̩̭͎̘͚̮͇̭͙͚̺͚̮͑́͒̒͋̒͊̒͊̒͑̒̒́̓̏͘͏̢̨͚̬̭͈̭͙͚̤̭͔͙͚̗̭̘͙̯͚̪̰̭̘͙̬͚̩̬̮̘͙̤͚̩̭͓̩͚͎̮̘͙͚̭͚̪̮͔͙̬͚̹̰̭̓̒͆̒́̓͂́͑͐͒̓̒́͒̒́͒͒̓̒͌̏̓͏̴̴̨̨̡̨̘͚̫̮͔̭͙͚̩̮͔͓͇͚̫̭͍̘͕͚̹̭͓̗͚̫͖̭͉̭͙͚̬̮͉̭͙͚̬̮͙͚̭͔̭͙̥͚̫̭͓͙͚̭̘͚̬͎̭͈̘͈͚̰̭͔̘͙͚̮̒̓͒̓̒̒͊͊̒͆̓͊̓͗́̏̓͒͆͂͂͌̒̒́͂͂͏̸̢̘͙͔͚̮͓͙͚̩̗̭̘̮͚̩͖̭͍̘͙͚̩̰̮͖͓͙͚̹͖̮͕͖͚̫̭͈̭͍͚̭͎̘͙͚͎̮͇̭͙͍͚͎̮́͒̏͋̒̓̒͒̒́͂͂́͘ͅ͏̡̖͚̬̮̘͙͚̤̭͔̘͙͕͚̗̭̓̒͆͒́́͏̴̴̨̨̨̭͙̯͚̪̰̮͇͙̬͚̪̭͔̭͙̤͚͖̭͓̹͚̮̭͙͙͚̩̮͓͙͚̪̭͙̬͚̹̤̭͔̘͚̮͓͙͚͎̭͍̭͚̬̰̭͍̘͕͚̺̭͓͙̱͚̺̭͉̘͙͚̬̮͉̭͚̬̮͚̭͔̭͚̮͕̭͙͚̪͚̭͍̘̤͚̬̗̭̘͈͚̪̗̭͔̘͕͚̮̓͒́̓̒͂̓͒͐͐̏͊̓̒̓́͑̓́̒͊̒͒͊̈́̒͋͊̓̒̑́̏̒͆́͂͆̒͌̒̒́͒͏̸̶̨̘͙͚̭͚̩̗̭͓͙͚̩͖̭͎͚̩̰̭̘͙͚̫̤̭͉̘͓͚̫̭͈̭͍͚̪̭͎̘͙͚̮͇̘͙͚̺͚̮͗͂͐̓̒͌̏̓̒̏͊̒̏̒̈́́̓͘̕͏̸̡̥͚̬̭͈̘͙͚̰̭̭͙͚̗̮͍͙̯͚͖̮͙̬͚̩͎̮͖̘͙̤͚̭͓̹͚̮̭͙̓̒͆́͒͂́̓͂͋̓͂͊̓̒́͒͏̴̸̴͚̩̮͓͎͚̪̮͔͓͚̹̤̭͖͙͚̫̭͇͙͚̩̭͐̒̏̒̓͒̓̓̕͏̴̴̨̨̘͇͚̬̭͓͕͚̹̭͓̗͚̭͉̘͙͚̭͇̘͙̳͚̬̮͉̘͔͚̭͔̘͚̫̭̘͙͚̩̭͍̘̤͚̬͚̮͙͚̭͔̘͙͚̩̮̒͆͒̒͒͊̒́͂̓́̏̒́̏̒͆̓͑͆̓̒͑̓͑͂͏̸̴̴̡̨̡̨̭͙͚̪͖̭̫͚̩̗̭̘͙̗͚̩͖̭͇͓͙͚̩̰̮̘͙͚̹̮͓͚̫̭̭͙͔͚̭͎̘͚͎̮͇̭͙͚̩̭͓͚̬̭͈̭͙͚̤̭͓͓͙͕͚̗̮͉̭͙̯͚̮͖͓͙̩͚̪̭͔̭̩͚̩̭͓̮͚̫͚̮̭͙͖͚̪̮͓͚̪̭͎͙͚̹̤̭͖̭͚̫̮͇̘͙͚̩̮͔͓͚̫̭͍̘͕͚̬̭͓͙͚̺͎̭͉̘͙̹͚̮͉̭͔͚̬̮͉̘͚̭͓͙̥͚̮͓͙͚̪̗̮͕͚̬͖̮͈͚̪̰̭͔̘͙͚̮̑͐̓̒͋̐͑͊͑̓̒̓͌́̒̒͂͆͑̒̐͆́́͂͊̏̒̓̓̒͒͐̒͌̏̓͗̒͐͒̓͆̒͊̓̒́͊́̏̒̒́̏͒́͂͐͆̓̒͑̓̒͂͒͘̕̕͏̨̭͙͚̫̗̮͓͚̩̗̭̦͚̩̭͇̘͚̩̰̮̭͙͚̺̮͖͚̫̗̮͓͙͔͚̭͎̘͚̩̮͇̭͙̖͚͎̮̐͒̒̑͋̓̒͊̒̏͑͊͒̓̒͑͂̒̒͆́͘͏̵̴̴̸̷̴̴̨̨̨̨͙͚̬̮͓͙͚̤̭͓͙͚̗̮͓͙̯͚͖̮͖͓͙̩͚̪̮͖̘͙̤͚̬̬̭͓̹͚̫͚̮̘͙͚̩̭͙͓͚̪̭͎͙͚̹̰̭͕͓͙͚̮͓͙͚̗̭͉̭͚̬̮͔͙͚̺̭͓͙͚̬̰̭͉̘͙͚̮͉̭͙͚̬̮͉̘͙͚͚̭̘͙̥͚̭̭͙͚̪̗̭̘̤͚̬̮͈͚̰̭͔̘͕͚̩̮̓͆͒̏́͒͂́͐͂͒̓̒͒̒͒̓̏̓́̓̓́̒͊̓͌͊̈́͂̏͌́͒́͂͊͆͊̒͆͑̓̒͂̒͏̸̸̸̴̵̴̢̡̨̢̨̡̘͙͖͚̮͓̫͚̩̗̮͕̘͙͚̩͖̭͍̘͚̩̰̮͖̭͙͚̹̭̭͓͚̫͖̭̭͍͚̫̗̭͎̘͙͚̮͇̭͙̘͚̪̭͓͚̬̮͙͚̤̭͔͓͙͕͚̫̮͕͙̯͚͖̭͓̘͙̬͚̪͚̮͖̘͙̤͚̭͓̬͚̫̮̘͙͚̭͙͚̪̭͙̰͚̹̤̭͓͚̭͎͓͙͚͎̭͎̭͚̫̗̭͍̘͙͚̺̗̭͓͙͚̫̭͉̘͙̦͚̭͇̘͙͚̬̮͉̭͚͚̭͔̘͙͚̫̮͙͚̪̗̮͚̬͖̭͈̘͙͚̭͔̘͙̥͚̩̮́͒̒̏̒̏͒͒̒͌̒̓͂͆͑̒͆͑̓́̓͂́̓̓̒͊͒̒́͒͒̓͒̏͊̓͐̒͐́̓́̒͊͌͊͆́̏̒͐́̓͐̓͆͐̓̒͑͂͊͘͏̨̭͙͙͚̫̗̮͓̩͚̩̗̮͕̭̦͚̩̭͇̘͖͚̩̰̮͕̭͙͚̹̮͖͖͚̬̬̮͎̘͙͔͚̭͎̘͙͚̪̰̮͇̭͙͚͎̮͒̒̒͊̒͒̓̒͂̈́̔́͘͏̸̘͚̬̮͖̘͙̹͚̰̭͚̫̭͔̭͙̯͚̭̓̒͆́͒̓̒̑͂͊͏̨̨̘͙̬͚̪̗̭͇͙̤͚̬̭͓̬͚̩͖̮̭͙͚͚̭͚̪̭͎͙͚̹̰̭͕͓͚̮̓̓̓̒͒́͒͒̓̒͑̏̓̒͐́͏̴̨̢̨̭͙͚͚̮͓͇͚̬̬̭͓͙͚̫̗̭͓͙͚̹̭͉̘͙͚̭͇̘͙͚̬̮͍̭̙͚͚̭͓̘͚̭͙͚̩̭͉̘̤͚̫̤̭͈̘͈͚̭͔̘͕͚̬̮̓͂͑̒͒͌͊̈́͂̏̒́̒͑́͂͑̓͆̓̒̒́͒̒̏͏̸̴̡̭͙͙͚̮͓͚̩̗̭͇̘͙͎͚̩͖̭͎͙͚̩̰̭͈̘͙͚̹̮͔͖͚̬̮͎̘͍͚̫͚̭͎̘͙͚͎̮͇̘͙͚̪̭͓͚̬̭͈̘̖͚̤̭͂͒̒́̓̐̓̓̒̒̈́͂̋͆͑̒͆̒́͘͏̸̴̸̴̨̨̨̡̨͙͚̫̮͉̘͙̯͚̪̮͈͙̬͚̪̮͖̘͙̤͚̪̬̭͓̬͚̮̭͙͖͚̩̮͓͙͚̪̮͔͓͙͚̹̰̭͕͓͚̫̮͇͓͙͚̩̭͇̭͚̫͚̭͍̘͕͚̬̭͓͙̤͚̹̭͉̭͙͚̩̮͉̭͙̬͚̬̮͍̭͙͚͚̭͙̥͚̫̮͙͚̪͚̭̭͚̬̭̘͙͚̩̭͔̘͙͚̪̮̓͂͂̓̓̓̒́̓͒͐̏͂̒̓͒̓͆̒͊̒͊͊̓͂́͒̓̓͒̓͆͑̒̏͌͑ͅ͏̴̴̴̸̡̘͙͚̪͖̮͓̤͚̩̗̭̭͙͖͚̩̭͍͓͙͚̩̰̭͎̭͙͚̹͖̮͕͓͚̬̮͎̘͙͔͚̫͖̭͎̘͙̯͚̩̮͇̘͙͚̺͚̭͓͚̬̭͈̘͙͚̤̭͔̘͚̗̭͕̘͙̯͚͖̭̘͙̩͚̩̭͇̩͚̭͓͙͇͚̫̮̭͙͈͚̩̮͓͙͓͚̪̭͚̹̤̭͕̭͙͚̫̮͓̘͙͚͎̮͗͒̒͋͊̐̓̒͂̏̏͑̒̐͆́̒͌́͂͐̓̒́̓͊͒͐̏͊̓̒͒̓́͘̕͏̷̨̨̨̡͓͇͚̫̗̭͍̘͕͚̹̭͓͙͚̭͉̭͙͚̩̮͉̭͚̬̮͍̘͙͚̭̘͚̫̮͓̘͙͚̮͚̬͎̮͙͚̩̭͔̘͚̫̮̒̒͒͊́͂̒͒͗́̏͒̒͆̓͆͂͂͑̓̒͑̓͑͒̒̏͆͏̭͙͚̪͖̭͚̩̗̭̘͚̩͖̭͍̘͖͚̩̰̮͕͙͚̹͖̮͖͚̫̗̮͓͙͔͚̫̭͎̘͚̪͖̮͇̘͙͚̪̮̐͐̓̒́͋̒̈́̒̓͑̓̒͑̏̒̑̔͆͘͏̸̴̴̴̴̴̨̨̨̗͚̬̮̭̖͚̰̭̘͚̫̮͇͙̯͚̪̤̮͕͓͙̩͚̪̭͔̭̩͚̭͓̮͚͎̮̘͙͈͚̺̭͚̪̭͎̭͔͚̹̤̭͔̘͚̫̭͈͓͙͚̩̮͓͚̬̮͔͙͚̫̭͓͙͚̬͖̭͉̘͙͚̬̭͇̘͙̦͚̬̮͉͓͙͚̭͔̭͚̮͓͙͚̪͚̭͍̘̤͚̬̗̭̘͈͚̬̭͔̘͙͚̮̓̒͆͒̒́͑̒͌̓̓̒́̓̒́͒̏͒̓̒̔̏̒̒͐͒̓͐̒͊̓͌͊̈́͂́̏̒͆́͂͒͆̒͌̒͂͂͒͏̘͙͚͚̫̗̮͓͍͚̩̗̭͇̘̺͚̩̭͎̭͙͚̩̰̭͍̘͙͚̫̤̭͓̭͓͚̫̮͓͙͔͚̪̬̭͎̘͙͚̬̤̮͇̭͙͈͚̪̮͒̒̒͊̐̒̓͑͆͘ͅ͏̴̨͚͚̬̮͙͚̰̭̘͚̗̮͉͓͙̯͚̪̮͎͙̩͚̪͚̮͖̘͙̤͚͖̭͓̹͚̪͖̮̘͙͚̪̭͔͚̪̭͎̭͙̓̒͆͑̓̓́͒̒͌́̓͂̓̒͒̑͒̓̒̏͏̴̸̴̴̨̨͚̹̤̭͕͙͚̫̭͈͙͚̩̮͖͓͇͚̬̮͔͕͚̹̭͓͙͚̬̭͉̭͙͚̬̭͇̘͙̺͚̬̭̓͒̓̓̒̓̒͆͊̏́͏̘͚͚̭̒͐́͏͚̮͓̘͙͚̪͚̭̭̤͚̬͖̮͎̭͈͚̩̤̭͔̘͚̪͚̮̓̒͑́͂͆͒̒̒̒͐͏̭͙͚̫̗̮͓͙̖͚̩̗̭̘͙͎͚̩͖̭͈̭͚̹̮͖̭͙͚̹̮͓͚̫̮͎̘͙͔͚̗̭͎̘͙͚̮͇̭͙͚̩̮͗͒͋̒̏͊̓͐̓̒͒͂͂̓͋͆͘ͅ͏̨̨̤͚̬̭͈̭͙͚̤̭̭͙͕͚̗̭͙̯͚̪̤̭͕̘͙̩͚̪͚̭͔̭͙̤͚̬̬̭͓̹͚̪̰̮̭͙͔͚̺̮͓͙͓͚̪̮͔͙͚̹̤̭͖͓͙͚̫̮̓̒͆̏́͑́͑̓̓̒͒̏͐̏̓͒͏̨̨̭͙͚̭͉̭͇͚̬̤̮͔͙͚̫͚̭͓͙̲͚̫̰̭͉̭͙͚̩̭͇̘͙̙͚̬̮͉̭͚̭̓͂̏̒̓͌͊͂̒̑́̏͏̡͚̫̮͙͚̪̭͍̘͚̫̬̮͎̭͈͚̭͔̘̘͚̮̓̒͆̓͑̓͆̓̒̒͂̏̒́͒͏̘͙͓͚̪͖̮͓͙͇͚̩̗̭̘̦͚̩͖̭͎̘͖͚̩̰̮̘͙͚̺̮͖͖͚̫̗̭͈̭͍͚̫͎̭͎̘͙̮͚͎̮͇̭͙͚̺͚̮͒͋̒̒͑͊̓̒̒͂̋͘͏͚̬̮͓͉͚̰̭͓̘͙͚̗̮͍͓͙̯͚̪̤̭͕̘͙̬͚̪̭͔̭͙̤͚̪̭͓̹͚̪̰̮̘͙͚̺̮͓͚̪̭͎͙̓̒͑͆͒̒́͂́̓͒̓̒͒̐̏͐̒͗̏̓͏̨̨̨͚̹̰̭͕̘͙͚̮͔̭͙͚͎̮͓͚̬̤̮͔͙͚̺͎̭͓̗͚̺͎̭͉̘͙͚̮͉̭͙͚̬̭́̓́͐̒͊̓͌͊̒̈́͂̏͌͏̵̨̘͙͚͚̭̘͙͚̭͓͙͚̭͍̘̤͚̬͎̮͎̭͙͚̪̭͔̘͙͚̩̤̮͂́͒́͂͋͆͂͂̒͑͆͏̸̸̨̭͙͚̮͓͚̩̗̭͇̘̺͚̩̭͇͖͚̹̭͉̘͙͚̺̭͉̘͖͚̬̭͈̭͍͚̫͖̭͎̘͙͚̮͇̭͙̘͚̪̮͐́͒̒̒͊̓̒͊͊̒͆̒̓͂͆͘͏̸̡͚̬̮͙͚̰̭̭͙͚̗̮͓͙̯͚͖̮͓͙̬͚̪̮̘̩͚̬̰̭͓̬͚̫̮̭͙͔͚̺̭͙͚̪̭͍̘͚̹̰̭͕͙͚̫̭͎͓͙͚͚̮̓̒͑͆͑̓́͒͂́͊͂͐̓͒̒̓̒͊͒̏͒̓͒̏̒̑̓͒̓́͏̴̸̴̧̨̡͓͇͚̬̬̮͙͚̫͖̭͓͙͚̬̰̭͉̭͙͚̭͇̘͙͚̬̮͉̭͚͚̭͓͙̥͚̮͓͙͚̭̘͚̬͎̭̘͙͚̭͔̘͙̥͚̪̮̒͐̓͌͊̓͂̏̒́͒́͂͒͆͂͂͌̒͌͑͂̕͏̸̸̸̴̷̴̨̨̨̨̭͙͚̭͙͚̩̗̭̭͙͎͚̩͖̭͎̭͙͚̩̰̭͖͓͙͚̺͖̮͖͖͚̫̮͎̘͍͚̭͎̘͚͎̮͇̘͙͉͚͎̭͓͙̤͚̬̮͙͚̤̭͓̭͚̫̭̭͙̯͚̪̤̮͓͙̬͚̪͚̮̘͙̤͚̗̭͓̬͚̩̮̭͙͙͚̪̮͓͍͚̪̭͎͙̬͚̹̤̭͕̭͚̮͕̘͙͚̮͔͓͇͚̫͎̭͍̘͙͚̹̭͓͙͚̬̰̭͉̭͙͚̬̭͇̘͙͚̬̮͉͓͚̭͗́͐̓͋̐̓̒͒̒́̒̒͂́͑͆͑̓̒́̒̑͒͐͒͂̓̒̏͒͐̒̏̓̒̓́̓́̏̒͌͊̈́̒́̏̕͘̕͏̸̡͚̫̭͓͙͚̮͕͚̬̮͙͚̹̭͔̘͙̥͚̮̓̒͆̓͑͆͂̓̒͆͑̓͑͂́͂͏̨̭͙͕͚̫̗̮͓͚̩̗̮͕̘̖͚̩̭͎̭͖͚̹̮͒̒̒͊̒͊͏̸͓͙͚̺̮͓͖͚̬̭͈̭͙͔͚̫͚̭͎̘͙͚̩̮͇̘͙͈͚͎̮͊̓̒̈́̏́͘͏̸̸̴̧̨̨͚̬̭͈̘̖͚̤̭͙͕͚̫̮͍̭͙̯͚̩̰̮͍͙̩͚̪͚̮͖̘̩͚͖̭͓͙͇͚̬̤̮̭͙͚̭͙̳͚̪̮͔͓͚̹̤̭͓͙͚̮͓̘͙͚̗̭͈̭͇͚̫͎̭͍̘͕͚̹̭͓͙̲͚̹̭͉̭͙͚̬̭͇̘͎͚̬̭̓̒͆̒́͒̓̓̒͂̓͒̓́͒͒̓̏̒͐́̓́̒̒͒͊̓̓̒̕͏̸̡̘͙̰͚̭͔̘͚̫̮͕̘͙͚̪͚̮͕͚̬̮͎̭͙͚̭͔̘͙̥͚̪̮́̏̒͑̓͆̓̒͊͑͂͊͏̸̴̘͙͙͚̭͙͍͚̩̗̭̭͚̩͖̭͎̘͙͚̹̭͖͙͚̹̭̭͖͚̬̰̮͓͍͚̭͎̘͙̯͚̪͖̮͇̘͙̗͚̪̮͂͐̓͋̒̈́̐͊̓͒͑̒͑̒͂͆͘͏̸̴͙͚̬̮͙͚̤̭͓̭͙͚̫̮͓͙̯͚̪̰̭̘͙̬͚̩̬̮̘͙̤͚͖̭͓̩͚͎̮̘͙͚̪̭͚̪̮͔͙̬͚̹̰̭̓͂͆͑̓̓́͂͊͐͒́̓̒́͒͐͒̓̒͌̏̓͏̴̸̴̵̴̨͓͚̫̮͔̭͙͚̩̭͍̭͚̬̰̮͕͚̹͚̭͓̗͚̹̭͉̭͙̪͚̭͇̘͙͚̬̮͍̘͙͚̭͓͓͙͚̮͙͚̪̮̤͚̫̮͙͚̩̰̭͔̘͕͚̬̮̒̓͒̓̒͊͐̓̒͊̒͂̏̋́̏́͂͐̓͆̓͐̓̒͑̓͑̒́͏̘͙͚̪͖̭͙͐͐̓͏̸̢̨͚̩̗̮͕̭͙̗͚̩̭͍̘͙͚̹̭͎͓͙͚̫̰̭̭͖͚̫̮͎̘͙͔͚̰̭͎̘͚̮͇̭͙͉͚̺͚̭͓̤͚̬̮͖̭͚̰̭̭͙͕͚̫̮͊͊͑̒͂̒̑́̓͑̒͆̒͑́͒͘͏̴̴̨̧̨͓͙̯͚̪̰̮͇͙̬͚̪̮̘̩͚̭͓͙͚̪̰̮̘͙͈͚̭͙͎͚̪̭͓͙͚̹̤̭͔̘͚̭͉͓͙͚̩̮͓͇͚̫̗̮͔͕͚̺̭͓̗͚̗̭͉̭͙͚̭͇̘͙͚̬̮͍̭͚͚̭͓͙̥͚̫̭̭͙͚̪̗̭͍̘̤͚̬̭͈̘͈͚̭͔̘͚̫̮̓̓͒̒́̏̓͊͒́͒͒̓̏͊͂̒͐́̓͐̒̓̒͆͊̒͂̈́́̏̒́͑̓͒͆̒̓̒͂̒͐͆͘͏̸̘͙͚̭̺͚̩̗̭͇̭͙͚͚̩͖̭͎͚̩̰̭̘͙͚̫̰̭̭͓͚̫͎̮͎̘͙͔͚̪̬̭͎̘͚͎̮͇̭͙͚̪̮̐͂͐̓̒̓̒̏͊͑̒̒̒͂͋͆͘͏̴̴̸̨̨͚͚̬̮͙͚̰̭̘͚̗̮͓͙̯͚̪̮͙̬͚̪͖̮͖̘̩͚̩̬̭͓̹͚̩̮̭͙͚̩̮͓͚̪̭͓͙͚̹̤̭͖̭͙͚̫̭͈͙͚͎̭͇̭͚̫̮͔͙͚̬̗̭͓̗͚̬̰̭͉̘͙͚̭͇̘͙̳͚̬̮͉̘͔͚͚̭̓̒͆͑̓̓́͒̒͌́͊͊̓̒̓̒̏͒͒͐̒͗̏͊͒̓̓́̒͊̏̓͌͊̒͆͂̏̒́͏̴̴̡͚̮̭͙͚̪͖̭̘͚̫̤̮͈͚̹̭͔̘͙̥͚̪̮̓̒͑́͂͒͆͊̒͑̓̒͏̘͙͚̫̗̮͓̗͚̩̗̭͓͚̩̭͎̭͚̹̮͖̭͙͚̫̤̮͖͚̬̰̭̭͍͚͎̭͎̘͙͚̬̤̮͇̘͙͇͚̺͚̮̐͒̒͌̒̈́͊̒̏͊͒̓̒͌̒́͘ͅ͏̸̴̸̴̸̨̨̨̨̢̨̡͚̬̭͈̭͙͚̤̭͓͙͚̫̭͔̘͙̯͚̪̮͙̩͚̪̭͔̭̩͚̪͚̭͓̮͚̬̤̮̘͙͚̪̭͚̪̮͔͙͚̹̤̭͕͙͚̮͕̘͙͚̩̮͔͓͚̫̭͍̘͙͚̹͖̭͓͙͚̹̭͉̘͙͚̮͉̭͔͚̬̮͉̘͙̰͚͚̭͓͓͚̮͓͙͚̪̭͉̘͚̫̮͈͚̭͔̘͖͚̬̮̓̒͆̒́͑͂͊̓̏̒̓̒͒̐͒̓̒͑̏̓̓́̓͆̒͊̓͌͊̓́̏̒́̒͑́͂͐͆̓̒͑̓̒͂͒̒͂͏̸̘͙͖͚̭͚̩̗̭̭͙͚̩̭͎͙͚̹̮̭͙͚̺̭͓̭͖͚̫̮͓͍͚̫͎̭͎̘͙͚̬̤̮͇̘͙͉͚̩̮́͐̓̒̈́͋͒͊̓̐͊͐͊̒͒͑̒̓͆͘͏̸̸̨̨̨͚̬̮͓͙͚̤̭͓͓͚̗̮͍͓͙̯͚͖̭͕̘͙̬͚̪̭͔̭͙̤͚͚̭͓͚̮̘͙͚̮͓͚̪̭͎̭͙͚̹̰̭͖͓͙͚̭̭͙͚̮͓͇͚̫̭͓͙͚̺̭͓͙̤͚̹̭͉̘͙͚̮͉̭͙͚̬̮͍̘͚͚̭̘͚̫̭͓͙͚̭͉̘̤͚̬͎̮͈͚̰̭͔̘͕͚̫̮̓̒͑͆͒͊́̒̑́͂̓́̓̒͂́̓͒̐́͒͐̒͑̏͂́͌̓͂̏͐̒͒͒͌͊̈́͂̏͌̒́͑̒͑̓͋͆͂͂̒͑̓̒͂̒͆͘͏̭͙͚̪͖̮͓̯͚̩̗̭͇̭͙͎͚̩͖̭͍̘͚̩̰̮͕͙͚̫̰̭̭͓͚̫̭̭͙͔͚̩͖̭͎̘͙̯͚̬̤̮͇̭͙̗͚̺͚̮͐͒̒̒̏̓͑̒͊͌͘͏̴̴̨̨̙͚̬̮̭͙͚̤̭͓̭͙͕͚̗̭̘͙̯͚̮͖͓͙̩͚̩̬̭͔̭͙̤͚̭͓̬͚̬̤̮̘͙͚͚̭͙͚̪̭͙͚̹̰̭͖̭͚̫̮͓͙͚̩̮͓͚̬̭͓͕͚̬͖̭͓͙̱͚̗̭͉̭͙̥͚̩̮͉̭͚̬̭̓̒͆͒̏́́͒͂͊͂͒̓̒͒́͒͒̓͒̏͊̓̒͐͒̓̓͑̒͊͂͒̒͊͂̒͊͏̭̙͚͚̭̒́͏̡͙̥͚̮̭͙͚̪̮͚̬̭̘͈͚̹̭͔̘͚̬̮̓́͂͒͆̓͒̓̒͆͌̒͂̒͐́͏̸̴̸̴̴̴̡̨̨̡̭͙͕͚̭͙͚̩̗̭̭͙͎͚̩͖̭͎̭͖͚̹̭̘͙͚̹̮͖͚̬̭̭͙͔͚̤̭͎̘͙͚͎̮͇̭͙͚̩̭͓͚̬̭͈̘͚̤̭͓̘͙͕͚̗̮͕͓͙̯͚̪̰̮͍͙̬͚̪͖̭͇͙̤͚̗̭͓̬͚͎̮̭͙͚̺̮͓͍͚̪̭͎͓͚̹̰̭͕̭͙͚̮͕͓͙͚̭̭͚̫̮͔͙͚̺͖̭͓͙̱͚̗̭͉̭͙͚̬̭͇̘͖͚̬̮͍̘͙͚̭͓̘͙̥͚̭͔̭͙͚̪͖̭̭͚̬͖̮͈͚̪̭͔̘̘͚̪͚̮͂͐̓͋̒͊͊͒͑̓̒͌͂́͆͑̒͆̒̒́́̓̓͂̓̒͂͒̑̏͐̒̏̒́̓́̏͌̒͊̏̓͌͊͂́̒́̏́͂͆͑̒͑̓̒̒̕͘̕̕ͅ͏̴̘͙͚͚̪͖̮͓͚̩̗̮͕̘̖͚̩͖̭͎͙͚̩̰̮͙͚̺̮͖͖͚̬̮͓͍͚̭͎̘͙͚̪͖̮͇̘͙̙͚̪̮͒̒́̒̓̐͑̓͊̓̒͑̒́̏̓͆͘͏̸͚̬̭͈̘̖͚̤̭͙͕͚̫̮̓̒̓͆̒́͒̓͏̴̨͓͙̯͚̩̰̮͙̩͚̪̮͖̘͙̤͚̪͖̭͓͙͇͚̬̤̮̘͙͙͚̪̭͙̳͚̪̭͎͓͙͚̹̰̭͚̮͓̘͙͚̗̭͊̓͒̓͒͒̓̏͗͐̓̒̓́̓́͏̴̸̢̨̨̘͚̫̗̮͔͕͚̬̭͓͙̤͚̺͎̭͉̭͙͚̭͇̘͙̘͚̬̮͍̭͙̬͚͚̭͓͚̫̮͙͚̩̗̭͈̘̤͚̫̮͎̭͙͚̩̭͔̘͙͚̪͚̮̒͊̓̒͊͂̏́͒̒͑̓͒̓͆̒͂͑͏̘͙͏̸̨͚̭͙͚̩̗̭̭͙͚̩̭͈̭͙͚̩̰̮̭͙͚̹̮͕͓͚̫̮͎̘͙͔͚̫̭͎̘͙͚̮͇̘͙͚̺͚̭͓͚̬̮͙͚̤̭͔̭͚̗̮͂͐̓͌͋͊͊̐͑͊̓̒͒͆̓͂̔͑̒͐͆͑̓̒́̒͌́͘͏̴̵̨̨̡̨͓͙̯͚̪̰̭͖̘͙̩͚̪͚̭͔̭̩͚̭͓̩͚͎̮̭͙͚̭͚̪̮͔͓͚̹̤̭͕͓͙͚̫̮͓͙͚̩̮͖͓͚̬̮͕͚̹̭͓̗͚̺̭͉̭͙͚̬̮͉̭͙͚̬̮͚̭͔̭͙͚̫̮͓͙͚̪̗̮͚̬͎̭͈̘͙͚̪͖̭͔̘͙͚̮̒́̓̓̒́͒͐́͒͒̓̒͌̏̒͒̓̓͆̒͊͆͐̓̒͊͊̒̓͆̓͊̓̒́̏̓͐͆͑̓̒͑͂͂̕̕͏̢̨̘͙͔͚̫̗̮͓͙͚̩̗̭̮͚̩̭͍̘͙͚̩̰̭͖͙͚̹̭̘͖͚̫̮͎̘͙͔͚̫̭͎̘͙͚͎̮͇̭͙͉͚̺͚̮͒͋̓̒͊̓͒͊̒̏̓͂̕͘͏̴̴̸̸̨̨̨̨̡̨͚̬̮͖̭͚̰̭̭͙͕͚̗̮͓͙̯͚̪̰̮͈͙̬͚̪̭͔̭͙̤͚͖̭͓̹͚̪̰̮̘͙͖͚̮͓͙͚̪̭͚̹̤̭͔̘͙͚̮͉̭͙͚̩̮͓͚̬̮͔͕͚̫̤̭͓̗͚̭͉̭͙͚̩̮͉̭͙͚̬̮͍̭͙͓͚͚̭̘͚̫̭̭͙͚̮͚̫̮͎̭͈͚̭͔̘͕͚̬̮̓̒͌͆̒͑́͒́͐̓̓́̓̒͒́͒͐͐̏͊̓̒́̓͐̒͊̓̒͊̒͂͒͆̒́͒̒͆̓͒͆͂͑̓̒̒͂̒̏̕͏̶̭͙͚̪͖̭͚̩̗̮͕̘͙͎͚̩͖̭͎͚̹̭͙͚̫̤̭͍̘͓͚̫̭͈̭͍͚̩͖̭͎̘͙͚̮͇̘͙͚̺͚̮͐͐̓̒̓̒̏͊͐̓̒̏̒̈́́̓͘̕͏̸̴̡̨̨̨̡̨̡͙̲͚̬̭͈̘͙͚̤̭͔͓͙͕͚̫̭̘͙̯͚̩̰̮͍͙̩͚̩̮͖̘͙̤͚̬͚̭͓̹͚̩͖̮̘͙͚̩̭͔͚̪̭͎̭͙͓͚̹̤̭͕̭͙͚̫̭͈͙͚̩̮͔͓͇͚̬̤̭͓͕͚̫͖̭͓͚̺̭͉̭͙͚̭͇̘͖͚̬̮͉͓͚͚̭̘͚̫̮͕͓͙͚̮͚̬̮͙͚̰̭͔̘͚̬̮̓͆́͐̓̓̒͒͐͒̓̒̏͒̓̓͆̒͒̒͊̒̔͂̏̒̒̑́͑̒͑̓͆͂͂͒̓̒̏͑̓͑́̒͐͂͏̸̸̢̭͙͚̮͓̖͚̩̗̭͓̮͚̩̭͈̘͙͚̩̰̮̘͙͚̹͖̮͓͚̫̗̭͈̭͙͔͚̗̭͎̘͙͚̮͇̭͙͚̪̭͓͚̬̮͉͚̤̭͓͙͕͚̫̮͖̭͙̯͚̪̤̭̘͙̬͚̪̮͖̘̩͚̬͖̭͓͚̮̭͙̐́͒̒͌̒͊͒͑̓̒͂̈́́̓̔͆͑̒̓͆͑̓̒́͑͐̏̒̓̒͂͂̓͒͘͏̸̨̨͚̺̮͓͚̪̮͔͓͙̬͚̹̤̭͖͓͙͚̫̭͈͓͙͚̗̭̘͚̫͎̭͍̘͙͚̫͚̭͓͚̫̭͉̭͙͚̩̭͇̘͙͚̬̮͉͓͚̭̏͐̒͌̏͒̓́͐̒͊͌͊̒̔͆͂̋̒́̏̕͏̡͚̫̮͓͙͚̪͚̮͕͚̫̬̮͎̭͈͚̗̭͔̘̘͚̮̓̒͑̓͑͆̓̒̒͂̒́͒͏̨̭͙͚̫̗̭͚̩̗̮͕̭͙͚̩̭͎͙͚̹̮̭͙͚̹̭͓̭͖͚̫̮͓͙͔͚̫̭͎̘͙͚̮͇̭͙͚͎̮̒͐̓̒̑͒͊̓̐͊͐͒̒͑͊̓́̓̔́͘͏̵͙͚̬̭͈̭͍͚̤̭͓͚̗̭̓͆̒́͑̒̑́͏̴̸̨̨̡̨̭͙̯͚͖̮͕͓͙̩͚̪̭͔̭͙̤͚̬̬̭͓̹͚̫͚̮̘͙͙͚̭͙͓͚̪̭͎͓͙̰͚̹̤̭͚̮͔̭͙͚͎̮͕͓͚̬̮͔͙͚̺̭͓͙̲͚̫̭͉̘͙͚̭͇̘͙̰͚̬̮͉̘͚͚̭͙̥͚̫̭͓͙͚̪̗̮͚̫̭̘͈͚̬̭͔̘͚̩̮͂̏̓̒͒́͒͒̓̏͐̓̒̓́̓́̒͊̓͌͊͆̈́͂̏̒̑́͒̓̓͋͆͐̓̒͌̒͂̒͐͊͏̸̘͙͚̮͓̫͚̩̗̭͇̘͙̗͚̩͖̭͍̘͚̹̭͉͙͚̹̭̘͓͚̫͖̭͈̭͍͚̭͎̘͙̯͚̪̰̮͇̭͙̗͚̪̮͒́͒̒̒̏͊̓͒͌̒̒́̓͆͘͏̴̸̡̨͎͚̬̮͙͚̰̭̭͙͕͚̗̭̭͙̯͚͖̮͓͙̬͚̪̭͔̭̩͚̬̭͓̫͚̮̘͙͚͚̩̭̖͚̪̭͙͚̹̰̭̓̒͆͑̓́͒́͒͂͐͒̒́̓̒͂͒͒̓̒̏͊̓͏̴̨̨̨̨̡̨͙͚̫̮͙͚͚̭̭͚̬̭͓͕͚̫̤̭͓͙̲͚̬̰̭͉̭͙͚̩̭͇̘͖͚̬̮͉̘͚͚̭̘͚̫̭̭͙͚̪̭̭͚̬͚̭̘͙͚̭͔̘͖͚̫̮̓͒͐̓̓́͌̒͊͒̒͊̒̒͐́͑̒͑̓͒͆̓͑̒͌͑͂̒͆͏̸̴̸̘͙͚̮͓̭͚̩̗̭̭͙̗͚̩̭͎̘͙͚̹̭̭͙͚̺̭̘͖͚̬̭͈̭͙͔͚̗̭͎̘͙͚̮͇̭͙͚̩̮̓́͒̒͋͊̐͊͊͊͌̒́͂́͆͘̕͏̖͚̬̭͈̘͚̤̭͓̘͙͚̗̮̓̒͆̒̒́͂́͏̴̵̨̨̨̨̡̨͓͙̯͚̪̰̮͍͙̬͚̩̭͇͙̤͚̬̰̭͓̬͚̩̮̘͙͔͚̺̮͓͍͚̪̭͎͚̹̤̭͖͓͚̮͕͓͙͚̮͔͓͇͚̬̮͕͚̭͓͙͚̹̭͉̘͙͚̮͉̭͙̳͚̬̮͍̭̙͚̭͓͙͚̭͙͚̩̗̭͈̘͚̬̗̮͎̭͈͚̪̭͔̘͚̮̓̓̓̒̏͒̏͐̒̏̓̒̒̓́̓́̏̒͂͐̓̒͂̏͊́́̏̒́̏͒́͂͑̓͆̒̒̒͐́͒̕͏̴̸̸̴̵̴̸̨̨̨̘͙͚͚̪͖̮͓͚̩̗̭͇̘͙͚̩͖̭͎͙͚̩̰̭͈͙͚̹̭͉̘͖͚̬̮͎̘͍͚̭͎̘͚̫͚̮͇̘͙̙͚̪̭͓͙͚̬̭͈̘̖͚̤̭͚̫̮͍̭͙̯͚̩̰̮͙̩͚̪̮̘̩͚͖̭͓͙͇͚̬̤̮̘͙͙͚̩̭͙̳͚̪̭͎͓͚̹̰̭͖̘͚̮͓̘͙͚̗̮͓͇͚̫͎̭͍̘͕͚̹̗̭͓͙̲͚̬͖̭͉̭͙͚̩̮͉̭͙͚̬̮͍̭͙͚͚̭̘͙͚̫̮͙͚̩̗̮͖̤͚̫̮͎̭͙͚̩̭͔̘͙̥͚̗̮͒̒́̏̓̐̓͒̒̒́͒̒̒͆͑͆̒́͒̓̒͌͊̓̏͒̒͂̓͒͒̓̏̒͌̒̓́̓́͐̒̒͊̓͂́͑̓͒̓͆̓̒͑͂͘̕͏̸̴̨̨̭͙͚̮͓͚̩̗̭̭̮͚̩̭͍͓͙͚̩̰̭͎͓͙͚̹̭͈̘͓͚̫̮͓͍͚̭͎̘͙̮͚̫͚̮͇̘͙̘͚̩̮̑͂͒̒͋̒͊̐͊̒͑̒͂͆͘͏̴̨͙̺͚̬̮̭͉͚̤̭͓͓͚̗̭͙̯͚̪̮͖͓͙̩͚̩̭͇͙̤͚̭͓̬͚̬̤̮̘͙͚̪̭͙͓͚̪̭͎͙̓͆͒̒́̒͌́͑̓͆̓́̏̓̒͒̓͒̓̏̓͏̸̴̵̨̨̨̡̨͚̹̤̭͖̭͙͚̭͎̭͙͚͚̭͎̭͇͚̫̭͍̘͕͚̹̭͓̗͚̫͖̭͉̭͙͚̬̮͉̭͙̣͚̬̮͚̭͔̭͙͚̫̮̘͙͚̪̗̮͚̬͎̭͈̘͙͚̭͔̘͙͚̮́̓́̒̒͊͊̒͆͊̓̒́̏̓͐͆͑̓̒͑͂̓͂͂̕͏̢̨̘͙͈͚̫̗̮͓̘͚̩̗̭̭͙͚̩̭͍̘͙͚̩̰̭͖͙͚̹̭̘͖͚̫̮͎̘͙͔͚̫̭͎̘͚̩̮͇̘͙͚̪̮͒̒͋̏͊̓͒͊̒̏̒̑͆̓͆͘͏̸̗͚̬̮̭̖͚̰̭̘͚̫̮͇͙̯͚̭͕̘͙̩͚̪̭͔̭̩͚̭͓͚̪̮̘͙͈͚̭͙̓̒͆͒̒́͑̒͌̓͂͊̓̒́͂̓̒͂͆͒́͒͒̓͏̴̴̸̴̨̨͚̪̭͓͙͚̹̤̭͔̘͚̫̭͇̘͙͚̩̮͓͚̬̮͕͚̫̤̭͓̗͚̭͉̭͙͚̭͇̘͙̯͚̬̮͍̘͔͚̭͔̭͚̭͓͙͚̭̭̤͚̬̭̘͈͚̭͔̘͙͚̮̏͊͂̒͐͒̓͐̒͊͐̓̒͊̒͂͒͆́̏̒́̏̒͆́͂͒͆͂͒̒̓͌̒͂͂͒͏̘͙͚͚̪͖̮͓͚̩̗̭͇̘̺͚̩̭͎̘͙͚̩̰̮̭͙͚̫̤̮͖͚̬̤̭͈̭͙͔͚̪̬̭͎̘͙͚̬̤̮͇̭͙͉͚̪̮͒̒̏̒͊̐͐͑̓̒͆͘ͅ͏̴̸̴͙͚̬̮͙͚̤̭͓͙͕͚̗̮͉͓͙̯͚̪̭̘͙̬͚̪͖̮͖̘̩͚̩̬̭͓͚̩̮̭͙͚̪̮͓͚̪̭͍̘͚̹̤̭͕̘͙͚̫̮͈̘͙͚͚̭͍̭͚̫̭͍̘͙͚̫̤̭͓̗͚̬̰̭͉̭͙̥͚̬̭͇̘̓̒͆͑̓̓́͑́͂͑̒̓̒͂̏͒͒͐̒͌̏̒̑͒̓́̒͊̓͌͊̒̒͏̴̨͚̬̮͉̭͚͚̭͓͚̮͓͙͚̩̭̭̤͚̫̮͎̭͈͚̹̭͔̘͙̥͚̫̮̒́͑̒͆́͂͑͆̓͑̒͂̒͆̕͏̸̴̢̨̨̨̨̨̭͙͚̪͖̭͚̩̗̮͕̭̦͚̩͖̭͈͙͚̩̰̭͍͓͙͚̫̤̭͍̘͖͚̬̬̮͓͙͔͚̭͎̘͚̩͖̮͇̭͙͚̩̭͓͚̬̭͈̭͙͚̰̭͓̘͚̗̮̭͙̯͚̪̰̮͈͙̩͚̪̭͔̭̩͚̩̭͓͚̮̘͙͚̩̭͓͚̪̭͎͓͚̹̤̭͕͓͙͚̫̭͇̘͙͚̩̮͔͓͇͚̬̰̭͍̘͙͚̹̭͓͚̫̰̭͉̭͙͚̩̭͇̘͙̙͚̬̮͉̘͚̭͗͐̓̒̒̓̒͑́̒̑͆͑̒͆̒́̒͌́͊̓̏̒̓̓̒͂͂͒̐͒̓̒̏̒͐͒̓͆̒͌͊̒̔͂̒̑́̏͘̕͘ͅ͏̸̡̨͚̫̮͓͙͚̮͚̫̮͎̭͙͚̹̭͔̘̘͚̮̓̒͆̓͒͆͂͒̓̒͑͂̒́͒͏̴̢̧̭͙͙͚̪͖̮͓͍͚̩̗̭̘̦͚̩͖̭͎̘͙͚̹̭͓͙͚̺̮͖͖͚̫̭̭͙͔͚͎̭͎̘͚͎̮͇̭͙͚͎̭͓͚̬̭͈̭͍͚̰̭͔̭͚̗̮̘͙̯͚͖̮͕͓͙̩͚̪̮̘̩͚̬̭͓̹͚̫͚̮̘͙͙͚̩̭͙͓͚̪̮͔͚̹̤̭͒̒͋̒͊͋͊̓̒͒͌́̒̑͂̓́͑̒͆̒́̒̑́͊͂̓͒̒͂̓̒͒͒̓̏̓̒͐͘͏̴̸̷̨̨͓͚̮͓͙͚̗̭͎̭͚̬̮͔͙͚̺̭͓͙͚̬̭͉̘͙͚̮͉̭͙͚̬̭̒̓́̓̓́̒͊̓͌͊̏̈́͂̏͌͏̨̘͚͚̭̘͙̥͚̭͉̭͙͚̪̮̤͚̬͎̮͎̭͈͚̩̬̭͔̘͙͚̩̤̮̒͌́͒́͂͆̓͒̓̒̒͏̸̴̸̡̨̨̨̭͙͚̫̗̭͚̩̗̭͇̘̮͚̩̭͎͓͙͚̹̭͕͙͚̺̭͍̘͖͚̬̮͎̘͍͚̫̭͎̘͚̩̮͇̭͙̘͚̪̭͓͙͚̬̮͙͚̰̭̭͚̫̮͔͙̯͚͖̭͓̘͙̬͚̩̭͇̩͚̗̭͓̬͚̮̭͙͚̪̭͙͚̪̭͓͙̰͚̹̰̭͕͚̫̮͓͙͚̩̮͓͓͇͚̬̰̮͕͚̬͖̭͓͚̹̭͉̭͙̥͚̩̮͉̭͍͚̬̭̒͐̓̒̋̒͊̐͊̓͊̒͂̒͒̒̑͆͆͑̓͆͑̓́͒̒͌̓͂̓̒͂̓̒́̓͒̒͒̓͒̏͊̓̒͐͒̓̓͆̒͐̓̒͊̒̔̒͘͏̭͙͏͚͚̭́͏̵̡͙͚̮͓̭͙͚̪̮͚̬̭̘͈͚̪͖̭͔̘͚̬̮̓́͂͆̓͒̓̒͊͌̒̒͐́͏̸̸̸̢̨̘͙͚̪͖̮͓͚̩̗̭̭͙̗͚̩͖̭͎͚̩̰̮͙͚̺͖̮͖͖͚̬̭͈̭͍͚̭͎̘͚̩͖̮͇̘͙͉͚̩̭͓̖͚̬̮͖̘͙̥͚̰̭̭͙͕͚̫̮͍͙̯͚̪̭̘͙̬͚̪͚̮͖̘͙̤͚̬͎̭͓̬͚̮̘͙̐͒̒͋̓̒̏͐̓̓̒̒́̒̒͆͑̒͆́͒̓͑̓̒͂̓͒͘͏̨͚̺̮͓̙͚̪̮͔͓͚̹̤̭͖̘͚̮͖̘͙͚͚̭̏͐̒̏̒͐̒̓́̓́͏̸̴̨̘͚̫͖̭͓͙͚̹̭͓͙͚̫͖̭͉̘͙͚̭͇̘͙̬͚̬̮͉͓͙͚̭̒͊͒͌͊́́̏͗́̏͏̸̡̨͚̫̮͔͙͚̮͕͚̬̮͈͚̭͔̘͙̥͚̮̓̒͆̓̓͆͂̓̒͆͑̓̒͂́͂͏̸̘͙͚̮͓͙͚̩̗̮͕̘̖͚̩̭͎̘͚̹̮̐́͒͋̒͊̒̏͊͏͓͙͚̺̮͓͓͚̫͖̮͓͙͔͚̫͚̭͎̘͙͚̩̮͇̘͙͚̪̮͊̓̒͑̈́̏͊͆͘͏̸̴̵̨̨̨̨̡͚̬̮͙͎͚̤̭͙͚̫̮͍͙̯͚̪̮͙̬͚̪̮͖̘͙̤͚̩̭͓̩͚̮̭͙͖͚̪̮͓͙̫͚̪̭͎͔͚̹̰̭͕͚̭͍̭͙͚̩̭͇̭͇͚̬̮͔͙͚̫̭͓͙̤͚̬͖̭͉̘͙͚̮͉̭͙̰͚̬̮͉͓͚͚̭̘͙͚̮̘͙͚̪͚̮͔͚̬͖̭̘͈͚͎̭͔̘͚̩̤̮̓̒̐͆͑̓́͑̓͂̓͊̓̓̏̓̒͂̓͒͐̏̓̒̓̒̓́̓͆̒͂̓͌͊͂͂̏̒́͑́͂͒͆̓̒͌̒́̒͐͘͏̴̴̴̨̡̨̭͙͚̪͖̭͙͉͚̩̗̮͕̘͍͚̩͖̭͎͚̹̮͖͓͙͚̹͖̮͖͚̬̮͎̘͙͔͚̫͖̭͎̘͙̯͚̪͖̮͇̭͙͚̪̭͓͚̬̭͈̭͚̤̭͔̘͚̗̭͖̘͙̯͚̭̘͙̩͚̩̭͇̩͚̭͓̩͚̪͖̮̭͙͈͚̩̮͓͕͚̪̭͎͓͙͚̹̰̭̭͚̫̮͓͙͚̩̮͕͓͇͚̫̗̮͕͚̹̗̭͓͙̲͚̹̭͉̭͙͚̬̮͉̭͙͈͚̬̭̒͐̓̒̓̒̏͊͒̓̒͆̏͆͑̒͆̒͑́̒͌́͂͊͑̓̒́̓̒͒͐̒̏͂͐̒̓͒̓̓͆̒͐̓̒͊̓͘͘͏̸̡̭͙͚̭͔̘͚̮͙͚̪̗̭͓̭͚̬̭̘͙͚̩̰̭͔̘͕͚̗̮́̏̒͑́͂͐̓͆̒͊͌͑̒͂͏̸̭͙͚̭͙͗͂͐̓͏̸̢̨͚̩̗̭͓͙̗͚̩̭͍̘͙͚̹̭͍̘͙͚̫̤̮͖͖͚̫̮͓͙͔͚̗̭͎̘͚̮͇̭͙͈͚̺͚̭͓̩͚̬̭͈̘͙͚̤̭͔̭͚̫̮͉̭͙̯͚̭͕̘͙̬͚̪͚̭͔̭͙̤͚̩̭͓̮͚͎̮̭͙͚͚̺̭͙͚̪̭͎̭͙͚̹̰̭͌͊͊̓̒͑́̒̒́̓͑̒͆͊́̒̑͂͊͆̓̒́͒̏͒̓̒̏͗͘͏̴̴̨̡͚̫̭͇̘͙͚̩̮͓͇͚̫̮͙͚̬̭͓̗͚̭͉̭͙͚̮͉̭͙͚̬̮͍̭͚̭͓͓͚̫̭̭͙͚̪̭̘͚̫̬̮͎̭͈͚̭͔̘͕͚̩̮̓̒̓͒̓͐̒͒͐̓͌̏͊̒͂͒̈́͂̏̒̒́̏̒͆̓͒͆̓͊̒̒͂̒͊͘͏̸̶̘͙͚̭͚̩̗̭̲͚̩͖̭͎͚̹̭͙͚̹̭̘͓͚̫̭͈̭͍͚̩̭͎̘͙͚̮͇̘͙̖͚̺͚̮̐͂͐̓̒͋̓̒̓̒̏͊͐̓͊͋̒̏̒̏̈́́̓͘͏̴͚̬̮͖̘͙̩͚̤̭͙͚̗̮͓͙̯͚̪̮͙̬͚̪͖̮͖̘̩͚̪̭͓͚̩̮̭͙͚̪̮͓̓̒͊͆́͑̓͂́͊͂͊̓̒̏̓̒͂̏͒͒͐̒͏̴̸̴̴̸̴̨̨̡͚̪̭͓͙͚̹̤̭͖̭͙͚̫̮͈̭͙͚͚̭͍̭͇͚̬̤̭͓͕͚̹̤̭͓͙͚̺̭͉̭͙̦͚̬̭͇̘͙̦͚̬̮͉̘͙͚̭͓̘͚̮͔̭͙͚̩̭̘͚̬̭̘͈͚̹̭͔̘͙̥͚̫̮̏͊͒̓́̒͒̒͊́̏̒͑́͂͆̓͋̒̏͌̒͆͏̸̢̘͙͔͚̮͓͙͚̩̗̭͚̩̭͈̭͙͚̹̮́͒͐͋̓̒̋͊͊͏̴̸̴̸̴̴̵̨̨̘͙͚̫̰̭̭͓͚̫̭͈̭͍͚̭͎̘͚̪͖̮͇̭͙͚̪̭͓͙̣͚̬̮͉͚̰̭͔̭͙͚̫̭͙̯͚̪̤̭̘͙̬͚̪̮͖̘̩͚̬͖̭͓͚̮̭͙͖͚̩̮͓͚̪̭͎͓͚̹̤̭͖͙͚̫̭͈͓͙͚̗̮͓͚̫͚̭͍̘͕͚̬̭͓͙͚̹̭͉̘͙͚̬̮͉̭͙̳͚̬̮͉̘͚̭͔͓͙͚̮͓͙͚̪̗̭͉̘̤͚̬̭̘͈͚̭͔̘͖͚̩̮͑̒̒͂̒̒̔͆͑͆͑̓̒́͂͐̓͐͒̒̓̒͂͂̓͒͐̒͌̏̒͌̓͒̓́͑̒͊̒͆͊̓̓̒́̏́͂͐͆̒͒͌̒͂͒̒͊͘̕͏̸̘͙͖͚̭͚̩̗̮͕̭̦͚̩̭͎͙͚̹̮͓͙͚̺̭͍̘͖͚̫͖̭͈̭͍͚̫͎̭͎̘͙͚̬̤̮͇̭͙͚̺͚̮́͐̓̒̈́̒͊̓̐͊͐͊̒̒̓̋͘͏͚̬̮͓͙͎͚̤̭̓̒͑͆͒́͏̸̴̸̨̨͚̗̮͍͓͙̯͚̩̰̮͕͓͙̬͚̪̭͔̭͙̤͚͎̭͓͚̮̘͙͚̮͓͖͚̪̭͎͚̹̰̭͖͙͚̮͖̭͙͚̩̮͕͓͚̬̰̭͍̘͙͚̹̭͓͙̤͚̺͎̭͉̭͙͚̮͉̭̖͚̬̮͉̭͚̭͔̭͚̮͕͙͚̮̤͚̫̭͈̘͙͚̹̭͔̘̘͚̮̓̒͌́̓́̓̒͂́̓͒̐́͒͐̒̏̓̒̓́̓͆̒͊͌͊́̏̒̒͐́̏̒͑́͂̓͆͂͑̓̒͂͑͂̒́͂̕ͅ͏̸̘͙͕͚̮͓̙͚̩̗̮͕̘͙͖͚̩͖̭͍̭͚̩̰̭́͒̒̒̏͏̸̸͙͚̺͖̭͉̘͖͚̬̭̭͙͔͚͎̭͎̘͙͚̮͇̭͙͚̪̮̓̒͌́͂́̔͆͘͏̴̴̨̢̨̨̘͚̬̮̭͍͚̰̭̘͙͕͚̗̮͇̘͙̯͚̪̤̮͇͙̩͚̪̭͔̭͙̤͚̩̗̭͓̬͚̮̭͙͈͚̺̮͓͚̪̭͍̘͙͓͚̹̰̭͖̭͚̫̭͎͓͙͚͎̭͎̭͚̫̮͔͙͚̹̗̭͓͙͚̫̭͉̘͙̦͚̭͇̘͙͚̬̮͉̭͙͚͚̭͓͚̫̮͙͚̪̗̮̤͚̬̮͎̭͙͚̭͔̘͙͚̬̮̓̒͆͒̒́͒́̓͒̓̒͂͒̏͐̒̏̒̓͒̓́̒͊͒̓͌͊͆́̏͗́͑̒͑̓͐̓͆͐̓̒̏͑͂́͘͏̸̸̧̨̭͙͚̫̗̭͙͚̩̗̭̭͙̗͚̩͖̭͍͓͖͚̩̰̭͖͓͙͚̺͖̮͖͖͚̬̮͓͍͚̭͎̘͙͚̬̤̮͇̭͙͚̪̭͓͙͚̬̮͙̩͚̰̭͙͚̫̭̭͙̯͚̪̭̘͙̩͚̪͖̭͇͙̤͚̬̭͓̫͚̩̮̘͙͈͚̭͙͖͚̪̭͎̭͚̹̤̭͗͐̓͌͋̒̓̒͂͑̒́̋͆͑͆͑̓́͑̓͂͒͐̓̓̓̒̏͒́͒͒̓̏̒͘̕ͅ͏̴̴̴̸̨̨͚̫̮͈͓͙͚̩̭̘͇͚̫͎̭͍̘͙͚̺̭͓͙͚̹̭͉̭͙͚̬̮͉̭͙͚̬̮͍̘͙͚̭̓̒̓͒̓͐̒͌̓͊̈́́̏̕͏̡͚̫̮͓̘͙͚̩̗̭͍̘͚̬̮͙͚̩̰̭͔̘͙̥͚̮̓̒͑̓͆̒͆͑̓͑́͂͏̸̸̘͙͚̮͓͚̩̗̭̘͚̩͖̭͈̭͙͚̩̰̭͇͓͙͚̫̰̮͓͚̫͖̮͓͍͚̭͎̘͙͚̮͇̘͙͚̺͚̮̐͂͒̒̓͋̒̈́̐͒̓̒͑̒͂͂͂̔͘ͅ͏̵̸̴̸̵̨̨̡͚̬̮͖̭͙͚̤̭͓͚̫̭̘͙̯͚̩̰̮͎͙̩͚̪͚̮̘̩͚̭͓͙͇͚̩̮̭͙͓͚̩̮͓͙̳͚̪̮͔̙͚̹̤̭̭͙͚̮͓͓͙͚̗̭͖̘͇͚̫̭͓͕͚̹̭͓͙̤͚̫̭͉̘͙͚̮͉̭͙͚̬̮͍̭͙͚͚̭̘͙͚̭̘͙͚̪͖̮͔͚̬͚̭̘͙͚̭͔̘͚̩̤̮̓̒͆́͑̒͌͒̓͒̒͂͊̓̏͒͐̏̓̒͐́̓́̒͒͒̒͒͊̏͂͂̏͆͗́͑́͂͐͆̓̒͌͑́͊̒͐͘͏̸̸̘͙͓͚̮͓͚̩̗̮͕̘͍͚̩͖̭͎̭͖͚̩̰̮͙͚̹͖̭̭͓͚̫̗̮͎̘͙͔͚̩̭͎̘͙͚̫͚̮͇̘͙̗͚̺͚̭͓͚̬̮͙͚̤̭͓̭͙͕͚̗̭͕͓͙̯͚̪̰̭͕̘͙̬͚̩̰̭͔̭̩͚̪̬̭͓̩͚̬̤̮̭͙́͒̒̔̒̒͒̓͑̒̓͑̒̓͆͑̓̓́́̒̓̒͒͘͏͚̭͚̪̮͔͚̹̰̭́͒͒̓̒͌̏̓̒̕͏̴̨̘͚̫̮͓͙͚̩̮͕͓͚̬̮͕͚̹̭͓͚̭͉̭͙͚̬̭͇̘͚̬̮͍̘͚̭͔̘͚̮͙͚̭͉̘̤͚̫̬̮͙͚̩̭͔̘͚̩̮̒̓͒̓̓͆̒͊͆͐̓̒͊͊̒̔͂͒͆̒̋̒͐́̏̒͑́͂͐̓͆͂͂̒͑̓͑͂̒͐͊͏̸̭͙͚̭͙̐͂͐̓͏̢̨͚̩̗̭̘̺͚̩̭͍̘͙͚̹̭͍͙͚̹̮͕͖͚̫̮͓͙͔͚̭͎̘͚̮͇̭͙͈͚̺͚̮͋̒͊͊̓͒̓̒͑́̓̒̒́̓͘͏̓̒͏̸̸̴̴̴̨̨̨̨͚̬̮͖̭͚̤̭͔͓͙͕͚̫̭͓͙̯͚̪̰̮͇͙̬͚̪͚̭͇͙̤͚̩̭͓̹͚̪̰̮̭͙͙͚̮͓͙̹͚̪̭͓͚̹̤̭͕͓͙͚̭̘͙͚͚̮͖͓͇͚̫̭͍̘͙͚̬̭͓͙͚̬͖̭͉̘͙̦͚̩̭͇̘͙̬͚̬̮͉͓͙͚͚̭͓͚̮͙͚̪̗̭̘̤͚̬͎̭͈̘͙͚̹̭͔̘͕͚̩̮͆̒͑́͒̓̓̓̒͒́͒͐̏͊̒̑́͋̓͂̒͒͌̓͊͂́͑̒͑́͂͒̓͆͊̒͑̒͏̴̴̴̡̡̨̨̭͙͈͚̪͖̭͙͈͚̩̗̭͇̭͙͚̩͖̭͎͚̹̭͙͚̹̭̭͓͚̫̭͈̭͍͚̩͖̭͎̘͚̪͖̮͇̘͙̖͚̺͚̭͓͚̬̭͈̘͙͚̤̭͔͓͙͚̗̮͇̘͙̯͚̩̰̮͙̩͚̪͖̮͖̘̩͚̬͎̭͓̹͚̪͖̮̘͙͚̪̭͔͚̪̭͓͙͚̹̰̭͓͚̫̭͈͙͚̩̮͖͓͚̫̭͓͕͚̹̰̭͓̗͚̬̰̭͉̭͙̣͚̭͇̘͙̳͚̬̮͉̘͔͚̭͓̭͙̥͚̫̭̘͙͚̩̭͈̘̤͚̬̮͙͚̭͔̘͙̥͚̫̰̮͐̓͊̓̒̏͊͐̓͊͑̒̏̒̒̒͑̒͆́͂́͊̓̒̓̒͒̑͒̓̒̏͊͐̒̓͒̓̓̒͊̏͒̒͊̒́̏̒́̏̓͑͆̓̒͆͑̓͑͂͘͏̴̸̴̴̸̢̨̨̨̘͙͚̫̗̮͓͙̗͚̩̗̮͕̘͍͚̩̭͈̭͙͚̩̰̭͍͓͙͚̹̭͍̘͓͚̫̭͈̭͍͚̭͎̘͚̪͖̮͇̭͙͚̪̭͓͉͚̬̮͉͚̤̭͓͙͕͚̗̮͉͙̯͚̪̤̭͕̘͙̬͚̪̮̘̩͚̩̭͓̮͚̬̤̮̘͙͚̩̭͚̪̮͔͙͚̹̤̭͕͙͚̫̭͉͙͚̩̮͔͓͚̫̭͍̘͕͚̗̭͓͙͚̹̭͉̘͙͚̬̮͉̭͔͚̬̮͉̘͙̰͚͚̭͓̭͙̥͚̮͓͙͚̭͓̭̤͚̬͖̭̘͈͚͖̭͔̘͖͚̩̮̒͒̒͊͊̒̒́͒̒̒̓͆͑̒͆͑̓̒́͒́̓̓͒̒̏̓̒͒̐͒̓̒͑̏̓̓͒̓̓͆̒͊̓̒͂͊̓̓̒́́͂͐͆͂̒͌̒͂̒͊͘͏̸̸̢̘͙͖͚̭͚̩̗̭̘̦͚̩̭͎͙͚̹̭͕͓͙͚̺̭͉̘͓͚̬̭͈̭͍͚̪͖̭͎̘͙̯͚͎̮͇̘͙͉͚̺͚̮́͐̓̒͋̒͊̓̐͊͊̒̒́͘͏̴̨̨̡̨͚̬̮͙͎͚̰̭͓̘͚̗̭̭͙̯͚͖̭͕̘͙̩͚̪̭͔̭̩͚̭͓̹͚̩̮̘͙͚̮͓͙͔͚̪̮͔͚̹̰̭͕̭͙͚̮͔̭͙͚̗̭͇̭͚̬̮͔͙͚̺͎̭͓͙͚̭͉̘͙͚̭͇̘͙̣͚̬̭̓̒͋͆͑̓́̒̑́͒͂͒̒͂̓̓̒͆͒̓́͒͐̏̓̒́̓́̒͊̓͌͊́͂̈́͂̏̕͏̘͚͚̭̘͙̥͚̭͓͙͚̪̗̮̤͚̬͎̮͎̭͈͚̭͔̘̘͚̪̮̒͌́͒́͂͋͆͒̓̒̒͂͆̒͊͏̴̨̨̡̨̭͙͚̫̗̮͓̫͚̩̗̭͇̭̖͚̩͖̭͍̘͚̩̰̮͖̭͙͚̹̭̘͓͚̫͎̮͓͙͔͚̭͎̘͙͚̫͚̮͇̭͙͚̩̭͓͙̦͚̬̭͈̭̖͚̰̭͓̭͙͚̗̮͇̘͙̯͚̭̘͙̩͚̪̭͔̭̩͚̬̭͓̮͚̪̰̮̭͙͈͚̺̮͓͙͚̪̭͚̹̰̭͖̭͚̭͍̭͙͚͎̭͎̭͚̫̭͍̘͙͚̫̭͓͙͚̫̭͉̘͙̣͚̭͇̘͚̬̮͉̭͙͚͚̭̭͚̫̮͙͚̮͕͚̫̰̭̘͙͚̭͔̘͙̥͚̪̮͑͒̒̒̒̏̓͊̒͑́̓̓̓͆͑͆̒́͂́͂͊͐͒̒̓̓̒͒̏͐̐̏͊̓̒̒̓́̓́̒͊͒͌͊͊͆͂̏̒͒͗́͑̒͑̓͐̓͆͂͂̓̒͌͑͂͊͘̕͏̴̭͙͈͚̪͖̮͓̭͚̩̗̮͕̘̺͚̩̭͎̘͙͚̩̰̮͖̘͙͚̹̮͕͖͚̬̭̭͙͔͚͖̭͎̘͙͚̪̮͇̭͙̙͚̺͚̮͒̒̒͊̐̓̓̒͌́̈́͆͘͏̴̨͚̬̮͓͙̩͚̤̭͔͚̗̮͖̭͙̯͚̪̰̭̘͙̬͚̪͚̮̘͙̤͚̰̭͓̬͚̮̘͙͚̪̮͓͙͔͚̪̮͔͓͙̓̒͆͒́̓̒͌́͐͒͂̓̒͂͒͒͐̏̕͏̵̨̢̨̡͚̹̤̭͓͚̮͓͙͚͚̮͕͓͚̫̮͙͚̫̭͓͙̱͚̹̭͉̘͙͚̮͉̭͙̳͚̬̮͍̭̙͚͚̭͓̭͙͚̭͙͚̪͚̭͓̭͚̬͖̮͎̭͈͚̭͔̘͚̬̮͐̒̓́͑̓͂̒͊͊͐̓͌̏͊̓́̏̒́́͂͑̓͆̒̒́͒̒͐͂͏̴̸̴̴̴̨̢̨̨̘͙͚͚̪͖̮͓͚̩̗̭̭͙͚̩͖̭͎͙͚̩̰̮͙͚̹̮͔͖͚̬̮͓͍͚̗̭͎̘͙͚̪͖̮͇̘͙̙͚̪̭͓̣͚̬̭͈̘̖͚̰̭͓̘͙͚̫̮̭͙̯͚̩̰̮͍͙̩͚̪͚̮͖̘͙̤͚̭͓͙͇͚̬̤̮̘͙͚̪̭͙͖͚̪̭͎͔͚̹̰̭͕͚̮͈̭͙͚̩̭͇̭͚̫͚̭͓͙͚̭͓͙̤͚̺͎̭͉̭͙͚̭͇̘̗͚̬̮͍̭͙͚͚̭̭͙̥͚̫̮͙͚̪͚̭̭̤͚̫̮͎̭͙͚̩̭͔̘͙̥͚̮͒̒͋͊̓̐͑̓̓̓̒͑̒́̓͆͑̒͆̒́͂͊̓́̓͒͐͒̓̏̓̒̓̒̓́̓͆̒͊͒͌͂͒͊́̏̒͂́͒̓͒̓͆͑̒͑́͂͘ͅ͏̴̴̸̨̨̨̘͙͖͚̫̗̮͓͚̩̗̮͕̘͚̩̭͍͓͙͚̩̰̭͎͓͙͚̫̰̮͓͚̫̮͓͍͚̭͎̘͙͚̪̰̮͇̭͙͚̺͚̭͓͙͚̬̮̭͙͎͚̰̭̭͚̗̮͎̭͙̯͚̪̤̭̘͙̩͚̪͖̭͔̭̩͚̗̭͓͙͇͚̮̭͙͈͚̩̮͓͚̪̭͎͔͚̹̤̭͔̘͙͚̮͇̘͙͚͎̮͒̒̒̈́͊̐͑̓̒͑̒͂͆͂͋͑͆͒́͒̒̑́͐̒́̓́̓͒͐̒͗̏̓̒́̓́͘͏̴̴̨͓͇͚̫̗̭͍̘͕͚̫͖̭͓͙̱͚̫̭͉̘͙͚̬̮͉̭͙̗͚̬̮͍̘͙͚̭͔͚̮͙͚̪̮̤͚̫̮͙͚̩̭͔̘͚̩̮̒̒͊͆̓́̏̓̒͆́͂͐̓͆̓͐̓̒͂͑̓͑͂̒͐͊͏̸̸̴̴̴̨̨̨̡̨̨̘͙͓͚̮͓̘͚̩̗̭̭͙͚̩̭͇̭͖͚̹̮͕̘͙͚̫̤̭͉̘͖͚̬̰̭̭͙͔͚̭͎̘͙͚͎̮͇̭͙̙͚̩̭͓͙̪͚̬̮͖̭̖͚̰̭̭͚̫̭̘͙̯͚͖̮͈͙̩͚̪̭͔̭͙̤͚̭͓͚̪̰̮̘͙͚͚̩̭͚̪̭͎̭͔͚̹̤̭͕̭͚̮͎̘͙͚̩̮͓͇͚̫̭͍̘͕͚̫͎̭͓̗͚̭͉̭͙͚̬̮͉̭͙͚̬̮͍̭͙͓͚̭͔͚̫̭̭͙͚̪̭̘͚̫̮͎̭͈͚̭͔̘͕͚̩̮͂͒̒͋̏͊̒͊̒͌͂͆́͆͑͆̒́͑̒͌͑͂̓͒́̏̓̒͂͒͒̓̒͐̏̒̒͐́̓͐̒̒͊̒͂͒͆̒́̏̓̒͆̓͒͆̓͋̒̒͂̒͊͘ͅ͏̶̭͙͚̪͖̭͚̩̗̮͕̘͙͖͚̩͖̭͎͚̩̰̭̘͙͚̫̰̭͍̘͓͚̫̭͈̭͍͚̩̭͎̘͙͚̮͇̘͙͚̺͚̮͐͐̓̒̓̒̏͊̒̏̒͆́̓͘̕ͅ͏̴̸̸̴̵̨̨̨̨͙̺͚̬̮͓͙̹͚̰̭̘͚̗̮͉͓͙̯͚̩̰̭͖̘͙̬͚̪͖̮͖̘̩͚̪̬̭͓̮͚̫͚̮̭͙͚̪̮͓͙͓͚̪̭͍̘͚̹̤̭͕̘͙͚̭͓͙͚͎̭͇̭͚̫͚̭͓͕͚̫̭͓̗͚̬̰̭͉̘͙͚̬̮͉̭͙͚͚̬̮͉̘͔͚͚̭͓̭͙͚̫̭̘͙͚̪͖̮̤͚̫̮͎̭͙͚̭͔̘͙͚̬̮̓͆͒́͑̒͌́̒̓̒͒͒͐̏̒̑́͋̓́̒͊͒̒͊̒͆̒́̓͑͆͑̓̒͂͑͂͂͏̸̴̴̸̢̨̨̨̢̨̡̭͙͚̮͓͙̗͚̩̗̮͕̭̲͚̩̭͈̭͙͚̹̭͕͓͙͚̫̤̭̭͓͚̫̭̭͍͚̭͎̘͙͚̮͇̭͙͚̪̭͓͙͚̬̮͉͚̤̭͓͙͚̗̭͔̭͙̯͚̪̮͙̩͚̪̭͔̭͙̤͚̗̭͓͙͇͚̪̰̮̘͙͚̪̭͚̪̭͎͓͚̹̤̭͕͓͙͚̫̮͉̭͙͚̩̮͔͓͚̫̭͍̘͙͚̺̭͓͙͚̹̭͉̘͙͚̭͇̘͚̬̮͉̘͚͚̭͓̭͚̮͓͙͚̪̭͉̘͚̫̭̘͈͚͖̭͔̘̘͚̮̓́͒̒͊͊͑̒͌̒́͒̈́́̓̓͆͑̈́͆͑̓̒́͒͂́͊̓̏͂̓͒̐͒̓̒͑̏̒͐͒̓͆̒͊̓͌͆͊̓́̏̒̋̒́̒͆́͂͐͆̓̒͌̒͂̒́͒͘̕͏̸̢̢̭͙͚̫̗̭̖͚̩̗̭̘͚̩͖̭͎͙͚̹̭͓͙͚̺̮͖͓͚̬̮͓͍͚̫͎̭͎̘͙͚̬̤̮͇̘͙͉͚̩̮̒͐̓̒͋̒̓͊͋͊̓̒͑̒̓͆͘͏̸̸̴̨̨͚̬̮͓͙͚̰̭͓͓͚̗̮̭͙̯͚̮͎͙̬͚̩̭͔̭͙̤͚̩̭͓̹͚̮̘͙͚͚̺̭͙̮͚̪̭͎̭͙͚̹̰̭͖͙͚̮͈͓͙͚̩̮͕͓͚̬̰̭͓͕͚̫̭͓͙̤͚̹̭͉̭͙͚̭͇̘͚̬̭̓̒͑͆͒͊́̒͌́͊͂͊̓͆̓̓̒́͒̏͒̓̏͂̓́̓͆̒͊͒̒͊̓́͂̏̒͋͏̸̡̭͙͚͚̭̭͙̥͚̫̭͓͙͚̭͉̘͚̬̭̘͈͚̬̭͔̘͕͚̮͗́͑̓͋͆͂̒̏͌̒͂̒́͒͏̭͙͚̫̗̮͓̫͚̩̗̭̦͚̩͖̭͍̘͚̹̭͓͙͚̫̤̮͔͓͚̫͖̭͈̭͍͚̭͎̘͙͚͎̮͇̘͙͚̺͚̭͓͙̦͚̬̭͈̭̖͚̤̭͔͚̗̮͈̘͙̯͚̩̰̭͑͒̒͋̓̒̒̏͊͋̓̒̒́͂͂́͋͑͆̒́̓̒̑́͘͏̸̨̡̨̘͙̩͚̪̭͔̭͙̤͚̩͖̭͓̫͚̮̭͙͈͚̺̮͓͚̪̭͍̘͙͓͚̹̰̭͖̭͚̫̭̘͙͚͎̭͎̭͇͚̬̤̭͓͕͚̺̭͓͚̹̭͉̭͙͚̮͉̭͉͚̬̮͉̭͚͚̭͓͙̥͚̮̘͙͚̪̗̮͚̬͎̭̘͙͚̭͔̘͙͚̬̮͒̓̒́̓͒̏͐̒̔̏̒̓͒͌̓́̒͒̒͆͊̒̔͆́̏̒̒́͒́͂͒͆͑̓̒͌͑͂͊́̕͏̸̸̸̨̘͙͚̮͓̪͚̩̗̭̭͙̗͚̩͖̭͎̘͚̹̭͕̘͙͚̺͖̭̘͖͚̬̰̮͎̘͍͚̭͎̘͙͚̬̤̮͇̭͙͚̩̭͓͙̤͚̬̮͓͚̰̭͓͙͕͚̫̭̭͙̯͚̪̭̘͙̩͚̪͖̭͇̩͚̩̗̭͓͙͚̮̘͙͈͚̺̭͖͚̪̮͔͓͔͚̹̤̭͐́͒̒͋̒̏͊͋̒̒́̈́̏͆͑͆͒̒̋́͑͒͒̓̒̓͊͂̓͒̏͒̓̒̏̒͘͏̴̨̨̨̨̡͓͚̭͇͙͚͚̮͓͚̫͚̭͍̘͙͚̫̗̭͓͙͚̹̭͉̘͙͚̩̮͉̭͔͚̬̮͍̭̙͚̭͙̥͚̫̮͙͚̪͖̮͚̬̮͙͚̪͎̭͔̘͙̥͚̮̒̓́̓̓͂͑̒͊͌͊͆̒̒́̏͒̓̓͑̓͆͒̓̒͊͑̓͑́͂͏̸̢̭͙͕͚̮͓͍͚̩̗̮͕̘͚̩̭͎̭͙͚̹̮͓͓͙͚̺̭̭͖͚̬̤̮͎̘͙͔͚̫͚̭͎̘͚͎̮͇̘͙͚̩̮́͒̒̒̋͊͊͊͒̒̒̑́͆͘̕͏̸̸̴̵̨̡̨͚̬̮͙͚̤̭͓͙͕͚̫̮͍͙̯͚̪̮͙̬͚̪̮͖̘͙̤͚̩̭͓͙͚̮̭͙͖͚̩̮͓͙̳͚̪̭͎͓͔͚̹̰̭͕͚̮̭͙͚͚̭͍̭͚̫̭͍̘͕͚̹͎̭͓͙̲͚̬͖̭͉̘͙͚̮͉̭͙̱͚̬̮͍̭͚̭͙͚̭̭͙͚̩̗̮͕̤͚̬̮͎̭͈͚̭͔̘͙̥͚̬̮̓̒͆͑̓͊́͑̓͂͋̓̓̏̓͊́͒͐̏̒̓̒̓́͑̓͂̒͊͒̒͊͂̏̒͐́̏͑̓́͂͒͆̓̒̏̒́͂̏͘͏̸̸̸̴̴̨̨̨̨̡̘͙͖͚̮͓̖͚̩̗̭͇̘͙͚̩̭͍͓͙͚̩̰̭͎̭͙͚̫̰̮͓͚̫̮͎̘͍͚̭͎̘͚̪͖̮͇̘͙̗͚̺͚̭͓͚̬̮͙͚̰̭͓͙͕͚̫̮͎͓͙̯͚̪̰̭̘͙̬͚̩̮͖̘͙̤͚̩̭͓̩͚̬̤̮̘͙͚̭͚̪̭͎͓͚̹̤̭͕͙͚̫̮͓͙͚̩̮͔͓͚̬̰̮͕͚̹͚̭͓͙̱͚̭͉̭͙͚̬̭͇̘͚̬̮͍̘͙̰͚͚̭̘͙̥͚̮͙͚̪̭͓̭͚̬̭̘͙͚̩̭͔̘͕͚̬̮͂͒̒͊͊̐͑̓̒̒͂͆̒̒͑̒͊͆͑̓̓́͑͐̓̒͒̑́͒͒̓̒͌̏̒͌̓͒̓̓̒͊͐̓̒͊́͂͆̒̏́͒́͂͐̓͆̓̒͆͌͑͂̒̏͘͏̸̴̴̸̴̢̨̡̨̨̘͙͚̪͖̭͙͓͚̩̗̮͕̭͍͚̩̭͍̘͙͚̹̭͓͙͚̹͖̮͖͚̫̮͓͙͔͚̭͎̘͚̮͇̭͙͉͚̺͚̭͓͙͚̬̮͖̭͚̰̭̭͙͚̫̮͇͓͙̯͚͖̮͙̩͚̪̭͔̭̩͚̬͎̭͓̫͚̩̮̘͙͈͚̭͚͚̪̭͎̭͔͚̹̤̭͕̭͚̫̭͎͓͙͚̩̮͓͚̬̮͔͙͚̬̭͓̗͚̭͉̭͙͚̩̮͉̭͉͚̬̮͍̭͚͚̭̭͚̫̭̭͙͚̮͔̤͚̬̭͈̘͈͚̭͔̘͚̬̮͐͐̓̒͊͊͊͐̓̒͑́̏̒̑́̓͑͆̒͑́͒͂͂͋̓̓̒̓̒̏͒́͒͒̓̒̏̒̒͐͒̓͐̒͊̓͌͆͊̒͂͒̈́̒̒́͒̒͆̓͒͆͂̓̒͒̒͂̒͐́͘͘͏̶̭͙͚̪͖̭͚̩̗̭͓͙͖͚̩͖̭͎͚̹̭͓͓͙͚̹̮͖͓͚̫̭̭͍͚̩͎̭͎̘͙̮͚͎̮͇̘͙̖͚̺͚̮͐͐̓̒͌̓̒̏͊͊̓̒̏͌̒͂͘͏̓̒͏̴̴̸̡̨͚̬̭͈̘͙͚̰̭̭͙͕͚̗̮͈̘͙̯͚̩̰̮͙̩͚̪͖̭͔̭̩͚̗̭͓̮͚̬̤̮̭͙͚̭̗͚̪̭͎̭͚̹̤̭͕̭͚̫̮͔͙͚̩̭͍̭͚̬̬̮͔͙͚̫̤̭͓͚̫̭͉̭͙͚̬̮͉̭̖͚̬̮͉̭͔͚͚̭͓͚̫̭̘͙͚̪͚̮͓̤͚̬̮͎̭͙͚̪̭͔̘͖͚̪̮͆́͒́͊̓̒́̓̒͒͒́͒͒̓̒̏̒̒̓͒̓̓̒͊̓͌͊̒̔̏̈́̒̒́͒̒͑̓͐͆̓̒͊͑̒͊̕͏̢̘͙͔͚̪͖̮͓͙̗͚̩̗̮͕̘͙͚̩̭͈̭͙͚̹̮͒̏͊͊͏̸̸̴̴̸̨̨̨͙͚̫̤̮͖͓͚̫̭͈̭͍͚̭͎̘͚̪͖̮͇̭͙͚̪̭͓͚̬̮͉͚̤̭͓͙͚̫̭͔͙̯͚̪̤̭͕̘͙̬͚̪̭͔̭͙̤͚̭͓͚̮̘͙͖͚̪̮͓͚̪̭͎͚̹̰̭͖̘͚̫̭͈͓͙͚͎̮͔͓͚̫͎̭͍̘͙͚̫͚̭͓͙͚̺͎̭͉̭͙͚̮͉̭͔͚̬̮͉̘͙̰͚͚̭͔̘͚̮͓͙͚̭͓̭̤͚̬̭̘͈͚͖̭͔̘͖͚̮̓̓̒̒́͒̒̒̓͆͑̒͆͑̓̒́͒͂̓̓́̓̒͂͂̓͒͐̒͌̏̓̒͌̒͐͒̓́̒͊͌͊͂̏̒́̒͑́͂͐͆͂̒͊͌̒͂̒͂͂͘͘͏̸̢̨̘͙͖͚̭͚̩̗̮͕̭͚̩̭͎͙͚̹̭͕͓͙͚̫̰̭̘͖͚̫̮͓͙͔͚̫̭͎̘͚͎̮͇̭͙͚͎̮́͐̓̒̒̋͊̓̐͊͋̒͑͆̒̑͂̔́͘͏̸̸̨̨͇͚̬̭͈̭͍͚̰̭͔̭͚̗̮͈̘͙̯͚͖̮͕͓͙̩͚̪͚̮̘͙̤͚̩̭͓̫͚̮̘͙͚̮͓͙͖͚̪̭͎̭͙͚̹̰̭͖͙͚̭͎̘͙͚̩̮͕͓͚̬̰̭͓͙͚̹̭͓͙̤͚̹̭͉̭͙͚̮͉̭͙̘͚̬̭̓̒͆̒́̒͌́͂͒̏̓̒́͒̐́͒͐̏͂̓́̓͆̒͊͒͌͊͊̓̈́͂̏͏̵̡̭͙͚̭͔͙͚̫̭͓͙͚̪̗̮͚̫̬̭̘͈͚̰̭͔̘͚̪͚̮͗́̏̓̓͋͆͐̓̒͌̒͂̒͐͏̸̸̸̴̸̴̨̨̘͙͖͚̮͓̯͚̩̗̭̮͚̩͖̭͍̘͚̩̰̮͕͙͚̺̭̭͓͚̫͖̮͓͙͔͚̩̭͎̘͙͚̪͖̮͇̘͙͚̩̭͓̗͚̬̮̘͙͚̤̭͚̫̮͓͙̯͚̩̰̭͓̘͙̩͚̩̤̮͖̘̩͚͎̭͓̬͚̮̭͙͕͚̺̮͓͚͚̪̮͔͙͚̹̰̭͖͚̫̮͕̭͙͚̩̮͓͓͚̫̮͕͚̹̭͓͙͚̫̭͉̘͙͚̮͉̭͔͚̬̮͉̭͙͚͚̭́͒̒͋̓̒̒̏̓͊͑̒͑̓͋͆͑̒͆͒̓́͑̓̒͌͐̒͂̓̒͂̓͒̏͐̒̏̓̓̒̓͒̓͆̒͊͒͐̓̒͊͆͂̏̒͗́͘͏̵̸̡̨͙͚̫̮͙͚̮͕͚̫̰̭̘͙͚̭͔̘͙̥͚̩̮̓̓͐̓͆͂̓̒͌͑͂͊͏̴̸̭͙͈͚̪͖̮͓̩͚̩̗̭̭͙͎͚̩̭͎̘͙͚̹̭͙͚̹̮͕͖͚̬̭̭͙͔͚͎̭͎̘͚̪̮͇̭͙̖͚̩̭͓͙̫͚̬̮͖̭͙͚̤̭͔̭͚̫̭̭͙̯͚̪̮͖͓͙̩͚̪͖̭͇͙̤͚̬̗̭͓͙͇͚̮̘͙͈͚̺̭͍͚̪̭͎̭͚̹̤̭͒̒͋͊̐͊͊̓̓̓̒͌́̒̒͆͆͑͆̏́̒̑͒͂̓̓́̓͒̏͒̓̒̏̒͘̕͏̴̴̸̨̡͚̫̭͍͓͙͚͚̮͓͇͚̬̭͓͙͚̺̭͓͙͚̹̭͉̘͙͚̭͇̘͙͚̬̮͉͓͔͚͚̭͔̘͚̭͔̭͙͚̪͖̭̭͚̬͖̮͙͚̩̤̭͔̘͙̥͚̬̮̓̒̓͒̓͂͑̒͂͒͌͊͆́̏͆̒́̒͆́͂͆͑̒͑̓͑̏͏̢̘͙͚̪͖̮͓̫͚̩̗̭̭̺͚̩͖̭͈͙͚̹̮͗͒̒͋̒̓͊͏̴͓͙͚̺̮͓͖͚̬̭̭͙͔͚̫͚̭͎̘͚͎̮͇̭͙͈͚̺͚̮͊̓̒͌̒̑́͘͏̸̴̴̨̢̨͚̬̮͚̤̭͓͙͕͚̫̮͙̯͚̩̰̮͇͙̬͚̪̮͖̘͙̤͚̪̭͓͚̬̤̮̭͙͖͚̩̮͓͙̮͚̪̭͎͔͚̹̰̭͕͓͚̮͓̘͙͚̩̭͇̭͚̫͚̭͓͕͚̺̭͓͙̤͚̺͎̭͉̭͙͚̮͉̭͙̬͚̬̮͍̭͙͚͚̭͓̘͚̫̮͙͚̩̗̭͍̘̤͚̫̤̭͈̘͙͚̭͔̘͚̩̤̮̓̒͆͑̓̒̋́͑͌̓̓̓̏̓̒͂͒͐̏̓̒̒̓́̓͆̒͊͒̒͆͊͂̏͂́̒͑̓͒̓͆̒͑́̒͐͘͏̸̴̴̢̘͙͓͚̮͓͙͓͚̩̗̮͕̘͙͚͚̩͖̭͎̭͙͚̹̮͖͓͙͚̹͖̮͓͚̫̮͓͙͔͚̫͖̭͎̘͙̮͚̩̮͇̭͙͚̪̭͓͚̬̭͈̘͙͚̤̭͓̘͚̗̭͖̘͙̯͚̮͓͙̩͚̩̭͇̩͚̭͓̫͚̩̮̭͙͈͚̩̮͓́͒͊͒̓̒͒͑̏͌͆͑̒̐͆̓́̒͌́͂͊͐̓̒́͂̓̒̏͒͐̒͘͏̸͚̪̭͎͔͚̹̤̭͕̭͙͚̫̭͇͙͚͎̮̏̓̒͒̓̓́͏̴̸̴̨̨̢̨̡͓͇͚̫̗̭͓͕͚̬̭͓͙͚̭͉̭͙͚̩̮͉̭͙͚̬̮͍̘͙͚͚̭̭͚̭͍͙͚̭͍̘͚̬̭͈̘͙͚̩̬̭͔̘͚̩̮̒͒̒͆͊͂͒͂́͑̒͆́͂̓͆͂̒͊͑̒͐͏̸̴̴̴̨̨̨̨̨̨̭͙͚̪͖̭͚̩̗̭̘͙͖͚̩͖̭͎͓͚̹̮̘͙͚̹̭͓̭͖͚̫̮͎̘͙͔͚̫̭͎̘͙͚͎̮͇̭͙͈͚̺͚̭͓͙̣͚̬̮͖̭͚̰̭̭͙͚̫̮͕͓͙̯͚̪̰̮͇͙̬͚̪̮̘̩͚̭͓̹͚̮̭͙͙͚̪̮͓͙͚̪̭͓͙͚̹̰̭͖̘͙͚̮͓͙͚͎̭͈̭͇͚̫̮͕͚̺̭͓̗͚̭͉̘͙̪͚̩̮͉̭͙͚̬̮͍̭͙͓͚̭͔̘͚̫̭̭͙͚̪̭͍̘̤͚̬̭͈̘͈͚̭͔̘͚̫̮͗͐̓̒́͋̒̏͊͒̓̒̓̓͂͑͆̒͑́͒͂̓͒͒̒́̓̓̒͂̓͒͐͐̏͊́͑̓́̒͐̓̒͒͊̒́͂̒́̏̒͑̓͒͆̓̒̓̒͂̒͐͆͘͏̭͙͚̪͖̭̺͚̩̗̮͕̘̺͚̩͖̭͎͚̩̰̭͎̘͙͚̹͖̭̘͓͚̫̭̭͍͚̪̬̭͎̘͙͚̮͇̘͙̖͚̺͚̮͐͐̓̒̒̓̒̏͋̒̏͌̒́̓͘ͅ͏̴̸̨̨̨̢̨̨̡̘͚̬̮͖̘͙͚̤̭͓͙͕͚̗̮͉͓͙̯͚̪̮͙̬͚̪͖̮͖̘͙̤͚͚̭͓͚̩̮̭͙͚̩̮͓͕͚̪̮͔͙͚̹̤̭͖̭͙͚̮͙͚͎̭͇̭͚̫͚̭͍̘͕͚̹̭͓̗͚̬̰̭͉̘͙͚̩̭͇̘͔͚̬̮͉̘͔͚͚̭͔̘͙̥͚̫̭̘͙͚̪͖̮͔͚̫̮͙͚̪̗̭͔̘͓͚̬̮̓̒͆̒́͑́͊̓͂̓̒͂̏͒͒͐̒̏̓́͑̓̓́̒͊̒͒͊̒̒̒́̓͑͆̓̒͂͑̓͑̒́͏̸̵̸̸̴̴̸̵̴̨̨̨̨̡̭͙͙͚̭͙͚̩̗̭̘͙͚͚̩̭͎̭͚̩̰̭͈͓͙͚̹̮͕͓͚̫̗̭͈̭͍͚̗̭͎̘͚̪̮͇̭͙͚̪̭͓͚̬̭͈̭͙͚̤̭͓̭͚̫̭͕͙̯͚̪̤̭̘͙̬͚̪͚̮͖̘͙̤͚̭͓͚̮̘͙͕͚̩̮͓͚̪̮͔͓͚̹̤̭͙͚̫̭͈͓͙͚̗̮͓͚̫͎̭͍̘͙͚̫͚̭͓͙͚̹̭͉̭͙͚̩̭͇̘͙͚̬̮͉͓͙͚̭͙͚̮͓͙͚̪̭͉̘͚̫̮͈͚͖̭͔̘͖͚̪̮́͐̓͒͋͊̒̏͊̓̒̒́̒̒͆͆͑̒̑͆́̒͌̓͐́̓̒͂͂̓͒͐̒͌̏̒͐̓͒̓́͑̒͊͌͊͂̋́̏͒̓́͂͐͆̓̒͂͑̓̒͂̒͘̕̕͏̴̸̴̢̨̨̭͙͚̫̗̭͚̩̗̮͕̘͚̩̭͎͙͚̩̰̭͈̘͙͚̹̭̘͖͚̫̮͎̘͙͔͚̬̭͎̘͙͚̮͇̭͙͚͎̭͓͙͚̬̭͈̭͍͚̤̭͓͚̗̮͈̭͙̯͚̮͎͙̬͚̪̭͔̭͙̤͚̩̤̭͓̹͚̪̰̮̘͙͚̺̮͓͙͕͚̪̮͔͓͙͓͚̹̰̭͖͓͙͚̫̮͇̭͙͚̩̮͕͓͚̬̰̭͍̘͙͚̹͚̭͓͙̤͚̺͎̭͉̭͙͚̬̭͇̘͙͚̬̭͑͐̓̒̒̈́͊̓̐̓͊̒͂́̓̓́͑́͆̒́͑̒͌́͂͊̓̓̓̒͒̐̏͐̏͒̓͆̒͊͌͊̓͂͘͏̭͚͚̭̘͚̫̭͓͙͚̮͕̤͚̬͎̮͈͚̰̭͔̘͕͚̗̮̒͐́͑̒͑̓͋͆͂͂̓̒͑̓̒͂̒͂͏̶̢̭͙͚̫̗̮͓͚̩̗̭͇̭͙͚̩͖̭͇̭͙͚̩̰̭͕͓͙͚̺͖̭̭͓͚̫͚̭͈̭͙͔͚̩͖̭͎̘͙̯͚̬̤̮͇̭͙͈͚͎̮̐͒̒̏͒̒́͘͏̴̴̸̸̨̨͚̬̮̭͙̥͚̤̭͓̭͚̗̮͓͙̯͚̪̤̭̘͙̩͚̩̮͖̘͙̤͚̩̭͓̫͚̫͚̮̭͙͚̩̮͓͓͚̪̭͚̹̰̭͕̭͙͚̫̮͕͙͚̭͎̭͚̫͖̮͕͚̬̭͓̗͚̬͖̭͉̭͙͚̩̮͉̭͚̬̭̓̒͌͆͒́̒̑́͐͑͂̓̒͒͑͐̒̏͊̓̒͐͒̓̓́̏̒͊͐̓̒͊̒̒̕ͅ͏̴̘͚͚̭̭͚̫̭͓͙͚̪̮͖̤͚̫̭̘͈͚̪͎̭͔̘͖͚̬̮̒͐́͑̒͆̓͊͆̓̓̒͌̒̒́͏̴̸̨̘͙͙͚̫̗̮͓͚̩̗̭̘̦͚̩͖̭͍̘͖͚̹̭̘͙͚̫̤̭͍̘͖͚̬̭̭͍͚̪̭͎̘͙͚̪͖̮͇̘͙͇͚̩̭͓͚̬̮͖̭͙̹͚̰̭͚̫̮͈̭͙̯͚̪̤̭͕̘͙̩͚̩̮̘̩͚͖̭͓̬͚̪̮̭͙͚̮͓͙̺͚̪̮͔͙̰͚̹̤̭͖͓͚̫̭͉͙͚̩̭͒̒͋̒̒͊͊̒͌̒̈́͆͑̒͂͆́͒̓̒̑͂͒̒́̓̒͆͒̑́͒͐̏̓̒͐͒̓̓͆͘ͅ͏̧̨̡̘͇͚̬̤̭͍̘͙͚̹̰̭͓̗͚̬͖̭͉̭͙͚̭͇̘͙̬͚̬̮͍̘͙̬͚͚̭͔̘͚̭̘͙͚̩̗̭̭͚̫̰̮͎̭͈͚̭͔̘͚̮̒͌͊̒́̏́̒͆́͂͌͆͒̒̒͂͂̒͐͂͒͏̴̭͙͚̪͖̮͓͙͚̩̗̭͇̘͙͚̩͖̭͈̘͙͚̩̰̮͓͙͚̹̮͖͚̫̮͎̘͍͚̭͎̘͚̫͚̮͇̘͙̙͚̪̮͗͒͒̏̐͒̓͒̓̒̏̒͂̒̑͆͘͏̸̸̨̡̨̡͙͚̬̭͈̘̖͚̰̭͓̘͙͕͚̫̭͓͙̯͚̩̰̮͙̩͚̪̭͇̩͚̬͚̭͓͙͇͚̬̤̮̭͙͚̭͙̳͚̪̮͔͓͙̬͚̹̤̭͓͙͚̮͓̘͙͚̗̮͕͓͚̫̮͕͚̹̭͓͙͚̫̭͉̘͙͚̮͉̭͙̣͚̬̮͙͚͚̭̭͚̫̭͓͙͚̪͚̭͈̘͚̬̮͙͚̭͔̘͖͚̪̮̓͆̒́͒͊̓̏̓̒̓͒̑́͒͒̓̏͐́̓́̒͊̏͐̓̒͒͊͆͂͂̏͊̓͂́͑̒͑̓͊͆̒͆͑̓͑͂̏̒͊ͅ͏̸̨̘͙͚̫̗̮͓͚̩̗̭͇̘̖͚̩͖̭͎͓͚̩̰̭͈̘͙͚̹͖̮͖͚̬̬̮͓͙͔͚͖̭͎̘͙̮͚͎̮͇̘͙̘͚̪̭͓͚̬̮̭̖͚̤̭͔͙͕͚̫̭̘͙̯͚̪̮͍͙̩͚̪̮̘̩͚͖̭͓͙͚̬̤̮̭͙͑͒̒̋̒̒̏͑̓̒͑͂́͆͑̒̒͆͒̒́̓͑̓͊͒̒͂̓͊͒͘͏͚̺̭͙̩͚̪̭͎͓͚̹̰̭̏͒̓̏̒͘͏̸̸̨̨̨̭͙͚̫̭͍͓͙͚͚̭͉̭͇͚̫̮͕͚̗̭͓͙̱͚̹̭͉̭͙̣͚̮͉̭͚̬̮͍̭͚̭͔̘͚̫̮͕̭͙͚̪̗̮͖̤͚̫̭͈̘͙͚̩̭͔̘͚̪͚̮͒̓́̒̏͐̓̒͂͊͂̏̒͒̒̑́̏̒͆̓͆̓̒͑̒̏͏̸̸̘͙͚̭͚̩̗̭̭͙͖͚̩̭͈̘͚̩̰̭͕͓͙͚̹̮͔͖͚̫̮͎̘͍͚̪̗̭͎̘͙͚̮͇̭͙͈͚̩̮̓͂͐̓̒̈́͋͊̒̏͒̓̒̓̒̓́͆͘͏͙͚̬̭͈̘͙͚̤̭͓̭͙͚̗̭̓́͆̏́͂́͏̸̸̸̵̨̨̨̘͙̯͚̪̭͕̘͙̩͚̩͎̮̘͙̤͚̪̤̭͓̹͚̮̭͙͚̮͓͙͚̪̭͍̘͚̹̤̭͔̘͙͚̭͙͚̮͓͓͇͚̫͚̮͔͙͚͖̭͓͚̫͖̭͉̘͙̪͚̭͇̘͙̹͚̬̮͉͓͙͚͚̭̘͙͚̫̭͙͚̪̗̮͔̤͚̬̮͙͚̪͎̭͔̘͚̮͒̓̒͂͒͗́͒͐͂̏̒́͋̓̓͂̏̒̓͌͂͊̒̔͂̏́͒̓͌̓͆̓̒͒͑̓͑̒̏́͂̕͏̸̴̴̸̵̸̧̨̡̨̡̘͙͚̭͚̩̗̭͓͙͎͚̩͖̭͉͖͚̹̭͕̘͙͚̫̤̭̭͓͚̫̮͓͙͔͚̫̭͎̘͙̮͚̫̮͇̭͙͚͎̭͓͚̬̮͖̘͙̹͚̤̭͓̘͚̗̮͉̭͙̯͚̩̰̮͈͙̬͚̩̮͖̘͙̤͚̬̭͓̮͚̬̤̮̭͙͈͚̪̭͙̪͚̪̭͎̭͙͚̹̰̭͓͙͚̫̭͈̘͙͚̭͍̭͚̫̗̭͍̘͕͚̭͓͙̱͚̹̭͉̭͙͚̭͇̘͙͚̬̮͉̭͙͚͚̭͓̭͙͚̫̭͈͙͚̪͚̭̭͚̫̤̮͙͚̭͔̘͙̥͚̬̮̑͂͐̓̒͌̓̒͊͒̒͒͑̏͊͋́͑̒͂͆́̒̑́̓͂͒̓̒͒͒̓̏͐͒̓́̏̒͊̒͂͒͊͂̏́͗́̓̓͆͑̒͑̓͑͂͂͘͏̸̸̨̧̨̨̘͙͕͚̮͓͙̘͚̩̗̮͕̘̺͚̩̭͎̭͙͚̩̰̭͓͙͚̹̮͔͓͚̫̭͈̭͙͔͚̪̭͎̘͚̮͇̘͙͚̪̭͓͙̳͚̬̮̘͚̤̭͓̭͙͚̗̮͓͙̯͚̪̰̭̘͙̩͚̩̤̮̘͙̤͚̭͓̹͚̩͖̮̘͙͕͚̮͓͙̮͚̪̮͔͓͙͓͚̹̰̭͖̘͙͚̫̮͖͓͙͚͚̮͓͇͚̬̤̮͕͚̭͓͙̱͚̹̭͉̭͙͚̩̭͇̘͚͚̬̭́͒̒͊̐͊̓̓̒̏͊̒̒͂̓̏͆͑͆͒̒͑́͂́͊͑͒́͂̓̒͒́͒͐̏͒̓͂͑̒͐̓̒́͂͊̒͘͏̨̭͚͚̭͓͓͙̥͚̭͓͙͚̮͕̤͚̬̮͎̭͈͚̩̰̭͔̘͙͚̗̮̒̑́́͂͌͆͂͂̓̒̓̒͂͏̸̢̭͙͙͚̮͓͙̗͚̩̗̮͕̭̖͚̩̭͈͙͚̹̮͕͙͚̫̰̮͓͖͚̫͎̭̭͍͚̪̭͎̘͙̯͚̮͇̭͙͚̪̮́͒̒͊̓͊̓̓̒͌̒͊́̓̔͆͘͏̴̸͉͚̬̮͖̘͙̹͚̰̭͓͓͙͚̗̮͍͙̯͚̩̰̮͙̬͚̩̮̘̩͚̭͓̫͚̪̮̭͙͚̺̭͙̬͚̪̮͔͙͚̹̰̭̓̒͆́͂́̓͋̓͒̒͂̏̓̒͆͒͒̏͒̓̏̓͏̨̡̧̨͙͚̫̮͉̭͙͚͚̭͉̭͚̫͎̭͍̘͙͚̫͎̭͓͙͚̫̭͉̘͙͚̮͉̭͈͚̬̭̓͒̓͂̒͊͌͊͆́̏̒͏̸̴̨̭̙͚̭͓̭͚̫̭͔̭͙͚̮̤͚̫̮͈͚̩̭͔̘̘͚̪̮̒́̏̒͑̓͆͂͂͐̓̒͑̓̒̒͏̸̸̴̸̴̢̨̨̘͙͈͚̮͓̘͚̩̗̭͇̭͙͎͚̩͖̭͉͙͚̹̮̘͙͚̫̰̮͕͓͚̫̭͈̭͙͔͚̩̭͎̘͙͚͎̮͇̘͙͚̩̭͓͚̬̮̘͙͚̰̭͓͙͚̫̭͕͙̯͚̪̰̮͖͓͙̬͚̪̗̭͇͙̤͚̩̭͓͙͚̪̮̘͙͚͚̭͙͚̪̭͙͚̹̤̭͓͙͚̫̮͓͙͚̩̮͕͓͇͚̬̮͕͚̬͖̭͓̗͚̬͖̭͉̭͙̥͚̩̭͇̘͙͚̬̭́͒̒̓͊͑̓̒͊̓̓͂͌͆͑̒͂͆͒̒́͑͂̓̓͆̓͊͆͒́͒͒̓͒̏͊̓͐͒̓̓̒͆͐̓̒͊̒́͘͏̭͙͏͚͚̭́͏̵̸̡͙͚̮̭͙͚̩̮͕͚̬̭̘͙͚̪̭͔̘͚̬̮̓́͂͑͆̓̓̒͆͌͑̒͐́͏̭͙͕͚̫̗̭͚̩̗̭̭͙͎͚̩͖̭͍͓͙͚̹̭͎̘͙͚̹̮͖͖͚̬̤̭͈̭͍͚̪̭͎̘͙͚͎̮͇̭͙̖͚͎̮͐̓̒̐͋̐͊͒̓̒̒͊͂́͘ͅ͏̴̸̴̨̨̨̡̖͚̬̮͖̭̖͚̰̭̭͙͕͚̗̭͖̭͙̯͚̪̤̭͓̘͙̩͚̩̭͔̭͙̤͚̬̭͓̫͚̮̘͙͚̭͚̪̭͎͚̹̰̭͖͓͚̭͇͓͙͚̩̭̘͚̫̭͓͙͚̺͖̭͓͙͚̬̭͉̭͙̪͚̩̮͉̭͙͚̬̮͍̭͙͚͚̭͔͓͚̭͍͙͚̪͚̭͉̘͚̫̰̮͎̭͈͚̰̭͔̘͚̩̮̓̒͆̒́͑́́̓̒͂͒͒́͒͒̓̒̐̏̓̒̒͐́̓͆͐̒͊͒͒͌͊̏͌͂́̒͑́͂̓͆̒̒́̒̏͊͘͏̘͙͚̪͖̮͓̺͚̩̗̮͕̘̲͚̩͖̭͈̭͖͚̩̰̭͎͓͙͚̺̭̘͖͚̬̰̭͈̭͙͔͚̩̭͎̘͙͚͎̮͇̘͙͈͚͎̮̒͒̒̒̒͊͊̒̓̈́́́͘͏̴͙͚̬̮͖̘͙͚̰̭͙͕͚̗̭̘͙̯͚̩̤̮͍͙̬͚̩͎̭͇͙̤͚̗̭͓͙͚̫̮̘͙͚̭͙̓͆̓́͑̓́͐̓̓́̓͊͊͒͗́͒͒̓͏̸̨̨̨͚̪̭͎̙͚̹̤̭͓͚̮͉̭͙͚͚̭͍̭͇͚̫̭͓͙͚̬̭͓̗͚̬̭͉̭͙͚̩̮͉̭͙̮͚̬̭̏̓̒͐̒̓́̓͂̒͊͒͌͊̒̏͆͏̴̴̡̘͙͚͚̭̘͙̥͚̭͓̭͙͚̪͚̭̘͚̫̤̮͙͚̹̭͔̘͓͚̩̮́͒́͂͆͌̒͑̓͑̒͊͏̶̭͙͚̫̗̮͓͉͚̩̗̭͇̭͙͚̩̭͈̘͖͚̩̰̭͇̘͙͚̹̮͖͚̬̭͈̭͙͔͚͚̭͎̘͙͚̩̮͇̘͙̙͚̩̭͓͙͚̬̮̘͉͚̤̭͔͓͙͕͚̗̮͎̘͙̯͚̪̰̮͕͓͙̩͚̪̭͔̭̩͚͚̭͓͙͚͎̮̘͙͚̭͙͚̪̭͎͓͚̹̰̭̐͒̒͒͊̒͊͐̓̒͆͂͂͆͆͑̓͆͒̒́́̏̒͂̓͊́͒͗́͒͒̓̏̒͘͘͏̸̴̴̨͙͚̫̮͙͚͚̭͎̭͚̬̬̭͍̘͕͚̗̭͓͙͚̫̭͉̭͙̤͚̮͉̭͙͚̬̭̓͒͐̓̓́̒͊̒͂͊̏́̏͏̡̭͚̭͓͓͚̭͙͚̪̗̭̭͚̫̮͎̭͈͚̤̭͔̘͕͚̩̤̮̒́̏̒͑́͂͊̓͆͒̒͂̒́̒͘͏̸̘͙͈͚̭͙͉͚̩̗̭͓͚̩̭͇̘͚̹̭̘͙͚̫̰̭͉̘͖͚̫̗̭͈̭͍͚̪̭͎̘͙͚̫͚̮͇̘͙͚̺͚̭͓͙̪͚̬̭͈̘͍͚̤̭͓̭͚̗̭͂͐̓͌̒̋͊̒̏͊͋̒̒̓̈́͑͆̒́̒̑́͘̕͏̴̸̸̴̵̸̸̨̨̨̡͓͙̯͚̪̰̭̘͙̩͚̩̮͖̘̩͚͎̭͓̮͚̪̮̘͙͚̩̮͓͙̳͚̪̭͚̹̤̭̭͙͚̮͖̘͙͚͚̭͖̘͇͚̫̭͍̘͕͚̹̭͓͚̬͖̭͉̘͙̦͚̩̭͇̘͙̬͚̬̮͉͓͙͚͚̭̘͙͚̮͓̘͙͚̭̘͚̫̭̘͈͚̭͔̘̘͚̩̮͒͂̒͂̓̒͆͒͒͐̏͊̓̒̑͐́̓͂̒͒̒͊̒̔́͑́͂͆͂͌̒͌̒́͊̒͊͏̸̢̘͙͚̮͓͙͉͚̩̗̭͓͚̩̭͎͓͙͚̩̰̭͍͓͙͚̫̤̭̭͖͚̬̤̮͓͙͔͚̫̭͎̘͚̮͇̘͙̖͚̩̮̐́͒͌̒̈́͊͒̒͑͊̒̒́̓͆͘͏̸̴̴̵̨̨͚̬̮͖̘͙̹͚̰̭̘͚̫̭̭͙̯͚̭̘͙̩͚̪̮̘̩͚̪̭͓̫͚̩͖̮̭͙͈͚̪̭͙̩͚̪̭͓͚̹̰̭͖̘͙͚̫̭͍̘͙͚͚̮͓͇͚̬̮͙͚̬͎̭͓͙̱͚̗̭͉̭͙̪͚̭͇̘͙̹͚̬̮͉̭͚͚̭̘͙͚̫̭͍͙͚̩̮̤͚̬͖̭͈̘͈͚̩̭͔̘͓͚̩̮̓̒̑͆́͒̒̑͐͂͊͐̏͒̒͒̓̒͒͒̓̏͊̒͒̓́͑̒͐̓͌͊͂́̏̒̑́͑̓̓͆̓͒̓̒̒͆̒͊͘͏̭͙͚̫̗̮͓͙͕͚̩̗̭͚̩̭͍̭͖͚̹̮͕͙͚̹̮͔͖͚̬̭̭͙͔͚̪̭͎̘͙̮͚̫͚̮͇̭͙̘͚͎̮̑͒͋̓̒̋͊̒͊̓̓̓̒͂͌̓́͘͏̴̧͚̬̮̭͙͚̤̭̭͙͚̗̮͉͓͙̯͚̪̤̭͓̘͙̩͚̩̬̮͖̘͙̤͚̬̭͓̹͚͎̮̘͙͚͚̩̮͓͙͚̪̭͎͓͙͓͚̹̰̭̓̒͆͒̒́͑͂́̓̓̒͂͒͐́̏͏̸̴̴̡̨̨̡͙͚̫̮̘͙͚͚̮͖͓͚̬̮͔͕͚̬̭͓͚̺̭͉̭͙͚̮͉̭͚̬̮͉̭͙͚̭͔͓͙̥͚̭͉͓͙͚̪̗̮͚̫̤̭̘͈͚̗̭͔̘͙̥͚̩̮̓͒͐̓͂̒͊͆̓̒͊̒̔̓́̏̒͐́̏́͂͆͐̓̒͌̒͂͏̸̘͙͚̪͖̮͓͙͎͚̩̗̭͙̗͚̩̭͈͙͚̹̭͓͓͙͚̹̮͖͖͚̫̗̮͎̘͍͚̩̗̭͎̘͚̮͇̘͙͚̺͚̮͑͒͋̓͊̓̐͊̓̓̒̒̒̑́̏͘͏̸̨̖͚̬̮͙͚̤̭͓͙͚̫̭͙̯͚̮͓͙̬͚̩͎̭͇̩͚̭͓͚͎̮̭͙͕͚̭͙͚̪̭͎͓͚̹̰̭̓̒͆͑̓͊́͑͂͐̓͂͊͐̓̒͂͊̓̒͂́͒́͒͒̓̏̒͐͏̨͓͙͚̫̭͇̭͙͚͚̭͒̓͂͏̨̨̘͇͚̫͖̭͍̘͙͚̫̬̭͓͙̲͚̫͖̭͉̘͙̥͚̩̭͇̘͚̬̭̒͌͊̒͒͏̸̴̭͙͚͚̭͔͚̫̭̘͙͚̪̮͕̤͚̬̭̘͈͚͎̭͔̘͚̩̮́̓̒͑̓͒͆̓̓̒͆͌̒́̒̏͏̭͙͏̸̨͚̭͙͈͚̩̗̭͓͚̩͖̭͉͚̹̭͙͚̺̭͈̘͓͚̫̭͈̭͙͔͚͖̭͎̘͚̬̤̮͇̭͙͚͎̭͓͙̩͚̬̮̭͙̹͚̤̭͔͚̗̭̘͙̯͚̪̰̭͖̘͙̩͚̩̬̭͔̭͙̤͚̭͓͙͇͚̮̭͙͖͚̺̭͙̹͚̪̭͍̘͙͂͐̓͌̒̋̓̒̏͊͐̓͊̒̓͂̒̑̓́͑͆͒́̓̒͌́͒́͊̓͂͒̏͒̓̏͘͏͚̹̤̭͏̸̴̸̨̡̭͚̫̭͓͙͚̭͎̭͚̫̮͕͚̬̭͓͙͚̬͖̭͉̭͙͚̭͇̘͙̳͚̬̮͚͚̭͓͙̥͚̫̮͖͙͚̪̗̭̘͚̫̮͙͚̪͚̭͔̘͙̥͚̮̒͐͒͌̓́̏̒͊̏͐̓̒͊͂́̏͊̓̒͌́͑̓̓͆͋̒͑̓͑́͒͏̭͙͓͚̫̗̮͓͚̩̗̭̘͍͚̩̭͉͚̩̰̮͒̒̋͋̒͊̓̒̏͏̸̨͙͚̫̤̭͈̘͓͚̫͖̭͈̭͙͔͚̬̭͎̘͙͚̩͖̮͇̭͙̘͚͎̭͓͙̤͚̬̮͖̭͙͚̰̭̘͙͕͚̫̮͈͙̯͚̪̤̭̘͙̬͚̪͚̮͖̘̩͚̭͓̫͚̮̘͙͚̮͓͙̮͚̪̮͔͔͚̹̤̭̓̒͂̈́́͑͆̏́͑̓͒̒́̏̓̒͂͒͒́͒͐̏̓̒͘͏̴̴̨̨̨̨͓͚̮͔̭͙͚͚̮͓͚̫͚̭͍̘͙͚̭͓͙͚̹̭͉̘͙͚̮͉̭͙̳͚̬̮͍̭͙͚̭͙̥͚̭͙͚̩̗̭͉̘̤͚̫̭͈̘͈͚̭͔̘͚̮̒̓́̓͂͑̒͊͌͂͒͊̓͂̏́̏͑̓́͂͑̓͆̒̒́͒̒͐͂͂͏̸̭͙͈͚̮͓͚̩̗̭̭͙̗͚̩͖̭͎͙͚̹̮́͒̒͋̓̐͊ͅ͏̴͙͚̹̭͉̘͖͚̬̮͎̘͍͚̭͎̘͙͚̫̮͇̘͙͇͚͎̮̓͒̒̒́͆̈́͊́͘͏̓̒͏̸̴̴̨͚̬̮͓͉͚̤̭̭͙͚̫̮͉̭͙̯͚̩̰̮͙̩͚̪͚̭͔̭͙̤͚̭͓͙͇͚̬̤̮̭͙͚̩̭͙̳͚̪̭͎͓͙͚̹̰̭͖̘͚̮͓̘͙͚̗̭͆͒̒́͑͂͊̓́̓͒͑͒̓̏͗̒̓́̓́͏̨̡̘͚̫̮͕͚̹̭͓͙̲͚̺͎̭͉̘͙͚̮͉̭͙͚̬̮͉͓͙͓͚͚̭̘͙̥͚̮͓͙͚̪͖̭͉̘͚̫̤̮͙͚̺̭͔̘͙̥͚̬̮̒͊̏͐̓̒͒͊͂͂̏͆́͑́͂͑͆̒͑̓͑̏͂͏̸̶̴̨̭͙͚̮͓̤͚̩̗̭͇̘͙̗͚̩̭͍͓͙͚̩̰̭͉̘͙͚̹͖̮͓͓͚̫̮͓͍͚͎̭͎̘͚̪͖̮͇̘͙̗͚̺͚̭͓͙͚̬̮͙͚̰̭͓͚̗̭̘͙̯͚̪̰̭̘͙̬͚̩̭͇̩͚̭͓̩͚̬̤̮̭͙͐͂͒̒͊̐̓̒͑̒́̒̒͑͆͑̓̓́͑̒̑́͒͐̓̒́̓̓̒͒͘͏̴͚̩̭͚̪̮͔͙̬͚̹̤̭͒̓̒͌̏̓͏̴̸̡̨̨̨̘͚̫̮͙͚͚̭͎̭͇͚̫̮͔͙͚̬̭͓͙͚̬͖̭͉̭͙͚̭͇̘͎͚̬̮͍̭͚̭͔̭͚̫̮͓͙͚̮̤͚̫̭̘͈͚̭͔̘͙͚̮̒͐͒͑̓̓́̒̏̓͌͒͊͂̏̒̒̑́̏̒͆̓̓͆͂͂͑̓̒͌̒́͂͂͏̨̭͙͚͚̫̗̮͓͙͚̩̗̭̘̺͚̩͖̭͇͚̹̮͙͚̹͖̭̘͖͚̫̮͓͍͚̩̗̭͎̘͙͚̪͖̮͇̭͙͈͚̺͚̮͒̏͋̒̓̒̏͊͒̓͊̒͑̒̈́͘͏̸͚͚̬̮͖̭͚̤̭͓͓͙͕͚̫̮̓̒͆̒͑́͏̴͓͙̯͚̪̰̮͇͙̬͚̪̭͔̭̩͚̪̬̭͓̹͚̮̭͙͙͚̩̮͓͙͚̪̭͓͙̬͚̹̰̭̓̓̒̓̒͂̓͒͐͐̏͊͏̴̸̴̨̨̨̨̡͓͙͚̮͓͙͚͎̮͔͓͇͚̫̮͕͚̫̭͓̗͚̭͉̘͙͚̬̭͇̘͙̥͚̬̮͍̭͙͚̭͔̭͙̥͚̮͔͓͙͚̭͈̘͚̫̭͈̘͙͚̹̰̭͔̘̘͚̫̮́͑̓́̒͊͐̓̒͂͊̒͂͒͗́̏́͂͆͂̒͑̒͆͏̸̴̴̴̨̨̨̢̨̘͙͚̪͖̮͓͙͚̩̗̭͓͙͚̩͖̭͉͖͚̩̰̭͈̘͙͚̫̤̮͓͖͚̬̤̭͈̭͙͔͚̫̭͎̘͙͚̮͇̘͙̘͚̩̭͓̣͚̬̮͖̭͙͚̰̭̘͚̫̮͖̭͙̯͚̩̤̮͖͓͙̬͚̩̮̘̩͚͎̭͓͙͚͎̮̭͙͚̺̭̗͚̪̭͍̘͙͚̹̤̭͖̘͙͚̫̮͍̘͙͚̭͎̭͇͚̬̮͔͕͚̬̭͓͙͚̫̭͉̘͙͚̬̭͇̘͚̬̭̑͒͊͌̏̓̒̓̒̓̈́͂͆͑̒͆̏́͒̒̑͂͒̒́̓͊͂͒̑̏͒̓̒̏͒̓́̏̒̓̒́͊̏̒͌͘͏̭͙͏͚̭͔̘͚̫̭͙͚̪͚̭̭̤͚̬̗̭͈̘͙͚͚̭͔̘͙̥͚̮́̏̒͑̓͌̓͆͑̒͑͂͂͂͏̸̶̸̴̴̸̢̨̨̡̧̨̡̘͙͓͚̫̗̮͓͙͚̩̗̭̘͙̗͚̩̭͎̘͙͚̹̮̭͙͚̫̤̮͓͚̫͖̮͓͙͔͚̩̭͎̘͙̮͚̮͇̭͙͚͎̭͓͙͚̬̮̘͙͚̤̭͓͚̗̮͇̘͙̯͚̪̮͈͙̩͚̩͎̭͔̭̩͚̩̤̭͓͚͎̮̭͙͓͚̺̮͓͙̪͚̪̭͎͚̹̤̭͕̭͚̮͖̘͙͚͚̭͖̘͇͚̬̭͍̘͙͚̫̭͓͙͚̺̭͉̭͙͚̮͉̭͙͚̬̮͉̘͙͚̭͓͚̭͎͙͚̭̘͚̫̬̭̘͈͚̭͔̘͖͚̬̮͒̐͋͊͊͒͑̓̒͑̏́͌́͑͆͒͊́͒̒͌́͂̓̒̓̒͂́͒̏͐̏̓̒̒͐́̓͂̒͌̏͊͂̏́̏͒̒͆́͂̓͆͂͊̒͌̒͂̏̒̏͘̕͏̭͙͚͚̫̗̭͚̩̗̮͕̭͙̗͚̩̭͈̘͙͚̩̰̭̭͙͚̹̮͓͚̬̭̭͍͚̭͎̘͙͚̮͇̘͙͍͚̺͚̮͐̓̒̐͊̐͊͒͒̓̒͆͌̒͂͒͂͂̓͘͏̴̴͉͚̬̮͖̘͙͚̰̭͔͓͚̗̮͍̭͙̯͚̪̰̭̘͙̬͚̩̭͇̩͚̰̭͓͙͚̬̤̮̘͙͚̩̭͙̫͚̪̮͔͙̬͚̹̰̭̓̒͆͊́̒͌́͐̓̒́̓͊͒̓͒̓̏̓͏̸̨̡̨͚̮͙͚̭̘͇͚̬̮͕͚̫̭͓͙͚̹̭͉̘͙̪͚̮͉̭̙͚̬̭̓̒͐́͑̓̓͂̏͐̒͆͐̓̒͒͊́̏̒͏̘͙͏̵͚̭͔͙͚̫̮͙͚̪̮͓̤͚̬͚̭͈̘͙͚̺͖̭͔̘͚̮́̏̓̓͐̓͆̓̓̒͑̒̏́͂͏̸̘͙͕͚̫̗̮͓͙̖͚̩̗̭͇̘͙͚̩̭͎̭͙͚̹̭͓̘͙͚̫̰̭̘͖͚̬̮͎̘͙͔͚̩̭͎̘͙̮͚͎̮͇̭͙̙͚͎̮͒͒͊̐͊͋̒̏́́͘͏̸͚̬̮̭͍͚̤̭͔̘͙͕͚̫̭̓̒͑͆͒̒́͏̸̴̴̸̨̡̨͙̯͚̭͕̘͙̩͚̩̮͖̘͙̤͚̭͓͙͇͚̩̮̭͙͕͚̺̭͙͚̪̭͙͓͚̹̤̭͚̭͎̘͙͚̭͎̭͇͚̬̮͙͚̫̭͓̗͚̬̭͉̭͙͚̬̭͇̘͙͚̬̮͙͓͚͚̭̘͙̥͚̫̭͍̭͙͚̪̮͓̤͚̫̭͈̘͈͚̩̭͔̘͓͚̩̤̮̓͂͊́͊̓͆͒̏͒̓̏͊̓͐̓̒͐́̓́̏̒͂͐̓͌̏͊̒̏̈́͊̓́͒̓͆̓̓̒̒͒̒͏̸̸̸̨̭͙͖͚̮͓͙͚̩̗̮͕̘̲͚̩̭͈̭͚̹̮̭͙͚̺͖̮͖͚̬̭̭͙͔͚̤̭͎̘͙͚̫̮͇̭͙͚̩̭͓͙̣͚̬̮͚̰̭͓͚̫̮͍͓͙̯͚̪̰̮͎͙̬͚̪͖̭͇̩͚̭͓͙͇͚̩̮̭͙͚̮͓͙̱͚̪̭͎͓͔͚̹̤̭͙͚̫̮͉͙͚̩̭́͒͐̒͊̒̏͊͐͒̓̒͆͌͂̓͊̔͆͑͆͑̓̒̒́͑̒͌̓̓̒́̓̏͒̒́͒͐̏̒͐̓͒̓̓͆͘͏̨̨̨̘͚̫̮͙͚̹̭͓͙̱͚̺̭͉̭͙͚̮͉̭̘͚̬̭̒͊͐̓͌͂͊̓͂̏̒͏̵̸̘͚͚̭͓͓͙͚̭͓͙͚̭̭̤͚̬̮͈͚̺̭͔̘͚̬̮̒̑́́͂͊͆͂͑̒̏͑̓̒̏̒̏́͏̸̸̸̧̨̭͙͓͚̫̗̮͓͚̩̗̭̭̲͚̩̭͎̭͙͚̹̮̭͙͚̹̭͉̘͓͚̫̮͓͍͚̭͎̘͚̮͇̭͙͚̩̭͓͚̬̮͓͉͚̰̭͔͚̫̭͖͙̯͚̪̮͍͙̬͚̩̮̘͙̤͚̪̭͓͚̮̭͙͒̒͋̒͊̐͊͐̓̒͒͑̒́̓̒̑͂͊͆͑̒͆͒̒́̓̒͌̓͂̓͂͒͒̓̒͂͂͒͘͏̸̴̨̨̡̡̨͚̭͚̪̭͎͓͙̬͚̹̰̭͕͓͙͚̭͇͓͙͚̭͈̭͚̫̗̭͍̘͕͚̬̭͓͙͚̬̭͉̘͙͚̬̭͇̘͎͚̬̮͍̘͙́͒͒̓̒͌̏́̓͂̏̒͊̒͊̏̒͏̵̡͚͚̭̭͙͚̫̭͓͙͚̪͚̮͖͚̫̤̭͈̘͈͚̭͔̘͓͚̫̰̮́͒̓͊͆̓̒̒͂͂̒͏̸̴̨̘͙͔͚̫̗̮͓̹͚̩̗̮͕̘̲͚̩̭͈̘͙͚̩̰̭͈̘͙͚̹͖̭̘͖͚̬̭̭͙͔͚̭͎̘͙̯͚̬̤̮͇̭͙͚̺͚̭͓͚̬̮̭͙͚̰̭̘͚̗̮̭͙̯͚̮͖͓͙̩͚̪̭͔̭̩͚̗̭͓͙͚̩͖̮̘͙͚̩̭͙̮͚̪̭͎͓͙͚̹̰̭͒̒̒͊̐͊̒͌͂͒͋͑̒̐͆͒͊́͒̒͌́͌͂͊͊̒͂̓͊͒̓͒̓̏͘͏̨̨̨̭͙͚̭͍͓͙͚̮͓͚̬̰̮͔͕͚̹̭͓̗͚̭͉̭͙̪͚̭͇̘͉͚̬̭́̓́̏͑̒͊̓̒͆͊̒͂͒͂̏̒͏̡̨̭͚̭͔̘͙̥͚̫̮͓̘͙͚̪͖̭͈̘͚̬̗̮͎̭͙͚̹̭͔̘͚̪͚̮̒̑́̏̓͆̒͑̒̏͏̸̘͙͚̮͓͙̙͚̩̗̭͓͙̗͚̩͖̭͎̘͙͚̹̭͈̘͙͚̹̭̘͓͚̬̰̮͓͍͚̩̭͎̘͙͚̬̤̮͇̘͙͚͎̮̓́͒͌̐͊͒͌̒͑̒͒̓̓́͘͏̸͙̦͚̬̭͈̭͙͎͚̤̭͓̭͙͚̫̮͔̭͙̯͚̪̰̭͕̘͙̩͚̩̭͇̩͚͚̭͓̫͚̮̭͙͚̮͓͙̺͚̪̭͓͙͚̹̤̭̭͚̫̭͇̭͙͚͎̮̓͆́͂͂̓̒͂̓̒́̓͒̓́͒͐̏͊͗͐̒̓͒̓́͏̨̨̡͓͇͚̫̭͓͙͚͚̭͓̗͚̬͖̭͉̘͙̦͚̩̮͉̭͚̬̮͍̭͙͚̭͓̘͚̫̭͓͙͚̪̗̭̭͚̫̰̭̘͙͚̪̭͔̘̘͚̪̮̒̏͒͌͂͊̒̒͗́̏̒͑̓͊͆͒̒͌͑͒̒͊̕͏̸̴̸̸̴̢̨̘͙͚̭͙͚̩̗̮͕̘͚̩͖̭͇͓͚̩̰̮̭͙͚̫̤̮͓͖͚̬̮͓͙͔͚̫̭͎̘͙͚̩͖̮͇̘͙͚̩̭͓̦͚̬̮͖̭͉͚̤̭͓̭͚̗̮͍̭͙̯͚̩̤̭̘͙̬͚̩̭͔̭̩͚̬̰̭͓͙͚̩̮̭͙͈͚̭͙̲͚̪̮͔͙͓͚̹̤̭͖̭͚̫̮͈͙͚͚̮͖͓͇͚̬̮͕͚̺̭͓͙̱͚̹̭͉̭͙̪͚̬̮͉̭͙͚̬̭͗́͐̓͑̒̒̏͒̓̒͑͊͆͑̒͆̒́̒̑́͑͆̒̓͊̏͒́͒͒̓̏̓̒̓͒̓̓́̒͐̓̒͊̓̒͘̕ͅ͏̴̡̘͙͚͚̭͚̫̭̘͙͚̪͖̭̘͚̫̤̮͎̭͙͚̪̭͔̘͓͚̬̮́͒̓̒͆̓͊͆͌̒͑͊̒́͏̸̸̨̘͙͓͚̮͓͙͇͚̩̗̭̺͚̩̭͍͓͚̹̭͓̘͙͚̫̤̭͍̘͖͚̬̤̮͓͙͔͚̭͎̘͚̮͇̭͙̘͚͎̭͓͚̬̮̘͚̤̭̭͙͚̫̭͂͒͋̓̒͊̒̏͊̒͑͂̓̒̑͂́͑̒̔͆͒̒͑́͑͂͘͏̸̴̴̴̵̸̸̨̨̡͓͙̯͚̪̭͕̘͙̩͚̩̭͇͙̤͚̰̭͓̮͚̫͚̮̘͙͙͚̺̮͓͙͚̪̮͔͓͚̹̤̭͕͓͚̮͙͚̗̭͍̭͚̫̭͍̘͕͚̬̭͓͙͚̺͎̭͉̘͙͚̬̭͇̘͚̬̮͉̘͚̭͙͚̮͓͙͚̮͚̫̮͈͚̭͔̘͖͚̪̮͂̓́̓̒͒̏͐̏̒̒̓́͑̓̓́̒͊̏̒́͊̒̋̒́̏͑̓́͂͐͆͂͐̓̒͑̓̒͂͒̒͊͘̕ͅ͏̢̭͙͚̫̗̭͚̩̗̮͕̭͙͚͚̩̭͇̘͚̹̭͖͙͚̺͖̮͖͚̫͖̭̭͍͚̪͚̭͎̘͙̯͚̫͚̮͇̭͙͚̩̮͑͐̓̒͊̒̏͊̓͑̓̒͌̒̔͆͘͏̸̸̸̡̨̡̨̢̨͙̳͚̬̮͖̭͙͚̰̭͚̗̮͍̭͙̯͚͖̭͖̘͙̬͚̩̮͖̘̩͚̫̭͓̫͚̮̭͙͔͚̺̭̖͚̪̭͎͓͚̹̤̭͓͙͚̫̭͇͓͙͚͚̮͖͓͇͚̫͚̭͍̘͙͚̺̭͓͙͚̺̭͉̭͙͚̭͇̘͚̬̭̓͆́͑̓̒̑́͂̒̓̒͂͒̏͒̓̒̏̒̑͐͒̓͂̒͌͆͊́̏̒̋͏̡̭͔͚̭͓͓͚̫̮͓͙͚̮͖͚̬̮͙͚̩̭͔̘͚̮̒́̏̒͆̓͑͆͂͂̓̒̏͑̓͑͆̒̏͂͂͏̸̸̭͙͚̭͚̩̗̭͇̭͙̗͚̩͖̭͈̭͖͚̩̰̭͕͓͙͚̺͖̭̭͓͚̫̮͓͙͔͚̪̭͎̘͙̮͚̩͖̮͇̘͙͈͚̩̮̓́͐̓̒̔̒͑̒͊͑͆͘͏̵̗͚̬̮̘͙͚̰̭̓̒͆͒́͏̸̴̴̸͙͚̫̭̭͙̯͚̪̤̭͕̘͙̬͚̪̗̮̘̩͚̰̭͓͙͚̩̮̭͙͖͚̩̮͓͚̪̭͍̘͙͚̹̰̭͖͙͚̫̮͓͓͙͚͚̭̓͂͐͒̒͂̓͊͆͒͐̒͒̏̓͒̓́͏̨̘͚̫͚̮͔͙͚̫̭͓̗͚̬̭͉̭͙͚̮͉̭̗͚̬̭̒͊̓͌̏͊̒̏͆͂̏̒͏̡̘͚͚̭̘͙̥͚̫̭̭͙͚̩̭͓̭͚̫̰̭͈̘͙͚̪̭͔̘͓͚̮̒͐́͑̓͊͆̓̒͑͊̒͂͂͏̭͙͏̸͚̮͓͙͂͒͏̸̵̸̴̴̸̨̨̨̡͚̩̗̭̘̦͚̩̭͇͓͚̹̭͈͙͚̺̮͔͖͚̬̮͓͍͚̩̭͎̘͙͚͎̮͇̘͙͍͚̩̭͓̣͚̬̮͖̘͙͚̤̭͔͚̫̮͈̭͙̯͚̪̤̭͕̘͙̩͚̩̮͖̘̩͚̩̭͓̬͚̮̘͙͈͚̺̮͓͙͚̪̮͔͙̰͚̹̰̭͔̘͚̫̭͇͓͙͚̩̭̭͇͚̬̤̮͔͙͚̹̭͓͙͚̫͖̭͉̭͙̥͚̮͉̭̖͚̬̮͉͓͙͚͚̭͔̘͚̫̮̭͙͚̭̭͚̬̭͈̘͈͚̪̭͔̘͚̮͋̒͊̒̏͊̓͊̓̒͂͑̒͂͆͑̒͆́̓̒͌͂̒̓̒͂͒̏͐͂̏̓̒͐͒̓͆͌̒̓͌̏͊́̏̒́̒͆̓͒͆͂͒̒͒̒͂̒͐͂͒͘ͅ͏̸̸̴̸̴̨̨̧̢̨̡̭͙͚̪͖̮͓͙͚̩̗̭̭͙͎͚̩͖̭͈̘͖͚̩̰̭͍͙͚̺̮͕͓͚̫̭̭͙͔͚̪̭͎̘͙͚̮͇̘͙͚͎̭͓͙͚̬̮͓͚̤̭̭͙͚̫̮̘͙̯͚͖̮͙̩͚̩̭͇͙̤͚̭͓͙͇͚̫̮̭͙͚̪̮͓͙̦͚̪̮͔͔͚̹̤̭͚̮̘͙͚̗̭͎̭͇͚̬̭͓͕͚̹̭͓͙̤͚̫͖̭͉̘͙͚̬̮͉̭͙͚̬̮͙͚͚̭̘͙̥͚̫̮͖̭͙͚̩̭͓̭͚̫̤̮͙͚̹̰̭͔̘͓͚̮͗͒͒͋̒̓͊̓̒͊͌͂̓͂́͑̓͆͒̒͑́͒͂͊͂͊̓̓́͊̓͊͒̐͐̏̓̒͐̓̒̓́͐̓́̒͆͒̒͊͊̓͂́͒̓͆̓̒͑̓͑̒͂͂͘̕͏̴̴̸̨̨̘͙͚̪͖̭͙͈͚̩̗̭̘͚̩͖̭͎͓͖͚̩̰̮͙͚̹͖̭͓̭͓͚̬̤̭̭͙͔͚̫͖̭͎̘͙͚͎̮͇̘͙̘͚͎̭͓͚̬̭͈̭͙͚̤̭͓̘͚̗̭͖̘͙̯͚͖̮͈͙̩͚̩̭͇̩͚̭͓͙͇͚̪̰̮̭͙͈͚̪̮͓͚̪̭͎͓͔͚̹̤̭͕̭͙͚̭͎͓͙͚͎̮͑͐̓͋̒̋̒͐̓̒͌͂́́͑̒͆̏́̒͌́͂̓̓̒́̓͒͐̒͒̏̒́̓́͘͘͏̴̸̨̡̨͓͇͚̫̭͍̘͕͚̹͎̭͓͙̱͚̬͖̭͉̘͙͚̭͇̘͚̬̮͍̘͙͚̭͔͚̭̘͙͚̭̘͚̬͎̭͈̘͈͚̭͔̘͙͚̮̒͒̒͊̈́͂̏̒͌́̏̓̒͑́͂͋͆͂͌̒̒́͊͂͂͏̘͙͔͚̫̗̮͓͚̩̗̭̘̺͚̩͖̭͇͚̹̭͓͙͚̹͖̭̘͖͚̫̮͓͍͚̭͎̘͙͚͎̮͇̘͙͚̪̮͒̒̋͋̒̓̒̏͊͋͊̒͊͑̒́͂̈́͂̋͆͘͏̸̸̖͚̬̮̘͚̰̭̘͚̫̮͎͙̯͚̪̰̭͖̘͙̬͚̪̗̭͔̭̩͚̬̭͓͙͚̮̘͙͔͚̺̭͚̪̭͍̘͙̬͚̹̤̭̓̒͆͒̒̒́͒̒͌̓̒̓̓͊͂͒̏͒̓̒͐̏͏̨̘͚̫̭͇͙͚̭͇̭͚̬̮͕͚̹͚̭͓̗͚̬̭͉̘͙̪͚̮͉̭͚̬̭̒̓͒̓̓͂̏̒͊͂͐̓̒͊̒̏͂̏̒̕͏̵̡̘̙͚͚̭͓͙͚̫̭͈̘͙͚̪̮͚̫̬̭̘͈͚̪̭͔̘̘͚̮̒́͑̓͆̓͑̓̒͌̒͒̒́͂͏̴̸̨̨̨̢̨̭͙͓͚̫̗̭͙͍͚̩̗̭͇̘͙͚̩̭͇͖͚̩̰̮͖͓͙͚̹̭̘͖͚̬̮͓͙͔͚̭͎̘͙͚̮͇̭͙͚͎̭͓̩͚̬̮͖̘͙͚̰̭̘͚̫̮͖̘͙̯͚̩̰̮͙̬͚̩̰̭͇̩͚̬̬̭͓̫͚͎̮̭͙͚͚̭͙͚̪̭͙͚̹̤̭͖̘͙͚̮͕͓͙͚͚̭͖̘͚̫̭͍̘͕͚̭͓̗͚̫̰̭͉̘͙͚̮͉̭̙͚̬̮͉̘͙͚͚̭͐̓͊͊̓̒͊͊̒͑́͒͂̏́͑̒͆̒́͑̒̑͋̓̓̒̓̒́͒́͒͒̓͂̏͊̓͗́̓́̒͊͒̒́͂͊̒́̏̒͂́͘ͅ͏͚̫̭̘͙͚̩̮̤͚̬͚̭̘͈͚̹̤̭͔̘͓͚̮̓̒͆̓͋͆̓͑̓̒͌̒̒͂͂͏̵̸̭͙͚̪͖̭͚̩̗̭͓͚̩̭͍̘͚̩̰̭͇̭͙͚̫̤̭͓̭͓͚̫͎̭̭͙͔͚̩̭͎̘͚̮͇̘͙͚̪̮̑͐̓̒͌̒̈́͊̒̏̒͌͆̒̑́̏͆͘͏̴̴̸̨̨̨̨̡̨͙̩͚̬̮̭̖͚̤̭͓̭͙͚̗̮͓͙̯͚̪̤̭͖̘͙̬͚̪͖̭͇̩͚̭͓̫͚̮̘͙͙͚̺̮͓͙̬͚̪̭͎͙͚̹̤̭͕͚̮͖͓͙͚͚̭͇̭͚̫̮͔͕͚̬͚̭͓͚̫͖̭͉̭͙͚̬̭͇̘͙͚̬̮͉͓͚͚̭͓̘͚̮͖͓͙͚̮͖͚̫̬̭͈̘͙͚̩̭͔̘͙͚̬̮̓͆͒̒́͂́͊̓̒́͊̓̒͂͒̏͐̏̓̓̒̓́̓͂̒͊̓̓̒͊̒̔̒̑́̒͆́͂͆͂̓̒͑͊͂̕͏̘͙͕͚̪͖̭̣͚̩̗̮͕̭͙͚͚̩̭͈̭͚̹̭͖͓͙͚̫̰̭͈̘͖͚̫̗̭͈̭͍͚̪͎̭͎̘͚̫͚̮͇̭͙͍͚̺͚̮͐̓̒͊̒̏͊̒̒̒̑͘͏̴̨͙̪͚̬̮͖̘͙̥͚̤̭̘͙͚̗̮͈͙̯͚̮͈͙̬͚̩͎̮̘̩͚̬̰̭͓̮͚̮̭͙͚̪̭̖͚̪̭͎͓͔͚̹̰̭͕͓͚̫̭͇̭͙͚̗̮̓͆́͑͂́̓͂͊̓͒̒̓̒͂͒͑͒̓̒̏̒̒̓͒̓́͏̴̨͓͇͚̫̭͍̘͕͚̫̭͓͙̤͚̫̭͉̘͙̤͚̬̭͇̘͙̥͚̬̭̒͊̒͆͊͆͏̸̵̘͙͚͚̭͓͙͚̫̮͓͙͚̮̤͚̬̭͈̘͈͚̪̰̭͔̘͚̩̤̮́͑̓͒͆͂͂͒̓̒̓̒̒̏͏̸̢̭͙͚̭͙͚̩̗̭͇̘͙͖͚̩̭͎̭͙͚̹̭̭͙͚̹̮͓͚̫͚̭̭͙͔͚̪̤̭͎̘͙̯͚̫̮͇̭͙̘͚͎̮̐͂͐̓͊͊͋͒͑̓̒͌͊́̕͘͏̴̸̴̴̨̨̨͚̬̮̘͙̹͚̤̭͔͚̗̮͍̭͙̯͚̩̰̮͖͓͙̩͚̩̭͔̭͙̤͚͖̭͓̫͚̮̭͙͖͚̩̭͙̳͚̪̭͍̘͙͚̹̰̭͔̘͙͚̫̭͙͚̩̭͇̭͇͚̬̮͙͚̫͖̭͓͙͚̭͉̭͙͚̮͉̭͚̬̭̓̒͊͆͒́̓̒͌́͆́̓̒͂͒͒̓̏͒͋̓̓̒͂͐̓͌͊͂͒́́̏̒̋͏̡̭͙̰͚͚̭̘͙̥͚̫̭͍͙͚̩̭̭͚̬̮͈͚̹̬̭͔̘͓͚̮́͒̓̓͆̓͒̒͆͑̓̒̒́͂͏̢̭͙͖͚̫̗̮͓͙͚̩̗̮͕̘̖͚̩̭͇̘͙͚̩̰̭͕̘͙͚̹̮͓͓͚̫̭̭͍͚̪̭͎̘͚̪̰̮͇̭͙͚̪̮͒̐̒͊̓̓̒̓͌̒͊̒̒͋͆͘͏̸̴̴̴̴̧̨̡͚̬̮͖̭͙͎͚̰̭̘͙͚̫̮̭͙̯͚̮͙̩͚̩͎̮̘͙̤͚̭͓͙͚͎̮̘͙͔͚̪̭͚̪̮͔̙͚̹̰̭͕͓͚̫̭͈̘͙͚̩̮͓͚̫͖̮͔͕͚̫̰̭͓͙͚̺͎̭͉̭͙͚̭͇̘͙̰͚̬̮͍̘͚̭͓̘͙̥͚̭̘͙͚̩̗̭̭͚̬̗̭͈̘͈͚̪̭͔̘͚̮̓̒̔͆́͒͂͌͂͊͊̓͒͂̏̓͊́͒͒̓̒̓̏̓̒̒͐͒̓͑̒͊̓̒͊́̏̒̑́̏́͂͊͆͒̒̒̒͐͂͒͏̭͙͚̫̗̭͙͈͚̩̗̭̘͍͚̩͖̭͈̭͙͚̩̰̭͍͙͚̹̭̘͖͚̬̤̮͓͙͔͚͖̭͎̘͚͎̮͇̘͙͈͚̩̮͒͐̓͋̒̐̓͒͋̒͑͂̒̑͂͆͘͏̸̨̨͙̺͚̬̮͖̭͙͚̰̭͓̭͚̫̮͍̘͙̯͚̪̮͍͙̬͚̩̭͇͙̤͚̩̭͓͙͇͚̮̭͙͈͚̺̭͙̓͆̒́̒͌̓͆̓̓̓͂͒̏͒̓͏̸̨̡̨̡͚̪̭͎͓͚̹̰̭͖͙͚̫̭͇͓͙͚͚̭͖̘͇͚̬̮͔͕͚̬̭͓͙͚̺͎̭͉̭͙͚̭͇̘̖͚̬̮͍̭͔͚͚̭͔͚̫̮͕͙͚̪͚̮͚̬̗̮͙͚̩̬̭͔̘͓͚̮̏̒̓͒̓͂̒͆̓̒͊͆́̏̒̒́̓̒͆̓̓͆͑̓̒͑̓͑̒́͒̕͏̸̵̸̨̡̭͙͚̭͙͚̩̗̭̘͙͚͚̩̭͈̘͖͚̩̰̭͇͙͚̫̰̭̘͖͚̬̭͈̭͙͔͚̪̬̭͎̘͙͚̩͖̮͇̘͙͚̩̭͓͙̳͚̬̭͈̭͙͚̤̭͔͓͚̗̮̭͙̯͚̪̤̮͕͓͙̬͚̩̰̭͇̩͚̬̗̭͓̩͚̮̘͙͚̭͙̰͚̪̮͔͔͚̹̤̭͔̘͚̫̭͎͙͚͚̮͓͓͚̬̰̮͔͙͚̬̭͓̗͚̭͉̭͙̦͚̭͇̘͍͚̬̮͙͓͚͚̭̭͙͚̫̮͔̘͙͚̪̭̘͚̬̮͈͚̭͔̘̘͚̪̮̑́͐̓͌͋͊̒̓͋̒͆͂̓͆͑͆̒́̒͌́͌̓̒̓̒́̓͒͐́͒͒̓̏̓̒̒͐͒̓̓́̒͊̓͌̏͊̒͂͒́̏̒͊̓́͑̓͆̓͋̒̓͑̓̒͂̒͊͘͏̸̵̸̴̡̭͙͙͚̮͓͙͚̩̗̭̭͍͚̩̭͈̘͙͚̹̭͈͓͙͚̹̭͉̘͓͚̬̭̭͍͚̪̬̭͎̘͙͚̬̤̮͇̘͙͚͎̭͓͚̬̭͈̘͙͚̰̭͓͚̫̮͉̘͙̯͚̪̤̭͓̘͙̩͚̩̰̮̘͙̤͚̪̭͓̹͚͎̮̘͙͚̪̮͓͙̲͚̪̭͓͚̹̰̭͂͒̔͋̒͊̐͊͒̒͂͌̒̋́͑̒͆́͒̒͌͒̓̓̒͂͒͐͐̏͊̒͐͘ͅ͏̴̴̨̨͓͚̫̭͉͓͙͚̮͕͓͇͚̬̤̮͙͚̫̤̭͓͚̫̭͉̘͙͚̬̮͉̭̘͚̬̮͉͓͚͚̭̭͚̮͔̘͙͚̭͍̘̤͚̬̗̮͙͚̹͎̭͔̘̘͚̩̮̒̓͒̓͂̏̒͐̓͌͊̒̔͆̒̒́͒̒͆́͂͆͂͂̒͑̓͑̒͘͏̸̴̘͙͙͚̮͓͙͍͚̩̗̭̲͚̩͖̭͉͙͚̩̰̭͙͚̫̤̭̘͖͚̬̮͎̘͙͔͚̭͎̘͚̬̤̮͇̘͙͚͎̮͂͒͋̓̒̓̐͊̓͌̒́͆̒̒͌́͘͏̴̨̘͚̬̮͖̭͍͚̰̭͓͙͚̗̮̭͙̯͚̪̭̘͙̩͚̪̭͇͙̤͚̭͓͙͚͎̮̘͙͚̩̭̖͚̪̭͓͔͚̹̤̭͖͚̫̮͇͓͙͚̮͖͓͚̫̗̭͓͙͚͖̭͓̗͚̺̭͉̭͙̪͚̭͇̘̓̒͆̒́͒͂́͊͂͒̏̓́͆̓͊͂͒̐͒̓̒̏͊̒̓̒̓͒̓́̏̒͊͒͌͂͊̒͂̏̒͏̵̨͚̬̮͉̘͚͚̭͓͙͚̫̭͙͚̪͚̭̘̤͚̫̤̮͈͚̹̰̭͔̘͓͚̬̮̒̑́͒̓͋̓͆͊̒͑̓̒̒̏͏̘͙͏̸̸͚̭̪͚̩̗̭̘͙͚͚̩̭͍̘͙͚̹̭͖͙͚̹̮͓͓͚̫͎̮͎̘͙͔͚̩̭͎̘͚̮͇̘͙͈͚̩̮͂͐̓̒͋͊̐͊̓͊̓̒̏̒̒͂͆͘͏̸̸̵̨̨̨̡̦͚̬̮̭͙̩͚̤̭̭͚̫̭͓͙̯͚̪̤̭͕̘͙̬͚̪̮͖̘̩͚̩̤̭͓͙͇͚̪̮̘͙͚̺̮͓͙̯͚̪̭͎͓̙͚̹̰̭͓͙͚̮͖̘͙͚͚̮͕͓͚̫͖̭͍̘͙͚̺͚̭͓͙̲͚̺͎̭͉̭͙̥͚̭͇̘͚͚̬̮͉̭͙͚̭͓̭͙͚̭͉͓͙͚̪̗̮͚̬͖̭͈̘͈͚̗̭͔̘͙̥͚̮̓̒͆͒́͒̒̑͑͊̒̓͆͒̑̏͐̏̒͐́̓͂̒͊͌͊͂̏̒́̏́͂͆͐̓̒̒͂́͂͏̸̨̘͙͚̮͓̖͚̩̗̭̮͚̩̭͇̘͖͚̹̮̘͙͚̫̰̮͓͖͚̫͖̮͎̘͍͚̪̤̭͎̘͙͚̮͇̭͙̗͚̪̮͑́͒̒͋̓̒͊̒͊͒̓̒̒͂͂͆͘͏̸̴̴̨͙͚̬̮͖̘͚̤̭̭͚̗̭͙̯͚̪̰̭̘͙̩͚̩̮̘̩͚̗̭͓͙͚̫̮̘͙͚̪̭͙͚̪̭͎͚̹̤̭̓͆̒̋́͒̒̑́͐̓͑͒̒͂̓͊͊͒̓͒̓̏̓̒͐͏̸̵̨̨̨̘͙͚̭̭͙͚̭̘͇͚̫͚̮͙͚̹̭͓͚̗̭͉̘͙͚̭͇̘͕͚̬̮͉̭͙̰͚͚̭̭͙͚̫̮͔̭͙͚̪̗̮͓̤͚̬͎̭̘͈͚͚̭͔̘͕͚̪̮́͌̓͂̏͐̒͐̓͌͆͊̒̔͂͂̏̒́͒̓͆̓̒͌̒͂̒͊͏̭͙͏̢͚̪͖̭͙͚̩̗̭͚̩͖̭͉͙͚̹̭̘͙͚̺͖̭͈̘͓͚̫̮͓͙͔͚̩̭͎̘͙̯͚̫̮͇̘͙͚̩̭͓̗͚̬̮̘͍͚̰̭͐̓̑͋̓̒̓̐͊͋̒̏͑͊͊̏͆͑̒͆͒̒́͘͏̸͙͕͚̫̭̓͏̴̸̷̴̵̨̨̡͙̯͚̪̤̮͎͙̩͚̩͎̮̘̩͚̤̭͓͙͚̪̰̮̘͙͚̪̭͙͚̪̭͍̘͙͚̹̰̭͕̭͙͚̭͎̭͙͚̮͕͓͚̫͚̭͓͙͚̫̭͓͙͚̺̭͉̭͙͚̬̮͉̭͚̬̮͙̬͚͚̭͔̘͙͚̫̭͍͙͚̭̭͚̬̮͈͚̪͎̭͔̘͓͚̫̰̮̓̓͒̒͂̓͊͒̑͒̓́̏͂́̓́̏̒͊͒͌̏͊̓̈́̒͐͊̓́̓̓͆͂͂͒̒͊͑̓̒̒͏̸̢̭͙͖͚̭̙͚̩̗̭͓̺͚̩̭͈͙͚̩̰̮́͐̓̒͌̒͊̓͏̸̴̵̡̨̨̨̘͙͚̺͖̭̘͖͚̫̭͈̭͍͚̪̤̭͎̘͙͚͎̮͇̭͙̘͚̺͚̭͓͙̦͚̬̮͖̭͙͚̰̭͔̘͙͕͚̗̮͓͙̯͚̪̰̭̘͙̩͚̩̭͔̭̩͚̪̰̭͓͙͚̮̭͙͙͚̩̮͓͙̪͚̪̭͎͓͚̹̰̭͔̘͚̮͖͙͚̩̭͇̭͚̫̗̮͙͚͎̭͓̗͚̫͖̭͉̭͙͚̮͉̭͙̙͚̬̮͍̭͚͚̭͓̭͙͚̭͙͚̩̗̭̭̤͚̫̮͎̭͈͚̬̭͔̘͚̫̮͊̒̏̒̈́͂͑͆́́͐͐͂̒̓͊͂͒͐̏̒͌̒̓́̓̓͆̒͊͐̓͌͂͊̒́̏̒́́͂͌̓͆͒̒͂̒͂̒͐͆͘̕͏̸̸̴̴̵̢̨̨̨̡̨̡̭͙͖͚̭͚̩̗̮͕̭̖͚̩͖̭͈̭͙͚̹̭͙͚̺͖̮͕͓͚̫̮͓͙͔͚̪̤̭͎̘͙͚͎̮͇̘͙͈͚̩̭͓͙͚̬̮͓͚̰̭͓͓͚̫̮͍̘͙̯͚̪̭̘͙̩͚̩̭͇͙̤͚̩̭͓͚̫͚̮̭͙͚̭͙͚̪̮͔͓͚̹̰̭͓͚̮͔͙͚͚̭͈̭͇͚̬̰̭͓͕͚͎̭͓͙͚̺͎̭͉̭͙͚̬̮͉̭͙͚̬̮͍̘͙͚͚̭͙͚̫̭͈͙͚̩̮͔͚̬̗̮͙͚̩̭͔̘͖͚̮͂͐̓̒̏̒͊͐̓̓̒͊͑́͆͑͆͒̒̋́̒̑͂͐̓͆̓̒͂͒͑́͒͒̓̒̏̒͌͐̒͐́̓̓͂̒͒̒͂͊͆̈́́͒̓̓̓͆̓̓̒͑̓͑͊̒́͂͘ͅ͏̸̸̴̷̸̢̨̨̨̨̡̭͙͚̫̗̮͓͍͚̩̗̭͇̘͙͎͚̩̭͈̭͙͚̩̰̭͇̘͙͚̫̰̭̭͖͚̬̭̭͙͔͚̪̬̭͎̘͙̯͚̮͇̭͙͍͚̺͚̭͓͙̲͚̬̮̭͙͚̰̭͓͚̗̭͔̭͙̯͚̪̭̘͙̩͚̪͚̭͇͙̤͚̪̬̭͓͙͇͚̮̭͙͚̪̮͓͚̪̮͔͓͙͓͚̹̰̭̭͙͚̭͇͙͚͚̭̭͚̫͎̭͍̘͕͚̺͖̭͓͙͚̭͉̭͙̦͚̭͇̘͙̙͚̬̮͍̭͙̬͚͚̭͓͙̥͚̭͎͓͙͚̮͚̬͎̮͎̭͙͚̺̭͔̘̘͚̬̮̓͒̒͊͑̒͂͌́͑͆͒̏́͑̒͌́͐̓̓͂͒͐͐̒̒̏͐́̓̓́͌̒͊̒͊́͂͂̏́͑́͂͆͂͐̓̒͑̏̒̏͘͏̸̸̘͙͖͚̮͓͍͚̩̗̭̭̮͚̩̭͉͖͚̩̰̮͖͙͚̫̰̭͉̘͓͚̬̮͎̘͍͚̪̤̭͎̘͙͚̮͇̭͙͈͚̩̮́͒̒͋̒͊̓̒̓̒͆̒́͆͘ͅ͏̸̨̨̢̨͙̺͚̬̭͈̭͙͎͚̤̭͔̭͙͕͚̫̮͍̘͙̯͚͖̮͎͙̬͚̪̗̭͔̭̩͚̬̬̭͓̫͚̮̘͙͕͚̮͓͙̲͚̪̭͚̹̤̭͖͓͙͚̫̭͈͓͙͚̭͎̭͇͚̫̭͓͙͚̭͓͚̺̭͉̭͙͚̭͇̘͙̺͚̬̭̓͆́͂̓̒̓̒́̓͒́͒͐̏͊̓̒͒̓͂̏̒̏͒͌͂̏͊̒̔͂̏͘͏̵̸̸̴̡̘̙͚̭͔̭͙͚̮͓̘͙͚̭̘͚̫̭͈̘͈͚̭͔̘̘͚̪̮̒́̏́͂͆͂͋̒̒͂͆̒͏̭͙͖͚̫̗̭͙͚̩̗̭͇̭͙͚͚̩͖̭͈̭͖͚̩̰̭͎͙͚̺͖̮͓͖͚̫͎̭͈̭͙͔͚̤̭͎̘͙̮͚̬̤̮͇̭͙͚͎̮͐̓͑̒̓̓̒͂͌́͘͏̸̴̴̵̢̧̨̨̡͙͚̬̮͖̭͙̹͚̤̭̭͙͕͚̫̭͔̭͙̯͚̩̰̮͍͙̩͚̪͚̮͖̘͙̤͚̭͓͚̪̮̭͙͕͚̩̭͙͚̪̭͎̭̙͚̹̤̭͔̘͚̫̮̭͙͚̭͎̭͇͚̫͎̮͙͚̫̭͓͙̤͚̭͉̭͙̣͚̬̭͇̘͚̬̮͉͓͚͚̭͔͓͙͚̮̭͙͚̩̗̮͚̫̮͈͚̪̭͔̘͓͚̬̮̓͆́͑̓́͆̓̒͂͆͒͒̓̏̒̒̓͒͐̓́̏̒͐̓͌͊́͂̒͒̒̑́́͂͒͆͑̓̒͂͑̓̒̓̒͂͏̸̵̸̘͙͚̭͙͕͚̩̗̭̭͙͚̩̭͎̭͚̹̮͖̭͙͚̫̰̮͖͚̬̭̭͙͔͚̪̬̭͎̘͙̮͚̫̮͇̭͙͚͎̭͓͚̬̮̭͙͚̰̭͔͓͙͚̗̮͖͓͙̯͚̪̰̮͍͙̩͚̩̭͔̭͙̤͚̭͓̮͚̪̰̮̭͙̐́͐̓͋͒͊̒̏͊͑̓̒͆͌͊̓́͑̒̓͆͒́͂́̓́͆̓̒͒͘͏̴̨͚̪̮͓͙̭͚̪̭͎͙͓͚̹̤̭͓͚̮͐̏̓͐̒̓́͏̴̴̨̧̨͓͙͚͚̭͖̘͇͚̬̬̮͔͙͚̫̭͓͙͚̺̭͉̭͙͚̭͇̘͙̗͚̬̮͉̘͚͚̭͓͓͚̭̭͙͚̪̮̤͚̬̗̮͎̭͈͚̭͔̘͙̥͚̩̮̓͂̒̓͌͊̓́̏̒́̒͑́͂͋͆̓͒̓̒̒͂̏͘͏̴̸̧̭͙͚̪͖̮͓͙͉͚̩̗̮͕̘̺͚̩͖̭͎͓͖͚̩̰̭͎̘͙͚̺̮͓͚̬̭͈̭͍͚̪̭͎̘͙͚̪͖̮͇̘͙͈͚̺͚̭͓͙͚̬̮͖̭͙͎͚̤̭̭͚̗̮͇͙̯͚̩̤̮͍͙̬͚̩͎̭͇̩͚͚̭͓̫͚̩̮̘͙͚̪̭͙̱͚̪̮͔͙͚̹̤̭̐͒̒̒͊͑̓̒͂̒͒̓͑͆́͑̒̑́̓̓̓̒͂̓̒͆͒̐͒̓̏̓͘͏̸̨̨̨͙͚̫̭͎͙͚̮͕͓͇͚̬̭͍̘͙͚̫͚̭͓͙̲͚̫͖̭͉̘͙̪͚̩̭͇̘͙͚̬̭̓͒̓̓͂̏̒͆͌͊͏̡̭͚̭͔͚̫̭͓͙͚̮͚̫̤̮͙͚̩̭͔̘̘͚̩̮̒́̏̓̒͑̓͑͆͂͂͐̓̒͑̓͑͆̒͊͘͏̸̡̘͙͚̪͖̮͓͚̩̗̭̦͚̩͖̭͈̭͚̩̰̭͕͙͚̺̮͓͚̬̮͓͙͔͚̩̭͎̘͙͚̪̮͇̘͙͈͚̩̭͓͙͚̬̮̘͉͚̰̭͑͒̒̔͋̓̒̒̏̓͊͒̓̒͂͑̓͆͆͑͆͒̒́͘͏̸͚̗̮͇͙̯͚͖̮͖͓͙̩͚̩͎̭͔̭͙̤͚͚̭͓̩͚̮̭͙̓̒͌́̓͂́̓̒́͒͏̴̨͚̩̭͙̳͚̪̭͓͔͚̹̰̭͕̭͙͚̫̮͒̓̏͊̒͒͏̸̨̨̨͙͚͚̮͕͓͚̫͚̭͍̘͕͚̫̭͓͚̹̭͉̭͙͚̩̮͉̭̗͚̬̮͉̘͙͓͚͚̭̓̓́̒͊̒͊̒̔͂̒́͏̡͚̫̭͉̭͙͚̪̗̭͍̘͚̬̮͈͚̹̬̭͔̘͓͚̬̮̓̒͑̓͆̒͆͑̓̒̒̏͏̸̸̢̘͙͙͚̪͖̮͓͙͚̩̗̭̘͙̗͚̩̭͇̭͙͚̹̭͇̘͙͚̺͖̭͉̘͖͚̬̮͓͍͚̪̭͎̘͙͚̪̮͇̭͙̙͚̺͚̭͓͙̥͚̬̮͖̭͙͎͚̰̭̘͚̫̮͎̭͙̯͚̪̤̮͍͙̬͚̪͚̭͇͙̤͚̬̭͓͙͚̮̘͙͚̮͓͙͚̪̭͎͓͚̹̤̭͒̓͋͊͊̒͂͑̒͂̈́͆͑͆́͒̒͌̓̓͂̓͊́͒͐́͒͐͂̏̒͌͘͏̸̸̨̭͙͚̫̮͈͓͙͚̮͖͓͚̫̗̮͙͚̭͓͙̲͚̬͖̭͉̘͙͚̭͇̘͙͚̬̮͉͓͙͒̓́̏̒͊͐̓͌͂͊́̏̈́ͅ͏̨͚̭͙̥͚̫̮̘͙͚̩̮͖̤͚̫̬̮͎̭͙͚̩̭͔̘͚̫̰̮́̏͒̓̓͒͆̓̓̒͑̒̏͏̸̴̴̸̴̸̴̵̧̨̡̨̨̡̭͙͖͚̫̗̮͓͙͕͚̩̗̮͕̭̺͚̩͖̭͈͚̹̮͖̭͙͚̺̮͔͓͚̫̭͈̭͙͔͚͖̭͎̘͚̩̮͇̘͙͉͚͎̭͓͚̬̮͖̭͙͎͚̤̭̭͙͕͚̫̮͉̘͙̯͚̪̮͙̬͚̩̭͇͙̤͚̩̭͓̬͚̮̭͙͚̪̭͙͚̪̭͎͚̹̰̭͖͓͙͚̭̭͙͚̮͓͓͇͚̬̰̮͕͚̹͎̭͓͙͚̗̭͉̘͙͚̮͉̭͙͚̬̮͉͓͙̬͚̭͔̭͙͚̫̭̭͙͚̪͚̮͖͚̬̭͈̘͙͚̹͎̭͔̘͓͚̬̮͒̒̓̒̏͊͊̓̒̓͂̒̑͆́͑̒͆́͑͂͊̓̓̓̒͂͒̐͒̓͐̏̓̒́͌̓͂̏̒͐̓̒͊͂́̏́̏̓͌͆̓̒̏͑̒́͘̕͏̢̨̭͙͚̫̗̮͓͚̩̗̭̘͙͚͚̩̭͈͓͙͚̩̰̭͈̭͙͚̹͖̮͔͓͚̫̭͈̭͙͔͚̪̭͎̘͙͚̪͖̮͇̘͙͚̪̭͓͗͒̒̏͋͊̓̒͒̓̋͆͑̒͘͏̸̴̴̨̡̢̨̡͚̬̮̘͍͚̤̭͓̘͚̫̮͇̭͙̯͚̪̮͍͙̩͚̪̭͇̩͚͎̭͓̩͚̩̮̭͙͚̩̮͓͚̪̮͔͔͚̹̤̭͕̘͚̫̮͔͓͙͚̩̮͕͓͚̬̭͍̘͕͚̹̭͓͙̱͚̬̭͉̭͙͚̮͉̭͙͚̬̮͍̘͙͚̭͓͓͚̭͍͓͙͚̮͔͚̬̮͙͚̹̭͔̘͕͚̩̤̮͆͒̒́̒̑̓͒̓̒͂̓̒͆͒͐͐̒̒̏̓̒̒͐͒̓̒͊͂̒͂͊̏͂̏͗́̏̒͆́͂͆͂͂̓̒͆͑̓͑͊̒͏̢̨̭͙͙͚̫̗̭̹͚̩̗̭̦͚̩̭͈͓͙͚̩̰̮͖̘͙͚̹͖̭͈̘͓͚̫͎̮͎̘͍͚̪̭͎̘͚̪͖̮͇̭͙͈͚̩̮͐̓̒͋̓̒͊̒̒̒̑͆͘͏̸̴̴̨̨̡͚̬̭͈̘͍͚̤̭͔̭͙͕͚̫̮͉͓͙̯͚͖̮͈͙̩͚̩͎̮͖̘̩͚̭͓̫͚̮̘͙͚̪̮͓͙͚̪̭͙͓͚̹̰̭̭͚̫̭͉̭͙͚̮͓͓͇͚̫͖̮͕͚̹͎̭͓͙͚̭͉̘͙̥͚̮͉̭͚͚̬̮͉͓͙͚͚̭̘͚̫̭͙͚̪̗̮͚̫̰̭̘͙͚̹̭͔̘̘͚̮̓̒͋͆̒́͂̓̒͂͊̓̒͂̓͒͒͐̈́̏͊̓͐̒͐͒̓͂̏̒͐̓̒͊́͂́̏̒́͒̒͑̓͋̓͆͒̓̒͌͑͆̒́͒͏̘͙͙͚̫̗̭̬͚̩̗̮͕̭͙̗͚̩͖̭͈͓͖͚̩̰̮͖̭͙͚̹̮͓͚̫̭̭͙͔͚̫̭͎̘͚̫͚̮͇̘͙͍͚͎̮͐̓̒̒͊͑̓̒̏͌͒̒̑́͘͏̶̵̴̸̴̨̨̧̨̨͙͚̬̮͖̭͙͚̤̭͓̭͚̗̮̭͙̯͚̪̮͖͓͙̬͚̩̮͖̘͙̤͚̬̭͓͚̮̭͙͈͚̩̭͙͚̪̭͍̘̙͚̹̰̭͖̘͙͚̫̮͈̘͙͚̩̮͓͓͚̫̮͕͚̫͖̭͓͙̱͚̬͖̭͉̭͙͚̩̮͉̭̙͚̬̮͉̭͚͚̭͔͓͙̥͚̫̮͖̭͙͚̩̗̮͔̤͚̫̤̭͈̘͙͚͎̭͔̘͓͚̗̮̓͆́̒̑́͌͂͂͊̓̒͂͂̓͒͒̓̏̒͒̓̒͊͐̓̒͊̒̒́̓͆̓̒͑́̒͂̕͏̭͙͚̫̗̭͙͚̩̗̭͍͚̩̭͍̭͖͚̩̰̭͎̘͙͚̹͖̭͈̘͓͚̫̗̮͓͙͔͚̪̭͎̘͚̮͇̘͙͉͚̺͚̮̒͐̓͒͋̓̒͊̒̒͑͒̒̑͂̓͘͏̨͚̬̭͈̭͙͚̤̭̓̒͆̒́͏̴̴̷̴̴̸̨̨͚̗̮͇̘͙̯͚̪̤̭͕̘͙̩͚̩̭͇̩͚̪̤̭͓͙͇͚̩̮̘͙͚̩̮͓͙͚̪̭͎͓͙͚̹̤̭̭͚̫̮͈̘͙͚̭͈̭͇͚̬̤̮͔͙͚̫͚̭͓͙͚̹̭͉̭͙͚̩̮͉̭͙͚̬̮͉̭͚̭̓̒͌́̓̒̓͆͒̑͐̏͐̒̓͒̓͂̏̒̓͌͊͂͂̒̑́̏͏̸̡̨̨͚̫̮̘͙͚̮͚̫̮͎̭͈͚̩̭͔̘̘͚̮̓̒͆̓͒͆͂͒̓̒̒̒́͒͏̘͙͓͚̫̗̭̫͚̩̗̭̭̮͚̩̭͎͙͚̹̮͐̓̒͋̒͊̓̐͊͏̨͙͚̺̭̭͖͚̫̮͓͙͔͚̰̭͎̘͙͚̩̮͇̭͙͚̺͚̮̓͊͒̒͑͂̓̏͘̕͏͚̬̮͓̖͚̤̭̓̒͑͆͒̒́͏̸̨̨̨͚̗̮͎͓͙̯͚̩̰̭͓̘͙̬͚̪̭͔̭̩͚̭͓̹͚̮̘͙͚̺̮͓͔͚̪̭͎̭͙͚̹̰̭͖͙͚̫̮͎̘͙͚̩̮͕͓͇͚̫̭͍̘͙͚̹͚̭͓͙̤͚̺͎̭͉̭͙͚̭͇̘͚̬̭̓̒͌́̓̒́̓̒͂̓͒̐̏͐̒̏͂̓͒̓͆̒͌͊̈́͂̏̒͋͏̵̡̭͙͚̭͔͙͚̫̭͓͙͚̭͉̘͚̬̮͎̭͙͚̩̬̭͔̘̘͚̬̮͗́̏̓̓͋͆͂͂̒̏͑̒̏͏̧̭͙͚̪͖̭͙̘͚̩̗̭͇̘͙̗͚̩͖̭͇̭͙͚̩̰̭͖̘͙͚̺͖̭̭͓͚̫͖̭̭͙͔͚̩͖̭͎̘͙̯͚̫̮͇̭͙͚̺͚̭͓͚̬̭͈̭͙̩͚̰̭̐͐̓̐͒̒͌͊͑̒͆́͘̕͏̸̴̨̨̨͚̗̮͖͓͙̯͚̮͎͙̩͚̩̬̭͇͙̤͚̩̭͓̬͚̬̤̮̘͙͚̭̙͚̪̭͚̹̰̭͖͙͚̫̭͍͓͙͚͚̭͍̭͚̬̮͙͚̺͚̭͓͙̲͚̬͖̭͉̭͙͚̮͉̭͙͚͚̬̮͉̭͙͚͚̭̓̒͌́͂͊̓̓̓̒͒̒́͒͒̓̒̏͊̓̒͐̓͒̓́̒͊͐̓͌͊́́̏́͏̵̸̨͙͚̮͕̭͙͚̭͓̭̤͚̫̭͈̘͙͚̪̬̭͔̘͓͚̮̓́͂͆͂̒͑̒͂͒͏̸̸̴̧̭͙͖͚̮͓͙͚̩̗̮͕̭͙͚̩͖̭͍̭͚̹̭̭͙͚̺̭̘͖͚̫̮͎̘͍͚̪͚̭͎̘͙͚̩̮͇̭͙͚̺͚̭͓͚̬̮͖̘͙̹͚̰̭̘͙͕͚̫̭͓͙̯͚̪̰̭̘͙̩͚̩̤̭͔̭͙̤͚̬̭͓͙͇͚͎̮̘͙͚̪̮͓͙͚̪̭͎̭͙́͒̓͊̒̏͊͋͊͊̒̓̒͂͆̋͑̒͊͆́͒͐͒́̓͂͒͐͐̏͘͏͚̹̤̭͕̘͚̫̭͉͓͙͚̩̭̒͐͒̓͆͏̴̸̨̨̨̡̘͇͚̬̤̮͔͕͚̫̰̭͓͙͚̬͖̭͉̭͙͚̭͇̘͙͚̬̮͙͚͚̭͓͓͚̭͓͙͚̭̭͚̬̭͈̘͙͚̺͖̭͔̘͚̬̮̒̓̒͊́̏̈́͊̓́̒͑́͂͋͆͂͒̒͒͑̒͐́͏̸̸̢̨̭͙͓͚̮͓̹͚̩̗̭͇̘͙͎͚̩͖̭͈̘͙͚̩̰̭͕̭͙͚̺͖̭͓̭͖͚̬̮͓͙͔͚̩̭͎̘͙͚͎̮͇̘͙̙͚͎̭͓͙͚̬̮͖̭͙̥͚̰̭͔͙͕͚̫̮͍͓͙̯͚̪̭͂͒̒̒͂͑͆̈́́́͑͆͆́̓͘͏̸̴̴̵̨̨̨̡̘͙̬͚̩̭͇͙̤͚̪̤̭͓͚̪̮̘͙͚̩̭͙͚̪̮͔͓̙͚̹̰̭͖͓͙͚̮͓͓͙͚̮͔͓͇͚̬̮͔͕͚̺̭͓͚̭͉̘͙̥͚̭͇̘̖͚̬̮͍̭̙͚̭͓̭͙͚̫̭͉͓͙͚̪͚̮͕͚̬͖̮͈͚̭͔̘͓͚̫̰̮̓̓̒͂͆͒̓͒̓͗̏̒́̓͂̏̒͆̓̒͊̒̔͂͒́̏̒̒́̏̓͆̓̒͑̓̒́͒̒͏̷̢̘͙͕͚̪͖̮͓͙͕͚̩̗̮͕̭͙͚̩̭͈͓͙͚̹̮͓̭͙͚̹̭͉̘͖͚̫͎̮͓͙͔͚̪̬̭͎̘͙̮͚̮͇̭͙͇͚͎̭͓͙͚̬̮̭͙͎͚̰̭̘͙͚̗̭͒̏͊͊͊̒͑́̓́͑͆͒́͒͂́͘͏̨̭͙̯͚̪̭͓̘͙̬͚̩̰̮͖̘͙̤͚̩͖̭͓̩͚̮̭͙̓̒́̓͒͏̴̴̴̵̴̨̨̢̨͚̩̭͚̪̭͎͓̙͚̹̤̭̭͙͚̮͇̘͙͚̩̭͖̘͇͚̫̭͓͕͚̫͎̭͓͙̱͚̬͖̭͉̭͙̦͚̬̮͉̭͙͚̬̮͍̘͚̭͓͓͙͚̭͙͚̪̮͖̤͚̬̭̘͙͚̹̤̭͔̘̘͚̩̮͒̓̒̋̏̒͐́̓̒͊͒̒͊̒͌́̏́͂͋̓͆̓̓̒̏͌͑̒͏̢̭͙͚̪͖̭͙͚̩̗̮͕̘̮͚̩̭͇̘͚̩̰̮͓͓͙͚̫̤̭̘͖͚̫͎̮͓͍͚̪̭͎̘͙͚͎̮͇̭͙̗͚͎̭͓͚̬̮̘͙͚̰̭̑͐̓̒͊̒̏͊̒͑̒͒́́͑̒͆͒͊́̕͘ͅ͏̸̴̴̴̴̨͙͕͚̫̮͍͓͙̯͚̮͈͙̩͚̩̭͔̭̩͚͎̭͓̹͚̩̮̘͙͚̩̮͓͙͚̪̭͙͓͚̹̤̭͓͚̫̮͎̘͙͚̭͍̭͚̬̭͓͕͚̹͚̭͓͙̤͚̗̭͉̘͙̣͚̮͉̭͚̬̮͍̘͚͚̭͓͚̫̭͉̭͙͚̪̮͔̤͚̬͖̮͎̭͈͚̭͔̘͚̪̮̓͂͊̓̒͂̓̒̏͒͑͐̏͊̓͐̒̓͒̓͂̏̒͊͆͒̒͊͂́̏̒̋̒́͑̒͆̓͆̓̓̒̒͂͂̒̏̕͏̸̸̴̸̢̨̨̨̨̨̘͙͚̮͓͚̩̗̭͓̖͚̩͖̭͈̘͙͚̩̰̮̭͙͚̫̤̮͓͚̫̮͓͙͔͚̫̭͎̘͙͚̪͖̮͇̘͙͚̩̭͓͙͚̬̮͖̭͍͚̤̭͓̭͙͕͚̫̭͔̭͙̯͚̩̤̮͓͙̩͚̪̮̘̩͚̬̬̭͓̫͚̬̤̮̘͙͚̺̭͙͚̪̮͔͙͓͚̹̤̭͖͓͚̮͖̘͙͚̭͉̭͚̫̮͙͚͖̭͓͚̗̭͉̭͙̪͚̬̭͇̘͙̥͚̬̮͉̭͙̬͚̭͚̫̮͕͓͙͚̩̮̤͚̫̭͈̘͙͚̭͔̘͖͚̬̮̐́͒̒̋͌̒͑͒̓̒͒͑͒͋͆͑͆̒́͐̏͒̒̓̒͒̒̏͒̓̓̏̓̒̓́̓́̏̒͊͐̓͌͂͊̒̔͂́̏͑̓̒͆̓͆̓͒̓̒͑́̒́͘ͅ͏̸̘͙͓͚̪͖̮͓͚̩̗̭̭̲͚̩̭͍͓͚̹̮̭͙͚̹̮͖͓͚̫̭̭͙͔͚̩͚̭͎̘͙͚̪͖̮͇̭͙̘͚̺͚̮͒̒͋̒͊̒̏͊͒͊̓̒͒͌͘ͅ͏̴̨͚̬̮̘͙͚̰̭͙͕͚̗̮͈̘͙̯͚͖̭͓̘͙̬͚̪͖̮̘͙̤͚̭͓̮͚̮̘͙͚̭͙͚̪̮͔͓͙̓̒͆͆͒̏́͑̓́͂͒́̓̒͂͒̒́͒͒̓̒̏͏̸̡̨̡̨͚̹̤̭͕̭͚̫̮͇͓͙͚̗̭͇̭͚̫͚̮͙͚̺̭͓̗͚̫̭͉̭͙͚̮͉̭͙̹͚̬̮͉͓͚̭͓͚̭͎͓͙͚̪͚̭͓̭͚̫̤̭̘͈͚̩̰̭͔̘͙͚̮̒̓͒̓́̒͊͐̓͌͊̒̏͂̏̒́̏͑̒͑́͂͆̒͌̒͂͂͘͏̴̧̨̨̘͙͕͚̪͖̭̤͚̩̗̮͕̭̲͚̩̭͈̘͖͚̹̭͖͓͙͚̹̭͈̘͖͚̫͖̭͈̭͍͚̩̗̭͎̘͙̯͚͎̮͇̭͙̗͚̪̭͓͙͚̬̮͖̭͚̤̭̘͙͕͚̗̭͓͙̯͚͖̮͕͓͙̬͚̩̰̮̘̩͚̗̭͓̹͚̩͖̮̘͙͚͚̪̭͙͚̪̮͔͙̰͚̹̰̭͕͓͚̭͇̭͙͚͚̮͖͓͇͚̫̭͍̘͕͚̭͓͙̲͚̫̰̭͉̘͙̦͚̮͉̭͚̬̭͐̓̒̒͊̒͊̓̒̒́͆͑͆̒͑́͒́͑͂͒̒͂̓̒͒͒̓̏̓̒͐́̓͂̒̏̒͂̓͊́̏̒͋͘ͅ͏̵̴̭͔͚͚̭͔̘͙͚̫̮͓̘͙͚̪̗̭̘̤͚̫̭͈̘͈͚̭͔̘͕͚̩̮̒́̓͆͊̒̒͂͆̒͊͏̭͙͏̸̨͚̮͓͚̩̗̭͇̭͙̗͚̩͖̭͇̭͙͚̹̭͓̘͙͚̹̭̘͓͚̫͎̮͓͍͚̫͖̭͎̘͙̮͚̮͇̭͙͚͎̮́͒̒̓̐͊̓͊̒͑̒͂̏́͘͏͍͚̬̮̭͍͚̤̭͔̭͚̗̮͕͓͙̯͚̩̰̭̓̒͆͒̒́̒̑́͏̸̴̴̸̨̨̘͙̩͚̩̭͔̭̩͚̬̭͓̩͚̩͖̮̘͙͚̪̭͚̪̭͚̹̤̭͓͚̮͍̘͙͚̩̭̭͇͚̬̮͙͚̫͖̭͓͙̱͚̹̭͉̭͙͚̭͇̘͙̣͚̬̭̒́̓̒͒̑͒̓̒̏͊̓̒̑͐̒̓́̓͌̒͂͐̓͌͊̈́́̏̕͏̡̨̭͚͚̭̭͙̥͚̫̭͎̭͙͚̩̭̭͚̬͖̮͙͚̭͔̘͖͚̪͚̮̒́͑̓͆̓͒̒͑̓͑͂̒̕͏̢̘͙͚̪͖̮͓͚̩̗̮͕̭͙͚͚̩̭͇͓͙͚̩̰̭͖͙͚̹̭̘͓͚̫̮͎̘͍͚̪̭͎̘͙͚̩̮͇̭͙͚̺͚̮̒͒̒́͊̓̓͋̒̓̒͆̈́̏̓͘͏̷̴̨̨̨̨̡͙͚̬̮͓͙̥͚̰̭͔̘͚̗̮͖̘͙̯͚̪̰̮͍͙̩͚̩̰̭͔̭͙̤͚̬̭͓͙͇͚̩͖̮̭͙͙͚̺̮͓͙͚̪̭͎͔͚̹̤̭͖͚̭̘͙͚̩̭͈̭͚̫̮͙͚̹̗̭͓͙̱͚̹̭͉̭͙̦͚̮͉̭͙͚͚̬̮͉͓̙͚͚̭͔͓͚̭͙͚̪͚̮͓͚̫̰̮͎̭͙͚̪̗̭͔̘͚̩̮̓͆͒́̒͌́̓͒̓͒̏͐̏̓̒̓̒͐́͋̓͆̒͊͐̓͌͊̓́̏̒́̒͆́͂͋̓͆̓̒͑̒̏͏̘͙͚̫̗̮͓̥͚̩̗̮͕̭͙͎͚̩͖̭͈̭͙͚̹̮̒͒̒̐͊͏̘͙͚̺̭͍̘͖͚̬̮͓͙͔͚̪̤̭͎̘͙͚̫͚̮͇̘͙̙͚͎̮͊̒͂͑́͘ͅ͏̵͙͚̬̮͖̭͙͚̤̭̘͚̗̭̘͙̯͚̩̤̭͓̘͙̬͚̩̮͖̘͙̤͚͚̭͓͙͚̮̭͙͚̺̮͓͙̦͚̪̮͔̙͚̹̤̭̓̓͆́͒̒͌́͐͂͂̓͊́̓͒̐̏͐̏̓̒͏̵̸̨̧̨̨̭͚̮͖̭͙͚͚̭̘͚̫̗̮͔͙͚̭͓͙̤͚̬͖̭͉̘͙͚̩̮͉̭͙͚̬̮͍̭͙͓͚͚̭͙͚̫̮͖̭͙͚̭̭̤͚̫̭̘͙͚̩̭͔̘͙̥͚̩̮̒͐́̓͂͐̒͊̓͌͂͊͊͌́͒̓̓͆͂͑̒͂͌͑͆͊͏̸̸̴̨̨̘͙͈͚̭̗͚̩̗̮͕̭͚̩̭͍͓͙͚̹̭͖͙͚̫̰̮͓͚̫̮͓͍͚̭͎̘͙̮͚͎̮͇̘͙̘͚̺͚̭͓͙͚̬̮͙͚̰̭͓͙͚̫̮͉͓͙̯͚̪̰̭̘͙̬͚̩̬̮͖̘͙̤͚̩̭͓̩͚͎̮̘͙͚̪̭͙̫͚̪̮͔͓͙͚̹̰̭́͐̓̒̒̈́͊̐͊̓͑̓̒͑̒͂͆͂͑́͆͑̓̓́͒͂͐̓̒́͒͐͒̓̏͗͘͏̴̴̴̵̸̨̨̡̨̘͚̫̮͓͙͚̩̭̭͚̬̮͕͚̹̭͓͙͚̭͉̭͙͚̬̭͇̘͚̬̮͍̘͙͚̭͔̭͙͚̫̮͓͙͚̭̘͚̬͎̭͈̘͈͚̭͔̘͙͚̮̒̓͒̓̓͌̒͊͆͐̓̒͊͊́͂͆̒̏́̏̓͒͆͂͌̒̒́͆͂͂͏̸̘͙͔͚̮͓͚̩̗̭̘̮͚̩͖̭͇͙͚̹̭͓͙͚̹͖̭̘͓͚̬̭̭͍͚̭͎̘͚̬̤̮͇̭͙͇͚͎̮́͒̒̋͋̒̓̐͊͋͊̒͂͌̒́͂̒̑́͘͏̸̗͚̬̮̘͙͚̤̭͙͚̫̮͇͙̯͚̭̓̒͆͒̓́͑̓͂̓͂͊͏̸̸̴̴̸̨̨̨̨̘͙̩͚̩̬̭͔̭̩͚̫̭͓̹͚̮̭͙͙͚̺̮͓͙͚̪̭͓͚̹̰̭̭͙͚̮͓͙͚͎̭͈̭͚̬̰̭͍̘͕͚̺̭͓͙͚̬̰̭͉̘͙̣͚̭͇̘͙̬͚̬̮͉͓͙͚̭͓̘͚̫̭͍̭͙͚̪̮̤͚̫̭͈̘͙͚̹̭͔̘̘͚̮̒̓̒͂͒̏͐͐̏͊̒͐́͑̓́̒͊̒͒͊͂̏́̏̒͆̓͆̓͒̓̒͑̒́͂̕͏̢̭͙͖͚̪͖̭̰͚̩̗̭͓̖͚̩̭͇͙͚̹̮͕̘͙͚̫̤̭͓̭͓͚̫̭̭͙͔͚̪̬̭͎̘͚͎̮͇̭͙͚̪̮͐̓̒͌̒͊̓͊̒̏͌̒̑͂͋͆͘͏͙͚̬̮͓͚̰̭͓͚̗̮͈̭͙̯͚̩̤̭̓̒͆͒̒͑́͒̒̑́͏̴̘͙̩͚̪͚̮͖̘͙̤͚͖̭͓̹͚̪͖̮̭͙͚͚̩̭͔͚̪̭͎̭͙͂̓̒͒͒̓̒̏͏̴̨̡̨͚̹̤̭͕̭͙͚̫̭͈̭͙͚̩̮͓͓͚̬̬̮͕͚̭͓͙͚̫̭͉̭͙͚̭͇̘͚̬̮͉̭͙͚̭͔̘͚̫̭̭͙͚̩̗̮̤͚̬͚̭͈̘͈͚̹̰̭͔̘͓͚̗̮͒̓͆̒͊͐̓̒͂̏͊͆͂̏̒͌͗́̏̒͑̓͊͆͒̓̒̒̒͂͏̷̘͙͚̫̗̮͓͙̘͚̩̗̭̭̮͚̩͖̭͇̭͙͚̹̭͖͓͙͚̫̰̮͓͚̫̗̮͓͙͔͚̩̭͎̘͙̮͚̬̤̮͇̘͙͈͚̪̭͓͙͚̬̮̭͚̤̭̘͚̗̭̭͙̯͚̪̰̮͓͙̩͚̩̮͖̘̩͚̭͓̮͚̪̰̮̭͙̐͒͋̒̐͊͑̓̒͑͆͆͑͆͒̒̒́͑̒͌́͑͐͆̒́͊̓̒͒͘͏̴̨̨̡̨̨͚̺̮͓͙̭͚̪̮͔͙͚̹̰̭͙͚̫̭͈̭͙͚͚̭͇̭͚̫͚̮͙͚̬̗̭͓͚̬̰̭͉̭͙̥͚̮͉̭͕͚̬̮͉͓͙͚̭͔͓͚̭̭͙͚̪̭̭͚̫̭͈̘͈͚̭͔̘͙͚̮̏͐̏̓͗͐̓͒̓͂̒͊͐̓͌͊̒̔́̏̒͂́̏̒͆́͂͌͆̓͒̒̒͂͂͂͏̸̭͙͚͚̭͚̩̗̭̭͚̩̭͈̘͚̩̰̭͙͚̹̮͖͚̫̮͓͍͚̪̬̭͎̘͙̮͚̬̤̮͇̭͙͚̺͚̮́͐̓̒̑͋̒̋͊̒̏͊̓͒͒̓̒͒͑̒͊͘͏͚̬̮͖̘͙͎͚̤̭̭͙͕͚̗̭̘͙̯͚̮͍͙̬͚̩̬̮͖̘̩͚͎̭͓͚̩͖̮̭͙͓͚̭͙͚̪̮͔͓͙͚̹̤̭̓̒͆͆́͑́͒͂͊̓̒͂̓̒͂͒́͒͒̓́̏͂͏̸̴̨̨̡̨̘͙͚̮͔͙͚̗̭̘͇͚̫͚̮͕͚̭͓͙͚̺̭͉̘͙̣͚̬̭͇̘͚̬̮͍̘͚͚̭̭͚̫̮͓͓͙͚̪̮͕̤͚̬̗̭̘͙͚̩̬̭͔̘̘͚̗̮́̓̓́͐̒͐̓̒͂͊̓̒͒̒́͒̒͑̓͆̓̓̒͌͑̒͂͘͏̭͙͏̸̵̢̨͚̮͓͚̩̗̭͇̘͙͚̩͖̭͈͓͙͚̩̰̮͙͚̫̰̭͓̭͓͚̫̭͈̭͍͚̫̭͎̘͙̮͚̬̤̮͇̭͙͇͚̩̮́͒̒͊͒̓̒̒͒͆͘͏̓̒͏̸̴̶͚̬̮̭͙͚̤̭͓̭͙͚̗̮͕̘͙̯͚͖̭̘͙̩͚̩͎̮̘͙̤͚͖̭͓̬͚̮̘͙͙͚̩̭͙͚̪̭͚̹̰̭͆͒̏́͂́͂͒͒͂̓̒́͒͒̓̏͊̓̒͌͏̸̨̨̨̡̨̡̭͙͚̮͇̘͙͚͚̭͍̭͇͚̬̭͓͙͚̹͚̭͓͚̺̭͉̭͙͚̭͇̘͙͚̬̮͙̬͚̭͔̘͙̥͚̫̭̭͙͚̭͓̭͚̬̮͈͚̩̭͔̘͓͚̩̤̮́̓́̒͂͒͌͊̒̔͂́̏͊̓́̏̓͌͆͂̒͊͑̓̒͒̒͏̸̢̘͙͚͚̭͙͚̩̗̭̘͙͚̩͖̭͍̘͙͚̩̰̮͂͐̓̋͋͊͏͙͚̺̮͔͓͚̫̭͈̭͍͚̩̭͎̘͙͚̩͖̮͇̭͙̘͚̺͚̮̓͊̓̒͊̒̓͘ͅ͏̸̴̴̸̸̨̨̨̙͚̬̮͖̘͙̥͚̤̭͚̫̮͇̭͙̯͚̪̮͇͙̩͚̩̮̘͙̤͚̬̭͓͙͚͎̮̘͙͚̩̮͓͙̲͚̪̭͎̭͚̹̤̭͕̘͙͚̫̭͇̭͙͚̩̭͎̭͚̫̗̮͔͙͚̭͓͙̲͚̹̭͉̘͙͚̭͇̘͙̱͚̬̭̓̒͆́͑̓̒̑̓͒́̓͊́͒̓͐̏̒͌͒̓͆̒͊̓͌͂͊́̏ͅ͏̨̡̘͙͚͚̭͓͓͙̥͚̭̭͙͚̩̗̮͚̫̰̮͎̭͈͚̪̬̭͔̘̘͚̫̰̮́́͂͋͆͐̓̒̒̒͏̨̭͙͖͚̫̗̭̘͚̩̗̭̭̲͚̩͖̭͇͓͙͚̹̭͓̘͙͚̹̭̘͖͚̫͚̭̭͙͔͚̩̗̭͎̘͚̩͖̮͇̘͙͇͚͎̭͓͚̬̮͖̭͉͚̤̭̘͙͚̗̭͐̓̒͋̒̐͊͒͌̒͌̒̑́͑̒͆̒́͒͂́͘͏̴̴̨̘͙̯͚̪̭̘͙̬͚̩̮͖̘͙̤͚̩̰̭͓͙͇͚̮̘͙͚̪̭͎͚̪̭͎͓͙̬͚̹̤̭͂͑̓͂͒͗͒̓̒̏͏̭͚̫̮͇͙͚͚̭̒̓͒̓̓͂͏̷̵̴̨̨̡̨̘͇͚̬̮͕͚̬̭͓͙͚̗̭͉̘͙̥͚̩̭͇̘͙͚̬̮͉͓͙̰͚̭͙͚̫̭͙͚̪͚̮͚̬̮͎̭͙͚̩̭͔̘͖͚̩̮̒͆͐̓̒͒͊͂̔́̏͑̓̓͋̓͆͑̓̒̓͑̒͏̴̨̘͙͕͚̫̗̮͓̥͚̩̗̭͇̘̖͚̩̭͉͚̩̰̮̘͙͚̫̰̭̘͓͚̫̮͓͍͚͖̭͎̘͙͚̪͖̮͇̘͙͚͎̭͓͚̬̮̭͙̩͚̰̭̭͚̗̭͓͙̯͚̪̤̭̘͙̩͚̪͚̮͖̘̩͚̗̭͓̩͚̫͚̮̘͙͚̩̭͙̮͚̪̮͔͚̹̤̭͕̘͚̫̮͉͙͚̮͕͓͇͚̫͚̭͓͙͚̫̭͓͙̱͚̭͉̘͙̹͚̮͉̭͙͚̬̭͒̒̒͊̓̒̏͑͌̒̓͑̒́̓̏́͑̒͑͆͒́͒̒̑́͒͒̒͂̓̒͒͗͒̓̏̓̒̑̒̓͒̓̓́̏̒͒͌͆͊́͂͂̏͌͘͏̡̭͙̬͚͚̭͓͚̭͈̘͙͚̪̭̘͚̬̮͎̭͈͚͎̭͔̘̘͚̬̮́͒̒͑́͂͆̓͋̒͊̒́̒̏͏̭͙͙͚̫̗̮͓͚̩̗̭̭͙͚̩̭͇̭͖͚̹̮̭͙͚̫̤̮͔͓͚̬̬̮͎̘͍͚̪͖̭͎̘͙͚̫͚̮͇̘͙͚̺͚̮͒̒̏͋͒͊̒͊͑̓̒̒̓̋͘͏͙̤͚̬̭͈̘͙͚̤̭͓̭͙͚̗̮̓͆̏́͂́͏̴̨̨̨̨̡̨͓͙̯͚̮͕͓͙̩͚̩̭͇͙̤͚̪̭͓̮͚̮̘͙͖͚̮͓͙͚̪̭͚̹̤̭͖͓͙͚̮͕̭͙͚̭͍̭͚̬̬̮͕͚̹̭͓͙̤͚̺̭͉̘͙̪͚̮͉̭͙͚̬̮͍̘͚̭͔̭͚̫̭͉̘͙͚̪͚̮͔͚̫̭͈̘͈͚̩̤̭͔̘͕͚̫̮͂͊͆̓̓̓̒͂͒́͒͐̈́̏͊̓̒͌́̓͂̏̒͊͐̓̒͊̓͂̏͌̒́̏̒͑̓͆̓̒̒̒͆̕͏̸̸̧̭͙͈͚̭͚̩̗̭͇̭͚̩̭͎͓͙͚̩̰̮̘͙͚̫̰̮͓͖͚̬̤̭̭͍͚̩̭͎̘͚̬̤̮͇̘͙̘͚̪̮͂͐̓̒̒̈́͊̐͑̓̒͌̒̒̑͆͘͏̴̷̨̨̨͚͚̬̮͖̭͍͚̤̭͔̭͙͚̗̭̘͙̯͚̩̤̮͎͙̩͚̪͚̭͇̩͚̩̤̭͓͙͚̫̮̭͙͈͚̪̭͙͚̪̭͚̹̤̭͕̘͚̮͕͓͙͚̭̭͚̫̭͓͙͚̬͚̭͓͙̤͚̬̭͉̭͙̣͚̮͉̭͙͈͚̬̭̓̒͆̒́͂́͒̓̓̒̓͊͊͒͒̓̏͊̓̒͐̒̓́̓́̏͌̒͊͒͌͊̏͂̏͏̡̭͙͓͚͚̭͚̫̭͙͚̪͖̭̘͚̬̮͎̭͙͚̭͔̘͓͚̮́͑̓̒͑̓͊̓͆͊̒̏͑́͆̒͂͒͏̸̭͙͚̮͓͙͕͚̩̗̮͕̘͍͚̩̭͎̘͖͚̹̮͓͙͚̫̰̮͔͓͚̬̰̮͓͍͚̭͎̘͚͎̮͇̭͙͚͎̮̑́͒̒͊̒͊͒̓̒͑̒͂͊̒̑́͊́͘͏̨͚̬̮̭͙͚̰̭͔͓͚̗̭͔̭͙̯͚̪̮͖͓͙̩͚̩̰̮̘͙̤͚̭͓͚̪͖̮̭͙̓̒͆͒̓́̒͌́͂͒́̓̓̒͂͒͏͚̺̮͓͙̺͚̪̮͔͓͙̏͐̏͏̴̨̨͚̹̤̭͖͚̫̮͔͓͙͚̗̭͉̭͚̬̮͔͕͚͚̭͓͙̱͚̬̭͉̭͙̦͚̮͉̭͖͚̬̮͉͓͙͚̭̘͚̭͉͓͙͚̪͚̭̭̤͚̬̮͈͚͎̭͔̘͙̥͚̩̮̓̒͐͒̓́̒͊͆̓̒͂͊̏́̏̒́̏͑̒͑́͂͆͒̒̓͑̓̒́͏̸̘͙͚̫̗̭͚̩̗̮͕̭̖͚̩̭͈͙͚̹̭͓̘͙͚̹̭̘͖͚̫͎̮͓͍͚̪̰̭͎̘͙̯͚̮͇̘͙͈͚͎̮͑͐̓̒͂̒͊̓̐͊̓͋̒͑̒́́͘͏̸͚̬̮͖̘͙̥͚̰̭͔͓͚̫̭̓̒̐͆́̒̑͏̴̸̸̨̡̧̨̨̭͙̯͚̩̰̮͖͓͙̬͚̩͎̭͇͙̤͚̩̭͓͚̩͖̮̭͙͔͚̩̭͙͚̪̭͎̭͚̹̰̭͕̘͚̭͎͙͚̭̭͚̬̮͙͚̬̭͓͙͚̹̭͉̘͙͚̩̮͉̭͈͚̬̭̓͊̓̒͂͒͒̓͂̏̒͐̒̓́̓̓͂̏͌̒͊͐̓͌̓͊̒͏̘͙͓͚͚̭͓͓͚̫̮̘͙͚̮̤͚̬̭̘͈͚͎̭͔̘͕͚̪̮́̒͑̓͑͆͂͂͑̓̒͒͌̒́̒͊͏̸̨̘͙͕͚̭͙̙͚̩̗̭͇̘͙̗͚̩̭͎̭͙͚̩̰̮͓͙͚̺̭̭͓͚̫̮͓͍͚̬̤̭͎̘͙̮͚͎̮͇̭͙̙͚̺͚̮͂͐̓͊̐͐͊͑̒͑̒́͘͏̗͚̬̮̘͙̩͚̰̭̭͚̗̮͖͓͙̯͚̭̓̒͆͒́͒̒̑́͂͊͏̸̴̸̨̘͙̩͚̩̮̘͙̤͚̭͓̬͚̩̮̭͙͚̪̮͓͚̪̭͍̘͚̹̰̭͖̭͙͚̫̭͓͙͚̮͓͇͚̬̬̮͕͚̫̗̭͓͚̗̭͉̘͙̤͚̮͉̭͙͚̬̮͉̘̙͚͚̭͂͒́̓̒̏͒̒͐̒͑̏̒͒͌̓́̏͐̒͐̓̒͊̒̔͂́̏͌̒́̕͏̵̸̸̡͙͚̫̭͉͙͚̮͔͚̬̮͎̭͙͚̭͔̘͓͚̮̓̓̓͆͂̓̒͆͑́̒͂͂͏̸̢̨̘͙͚̫̗̮͓̫͚̩̗̮͕̘͙͚̩̭͈̘͙͚̹̭̘͙͚̺̭͉̘͖͚̫̗̭͈̭͍͚̪̭͎̘͙͚̩͖̮͇̭͙̙͚̺͚̭͓͚̬̮͖̭͙̥͚̰̭͔̘͚̫̭̒͒̒͊͊͊͋͊̒̒͆̈́͑̒͆́̒̑͘͏̨͓͙̯͚̪̭̘͙̩͚̩͎̭͔̭͙̤͚̤̭͓͙͇͚͎̮̘͙͈͚̮͓͙̳͚̪̮͔͚̹̤̭͑́̓͂͒́͒͐̏̓̒͘͏̸̨̢̨̭͙͚̮͙͚̩̭̘͇͚̫̮͔͙͚̹̗̭͓͙̲͚̹̭͉̘͙͚̭͇̘͙͚̬̭́͐̓̓͆͐̒͊̓͌͊̓͂̏̈́͏̸̸̡̘͙͚͚̭͔͓͙̥͚̮͖̭͙͚̭͓̭͚̬̭̘͙͚̺̭͔̘͚̬̮́́͂͆͂̒͊͌͑̏̒̏̏͏̢̘͙͚̪͖̭̘͚̩̗̭̭͙͚̩͖̭͇͓͙͚̩̰̭͉̘͙͚̺͖̮͔͖͚̫̭͈̭͍͚̰̭͎̘͙͚̪͖̮͇̘͙̙͚̪̮͐͐̓̒͋̏̓̒̏̒͂̓͆͘͏̸̴̸̵̸̨̡̨̨͙͚̬̭͈̘̖͚̤̭͚̫̮̭͙̯͚̩̰̮͍͙̩͚̪̭͔̭͙̤͚̪͖̭͓͙͇͚̬̤̮̭͙͙͚̭͙̳͚̪̮͔͙̬͚̹̰̭͔̘͚̮͓͓͙͚̗̮͓͇͚̫̭͍̘͕͚̹͎̭͓͙͚̹̭͉̘͙̦͚̬̭͇̘͙͚̬̮͍̭͙͚̭͙͚̫̮͙͚̪͚̭̭̤͚̫̤̮͎̭͙͚̩̭͔̘͙̥͚̬̮̓́͆̒́͒̓̒͌͌̓͒̓͒́͒͒̓̏̓̒͐́̓́͐̒͊̒͊̔́̏͑̓̓͒̓͆͑̒͑́͏̸̸̶̴̴̸̨̨̭͙͚̮͓͚̩̗̭̭͙͚̩̭͍͓͙͚̩̰̭͓͙͚̹͖̭̘͓͚̫̮͓͍͚̭͎̘͙͚̫͚̮͇̘͙̘͚̺͚̭͓͙͚̬̭͈̭͚̰̭͔͓͙͕͚̗̭͖̘͙̯͚̮͕͓͙̩͚̩̭͇͙̤͚̪̭͓̫͚̩̮̭͙͈͚̩̮͓͚̪̭͎͓͔͚̹̤̭͕̭͙͚̫̭͍̭͙͚͎̮̑͂͒̒͋͒͊̐͊͌̒͑̒͂̓͑͆̒̒́́͂͊̓͒̓̒̏͒͐̒͑̏̒͒̓́͘͏̴̨̡͓͚̬̭͍̘͕͚̬̭͓͙̱͚̬͖̭͉̘͙͚̮͉̭͙̪͚̬̮͍̘̙͚͚̭̭͚̮͙͚̭͉̘͚̬̭̘͙͚̩̰̭͔̘͚̪̮̒͊̒͒͊̈́͂̏̒́͒̒͑́͂͐̓͆͂͂̒̓͌͑̒͐͊͏̸̢̘͙͚̫̗̮͓͙͚̩̗̭̘̺͚̩͖̭͍̭͙͚̹̭͓͙͚̹͖̮͕͓͚̬̮͎̘͍͚̭͎̘͚̬̤̮͇̘͙̖͚̪̮͒͒͊͋̒͊͋̓̒̒́͂̒̑͆͘͏̸̴̗͚̬̮̘͍͚̤̭͓͙͕͚̫̮͇͙̯͚̪̰̮͙̩͚̪̭͔̭̩͚̬̭͓̫͚̩̮̭͙͙͚̩̮͓͙͚̪̭͓͚̹̰̭̓̒͆͒̒́͑̓͊̓̓̒͒̓̒͆͒͐͐̏͊̒̕͏̴̴̨̨̨̨͓͙͚̮͓͙͚͎̭̭͇͚̫̮͕͚̺̗̭͓͙͚̫͖̭͉̘͙͚̬̭͇̘͙͚̬̮͚̭͔̭͚̭͙͚̪̗̮͔̤͚̫̬̮͈͚̩̤̭͔̘͕͚̫̰̮́͑̓́͌̒͐̓̒͊̈́́͊̓̒͌́̏̒͑́͂͒̓͆̓̒͑̓̒̒͏̸̢̭͙͓͚̭͙͉͚̩̗̭͇̭͙͚̩͖̭͈̭͙͚̹̭͖̘͙͚̹͖̮͔͓͚̫͚̮͎̘͙͔͚̭͎̘͙͚͎̮͇̘͙͚̩̮͂͐̓͒͊̓̒́̓̈́͂͆͘̕͏̴̴̨̨̨̨̨͙͚̬̮͖̭͉͚̰̭̘͚̗̮͈̭͙̯͚̪̮͙̬͚̩̤̭͔̭̩͚̫̭͓̫͚̩͖̮̘͙͚̪̭͚̪̭͎̭͙͚̹̰̭̭͙͚̮̭͙͚̩̮͓͓͚̫̮͕͚͖̭͓͚̫͖̭͉̭͙̥͚̮͉̭͚̬̮͉̭͚͚̭͔͓͚̫̭͙͚̪͖̭͍̘̤͚̬̭͈̘͈͚̹̭͔̘͓͚̬̮̓͆̒́͒̒̑́͊̓̒̓̒͒̑͒̓̒̏͂͐́͐̓̒͊͒͐̓̒͂͊̒̔́̏̒̏̒̑́̒͑̓͋̓͆̒͊̒͊̒̏̕ͅ͏̘͙͏̸̸̸̴͚̪͖̮͓͚̩̗̭̘͙͚̩͖̭͇̭͙͚̩̰̭͓͙͚̹̭͉̘͓͚̫̗̮͎̘͙͔͚̪̭͎̘͚̮͇̭͙͚͎̭͓̘͚̬̮̭͙͎͚̤̭̭͙͚̫̭͓͙̯͚̭͕̘͙̬͚̪̭͔̭̩͚̩̭͓̫͚̮̭͙͚̺̮͓͙̪͚̪̭͎͓͙̬͚̹̤̭͕͚̫̭͉̭͙͚̭͒̒͆͋͊̐͋̓̒̒̑́̓́͑̒͆͒́͒͂͐͂͊͊̒̓̒͂̓͒͑̏͐̏̓̒̓͒̓͂̏͘͏̡̨̧̨̘͇͚̬̤̮͕͚͖̭͓͚̺͎̭͉̭͙͚̩̮͉̭͙͚̬̭̒͐̓̒͂͊̒̔͏̸̡̨̨̭͙̰͚͚̭͔͚̭͉̘͙͚̭͉̘͚̫̭͈̘͙͚̺̭͔̘͙͚̮́̓̒͑́͂͆͂̒͑̏͂͂͏̘͙͚̫̗̭͙͚̩̗̭̺͚̩̭͈͙͚̹̭͓̘͙͚̺͖̭͉̘͓͚̬̮͎̘͍͚̪̭͎̘͙̮͚̫͚̮͇̘͙͍͚̺͚̮͑͐̓͐͋̓̒͊̓̐͊̒͂̒̓͘͏̷̸̸̴̨͙͚̬̮͖̘͙͚̰̭͔͓͙͚̫̭͔̭͙̯͚̩̰̮͕͓͙̬͚̩̮͖̘̩͚̫̭͓͙͚͎̮̘͙͚͚̩̭͙͚̪̮͔͙͚̹̤̭̓͆̒́͂͆̒̓͊́͒͒̓͂̏̓͏̸̨̡͓͙͚̫̮͇͓͙͚͚̭͈̭͚̬̭͍̘͙͚̫͎̭͓͙͚̺̭͉̘͙̥͚̭͇̘͒̓͂̒͊͌͊̓͂̏̒͏̨͚̬̮͉̭͚͚̭̭͚̫̭͓͙͚̩̭̭̤͚̬̭͈̘͈͚̭͔̘͚̬̮̒́͒̒͑̓͒͆̓͑̒͒̒́͊̒̏͂̕͏̭͙͏̸̸̴̢͚̫̗̮͓͚̩̗̭͇̭͙͚̩͖̭͉͙͚̹̮͓͙͚̺͖̭͈̘͓͚̫̭̭͙͔͚̩̭͎̘͙͚̩͖̮͇̭͙͚̺͚̭͓͚̬̮̭͙͚̤̭͔̭͚̗̮͈͙̯͚̮͇͙̩͚̩̮͖̘̩͚̬̭͓̫͚̮̘͙͚͚̪̭͙̲͚̪̭͍̘͙͒̒̔̏̓͊͒̒̏͌̏̓͑̒͋͆͒̏́̒͌́̓͂͊̓̒́̓̒͂͒͒̓̏͘̕͏͚̹̤̭͏̨̨̘͚̫̭͎̘͙͚͚̮͕͓͇͚̬̭͓͕͚̭͓͚̗̭͉̭͙̹͚̮͉̭͚̬̮͉̘͙͚͚̭̒̓͒̓́̒͂͒̒́͂͊̒̔͂́̏̒́̕͏̡̨͚̫̭͓͙͚̪̮͓͚̬̮͎̭͈͚̩̭͔̘͙̥͚̗̮̓̒͆̓͋͆̓̓̒̓̒͂͏̭͙͚̪͖̮͓͙͒͒͏̴̢͚̩̗̭̭͙̗͚̩̭͇̭͙͚̹̭͓̘͙͚̹̭̘͖͚̬̭͈̭͍͚̪̭͎̘͙͚͎̮͇̭͙͚̺͚̮͋͊͊̓͋̒̒͊̈́͂̔͘͏̴̴̨̨̖͚̬̮͖̭͙̹͚̤̭͓͓͚̗̮͖̭͙̯͚̪̰̭͖̘͙̩͚̩̭͔̭͙̤͚̫̭͓̬͚̩̮̘͙͚̺̮͓͙͚̪̮͔͚̹̰̭͖͓͚̭͈̭͙͚̩̭̓̒͆́̒̑́̓̒͆͒̒̏͐̏̓̒̒̓́̓̕ͅ͏̴̵̴̨̧̨̨̡̘͇͚̫̭͍̘͙͚̺̭͓͙͚̺̭͉̭͙͚̩̮͉̭͙͚͚̬̮͍̭͙͚̭͔͓͙͚̮͕͓͙͚̩̭͓̭͚̫̰̭̘͈͚̰̭͔̘͚̪̮̒͊͌͆͊͗́̏́͂͆̓̒͌̒͂̒̏͏̸̘͙͙͚̭͙͇͚̩̗̭͇̘͙͚̩͖̭͉͚̹̭͙͚̺͖̮͕͖͚̬̭̭͙͔͚̭͎̘͙͚͎̮͇̭͙͚̪̮͂͐̓͊̓̒̏͊͐̓̓̒͆͌͂͒́͌͆͘ͅ͏̸̴̴̴̨͙͚̬̮͖̘͍͚̤̭͔̘͙͚̫̭͖͙̯͚̩̰̭͖̘͙̬͚̩͎̮̘̩͚̭͓̩͚̬̤̮̘͙͙͚̪̭͙͚̪̭͎͓̙͚̹̤̭͚̫̮͎̘͙͚̭͍̭͇͚̬̭͓͙͚̬̭͓͙̤͚̬͖̭͉̭͙͚̬̭͇̘͍͚̬̮͍̭͙̓̒͆̒́͂̓͒̒́̓̒͒͒̓̐̏̒͐̓̒̓͒̓͂̏̒͆͒͌̓͊̓̒͏͚͚̭́͏̡͚̭͓̭͙͚̩̮͚̬̮͎̭͈͚͖̭͔̘͖͚̩̮̓̒͑́͂͆̓͑̓̒̓̒͂̒͊͏̸̷̸̴̴̴̴̸̨̨̨̡̘͙͓͚̮͓͚̩̗̮͕̭͙͚̩̭͈͓͖͚̩̰̮͙͚̹͖̭̘͓͚̬̭̭͍͚̭͎̘͙͚͎̮͇̘͙̘͚̪̭͓͙͚̬̮̘͍͚̤̭͓͓͚̗̭͓͙̯͚̮͖͓͙̬͚̩̰̮̘̩͚̫̭͓̬͚̮̭͙͈͚̪̭͙͚̪̮͔͓͚̹̤̭͙͚̫̮̘͙͚̩̮͓͇͚̫͚̮͔͕͚̹̭͓͙͚̺̭͉̭͙̤͚̮͉̭͙͈͚̬̮̙͚̭̘͚̭͍͓͙͚̭̭͚̬̮͎̭͈͚̰̭͔̘͚̮͂͒̒̋͊͊̒͐̓͊̒͂͌̒́͒͂͂͆͑͆͒̒́̒͌́͒͂͊͒̒̓̒͂̓͒͒̓̏̒̑͐̓͒͐̓͑̒̓̒͂͊́̏͊̓̒́̏͒̒͆́͂͆͂͒̒͊̒́̒̏͂͂͘͏̸̘͙͓͚̪͖̭͚̩̗̮͕̘͙͎͚̩͖̭͎̘͖͚̹̮͕̘͙͚̹͖̭̭͖͚̫͖̭͈̭͍͚̩̭͎̘͙͚̮͇̭͙͚̪̮͐̓̒̓̒͊͑̒̒͂́͌͆͘ͅ͏̸͚̬̭͈̘͍͚̰̭͓͙͚̫̮̘͙̯͚͖̮͈͙̬͚̪̗̮͖̘̩͚̬̭͓̫͚̫̮̭͙͙͚̺̮͓͚̪̭͓͚̹̤̭̓̒̋͆̒́͒͂͌͂̓̒̓̓̒͊͒̏͐̒̏͊̒͌̕͏̸̴̴̸̨̨̨̘͙͚̭͉͙͚̮͖͓͚̬̰̭͍̘͕͚̺̭͓͙͚̫̭͉̘͙͚̬̮͉̭͚̬̮͍̘͔͚̭͔̭͚̮̘͙͚̭̭̤͚̬̭̘͈͚̭͔̘͙͚̮́̓̓͂̏̒͊̒͒͊͆̈́̒͋̒́̏̒͑́͂͑͆͂͂͒̒̓͌̒͂͂͒͏̢̘͙͚͚̪͖̮͓͙͚̩̗̭͇̘̺͚̩̭͍͓͙͚̩̰̮͖̭͙͚̫̤̭̘͓͚̫̭͈̭͙͔͚̪̬̭͎̘͚̩͖̮͇̘͙͍͚̺͚̮͒̐̒͊͋̒̓̒̑͘͏̴̸̸̨̨͙͚̬̮͙͚̤̭͓͙͕͚̗̮͉͓͙̯͚̪̮͍͙̬͚̪͖̮͖̘̩͚̪̬̭͓̹͚͎̮̭͙͚̪̮͓͙͔͚̪̭͍̘͚̹̤̭͖̭͙͚̭͙͚͎̭͇̭͇͚̬̭͍̘͕͚̹̭͓̗͚̭͉̘͙͚̭͇̘͖͚̬̮͉̘͙͚͚̭̓̒͆͑̓̒́͑́͂̓̒̓̒́͒͒͐̏̒̑́͋̓̓́̒͂̒͒͊̒́͂́́̏̒́͏̨͚̮͔̘͙͚̭͍̘̤͚̬͚̮͎̭͙͚̪̭͔̘͚̪͚̮̓̒͑́͂͆͂͂̒͑̒͐͏̸̷̸̴̨̨̧̨̘͙͚̪͖̮͓̦͚̩̗̭̘͙͎͚̩͖̭͈͖͚̹̮͙͚̹̭͓̭͓͚̫̮͎̘͙͔͚̭͎̘͚̪̰̮͇̭͙͚̺͚̭͓͙͚̬̮̭͚̰̭͓͓͚̗̮͎̘͙̯͚̪̰̮͙̬͚̪͖̮͖̘͙̤͚̬̭͓̹͚͎̮̘͙͚̺̮͓͙͚̪̭͍̘͙͚̹̤̭̭͙͚̮͙͚̭͈̭͚̫͖̭͓͙͚̬̭͓͚̫̭͉̭͙͚̬̭͇̘͚̬̭͑͒̒͋̓̒͊͒̓͊̒̏́̒̒̔͑̓͆͒̒͑́̒͌́͊̓̓̓̒͂͒̑̏͐̏͐́͑̓̓͂̏̒͊͒͌̓͊̒̔̏̒͗͘͏̡̨̭͚̭̘͙̥͚̭͍̘͙͚̪̭̭͚̬̮͈͚̪̭͔̘͙͚̫̰̮̒́̏͑́͂͆̓͒̒̓͑̓̒̏̕͏̭͙͏̸̸̨͚̫̗̭̘͚̩̗̭͙̗͚̩̭͈̭͚̹̭͖̘͙͚̺͖̭͉̘͓͚̬̬̮͎̘͍͚̪̬̭͎̘͙̯͚̫͚̮͇̘͙͚͎̭͓͙̩͚̬̮͉͚̤̭̘͙͚̗̮͇͙̯͚͖̭͖̘͙̬͚̩̭͇̩͚̗̭͓̮͚̮̭͙͔͚̭̖͚̪̭͎͓͙͓͚̹̤̭͓͙͚̫̮͈͓͙͚̗̮͐̓̒͋̓͊̒̏͊̒̒̏́͑͆͑̓̒́͒͂́̓͂̓̒͂̓̒͂͒́͒͒̓̒̏͐͒̓́͘͏̴̵̨̢̨͓͇͚̬̮͔͕͚̫̭͓͙̲͚̺̭͉̘͙̤͚̬̭͇̘͙͚̬̮͉̘͙͚͚̭͓͙͚̫̮͓͙͚̮͔̤͚̬͚̭͈̘͈͚̪̰̭͔̘̘͚̬̮̒͆̓̒͆͊͗́͑̓͒͆͂͂̓̒̒̒́͏̸̵̴̧̭͙͚̮͓͚̩̗̭̺͚̩̭͎̭͚̩̰̮͕͓͙͚̫̰̮͕͓͚̫͖̮͎̘͙͔͚̪̭͎̘͙͚̪̮͇̘͙͚̩̭͓͚̬̮̭͙̹͚̤̭͔̘͙͕͚̗̮͈͙̯͚̪̰̭͓̘͙̩͚̩͎̭͇̩͚̤̭͓͙͚̪̰̮̘͙͚̩̭͙͚̪̭͓͚̹̰̭͗͂͒̒͋̓̒͊̒̏̓̒͂̓͆͋͆͑̒͆͒́́̓̓̒́̓͊͒͐͒̓̓̏͊̒͌͘͏̵̨̨͚̫̭͓͙͚͚̮͖͓͚̫̭͍̘͕͚̺͚̭͓͙̲͚̭͉̭͙͚̮͉̭͕͚̬̮͉̭̙͚̭͔͙͚̫̭͉͙͚̪̭͉̘̤͚̫̭͈̘͙͚͎̭͔̘͖͚̮̓̒͐͒͋̓́̒͊͊̒͊́͂͂͂̏̒̒́̏̓̓̓͆̓̒͑́̒́͒͏̸̸̴̴̢̨̨̘͙͙͚̮͓͚̩̗̮͕̘̖͚̩̭͉͙͚̩̰̮͓͙͚̹̮͖͖͚̫̗̭͈̭͍͚̪͚̭͎̘͙͚̩͖̮͇̘͙͉͚̩̭͓͚̬̮͖̘͙͚̤̭͔͚̫̮͍̭͙̯͚̪̰̮͍͙̩͚̩͎̭͔̭̩͚̩̰̭͓̫͚̪̮̘͙͚̩̮͓͙̲͚̪̭͎͔͚̹̰̭͖͚̫̭͈̘͙͚̩̭͈̭͇͚̬̮͕͚̬̭͓̗͚̬͖̭͉̘͙͚̩̮͉̭͙͚͚̬̮͉͓͙͓͚͚̭͚̭͙͚̩̭̭̤͚̬̮͈͚̹̭͔̘͚̩̮́͒̒̒͊̓̐͐͒̓̒̒̈́͆͑̒̋͆͊́̓̒̑̓̒̓̒͆͒͑͐̏̓̒̓̒̓͒̓̒͂͐̓̒̏͊̒́͑̓̒͆́͂͋̓͆̓͒̒̏͑̓̒͆̒̏͊͘ͅ͏̸̢̘͙͚̮͓͚̩̗̮͕̘͙͚̩͖̭͈͓͚̩̰̭͇͓͙͚̺͖̭͓̭͓͚̫̗̮͓͙͔͚̩̭͎̘͙͚̮͇̘͙͇͚̩̮͐́͒̒͊̒̏̒͑̓̓́̓͆͘͏̸̸̴̸̷̨̨̨̧̨̨̨̡͚̬̮͖̭͙͎͚̤̭̘͙͕͚̫̭͓͙̯͚̪̮͙̬͚̩̮͖̘̩͚̭͓͚̪͖̮̭͙͚̩̭͙͓͚̪̮͔͚̹̤̭͓͚̭͇͙͚̮͔͓͚̫̮͔͕͚̬̭͓͙͚̺̭͉̘͙͚̩̮͉̭͙͚̬̮͉͓͚̭͔̘͚̫̮͕̘͙͚̪͖̭͈̘͚̬͎̮͎̭͙͚̹̰̭͔̘͓͚̫̮̓̒̑͆́͒͐͊̓̒͂͒̓̒͂͒̓͒̓̏̓̒͐͐̒͐́̓̓͂̏̒͊̏̓̒͊̒̑́̏̒͑̓͆̒͑̒͆͏̸̸̸̴̶̴̴̵̨̡̨̨̨̘͙͚̮͓͍͚̩̗̭̘͙͎͚̩̭͇̭͚̩̰̮̘͙͚̹͖̭͉̘͓͚̫̮͎̘͙͔͚͖̭͎̘͙̮͚̮͇̭͙͍͚̺͚̭͓͙͚̬̮̭͙͚̰̭̘͙͚̫̮͉͙̯͚̪̰̮͕͓͙̩͚̪͖̭͇̩͚̬̬̭͓̬͚̮̘͙͚̪̭͙͚̪̭͎͓͚̹̤̭͖͚̮͇͓͙͚̩̮͓͇͚̫͚̭͍̘͕͚̹̗̭͓͚̬̭͉̭͙̪͚̬̭͇̘͉͚̬̮͍̘͙̬͚̭͓̭͙͚̭͙͚̪̭̘̤͚̫̭͈̘͙͚̤̭͔̘̘͚̫̰̮͑́͒̒͋͊̒̏͑̒͂͂͑̒͆͒́͒͂̓̓̒̓̒͂͒̒͒̓̏̒̓̒͐́̓͐̒̒͊̒̔̏̒́̏́͂͊̓͆̓͌̒͂͑́̒͘͘͏̸̸̴̨̭͙͚̮͓͙͚̩̗̮͕̘̮͚̩̭͈̘͖͚̹̭͇͙͚̹̭̘͖͚̫̗̭͈̭͙͔͚̭͎̘͙͚̫͚̮͇̭͙͚̩̭͓͙͚̬̭͈̭̖͚̤̭͓̘͚̫̮͉̘͙̯͚̭̘͙̩͚̩̭͔̭͙̤͚̩͖̭͓̫͚̮̘͙͚̩̮͓͚̪̭͓͚̹̰̭̑͂͒̐̒͊̒͊̓͒͌̒͂̓̋͆͑́͆̒́̒̑͂͊͑͆̓̒́̓͒͑͐̒̏͊̒͌͘̕͏̴̴̵̸̨̨̨̘͚̭̘͙͚͚̮͖͓͇͚̫̭͍̘͙͚̬̭͓͙͚̬͖̭͉̘͙̦͚̩̭͇̘͙̬͚̬̮͉͓͙͚͚̭̘͙͚̮͓̘͙͚̭̭̤͚̫̬̭͈̘͈͚̬̭͔̘̘͚̮̒͐́͋̓͂̒͒͌̓͊́͑́͂͆͂͑̒̒͂̒͂͂͏̴̭͙͖͚̪͖̮͓̙͚̩̗̭͓̮͚̩͖̭͈̘͙͚̩̰̭͙͚̹̭͓̭͓͚̬̬̮͓͙͔͚̬̭͎̘͙͚̩͖̮͇̘͙̘͚̩̮͒̒͌̒̐͊̓͊̒͑͆͘ͅ͏̸̴̨͚̬̮͖̘͙͚̤̭̭͙͕͚̫̮͖̭͙̯͚͖̭͕̘͙̬͚̩̭͔̭͙̤͚̭͓͙͚̫̮̭͙͕͚̩̭͙͚̪̭͎̭͙̬͚̹̤̭̓̒͐͆̒́͑͂͆́̓͊͊͒͒̓̈́̏͏̸̴̴̨̭͙͚̫̭͈̭͙͚̩̮͓͚̫̭͓͕͚̹̰̭͓̗͚̭͉̭͙͚̬̭͇̘͙͚̬̮͉͓͔͚͚̭͒̓͑̒͊̏͒̒͊̒́͂́̒́ͅ͏͚̮͙͚̪͖̭̭̤͚̬͖̮͎̭͙͚̭͔̘͚̪͚̮̓̒͆́͂͑̓͆͒̒͑́͆̒͐͏̸̴̸̸̨̨̨̨̘͙͚̫̗̮͓͙͚̩̗̮͕̭̖͚̩͖̭͇̘͚̹̮͙͚̹̮͓͚̫̮͓͙͔͚̭͎̘͚̩͖̮͇̭͙͚̪̭͓͚̬̭͈̭͚̤̭͓͓͙͕͚̗̮̭͙̯͚̪̭͕̘͙̩͚̪̭͔̭̩͚̩͚̭͓͙͇͚̮̘͙͚̪̭͚̪̮͔͓͙͚̹̤̭͕͓͙͚̫̮͔͓͙͚̩̮͔͓͇͚̬̰̭͍̘͙͚̺͎̭͓͙̱͚̹̭͉̭͙͚̩̭͇̘͙͚̬̮͉͓͚̭͑͒̐̒̒̏͊͒̓͊͑̓̒͑́̒̑͊͆͑̒͆̒̒́́͊͂̏̒̓͂̓͒̐͒̓̒͐̏͒̓͆̒͌͊͂̋̒́̏͘͘̕͏̡̨͚̫̮͙͚̪͚̮͕͚̫̮͎̭͈͚͎̭͔̘̘͚̮̓̒͆̓͐̓͆̓̒̒́̒́͒͏̢̨̘͙͓͚̪͖̭͙͕͚̩̗̭̘͚̩͖̭͎̘͙͚̹̮͙͚̺̭̘͓͚̬̬̭̭͍͚̩̭͎̘͙̯͚̮͇̭͙͚̺͚̮͐̓͋̒̐͊͒̓͊͋̒͌̒͂͂͊͘͏̸̴̴̴̴̨̨̡̨̨̥͚̬̮͖̘͚̰̭͓͓͚̗̮͍͙̯͚̩̰̮͖͓͙̬͚̩̮̘͙̤͚̩̭͓̫͚̪̰̮̭͙͚̩̭͙̭͚̪̭͎͓͙͓͚̹̤̭͙͚̮͓̘͙͚͚̭͖̘͇͚̫͚̭͓͙͚̫͚̭͓͙͚̺̭͉̘͙̪͚̬̭͇̘͙͚̬̭̓̒͆̒̋́̒͌́̓͒̓̒͒͒͒̓̏͐̓́̓͂̒͒͌͊͏̴̡̘͙͚̭͔̭͙̥͚̫̮͙͚̮͚̬̮͙͚̹̤̭͔̘͕͚̪̮́̏̓͑̓͆͂͂͑̓̒̏͑̓͑̒͊͏̸̨̘͙͕͚̭͙̙͚̩̗̭͇̘͙̗͚̩̭͎̭͙͚̩̰̮͓͙͚̺̭̭͓͚̫̮͓͍͚̬̤̭͎̘͙̮͚͎̮͇̭͙̙͚̺͚̮͂͐̓͊̐͐͊͑̒͑̒́͘͏̗͚̬̮̘͙̩͚̰̭̭͚̗̮͖͓͙̯͚̭̓̒͆͒́͒̒̑́͂͊͏̸̸̴̴̵̨̨̨̨̡̘͙̩͚̩̬̮͖̘̩͚̬̭͓̫͚̩̮̘͙͚̭͙͚̪̭͙͚̹̰̭͖̭͙͚̫̮͖̭͙͚͚̮͓͚̬̮͙͚̺͚̭͓͙͚̹̭͉̭͙͚̩̮͉̭͚̬̮͉̭̙͚̭͓͓͙͚̫̭͈̘͙͚̩̭̭͚̬͎̮͙͚̭͔̘͓͚̬̮̒͂̓̒͆͒̓́͒͒̓̏͊̓͒̓́͐̒͊͐̓͌͊̓̒͌̒́̏̓͆̓͑̒͑̓͑́͊̒͂͏̸̨̘͙͚̪͖̭̙͚̩̗̮͕̘͙͎͚̩̭͈͙͚̩̰̮͓͙͚̹̮͖͚̫̭̭͍͚̪͚̭͎̘͙͚̩̮͇̭͙͚̺͚̭͓͚̬̮͖̭͙͎͚̤̭͓̭͚̫̭͖͓͙̯͚̪̭̘͙̬͚̪͚̮̘̩͚͎̭͓̩͚̮̘͙͕͚̭͚̪̭͎̭͙̒͐̓̒͊̓̐͐̓͒̓̒̏͌̒̏͋͑̒̑͆́̒͌͐͒̒́̓̒͂̓͒́͒͒̓̒̐̏͘ͅ͏̴̷̨̨̢̨̨͚̹̤̭͙͚̮̭͙͚̩̮͖͓͇͚̫̮͔͕͚͎̭͓͙͚̫̰̭͉̘͙͚̩̮͉̭͙̙͚̬̭͐̓́͐̓̒͊̓̒͂͊͏̡̘͙͚͚̭͓̘͚̭͎̭͙͚̪͚̮͖͚̫̰̭̘͈͚̺͖̭͔̘͚̗̮͂́̒͆́͂͆̓̒͌̒̒̏͂͏̨̘͙͚̪͖̮͓͚̩̗̭̭͍͚̩͖̭͈͓͖͚̹̮͖̘͙͚̺͖̮͔͖͚̫̗̭͈̭͍͚̰̭͎̘͚̪̮͇̘͙͉͚̩̭͓͙͚̬̮͖̭͙͚̤̭̭͚̗̭͐͒̒̓͋̒̒͊̓̒̒͂̒̒͆͆͑͆̓́͒̒̑́͘͏̴̴̨̨̡̘͙̯͚̩̤̭̘͙̬͚̩̭͇̩͚̬̭͓̩͚͎̮̭͙͔͚̺̭͙͚̪̭͎͚̹̰̭͕͙͚̫̮͈͙͚̭͇̭͇͚̬̤̭͍̘͕͚̹̤̭͓̗͚̺̭͉̘͙̥͚̬̮͉̭͙̮͚̬̮͙͚͚̭̘͚̫̭͎̭͙͚̩̭̭͚̬̗̮͎̭͙͚̭͔̘͓͚̮͑͂̓̒͒̓̒́͒̏͒̓͐̏̓̒̓͒̓̓͂̏̒̒͊̒̓͊̓͗́͒̒͑̓͆̓͒̒͑́̒́͂̕͏̵̸̨̭͙͚̫̗̮͓̹͚̩̗̮͕̭̮͚̩̭͈͖͚̹̮͙͚̫̰̮͖͓͚̫̭̭͙͔͚͎̭͎̘͙̯͚̫͚̮͇̘͙͚̩̭͓͚̬̮̘͙͚̰̭͓͚̫̮͎̭͙̯͚͖̮͕͓͙̩͚̪͚̭͔̭̩͚̭͓͙͇͚̪͖̮̘͙͙͚̮͓͚̪̭͎͓͙͚̹̰̭̐͒̒̒͊̓̒͊͒̓̓̒͊͌͂͆͑̒̓͆͒́͒̒͌͂̒͂͊̓͒́͒͐̒̓̏͘̕͏̴̴̴̨͙͚̫̮͕̘͙͚̩̭͖̘͚̬̮͔͕͚̹̬̭͓͙͚̹̭͉̘͙̹͚̬̮͉̭̓͒̓̒͊͂̓̒͊̓̒͏̵̴̴̨̡͚̬̮͍̘͚͚̭̘͙͚̭͉͙͚̪̗̭̭͚̫̮͎̭͙͚̹̭͔̘̘͚̩̮̒͐́͒́͂̓͆͒̒͑̒͊͏̸̸̭͙͚̮͓͙͚̩̗̭͙͚̩͖̭͎̭͚̩̰̮͓̭͙͚̹̭͍̘͖͚̫͖̮͓͍͚̪̤̭͎̘͙͚̮͇̭͙͚̪̮͐͂͒̐͋̓͊̒̏͒̒͑̒̈́́͊͆͘͏̓̒͏̸̨̨̡̧̨̨͚̬̭͈̘͚̰̭͓͚̫̮̘͙̯͚̪̤̮͙̩͚̩̬̮͖̘͙̤͚̩͎̭͓̫͚̪̰̮̘͙͚̺̮͓͙̺͚̪̭͚̹̤̭͖͓͙͚̭͙͚͚̮͓͚̫͎̮͙͚̭͓͙͚̫̭͉̘͙͚̩̮͉̭͚̬̭͆̒̒́͒̒̑͊͊̓̓̒͒͒̏͐̏͊̓̒́͌̓̓͂͑̒͊͐̓͌́͂͊̏̒̋͘͏̸̴̘͔͚̭̭͙̥͚̫̭͎͙͚̭̭̤͚̬͚̮͎̭͙͚̪̭͔̘̘͚̪̮̒́̏͒̓̓͆͂͑̒͑̏̒͏̸̘͙͚̪͖̭͚̩̗̭͇̘͚̩̭͎͓͙͚̩̰̮͖̘͙͚̫̰̮͓͚̫̭̭͍͚̪̭͎̘͙͚̮͇̘͙̖͚̺͚̮̑͐̓̒́̒̈́͊̐͐̓̒̏͌̒́̓͘ͅ͏̴̸̴̡̨͙͚̬̭͈̘͙͚̰̭̭͙͕͚̗̮͎̘͙̯͚̩̰̮͙̩͚̪͖̭͇̩͚̬͎̭͓̹͚̪͖̮̘͙͚͚̩̭͔͚̪̭̙͚̹̤̭͖̘͚̫̮͕͙͚͚̮͓͇͚̬̮͔͕͚̹̰̭͓͙̱͚̫̭͉̭͙͚̬̮͉̭͙͚̬̭̓͂͆́͒́͊̓̓̒̓̒͒͒̓̒̏͊̓̒̒͐͒̓̓́͐̒̓̒͊̏́̋͏̭͚͚̭̒́̕͏͚̮͔̭͙͚̩̮͕̤͚̬͚̮͎̭͙͚̭͔̘͚̪͚̮̓̒͑́͂͆̓̓̒͑́͊̒͐͏̸̭͙͚̪͖̭͚̩̗̭̘͙̗͚̩͖̭͇͓͖͚̹̭͓͙͚̹̭͓̭͖͚̬̭̭͙͔͚̭͎̘͙͚̬̤̮͇̭͙̘͚̺͚̮͗͐̓̒͋̒͊͋͊̒͂͌́͘ͅͅ͏̸̴̸͙͚̬̮͉͚̤̭͓͚̫̮͔̭͙̯͚̪̤̭̘͙̬͚̪̭͔̭̩͚̬͖̭͓͚̪̰̮̘͙͚̩̮͓͚̪̮͔͓͚̹̤̭͔̘͙͚̫̭͈͓͙͚̗̮̓͂͆͑̓̒́͒̒̑͐͒̒̓̒͂͒͗͐̒͌̏̒͒̓́̕͏̵̨̡͓͚̫̭͓͙͚̫̭͓͙̲͚̹̭͉̘͙͚̭͇̘͚̬̮͉̘͙̰͚͚̭͙͚̮͓͙͚̪̭͉̘͚̬̮͎̭͈͚̭͔̘͖͚̩̤̮̒͊͒͒͌͊͊̓̓́̏̒̋́͑̓́͂͐͆̓̒̓̒͂͒̒͏̸̸̸̨̡̢̨̡̭͙͚̪͖̭͚̩̗̭̭̮͚̩̭͎͙͚̩̰̭͈̘͙͚̺̭̭͖͚̫̮͓͙͔͚͖̭͎̘͙͚̮͇̭͙͚͎̭͓͙͚̬̭͈̭͍͚̤̭͓͚̫̮͕͓͙̯͚͖̮͕͓͙̩͚̪͚̭͔̭͙̤͚̬̭͓͚̮̭͙͕͚̭̗͚̪̭͎͓͔͚̹̰̭͖͚̫̮͇̘͙͚͚̭͇̭͇͚̬̭͍̘͙͚̺̗̭͓͙͚̬͖̭͉̭͙͚̭͇̘͙̤͚̬̮͉̘͙͚͚̭̭͚̫̮͓̭͙͚̩̭͓̭͚̫̤̮͎̭͈͚̪̭͔̘̘͚̫̮͐͐̓̒̈́͋̒͊̓̐͊͒̒͑́̓́̓̓́͑̈́͆̒́͑̒͌͂͒̓̒͂́͒́͒͒̓̒̏̒̓̒͐͒̓͂̒͆͌͊́̏͗́͒̒͑̓͆̓̒̒̒͆͘͏̸̵̸̭͙͚͚̮͓͚̩̗̭͇̭͙͚̩͖̭͇̘͙͚̹̭̭͙͚̹̭͉̘͓͚̫̭̭͙͔͚̩̭͎̘͙͚̮͇̘͙͇͚̪̭͓͙̩͚̬̮̭͚̰̭͓͙͕͚̫̭͖͙̯͚̮͓͙̩͚̩͎̮͖̘͙̤͚̗̭͓͙͚̮̭͙͔͚̭͙͚̪̭͔͚̹̰̭́͒̒͒̐͊͋͒̒̓͌̓͂͂̓͆͑͆͒̒̒́͒̓͂͊͐́̓͊͂̓͒́͒͒̓̏͊̓̒͘ͅ͏̴̨̨̭͚̫̮͕͓͙͚͚̮͔͓͚̫͚̭͍̘͕͚̫̭͓͙͚̬̭͉̭͙͚̭͇̘͙̮͚̬̭̒͐͒̓́̒͊̒͊̏̈́͂̏͏̸̴̴̡̭͚͚̭͓͙̥͚̮͕̭͙͚̭͓̭͚̫̭͈̘͙͚̭͔̘͓͚̗̮̒́͑́͂͆͂̒͑́̒͂̕͏̭͙͏̸̴͚̮͓̤͚̩̗̭̭͙̗͚̩̭͈̘͚̩̰̮͓͙͚̺̮͔͖͚̬̭͈̭͍͚̩̭͎̘͙͚͎̮͇̭͙͚̺͚̭͓͙͚̬̮͓͙̹͚̰̭̭͚̗̭͔͙̯͚̪̤̮͎͙̩͚̩̤̮̘̩͚͖̭͓̫͚̩͖̮̭͙͚̩̭͚̪̮͔͙̬͚̹̤̭͂͒̒͋͊̒̏͐͊̓̒͂̒̏͂͋͑͆͆͒́͒̒͌́̓̓͒̒́̓̒͒͐͒̓̒̔̏̓͘ͅ͏̸̨̘͙͚̭͇̘͙͚̩̭́̓͆͏̧̨̡̘͇͚̬̰̮͙͚̺͖̭͓̗͚̺͎̭͉̭͙͚̮͉̭͖͚̬̮͍̘͙͚͚̭͔͓͙̥͚̭̘͙͚̪͚̮͕͚̫̰̮͎̭͈͚̤̭͔̘̘͚̮̒͐̓͌͊̒́̏̒͂́́͂͊͆̓̒̒́̒́͒͏̭͙͏̸̸̴̨͚̭͙͇͚̩̗̮͕̘͙͚̩͖̭͈͓͖͚̩̰̭͕̭͙͚̺̭͓̭͓͚̫͖̭͈̭͙͔͚̪̭͎̘͙͚̮͇̘͙͈͚͎̭͓̤͚̬̮͖̭͍͚̰̭͙͚̗̮͕͙̯͚̪̮͓͙̬͚̩̭͔̭̩͚̬̭͓͚̪͖̮̘͙͚̩̭͙͕͚̪̮͔͙͚̹̰̭͕͙͚̫̭͉͙͚͚̮͂͐̓͒̒͊̒͊̈́́́͑̒͆̒́͑̓͂́̓͂͐͂̒̏̓̒͂͒͐͒̓̏̓͗̓͒̓̓͂͘͏̸̡̨̨͓͚̫͖̮͔͙͚̬͚̭͓͙͚̹̭͉̭͙͚̭͇̘͎͚̬̮͍̭͙͚͚̭͔͓͚̫̭̭͙͚̩̭̭̤͚̫̰̭̘͈͚̰̭͔̘͙̥͚̮̒͊̓͌͊͆́̏̒́̒͑̓͌͆̓͒̒͌̒́͂͂͏̸̡̘͙͕͚̫̗̮͓͚̩̗̭̘̖͚̩̭͉͙͚̩̰̭͇͙͚̫̰̮͖͓͚̫͖̭̭͙͔͚̪̤̭͎̘͙̯͚̪̮͇̭͙͚͎̭͓͙͚̬̮̭͙͚̤̭͓͓͚̫̭̘͙̯͚̪̮͙̩͚̪͚̮͖̘̩͚̬̭͓͙͚̬̤̮̭͙͈͚̺̭͙̹͚̪̭͎͙̬͚̹̰̭͒̒͋̒͊̓̐̓̓̒͌͆͌́͑͆͆͒̏́̒̑͒͂͊̓̒͊̓͊͒̏͒̓̏̓͘͏̸̴̸̴̨̨̨̡͙͚̭͉̭͙͚̮͓͇͚̫̮͔͙͚̫̭͓̗͚̹̭͉̭͙̥͚̬̭͇̘͙̖͚̬̮͉͓̙͚̭̭͚̭͍͙͚̪̭̘͚̬̮͎̭͈͚̪̭͔̘̘͚̪̮̓́̓́̏͑̒̏̓͌͆͊̒̒́̏͒̒͑́͂̓͆̓͊̒͒̒̒͏̸̸̘͙͚̮͓͚̩̗̭̭͙͚͚̩̭͈̘͙͚̹̭͇̘͙͚̹̮͖͖͚̬̮͓͍͚̩̭͎̘͙͚̮͇̭͙͚͎̮̓́͒̒̔͋͊̐͊͊̓̒͆͑̒̏̈́́̋́͘͏̸̴̨̨̧̨͇͚̬̭͈̘͚̰̭͓͙͚̗̮͕͙̯͚̮͓͙̩͚̩̮̘͙̤͚̪̭͓̫͚̩̮̭͙͚͚̺̮͓̘͚̪̭͎̭͚̹̤̭͕͓͙͚̭̭͙͚͚̮͓͇͚̫͚̮͕͚̺̭͓͙̤͚̬̰̭͉̘͙͚̭͇̘͙̮͚̬̮͉͓͙͚̭͓̭͚̮͔͓͙͚̭͍̘̤͚̫̬̭͈̘͈͚̭͔̘̘͚̬̮̓̒͆̒̋́͑͂́̓͂͊͐͂͒̓̓̒͆͒̏͐̒̏̒́͌̓͂͑̒͐̓̒͊͂̏́̏̒͑́͂͆͂͂̒̒́͒̒̏͘͏̸̸̢̭͙͖͚̭͙͍͚̩̗̭͇̭̖͚̩͖̭͈͙͚̩̰̮͓͙͚̫̤̮͓͖͚̬̬̭͈̭͙͔͚̭͎̘͚̮͇̘͙͚̪̮́͐̓̒̓͒̓̒́͒̒̑͂̋͆͘͏̸̩͚̬̮͖̘͙̹͚̤̭͔̭͙͕͚̫̭̓̒͆́͏̨̨͙̯͚̩̰̭̘͙̩͚̪͚̭͔̭̩͚̬̰̭͓͙͚̪̰̮̘͙͚̺̭͙̰͚̪̭͚̹̤̭͖͚̮͓͙͚͚̮͓͇͚̬̭͓͙͚̫̭͓͚̬͖̭͉̭͙̦͚̭͇̘̓͑̒̓͊͒̑̏͒̓̏͊̓̒͐̓̒͐́͑̓́͐̒͆͒͌͊̒̔͂̏̒͏̨͚̬̭͏̵̸̨̭͙͚͚̭͓͙͚̫̭̭͙͚̪͚̭̘̤͚̬̭͈̘͈͚̹̭͔̘͓͚̬̮́͑̓͋͆͊̒͊̒̒́͏̴̘͙͚̫̗̮͓͙͚̩̗̮͕̭͙͚̩͖̭͇̭͚̹̮͕̘͙͚̹͖̭̭͓͚̫̭͈̭͙͔͚̪͚̭͎̘͚͎̮͇̘͙͉͚̩̭͓͙̹͚̬̭͈̭͙͎͚̰̭͔̘͚̗̮̭͙̯͚͖̮͕͓͙̩͚̪̭͔̭͙̤͚̭͓͙͚̫̮̘͙͚̩̭͒͒͒̒̏͊͒̒̏̒̑́͆͑͆́̒͌́͊͂̏͂̏̓͊͊͒̐͒̓̒̕͘͏̴̵̸̨̨̨̨̨͚̪̭͍̘͚̹̤̭͕͙͚̮̭͙͚̩̮͔͓͚̫̭͓͕͚̬̭͓͙͚̹̭͉̘͙͚̩̮͉̭͔͚̬̮͉̘͚̭͓͙͚̮͓͙͚̭͓̭̤͚̬̮͈͚̩̭͔̘̘͚̮̏̒͌̓́͐̓͆̒͊͒̒͆͊̓̒̒́̏͑́͂͐͆͂̒͒͑̓̒͆̒́͒̕ͅ͏̸̘͙͓͚̫̗̭̖͚̩̗̭̘̦͚̩͖̭͎͖͚̩̰̭͇͙͚̺̮͖͖͚̬̭̭͍͚̫͎̭͎̘͙͚̮͇̘͙͉͚̩̮͐̓̒͋̒̓̒̓͊̓̒͆͌̒̓́͆͘͏̨͙̲͚̬̮͙͚̤̭͓͓͚̗̮͎͓͙̯͚͖̮͙̬͚̪̭͔̭̩͚̭͓̫͚̮̘͙͚̭͙͓͚̪̮͔͚̹̰̭̓͆͑̓̓́̒̑́͂͋̓̓̒́̓̒́̓͒̐́͒͒̓̏̓̒͐͏̸̸̷̨̨̡͓͙͚̮͓͙͚̗̭͍̭͇͚̫͎̭͍̘͙͚̺̭͓͙͚̺͎̭͉̘͙͚̭͇̘͙͚̬̮͍̘͚͚̭̘͙̥͚̭̭͙͚̩̭̭͚̫̤̭̘͈͚̬̭͔̘͕͚̫̮́̓̓́̒͌͊̈́͂̏͆̒͐́͒́͂͌͆̓͑̒͌̒͂̒͆͏̸̸̡̘͙͖͚̮͓̫͚̩̗̮͕̘͚̩͖̭͍̘͚̩̰̮͕͙͚̺͖̭̘͓͚̫͖̭͈̭͍͚̫̭͎̘͙̯͚̪̰̮͇̭͙̗͚̪̭͓̙͚̬̮͙͚̤̭͔͓͙͚̫̭́͒̒̒̈́̒̏̓͊̒̒̓͆͑̒͆͑̓́͂͘͏̴̡̨͓͙̯͚͖̭͓̘͙̬͚̪̭͇͙̤͚̪̬̭͓̬͚̫̮̘͙͚̮͓͓͚̪̭͓͙͓͚̹̤̭͚̫̭͎͙͚͚̭͈̭͚̫͚̮͔͕͚̺̭͓͙̱͚̭͉̭͙͚̭͇̘͙͚̬̭͂̏̓̓̒͊͒̑́͒͐̒̏͊͐̓̒̓͒̓̓́̒͊̓̒͊́͂̓́̏͏̵̸̡̭͙͚̭͓̭͙͚̮͕̭͙͚̮͖͚̫̮͙͚̭͔̘͖͚̩̤̮͗́̏́͂͆͂͂̓̒͑̓͑́͆̒͏̴̸̸̴̴̢̨̭͙͓͚̪͖̭͙͍͚̩̗̭̘̖͚̩̭͇͓͙͚̹̭̭͙͚̫̤̮͓͓͚̫͖̮͓͍͚̩̭͎̘͙͚͎̮͇̘͙͈͚̩̭͓͙͚̬̮͖̭͉͚̰̭̘͚̗̭͔̭͙̯͚̪̤̮͓͙̩͚̩̭͔̭̩͚̩̭͓͙͚̮̘͙͚̪̮͓͙̬͚̪̭͎͓͚̹̰̭͖͓͚̫̭͇͙͚̩̮͖͓͇͚̬̭͓͙͚̹̭͓͙̲͚̺̭͉̭͙̥͚̭͇̘͙̯͚̬̮͉͓͙͚̭͐̓͋̒͊̐͊͋̓̒͑̒͒̈́͂͆͑͆̒́͑̒͌́͐̒̓͊͂͒͗͐̏̒͐̒̓͒̓̓͆̒͆͒͌̏͊̓́̏́̏͘͏̡͙̥͚̫̮̭͙͚̩̮͚̫̮͎̭͈͚̭͔̘͚̮̓̓͒͆̓͒̓̒͂̒͂͆̒̏͂͂͏̸̢̘͙͚̭͙͚̩̗̮͕̘͚̩̭͎͓͙͚̹̮͐́͐̓͊̒̋͊͊͏͓͙͚̺̮͓͓͚̫̮͎̘͙͔͚̫͚̭͎̘͙͚̩̮͇̘͙͚̩̮͊̓̒̏̏̔͆͘ͅ͏̸̴̨̡̨͚̬̮͓͙͚̤̭͙͚̫̮͍͙̯͚̩̤̮͎͙̬͚̩̮͖̘̩͚͖̭͓͙͇͚̬̤̮̘͙͙͚̪̭͙̳͚̪̭͎͓͙͚̹̰̭͖̭͚̮͓͓͙͚̗̭͈̭͚̫̮͕͚̹̗̭͓͙͚̬͖̭͉̘͙͚̮͉̭͙̣͚̬̭̓̒͆͒̏́͑̓͂̓̓͆̒͂̓͒͒̓̏͗̒͐́̓́̒͊̏͐̓̒͊͂͂̏͘͏̵̸̡̘͙͚͚̭̘͙͚̭̘͙͚̪͖̮͔͚̬͚̭̘͈͚̭͔̘͚̩̤̮͂́͑́͂͒͆̓̒͌̒́̒͐͏̢̨̭͙͚̫̗̮͓̫͚̩̗̮͕̘͍͚̩͖̭͎̭͙͚̩̰̭͈̘͙͚̫̰̭̘͓͚̫̮͎̘͍͚̫̭͎̘͙̮͚͎̮͇̘͙̘͚̺͚̮̒͒̒̒͊̒̒͂͂͘͏̸̴̸̴̴̵̨̨̡͙̣͚̬̮͙͚̰̭͓͚̫̮͎͓͙̯͚̪̰̭̘͙̬͚̩̬̮̘͙̤͚̩̭͓̩͚̬̤̮̘͙͚̪̭͚̪̮͔͙̬͚̹̤̭̭͙͚̫̮͔̭͙͚̩̮͔͓͚̬̰̮͕͚̹̭͓͙̱͚̭͉̭͙͚̬̭͇̘͚̬̮͉͓͙̰͚̭͔̭͙͚̫̭̭͙͚̪͖̭͉̘͚̬̭̘͙͚̩̭͔̘͕͚̮̓͆͑̓̓́͑̒̑͐͒̓̒͒̑͒̓̒͌̏̓͐͒̓̒͊͐̓̒͊͊́͂͆̒̏́̏̓͒͆̒̓͌͑͂̒͂͒͏̘͙͓͚̪͖̭͚̩̗̮͕̭̦͚̩̭͈̘͚̩̰̮͐̓̒̈́̒͊̒̏͏̨̭͙͚̫̰̭͓̭͓͚̫͎̭̭͍͚̪̬̭͎̘͚̮͇̘͙̖͚̺͚̮̒͌̒̒̑͂͘͏̸̸̸̸̸̡̨̨̨̡̨͙͚̬̭͈̭͙͚̰̭͓͚̫̮͇͓͙̯͚̪̮͙̩͚̩͎̭͇̩͚̭͓̹͚̮̘͙͕͚̮͓͙̱͚̪̭͚̹̤̭͔̘͙͚̮͈͓͙͚̭͎̭͚̬̭͓͕͚̫̭͓͚̺̭͉̘͙̥͚̮͉̭͙͙͚̬̮͍̭͚̭͔͚̫̭͎̭͙͚̭͍̘͚̫̬̭͈̘͈͚̪̭͔̘̘͚̬̮̓͆͊́͑̒͌͊̓̓̒́̓̒͂͒́͒͐̏͊̓̒͌́̓͂̏̒͊͆͒̒͒͊̒̔̓͂̏̒́̏̓̒͆̓͆͂̒̒̒̏̕͏̸̴̸̢̭͙͚̮͓͙͍͚̩̗̮͕̘͙͖͚̩͖̭͇̘͙͚̹̭͕̘͙͚̺͖̭͍̘͖͚̬̭͈̭͙͔͚̫͎̭͎̘͙͚̩̮͇̘͙͚͎̭͓̤͚̬̮͖̭͙͚̤̭̭͚̗̮̭͙̯͚͖̮͇͙̬͚̩̤̮͖̘͙̤͚̬̭͓̫͚̮̭͙̓́͒͊̒͆͌́͑̒͆̏́͑̒̑́͌͂̓͊̓̒́͒͘ͅ͏̴̸̴̨͚̩̭͙͚̪̮͔͙͚̹̰̭͓͚̫̭͈̭͙͚̩̭͉̭͇͚̬̮͔͕͚̹̭͓͚̺͎̭͉̭͙͚̬̭͇̘͙͚̬̮͉̭͚͚̭͒̓̓̏̓͗͐̒̓͒̓͆̒̓̒͆͊̒̔́͂̒́͘͏̨͚̭̭͙͚̩̮͕̤͚̬͚̮͎̭͈͚̹̭͔̘͚̪͚̮̓̒͆́͂͑͆̓̓̒̒̒͐͏̸̢̨̭͙͚̫̗̭͚̩̗̭̘͙͎͚̩͖̭͈̘͙͚̹̮͙͚̹̮͓͚̫̭̭͙͔͚̭͎̘͚̩͖̮͇̭͙͚̪̭͓͚̬̭͈̘͚̤̭͗͐̓̒͋͊͒̓͊͑̓̒͌́̒̑͋͆͑̒͆̒̋́͘͘ͅ͏̴̨̨͙͚̗̮͉̭͙̯͚̪̰̮͈͙̩͚̪̭͔̭̩͚̪̭͓͚̩̮̘͙͚̩̭͙͔͚̪̭͎͓͙͓͚̹̰̭͓͚̫̭͈͓͙͚̗̮͖͓͚̫̭͓͙͚̫͚̭͓͚̗̭͉̭͙͚̩̭͇̘͙͚̬̭̓͂́̓̏̒̓̓̒͂͆͒̐͒̓̏͐̒͐͒̓́̒͊͒͒͌͊̒̔͂͂̋͏̴̭͙͚̭́̏͏̡͚̫̮͓̘͙͚̮͚̫̬̮͎̭͈͚̹̤̭͔̘̘͚̮̓̒͑̓͆͂͂͒̓̒̒̒́͒͏̸̢̭͙͙͚̫̗̮͓͙͚̩̗̭̘͚̩͖̭͎͙͚̩̰̭͇͙͚̺̮͖͓͚̬̭͈̭͍͚̪̭͎̘͚͎̮͇̭͙͚͎̮͒̔͋̒̓̐̓͊̓̒̒͂̒̑͂̓́͘͏̸͚̬̭͈̭͍͚̰̭͔̭͚̫̭̓̒̓͆̒́̒̑͏̴̴̨̘͙̯͚͖̮͖͓͙̩͚̪̭͔̭͙̤͚̩̭͓̹͚̮̭͙͚̪̭͙͓͚̪̭͎͙͚̹̰̭͂̓͂̓̒͂͒͑͒̓̏̓͏̸̨̡̨̨̘͙͚̮͔̭͙͚͎̭̘͇͚̫̭͓͙͚̺͎̭͓͙͚̬̰̭͉̘͙͚̮͉̭̗͚̬̭́̓́͐̒͒͒͌͊͂̏̒͏̨̭͙͚̭͔͚̫̭͓͙͚̭͉̘̤͚̬͚̭̘͈͚̰̭͔̘͙͚̩̤̮͗́̏̓̒͑̓͋͆͂͂̒͌̒͂͏̴̘͙͓͚̪͖̮͓͙͚̩̗̭͇̘̺͚̩̭͎̭͖͚̹̭͕͙͚̺̭͉̘͖͚̬̮͎̘͙͔͚̭͎̘͙͚̫͚̮͇̭͙͇͚̪̭͓͙̦͚̬̭͈̘͙͚̤̭͔͚̗̮͇̘͙̯͚̪̤̮͈͙̩͚̪̭͔̭͙̤͚̩̗̭͓͙͚̪̮̘͙͙͚̪̭͙̰͚̪̭͍̘͙͒̐̒͊̒͊̓͊̒͂́̓̓͆͑͆̒́̓̒̑́̓͒̓͊͆͒͒̓̏͘͏̴̸̨̨̨̡͚̹̰̭͖̘͚̭͉͓͙͚̭͎̭͇͚̬̮͔͕͚̭͓͙͚̹̭͉̭͙͚̮͉̭͚̬̮͙͚̭͓̘͚̫̭͉͓͙͚̪̗̭͍̘͚̬̮͎̭͙͚̭͔̘͓͚̫̮̒͐́̓́̏̒͆̓̒́͂͊̈́͂̏̒̋͊̓́̏̒͆̓͆̒͊͑́͂̒͆͏̸̸̴̘͙͚̭͙͚̩̗̮͕̭̖͚̩̭͇͓͖͚̩̰̭͕̭͙͚̹̮͖͖͚̬̬̭͈̭͙͔͚̭͎̘͙͚̪͖̮͇̭͙͍͚̺͚̭͓͙̦͚̬̮͖̘͚̰̭̭͙͚̫̮͎̭͙̯͚̪̤̮͙̩͚̩̮͖̘̩͚̪̰̭͓͙͚̩͖̮̘͙̒͂͐̓͑̒͊̒͒̓̒͂͆͑͆̒̒́͑͂͊̓̒̓͊͒͘ͅ͏̴͚̩̭͚̪̮͔͙̰͚̹̤̭͒̓̒̔̏̓͏̸̴̴̨̨̨̘͙͚̫̭͉͙͚̩̭͖̘͇͚̬̰̮͔͙͚̹̬̭͓̗͚̫͖̭͉̭͙̦͚̩̮͉̭͚̬̮͉͓͙͚̭͔͓͚̮͖͙͚̪͚̮͓̤͚̫̮͎̭͈͚̹̭͔̘̘͚̪͚̮͒̓̓̒̓͌͊̒̒͌́̏̒͑́͂̓͆̓̒̒͂̒͏̸̸̸̴̴̡̨̨̨̘͙͚̮͓͙͉͚̩̗̮͕̘͙͎͚̩̭͎͓͖͚̩̰̭͕̘͙͚̺͖̭͓̭͖͚̬̬̭͈̭͙͔͚̩͚̭͎̘͚̩̮͇̘͙͉͚̩̭͓͙͚̬̮͖̭͙̹͚̤̭͔̘͚̫̭͓͙̯͚̪̮͍͙̬͚̩̮͖̘̩͚̰̭͓̩͚͎̮̭͙͚̭͙͚̪̭͎͓͚̹̰̭͕̭͙͚̫̮͇̘͙͚̭͈̭͇͚̬̭͓͕͚̹̭͓̗͚̫̭͉̘͙̦͚̩̮͉̭͙͚̬̭͐͂͒͊̒̒̒̒̏͆͑͆́̒̑͑̓͆̒͂̓̒́͒̓́͒͒̓̐̏̒͒̓͂̏̒͒̒͊̒̏͌͘͘͏̵̴̡̘̙͚͚̭̘͙͚̭͔̭͙͚̪͚̮͖͚̫̤̭͈̘͈͚̪̭͔̘͓͚̮̒́͒́͂͆̓̒̒̒́͂͏̵̴̴̸̨̨̭͙͚̫̗̮͓͙͚̩̗̮͕̘͙̗͚̩̭͈͓͚̹̮͓̭͙͚̹͖̭̘͖͚̬̬̭̭͙͔͚̪̤̭͎̘͙̮͚̬̤̮͇̘͙͈͚͎̭͓͚̬̮̘͙͚̰̭͙͚̗̭͖̘͙̯͚̪̮͖͓͙̩͚̩̭͇̩͚̰̭͓̩͚̩͖̮̭͙͈͚̩̮͓͚̪̮͔͓͙͚̹̤̭͔̘͙͚̮͇̘͙͚͎̮̐͒͒͊̒̏͊͊̒͌́͑̒͊͆͒́͒̓͂́̓̒́̓̒͒͐̒͌̏͂́̓́͘͏̴̸̨̡̨͓͚̬̭͓͕͚̺̭͓͙̱͚̫̭͉̘͙͚̮͉̭͙̗͚̬̮͍̘̙͚̭̘͚̮͙͚̪̗̮͚̫̭̘͈͚͎̭͔̘͙͚̮̒͊͒̒̓͊͆́́̏̒́̏͒̒͑́͂͐̓͆͐̓̒͌̒́͂͂͏̢̭͙͚͚̪͖̮͓͉͚̩̗̭̘̮͚̩͖̭͎͓͙͚̩̰̮͖͓͙͚̹͖̮͕͖͚̫͖̭̭͍͚̭͎̘͙͚͎̮͇̘͙͚̪̮͒̒͋̒̓̒͌̒́͂̈́͂̔͆͘͏̸̸̨̨̖͚̬̮̭̖͚̤̭͙͚̫̮͇͙̯͚̪̰̮͙̬͚̪̗̮̘̩͚͖̭͓͚̪͖̮̘͙͔͚̮͓̙͚̪̭͎̭͙͚̹̤̭͔̘͙͚̫̭͉̭͙͚͚̮͖͓͇͚̬̤̭͍̘͕͚̫̭͓͙̱͚̬̭͉̘͙̦͚̮͉̭̖͚̬̮͍̭͚͚̭͓͚̫̭̭͙͚̪̭͍̘̤͚̬͚̭͈̘͈͚̭͔̘͕͚̪͚̮̓̒͆͒̒́͑̓͂̓͋̓͒̒͂̓̒͂͒́͒͐̒̏͂͒̓͂̒̒̏͊̏͂̏̒̒̑́͒̒͑̓͒͆̓̒̒͂̒͏̸̶̴̡̘͙͚̭͚̩̗̭͇̭̖͚̩͖̭͎͚̹̭͙͚̹͖̮͓͚̫̭̭͍͚̪̤̭͎̘͚̪͖̮͇̘͙̖͚̺͚̭͓͙̪͚̬̭͈̘͙͚̤̭͓͓͙͕͚̗̭͕͓͙̯͚͖̭͕̘͙̬͚̩̭͇͙̤͚̬̭͓̫͚̩̮̭͙͕͚̩̭͙̩͚̪̭͓͔͚̹̤̭̐͂͐̓̒̒̓̒̏͊͐̓͒̓̒̏͌̒̒̒͑͆́́͂͂̓͒̓̒̏͒͒̓̏͊̒͘͏̴̨̨̡͚̫̭͈̭͙͚̭͇̭͚̫̭͍̘͙͚̫̭͓͙̱͚̫̭͉̭͙̪͚̮͉̭͚͚̬̮͉̭͚͚̭͓͚̫̭͍͙͚̪͖̭͍̘͚̬̮͎̭͙͚̭͔̘͓͚̪̮̓̒͐͒̓́̏̒͊̓͌͊͆͂̏̒̒͌́͑̒͑̓̓͆̒̏͑́͒̒͏̸̸̴̸̴̵̸̴̨̨̨̨̨̡̘͙͚̭̭͚̩̗̮͕̭̲͚̩̭͎̘͚̩̰̭͉͙͚̫̤̭͍̘͖͚̬̤̮͓͙͔͚̩͚̭͎̘͙͚̩̮͇̭͙͚̩̭͓͙͚̬̮̭͚̤̭̭͚̫̮͖͓͙̯͚̪̤̮͓͙̩͚̪̭͔̭͙̤͚̗̭͓͚̩̮̘͙͚̪̭͚̪̮͔͓͙͚̹̤̭͕͙͚̮̭͙͚̩̮͔͓͚̫̭͍̘͕͚̬̭͓͙͚̺͎̭͉̘͙͚̩̮͉̭͙̳͚̬̮͉̘͚͚̭͓͓͙͚̮͓͙͚̭͓̭͚̫̰̮͈͚̭͔̘͖͚̪̮͒͂͐̓̒̒͊̒̏̓̒͑͆͌͆͑͆͒̒̒́͑̒̑͐̏͂̓̒͂͆͒̐͒̓̒͗̏̓́͐̓͆̒͊̒́͊͂̒́́͂͐͆͂̒͑̓̒͂͒̒͘̕ͅͅ͏̸̢̨̭͙͚̫̗̭͚̩̗̭͙͚̩̭͎͙͚̩̰̭͈̘͙͚̺̭͈̘͖͚̫̮͓͙͔͚̬̤̭͎̘͙͚̮͇̭͙͚͎̭͓̥͚̬̭͈̭͍͚̤̭͓͚̫̭͑͐̓̒͋̓͒͊̓̐͊̒͑̓́̓̓́͑̒͆̒́͒̒͌͘͏̷̨̨̨̨̨̘͙̯͚͖̮͖͓͙̩͚̪̮͖̘͙̤͚̩̭͓̹͚̫͚̮̘͙͙͚̺̭͙͚̪̭͎͓͚̹̤̭̭͙͚̮͈͓͙͚̭͎̭͚̬̬̮͔͙͚̫͎̭͓͙͚̺̭͉̘͙͚̭͇̘͙̥͚̬̭͂̏͂̓̒͒̏͒̓̓̏̒͐͐́̓͂̏̒͊̓͌͊́̏͏̸̨̡̭͙͚͚̭͓͙̥͚̫̮͙͚̭̭͚̫̤̮͎̭͈͚̪̰̭͔̘͚̮́͑̓͒̓͆͂͒̒̒̒̏͂͂͏̸̸̴̢̨̘͙͚̪͖̮͓̭͚̩̗̭͙͚̩͖̭͈͙͚̹̭͙͚̹̮͕͖͚̬̰̭̭͙͔͚̩̭͎̘͙̮͚̬̤̮͇̭͙͚͎̭͓͙͚̬̭͈̭͙͚̰̭͓͓͚̗̮͕͓͙̯͚̪̰̮͙̩͚̩̭͔̭͙̤͚̩̭͓̬͚̩͖̮̘͙͙͚̭͙͚̪̭͍̘͚̹̤̭͚̫̮̘͙͚̮͔͓͚̫̭͍̘͙͚̫͖̭͓͙͚̬̰̭͉̭͙͚̮͉̭͙͚̬̭͑͒̒͋̓̏̓͊͐̓̓̓̒͌̏̏́͑͆͆̒́̒͌́͋̓̓̒͒́͒͒̓̏̒͐̓̒̓͒͐̓́̏̒͊͊͌͊̓͂̏̔͘̕ͅ͏̘͙̬͚̭͔͓͙̥͚̫̭͍͓͙͚̮̤͚̫̰̭̘͈͚̪͖̭͔̘͓͚̬̮́̏̓͆͂͂͐̓̒͌̒̒͂͏̭͙͏̸̸̴̢̨̨̨͚̫̗̮͓͚̩̗̭̘͚̩̭͈͙͚̹̭̘͙͚̫̤̭͍̘͖͚̬̤̮͎̘͍͚̪̬̭͎̘͚̬̤̮͇̘͙͉͚̩̭͓͚̬̮͖̭͙̩͚̰̭͔̘͙͕͚̫̮͍̭͙̯͚̪̰̭̘͙̩͚̩̰̭͔̭̩͚̪̰̭͓̩͚̮̘͙͚̮͓͙̲͚̪̮͔͙͚̹̰̭͔̘͚̫̮͉͙͚̩̭͉̭͇͚̫̭͓͙͚̹̬̭͓͚̹̭͉̭͙̥͚̭͇̘͙̭͚̬̮͙͚͚̭͓͓͚̭͈͙͚̩̮͔̤͚̬̮͈͚̭͔̘͚̩̮͒̒̋͋̒̋͊̓͊͋̒̒̒̒͆͑̒̑͆́͑̒̓̒͂͒͐́͒͐̏̓͂̒̓͒̓̓͆̒͊͒͌͊̒̔́̏͊̓́̒͆́͂̓͆̓̓̒̏͑̓̒͂͆̒̏͘͏̸̸̨̘͙͚̮͓͚̩̗̭̭̖͚̩͖̭͉͖͚̩̰̭͉͙͚̹̮͖͖͚̫̗̭͈̭͙͔͚̩͎̭͎̘͚̩̮͇̭͙͈͚̩̭͓͙͚̬̮͖̘͚̤̭̘͙͚̫̭̭͙̯͚͖̮͎͙̩͚̩̮̘͙̤͚͎̭͓͙͚̪̰̮̭͙͖͚̺̭̒͂͒̒̓͋̒̓̒̓͒̓̒̒̑͆͆͑͆̒͑́͑͂͑͂̓͒͂̓͊͒̏͒̓̒͘ͅ͏̸̴̨̨͚̪̭͎̙͚̹̰̭͖̭͙͚̭͙͚͚̮͓͓͇͚̬̮͕͚͚̭͓͙̲͚̫͖̭͉̘͙̪͚̬̭͇̘͈͚̬̮͍̭͙̏̓̒́͋̓̓͂̒͆͐̓̒͂͊̒͏̸̴̡͚̭͔͚̫̭͓͙͚̭̭͚̬̭͈̘͙͚̭͔̘͖͚̪̮́̏̓̒͆̓͋͆͂͒̒̏͑͂̏̒͏̴̢̨̘͙͕͚̫̗̮͓͙͕͚̩̗̮͕̘̖͚̩̭͈͓͙͚̹̮͖̘͙͚̫̤̮͖͚̬̮͓͙͔͚̪̭͎̘͚̮͇̘͙̗͚̩̭͓̘͚̬̮̭͙͚̤̭͓͓͙͕͚̗̭͕͙̯͚̪̤̭̘͙̩͚̪͖̮̘͙̤͚̩̬̭͓͙͇͚͎̮̭͙͈͚̩̮͓͚̪̮͔͔͚̹̤̭͒̒͊͊͒̓̒͆͑͆̒̒͂͆͑̒͆͒̏́́̓͒͒̓͂͒͐̒̏̓̒͘͘͏̴̵̸̨̨̨̡̘͙͚̭͎͙͚͚̭͉̭͚̬̮͔͕͚̫̭͓͚̫̰̭͉̭͙̥͚̬̭͇̘͈͚̬̮͍̭͙̰͚̭͓̘͙͚̫̮͔͓͙͚̪͖̮͕͚̫̮͎̭͙͚̭͔̘͚̪̮́̓̓́̒͊͆̓̒͊͊̒̔̒́̏̓͆̓̒͑͂͒̒̏͊͏̶̭͙͚̫̗̭͚̩̗̭̭͙͚͚̩̭͇̭͚̩̰̮̑͐̓̒͋͊̒̏͏̸̨̭͙͚̫̰̭͉̘͖͚̫̭̭͍͚̩͎̭͎̘͙͚̮͇̘͙͚̺͚̮̒͌̒̈́͂̔͘͏͚̬̭͈̭͚̰̭̓̒̏͆̒͑́͏̸̨͙͚̗̭͕̘͙̯͚̪̰̮͙̩͚̩̭͇̩͚̭͓̹͚̮̘͙͚̺̮͓͙͚̪̭͎̭͚̹̤̭̭͚̮͓͙͚̗̭̓͂́͊̓̓̒́̓̓̒͂̓͒̒̏͐͐̏̒͌͐̒͐́͑̓́͏̴̨̘͚̬̰̭͍̘͕͚̺̭͓̗͚̫̰̭͉̘͙͚̬̭͇̘͚̬̭̒͊̒͒͊̒̈́̒͐͏̸̨̭͙͚̭͔̭͚̭͓͙͚̪̗̮̤͚̬͖̭͈̘͈͚̭͔̘͕͚̬̮́̏̒͆́͂͒͆͐̓̒̒͂̒͂͏̸̶̸̘͙͚̭͚̩̗̭͓̖͚̩͖̭͎͚̹̭͓͓͙͚̫̤̮͓͚̫̭͈̭͍͚̪̭͎̘͙͚̮͇̘͙̖͚̺͚̮͗͂͐̓̒͌̒̓̒̏͊͐̓̒̏̒̈́́̓͘͏̸̡͙͚̬̭͈̘͙͚̤̭͔͓͙͚̫̭̓́͆́͂͏̴̨̘͙̯͚̩̰̮͙̩͚̩̮̘͙̤͚͖̭͓̹͚̩͖̮̘͙͚̪̭͙͚̪̭͙̬͚̹̰̭͊̓͒͂̓̒͒̓͒̓͂̏͊̓͏̴̴̨̭͚̫̭͈͙͚̩̭͈̭͇͚̫͎̮͔͕͚̹̰̭͓̗͚̭͉̭͙͚̬̭͇̘͙̯͚̬̮͉̭͙͓͚͚̭̒̓͒̓̓̒̓̒͊̒́͂́́͏̴͚̮͕̭͙͚̩̮͕̤͚̬͖̮͎̭͙͚̪̭͔̘͚̪͚̮̓̒͑́͂͆̓̓̒͑̒͐͏̸̴̨̨̨̨̨̡̭͙͚̪͖̮͓̦͚̩̗̭̘͙̗͚̩͖̭͈͖͚̹̮͖̭͙͚̫̤̭̭͓͚̫̭̭͍͚̭͎̘͙͚̮͇̭͙͚̪̭͓͈͚̬̮͉͚̤̭͓͙͕͚̫̭͕͙̯͚̪̤̭͕̘͙̬͚̪̭͔̭̩͚̩͎̭͓͚̮̭͙͓͚̺̭͚̪̭͍̘͚̹̤̭͕͙͚̭͓͙͚̩̮͔͓͚̫̭͓͕͚̬̭͓͙͚̺͎̭͉̘͙̹͚̭͇̘͙͚͚̬̮͉̘͚͚̭͔̘͚̮͓͙͚̪̗̭͉̘͚̬̮͎̭͈͚͖̭͔̘͓͚̮͗͒̒͋̓̒͊͑̒͌̒́͊́̓̓͆͑̒͆͑̓̒́͒̓̏̒̓̒͂͂̓͒̏͒̓̒̓̏̒͌̓́͋̓͆̒͊͒̒͆͊́̏̒́̒͑́͂͐͆̒̓̒͂̒͂͒͘̕ͅ͏̸̢̭͙͙͚̮͓͍͚̩̗̭̘͚̩͖̭͎̭͖͚̩̰̭͇͙͚̺̮͖͓͚̫͎̮͎̘͍͚̫͎̭͎̘͙͚̬̤̮͇̭͙͚͎̮́͒̒͋̒̒̓͊̓̒̒̓͋́͘͏̸͚̬̮͓͙͚̰̭͓̘͙͚̗̮͍͓͙̯͚̩̰̭͕̘͙̬͚̪̭͔̭͙̤͚̩̤̭͓͚̮̘͙͚̺̮͓͚̪̮͔͓͙͓͚̹̰̭͖͙͚̫̭͈̘͙͚͚̮̓̒͑͆͒͊́͂́̓̓̒͂́̓͒̐̏͐̒͗̏̓͒̓͂͏̴̴̨͓͚̬̮͕͚̗̭͓͙̲͚̺͎̭͉̘͙̥͚̭͇̘͚̬̮͍̘͚͚̭͓͚̫̭͙͚̩̭̭̤͚̫̭͈̘͈͚̪̭͔̘̘͚̪̮̒͊͐̓̒͂͊͂̏̒͒̒͌́͑̒͑̓͒̓͆̓͑̒͂̒̒͊͏̸̸̴̢̡̘͙͕͚̮͓̘͚̩̗̭͓͚̩͖̭͇̘͖͚̹̮̭͙͚̺͖̮͖͓͚̫̮͓͙͔͚̩͚̭͎̘͙̮͚̮͇̭͙̘͚̺͚̭͓͚̬̮͙͚̰̭̭͚̗̮͕̭͙̯͚͖̮͓͙̬͚̪̭͇͙̤͚̪̬̭͓̬͚̫̮̭͙͈͚̩̭͙͚̪̭͓͙̰͚̹̤̭͂͒̒͌̒̈́̒͊͑̓̒͊͑͂͑̒͆͑̓́͒̒͌́͂͐͒̓̓̒͊͒͒̓͒̏͊͘͏̸̴̘͙͚̫̮͔̭͙͚̩̮͒̓͏̨̨̡͓͚̫̗̮͙͚̹͚̭͓͙̱͚̫̭͉̭͙͚̮͉̭͙͚͚̬̮͉̘͙͚͚̭͙̥͚̫̭̘͙͚̪̗̮͓͚̬̮͈͚̪̭͔̘͓͚̩̮̒͊͐̓͌͊̏͂́̏́͑̓̓͊͆̓̒̓͑̓̒͆̒͊͏̵̸̸̧̨̨̨̭͙͚̫̗̮͓͚̩̗̮͕̘͙̗͚̩̭͇͓͖͚̩̰̮̘͙͚̹̭͈̘͓͚̫͚̮͎̘͍͚̪̗̭͎̘͙͚̮͇̭͙͚͎̭͓̣͚̬̮͖̘͙͚̤̭͙͚̫̭͖͓͙̯͚̪̰̮͇͙̩͚̩͎̭͇̩͚̪̭͓͙͚͎̮̘͙͖͚̮͓͙͚̪̭͎͓͔͚̹̤̭͖͚̭͇̘͙͚̩̮͕͓͇͚̬̤̭͍̘͙͚̭͓̗͚̺͎̭͉̭͙͚̭͇̘͙̱͚̬̭͗͒̒͊̒͐͒̒̒̈́͂̓̓́͑̒͆́͑̓͂̓̓̒͒̓͊́͒́͒͐͂̏̒̓̒͐́̓͆̒͌͂͊̒͂̏͘͏̴̡̘͙͚̭̘͚̭͍͓͙͚̩̗̭͓̭͚̫̭̘͙͚̩̭͔̘͚̫̰̮͂́̏͒̒͑́͂͆̒͌͑͂̒͐͏̸̸̴̸̴̵̨̡̧̨̡̭͙͚̫̗̭͙͈͚̩̗̭͇̘͙͚͚̩͖̭͈͓͚̩̰̭͍̭͙͚̺̮͖͚̬̤̮͓͍͚̭͎̘͙͚̮͇̭͙͍͚̪̭͓͙͚̬̮͖̭͙̩͚̰̭͙͕͚̫̮͓͙̯͚̩̰̮͙̬͚̩̭͔̭͙̤͚̩̭͓̬͚̮̘͙͚̩̭͙͓͚̪̭͙͚̹̰̭͕̭͙͚̫̭͎̭͙͚̭̭͇͚̬̭͍̘͕͚̭͓͙͚̬̭͉̘͙͚̮͉̭͙̱͚̬̮͍̘̙͚͚̭͓͙͚̫̭͈͓͙͚̩̗̮͔͚̬̮͈͚̭͔̘͓͚̮͒͐̓̒̏͊͑̓̒͑̒͂͂̈́͂͆͑͆͆́͑̓͊͊̓͂̓̒͂͒͗͒̓̏͊̓͗͒̓͂̏͌̒͆̒͂͊͊̏́̏̒́͒̓͆̓̒͆͑̓̒͂̏̒́͂͘͏̸̴̵̘͙͕͚̫̗̮͓̗͚̩̗̭͇̘͚̩̭͈͓͖͚̹̮͖̘͙͚̹̮͖͚̬̰̭͈̭͙͔͚̪͖̭͎̘͙͚̪͖̮͇̘͙̙͚̩̭͓͚̬̮̭͙͚̤̭͔̘͚̗̭͕̭͙̯͚̪̤̭̘͙̩͚̪̮͖̘͙̤͚̪̭͓͙͚̮̭͙͚̩̭͙͚̪̭͎͓͚̹̰̭͒̒̒̋͊̒͊͊͐̓̒̓͆͑̒̐͆͒͊́̒̑́͒͊̏̓͊́͒͐͒̓̏̒͘͘͏̸̷̸̨̨̭͙͚̮͈͓͙͚̭͖̘͇͚̫͖̭͍̘͕͚̹̭͓͙͚̹̭͉̭͙̥͚̮͉̭͙̱͚̬̭́̓́̏̒̒͒͊́̏͏̭͙͚̭͔͙̥͚̭͙͚̪̗̭͉̘̤͚̬̭͈̘͙͚̰̭͔̘̘͚̮͂́̏̓́͂͊̓͆̒̏͑́̒́͒͏̸̢̭͙͚̮͓͙͚̩̗̮͕̭̮͚̩̭͉͙͚̩̰̮̑͂͒̔̒͊̓͏̭͙͚̹̭͍̘͖͚̫̮͎̘͍͚̪̭͎̘͙͚̮͇̭͙͍͚̩̮͒̒͊̒͒̈́́̓͆͘͏̸̴͎͚̬̭͈̭̖͚̰̭͓͙͕͚̫̮͍͓͙̯͚͖̮͇͙̬͚̪̗̭͔̭̩͚͎̭͓͚̩͖̮̘͙͚̪̮͓͙̰͚̪̭͓͚̹̤̭̓̒͆̒́͒͂̓̒͂̓̒͂͒̓͐̏͊̒͐͏̴̨̨̘͚̫̭͎̘͙͚̭͉̭͇͚̫̭͓͕͚̫̭͓͙͚̭͉̘͙̥͚̮͉̭͚̬̮͍̘̙͚̭͔̭͚̮͓̭͙͚̪̮͕̤͚̬̭̘͈͚̩̤̭͔̘͙͚̮̒̓͒̓͂̏̒͊͒̒͒͊́͂́̏̒͌̒́̏̒͑́͂͆̓̓̒̓͌̒͂͒͏̘͙͚͚̪͖̮͓͙͚̩̗̭͇̘̺͚̩̭͎͚̹̮͕̘͙͚̫̤̭͓̭͓͚̫͖̭̭͙͔͚̪̬̭͎̘͚͎̮͇̘͙͚̺͚̮͒̐̒͊̓̒̏͊̒͌̒̒͂͌͘͏̸̴̸̴̡̨͚͚̬̮͓͚̤̭͙͚̗̮͉͓͙̯͚̩̰̮͎͙̩͚̪͚̭͇̩͚̩͖̭͓̹͚̩͖̮̭͙͚̺̭͔͚̪̭̙͚̹̤̭͖̘͙͚̫̭͈͙͚̩̭͖̘͇͚̬̮͔͕͚̹̭͓͙͚̫͖̭͉̭͙͚̬̭͇̘͙͚̬̮͉͓͔͚͚̭̓̒͆͒̒̋́͑̓͂́̓̓̒̓̒͒͒̏͒̓̒̏͊̓̒͒̓̓̒̓̒͆͊́͂̒́͏͚̭͓͙͚̪͚̭̭̤͚̬͚̮͎̭͙͚̭͔̘͙̥͚̮̓̒͑́͂͑͆͒̒͑́͒͂͂͏̸̢̨̨̭͙͚̮͓͙͚̩̗̮͕̭͚̩̭͍̭͙͚̩̰̭͙͚̫̰̮͓͚̫̮͓͍͚̭͎̘͙͚̮͇̭͙͚̩̮̓́͒̏̒͊̐͊̓͑̓̒͑̒͂͆̈́͂͌͆͘͏̸̴̴̴̸̨̨̨̨̡͚̬̮̘͍͚̰̭͓̘͚̫̭͔̘͙̯͚̪̤̮͖͓͙̩͚̪̭͔̭̩͚̪͚̭͓̹͚̩̮̘͙͚̪̭͓͚̪̭͎͓͚̹̤̭͕͙͚̮͕͙͚̩̮͔͓͚̫̮͕͚̬̭͓͙͚̹̭͉̘͙͚̬̮͉̭͙̳͚̬̮͉̘͙̰͚̭͓͚̮͓͙͚̪̮͕͚̬̗̭͈̘͈͚̩̭͔̘̘͚̮̓̒͆͒̒́̒̑̏̒̓̒͆͒̐͒̓̒̏̒͐̓́̓̓͆̒͊̓͐̓̒́͊̓̓́̏͑̒͑́͂͐͆̓̓̒̒̒́͒͏̵̭͙͚̪͖̭͚̩̗̭̘̦͚̩͖̭͍͓͙͚̩̰̭͇͙͚̺̭̘͖͚̫̭͈̭͍͚̫͎̭͎̘͙̯͚͎̮͇̭͙͚̺͚̮̒͐̓̒͋̒̐̓͊͋̒̓̒͂͘̕͏̸̸̴̨̨͚̬̮͚̤̭͓͙͚̫̭͖̘͙̯͚͖̮͕͓͙̩͚̪̮̘̩͚̭͓̫͚̩͖̮̘͙͚̮͓͙͔͚̪̮͔͓͙͓͚̹̰̭͖͓͙͚̮̭͙͚̩̮͕͓͇͚̫̭͍̘͕͚̬͚̭͓͙̤͚̹̭͉̭͙͚̬̭͇̘͙͚̬̭̓̒͑͆͑̓̒̒́͑͂͂̏͒̒͂̏̓̒͒̐́͒͐̏́͐̓͆̒̓̒͊̓̈́͂͏̭͙͚͚̭͙̥͚̫̭͓͙͚̪̗̭͓̭̤͚̬̗̮͈͚̰̭͔̘͕͚̮͗́͒̓̓͋͆̒͑̓̒͂̒́͒͏̸̡̭͙͚̫̗̮͓̫͚̩̗̭͓̖͚̩͖̭͍̘͚̩̰̮͖̭͙͚̹̭̘͓͚̫͖̭͈̭͍͚̤̭͎̘͙͚̪̰̮͇̭͙͚̺͚̭͓͙͚̬̮̭͚̰̭͓͙͕͚̫̭͑͒̒͌̒̒̏͒͌̒̒͂̓̔͑͆͒̒̋́͒͘͏̴̴̨̨̨̡̨̨͙̯͚̭͓̘͙̩͚̩̤̭͔̭͙̤͚͖̭͓͙͇͚͎̮̭͙͈͚̺̮͓͚̪̮͔͓͙͚̹̰̭͖̭͚̭̘͙͚͎̭͎̭͚̫̗̭͍̘͕͚͎̭͓͙͚̫̭͉̘͙͚̮͉̭͔͚̬̮͉̭͙͚͚̭͓͚̫̮͙͚̪̗̮͚̫̭̘͙͚̭͔̘͙͚̬̮̓͂͊͂̓͂͒̏͐̒̒̏͂̒̓́͌̓́̒͊̒͂͊͆́̏̒͗́͑̒͑̓͐̓͆͐̓̒͌͑͂́͏̴̸̭͙͙͚̫̗̮͓̩͚̩̗̭̭͚̩̭͎̘͙͚̹̭͎̭͙͚̹̭̘͖͚̬̭͈̭͙͔͚̭͎̘͙͚͎̮͇̘͙͉͚͎̭͓͙̤͚̬̮͚̰̭͓͙͕͚̫̭̭͙̯͚͖̮͇͙̩͚̪͖̭͇̩͚̪͖̭͓̫͚͎̮̘͙͈͚̭͚̪̮͔͔͚̹̤̭͒̒͋̒̋͊̐͊͒͊̒́̏͂́͑͆͑̓̒̒́͑͒͂̓̓̒̓̒͂͒́͒͒̓̒͌̏̓̒͘ͅ͏̨̨̨̡͓͚̮͕͓͙͚͚̮͓͚̫͚̭͍̘͕͚̫̭͓͙̲͚̺͎̭͉̭͙̦͚̩̮͉̭̘͚̬̮̙͚͚̭͓̭͚̭͈͓͙͚̩̭͓̭͚̬̗̭͈̘͙͚̩͎̭͔̘͙̥͚̮̒̓́̓͂͑̒͊̒͂͊̒͊̓̒́̒͑́͂͆̓̒͑́͂͏̸̭͙͚̭͙͚̩̗̮͕̘̖͚̩̭͎̘͖͚̹̮͑́͐̓̏̒͊̒͊͏̸͓͙͚̺̮͓͖͚̬̭͈̭͙͔͚̫͚̭͎̘͙͚̩̮͇̘͙͚̪̮͊̓̒̈́̏͊͆͘͏̸̴̷̨̨͚̬̮͓͙̥͚̤̭͓͙͕͚̫̮͍͙̯͚̩̰̭̘͙̬͚̪̮͖̘͙̤͚̩̬̭͓̩͚̮̭͙͖͚̩̮͓͙̲͚̪̭͙͓͚̹̰̭͚̮͓͓͙͚͎̭͇̭͚̫͖̮͕͚̹̭͓͙͚̫͖̭͉̘͙͚̭͇̘͚̬̭̓̒̐͆͒́͑̓͒̓̓̒͂̓͒͐̏͊̓͐̓̒̓́̓́̒͊͐̓̒͒͊͂͂̏̒̕͏̡̘͙̬͚͚̭̘͙̥͚̮̘͙͚̪͖̮͔͚̬͖̭̘͙͚̹͎̭͔̘͚̩̤̮́͑́͂͑͆̓̒͌͑̒͐͏̵̴̴̸̨̘͙͓͚̫̗̭͙͍͚̩̗̮͕̘͙͚͚̩͖̭͎̘͙͚̹̭͕̘͙͚̹͖̮͓͓͚̫̮͓͍͚͎̭͎̘͙͚̫͚̮͇̘͙̗͚̺͚̭͓͎͚̬̮̘͙͚̤̭͓̘͚̗̭͖̘͙̯͚̮͕͓͙̩͚̩̭͇͙̤͚̩̭͓͙͚̮̭͙͈͚̩̮͓͚̪̮͔͓͙͚̹̤̭͕̭͙͚̫̮͓͓͙͚͎̮͐̓̐͊̓̒͑̒́͂͑̒͆͒́̒͌́͂͊̓͆̓͊́̓͒͐̒͑̏͂͒̓́͘͏̴̨̨̡̨͓͚̬̭͍̘͕͚̫͖̭͓͙̱͚̫̭͉̘͙͚̩̮͉̭͙̗͚̬̮͍̘̙͚̭͔̭͙̥͚̮͙͚̪̮͚̬̮͙͚͚̭͔̘͙͚̮̒͊̒͊͆͆̒́̏́͂͐̓͆̓͐̓̒͊͑̓͑͂͂͂͏̸̸̘͙͔͚̭̬͚̩̗̭̘̮͚̩͖̭͎͓͚̹̮͙͚̹͖̭̘͖͚̫̗̮͎̘͍͚̭͎̘͚̮͇̘͙̖͚̪̮́͐̓̒͋̒̒̏͊͒̓͊̒̒́͂̒̑́͆͘͏̸̖͚̬̮̭͚̤̭͔̘͙͚̫̭͙̯͚̭̓̒͆͒̒̋́͂͑̓͂͊͏̸̴̴̵̸̨̨̡̨̨̘͙̩͚̩̭͇̩͚̫̭͓̹͚̩̮̭͙͙͚̭͓͚̪̭͓͙͚̹̤̭͔̘͚̮͕͓͙͚̩̮͓͚̬̮͔͕͚̹͖̭͓̗͚̭͉̭͙͚̮͉̭͉͚̬̮͍̭͚̭̭͙͚̫̭̭͙͚̮͚̫̮͎̭͈͚̭͔̘͕͚̪͚̮͂̓̒̓̒̏͒́͒͒̓̒̏͊͂̒͐́̓͐̒͊̓̒͊̒͂͒̈́́̏̒̒́̏͒̓͒͆͂͑̓̒̒͂̒͘͏̶̢̭͙͚̫̗̭͚̩̗̭͚̩͖̭͎͚̹̭͙͚̫̰̮͓͚̫̭̭͙͔͚̪̬̭͎̘͚͎̮͇̘͙͚͎̮͑͐̓̒͋̓̒̓̒̏͊͐̓͒̓̒̏͌̒̒͂̋́͘͏̴̸̴̨̨͚͚̬̮͓͍͚̰̭̘͚̗̮͉͓͙̯͚̪̮͎͙̬͚̪͖̮͖̘͙̤͚͚̭͓̫͚̮̭͙͚̪̮͓͎͚̪̭͎̭͚̹̤̭͖̭͙͚̫̭͎̭͙͚̭̭͇͚̫͎̮͔͕͚̹̭͓͙̤͚̭͉̭͙͚̬̮͉̭͙̙͚̬̮͉͓͔͚͚̭̓̒͆͒̒́͑̒͌́͂̓͂̓̒͂͒͒͐̒̏̒̑͒̓́̏͌̒̓̒͆͊͂͒́̒́͏̨͚̮͔̭͙͚̪͖̭̭̤͚̬͚̮͎̭͙͚̪̭͔̘͚̪͚̮̓̒͆́͂͆͒̒͑̒͐͏̴̸̢̨̨̘͙͚̪͖̮͓͙͚̩̗̭̘͙̗͚̩͖̭͈̭͙͚̩̰̭͎͙͚̹̭̭͓͚̫͎̭̭͙͔͚̪̬̭͎̘͚̮͇̭͙͚̺͚̭͓͚̬̭͈̭͚̤̭͓̭͚̗̮͙̯͚̪̤̭͕̘͙̬͚̪͚̮͖̘̩͚̩͎̭͓͚̪̰̮̭͙͕͚̪̮͓͚̪̮͔͓͙̬͚̹̤̭͖̭͙͚̫̭͈͓͙͚͎̭͉̭͚̫̭͓͙͚̫͚̭͓͚̬͖̭͉̭͙͚̩̮͉̭͙̺͚̬̮͉͓͙̰͚̭͑͒͑͋̓͊͑̒͌̒̑́̓͑̒̓͆̒̋́̒͌́͌̓̒̓̒͂͒͐̒͌̏͒̓́̒͊͒͒͌͊̒̔͂́̏͘̕͏̸̴̡̨̨͚̫̭̭͙͚̪̭͍̘͚̫̮͎̭͈͚̭͔̘͙͚̩̮̓̒͆̓͒͆̓̒̒́͏̸̨̘͙͚̭͚̩̗̭̘͙̗͚̩̭͎͙͚̩̰̭͍͓͙͚̺͖̭͈̘͖͚̫̮͓͙͔͚͖̭͎̘͙̯͚̪͖̮͇̭͙͚͎̮͒́͐̓̒̈́͋͊̓̐̒͑́̓́͘͏̸̴̸̴̨̨̨̨͙͚̬̭͈̭͍͚̰̭͔̭͚̗̮͈̘͙̯͚͖̮͕͓͙̩͚̪̭͔̭͙̤͚̩̭͓̹͚̮̭͙͓͚̪̮͓͚͚̪̭͎̭͙͚̹̰̭͖͙͚̮͕͙͚̩̮͕͓͇͚̫̭͓͙͚̹͚̭͓͙̤͚̺͎̭͉̭͙͚̬̮͉̭̗͚̬̭̓͆̒́̒͌́͂̓͂̓̒͂͒͐̒̏͂̓́̓̓͆̒͒͌͊́̒͏̸̡̭͙͚͚̭͔͚̫̭͓͙͚̭͈̘͚̫̭̘͈͚̬̭͔̘͕͚̬̮͗́̓̒͑̓͋͆͂͂̒͌̒͂̒́͏̸̸̘͙͚̮͓̯͚̩̗̭͇̘͙͚̩͖̭͍̘͚̹̭͎̘͙͚̺̭̭͓͚̫͖̭̭͍͚̬̤̭͎̘͙̮͚̮͇̘͙͚̪̮͒́͒̒̏̒̏͊͊͑̒͌̒͂͌͆͘͏̴̨̨̨͚̬̮̘͙͚̰̭͓͓͚̗̮̭͙̯͚̭̘͙̩͚̪̭͔̭͙̤͚̪͚̭͓͙͚̩̮̭͙͈͚̺̮͓͚̪̭͎̭͙͓͚̹̰̭͕̘͚̮͇̭͙͚͎̭͎̭͇͚̬̤̭͓͕͚̬̗̭͓͙͚̫̭͉̘͙̥͚̩̮͉̭͙̙͚̬̮͙͚͚̭̓̒̒͆͒̒́̒͌́͊͂͊͐͒̓͊̏͒̏͐̒͐̏̒̓́̓́̒͒̒͊͆͊̓͗́͏̴̡͙̥͚̭̭͙͚̪̗̮͚̬̭̘͙͚̪̭͔̘͚̬̮̓́͂͒͆͒̓̒͆͌͑̒͐́͏̸̢̨̘͙͚̪͖̭͙͚̩̗̭̭͙͎͚̩͖̭͍͓͙͚̩̰̮͙͚̺͖̮͖͓͚̫̮͎̘͍͚̭͎̘͙͚̮͇̘͙͍͚̩̮̐͐̓͌͋͐̓̓̒͒̒́͂͆͘ͅ͏̶̸̸̴̴̨̨̨̨͙͚̬̭͈̘͚̰̭͙͚̫̮͎̘͙̯͚̪̰̮͍͙̬͚̪̗̭͇̩͚̭͓̬͚̩̮̭͙͙͚̺̮͓͍͚̪̭͎͚̹̰̭͖͙͚̮͕̘͙͚͚̭̘͇͚̫͎̭͍̘͙͚̹̭͓͙͚̫̭͉̭͙͚̬̭͇̘͙͚̬̮͙̰͚̭̓͆̒̒́͒̓͂̓̓̒́̓̓̒̏͒̏͐̒̏̓̒̓́̓́͐̒͌͊͆̈́͊̓́̏̕͏̡͚̫̮͕̭͙͚̩̗̭͍̘͚̬̮͈͚̪̰̭͔̘͙̥͚̮̓̒͆̓͆̒͆͑̓̒́͂͏̭͙͈͚̪͖̭͚̩̗̮͕̘͚̩̭͎͙͚̩̰̭͓͓͙͚̺̮͓͓͚̫̭̭͙͔͚̫͚̭͎̘͙͚̩̮͇̘͙̗͚̺͚̮͐̓̒̋̒̋͊̓̐͊̓̒͊͌̈́̏͘͏̸̸̴̸̷̸̵̸̨̨̡͙͚̬̭͈̘̖͚̰̭͓̘͙͕͚̫̭͓͙̯͚̩̰̮͙̩͚̪̭͇͙̤͚̪͖̭͓͙͇͚͎̮̭͙͚̩̭͙̳͚̪̭͎͓͙͚̹̤̭͓͙͚̮͓͓͙͚̗̭̘͚̫̮͕͚̹̭͓͙͚̗̭͉̘͙͚̮͉̭͙̳͚̬̮͙͚͚̭̘͙͚̭͓͙͚̭͈̘͚̬͚̭̘͈͚̬̭͔̘͚̩̤̮̓͆̒́͒͊̓̏̓̓́͒̓͒̓̏͗͐́̓́͐̒͊̏͐̓̒͒͊͂͂͂̏͊̓́͑́͂͒͆͂̒͌̒́̒͐͏̭͙͚̪͖̭͚̩̗̮͕̘͍͚̩͖̭͎̘͖͚̹̭͓̘͙͚̹͖̭̭͓͚̫̮͓͙͔͚̫͖̭͎̘͙̮͚̪͖̮͇̭͙͚̪̭͓͚̬̭͈̭͉͚̤̭͔͙͕͚̗̭̒͐̓̒̒̒͊͑̒͒͑͊͆͑̒͆̒́̓́̕͘͘͏̴̴̴̨̨̨̡̨͙̯͚̪̤̭͓̘͙̩͚̪̭͔̭̩͚̭͓̩͚̮̭͙͈͚̩̭͙̯͚̪̮͔̙͚̹̰̭̭͚̫̮͓͙͚̩̭͍̭͇͚̫̭͍̘͕͚̹͚̭͓͙̱͚̬̰̭͉̭͙͚̬̮͉̭͙͚̬̮͙̰͚̭͔̭͙̥͚̫̮͓͙͚̪͖̮͚̬̭͈̘͙͚̩̭͔̘͙͚̮̓͊̒́̏̓̒͂͒͒̓̏̓̒͐̒̓͒̓̓̒̒͊͆̈́͊̓́̏̓͒͆͐̓̒͒͑͆͂͂͏̸̢̨̘͙͈͚̫̗̭͚̩̗̭̘̺͚̩͖̭͇͙͚̹̮͕̘͙͚̫̤̭̘͖͚̫̮͓͙͔͚͖̭͎̘͙͚͎̮͇̭͙͈͚̺͚̭͓̦͚̬̮͖̭͚̤̭͔͓͙͚̫̮͍̭͙̯͚̪̰̮͇͙̬͚̪̮̘̩͚̭͓̹͚̪̰̮̘͙͐̓̒͆͋̒̓͊͋̒͑́̓͂͑̒͆̒͑́͂̓͒͒̒́̓̓̒͒͘͏̴̴̴̸̴̨̨̨͚̩̮͓͙͚̪̭͚̹̤̭͖̭͙͚̭͍̘͙͚̩̮͓͇͚̫̮͙͚̫̰̭͓̗͚̭͉̭͙͚̬̭͇̘͙͙͚̬̮͍̭͙͓͚͚̭͓͚̫̭̭͙͚̮͔̤͚̬̭͈̘͈͚̭͔̘͚̮͐͐̏͊̓̒́̓͐̒͒͐̓͌͊̒͂͒̓́͒̒͆̓͒͆͂̓̒͊̒͂̒͐͂͒̕͏̸̘͙͚̭̺͚̩̗̭͓͚̩͖̭͇͓͚̹̭͖̭͙͚̫̤̮͓͚̫̭͈̭͙͔͚̪̬̭͎̘͚͎̮͇̭͙͚̪̮͗͂͐̓̒͌̒̈́̒̏͊͑̓̒͊̒̒͂͌͆͘͏̴̶̨͙͚̬̮͙̩͚̰̭̘͚̗̮͉͓͙̯͚̪̮͇͙̬͚̪͖̮͖̘̩͚̩̭͓̹͚̪̮̭͙͚̪̭͙͚̪̮͔͚̹̰̭̓̒͆͑̓́͑̒͌́̓̒̏̓̒͆͒͒͒̓̏̓̒͌͏̴̴̨̨̨̭͙͚̫̮͎̘͙͚̩̭̭͚̫̮͙͚̫̭͓̗͚̭͉̘͙͚̬̮͉̭͚̬̮͉̘͙͒̓͌̒͊͐̓͌͂͊̒́͂̈́̒̋͏̨͚̭͚̫̭̘͙͚̪͖̮̤͚̫̮͎̭͙͚̭͔̘͙̥͚̮́̏͑̓̒͆̓͑͆͑̓̒͂͑͂͂͒͏̸̴̸̴̢̨̨̨̨̡̭͙͚̮͓͙̗͚̩̗̭̘̦͚̩̭͈̭͙͚̹̭͕͙͚̹͖̭͉̘͓͚̫̭͈̭͍͚͚̭͎̘͚̪͖̮͇̭͙͚̪̭͓͙͚̬̮̭͚̰̭͓̘͚̗̮͉̭͙̯͚̪̤̭̘͙̩͚̪̭͔̭͙̤͚̭͓̮͚͎̮̘͙͚̪̭͙͓͚̪̮͔͙͚̹̤̭͕͙͚̫̭͉͙͚̩̮͔͓͇͚̬̰̭͍̘͙͚̺͖̭͓͙͚̺͎̭͉̘͙͚̩̭͇̘͚̬̮͉̘͙̰͚̭̘͚̮͓͙͚̪̗̮͕͚̫̬̮͈͚̭͔̘͓͚̮̓́͒͋̒͊͊̓̒̒́̒̒̔͆͑̒͆͒̒̋́̒͌́͐̏͂̏̓̒͂͒̐͒̓̏̓̓͒̓̓͆̒͌͊̒̋́̏͒̒͆́͂͐͆̓̒͑̓̒͂͒̒́͒͘ͅ͏̸̸̢̭͙͙͚̭̖͚̩̗̭̘̦͚̩͖̭͎̘͙͚̩̰̮̘͙͚̺̮͖͓͚̬̬̮͓͍͚̫͎̭͎̘͙͚̮͇̘͙͚̩̮́͐̓̒͋̒͑͊̓̒͑̒̓́̏͆͘͏̸̴̨̨̨̨͙̲͚̬̮͙͚̰̭͓̘͙͚̗̮͎͓͙̯͚̮͕͓͙̬͚̪̭͔̭̩͚̭͓͚̮̘͙͚̮͓͖͚̪̮͔͙͓͚̹̰̭͖͙͚̮̭͙͚̩̮͕͓͇͚̫̭͍̘͙͚̺̭͓͙̤͚̹̭͉̭͙͚̩̮͉̭̗͚̬̭̓͆͑̓̓́͂́͂͊̓̒́̓̒͂͂̓͒̐́͒͐̒̏̓̓́͑̓͆̒̓͌͊̓͆̒͏̵̨̨̭͚̭͔̘͙͚̮͖͓͙͚̭͍̘̤͚̬͎̮͎̭͙͚̩̭͔̘͙͚̩̤̮̒͐́̏́͂͆͂͂̒͑͏̴̨̨̨̡̭͙͙͚̪͖̭͙̙͚̩̗̭͇̭͙͚̩͖̭͈͓͖͚̩̰̭͕͓͙͚̺̮͓͓͚̫͖̮͎̘͙͔͚̪̬̭͎̘͚̬̤̮͇̭͙͚̪̭͓͙̦͚̬̭͈̘͙̩͚̤̭͔͚̗̮͇̘͙̯͚̪̤̭͓̘͙̩͚̪̭͔̭͙̤͚̪̗̭͓̩͚̮̭͙͈͚̮͓͚̪̮͔͓͙͚̹̰̭͖̭͚̭͇̭͙͚͎̭͎̭͚̫̗̭͓͙͚̹̭͓͙͚̫̭͉̘͙̥͚̮͉̭͙̳͚̬̮͉̭͙͚̭͙̥͚̫̭͎͙͚̩̮͕͚̬̭̘͙͚̪̰̭͔̘͚̬̮͐̓͊̒͊̓̒̒̑̏͆͑͆́̓̒̑́͒̓̒͂͒́͒͐̒͐̏͂̒̓́̓́̒͊͒͌͂͊͆͂̏͗́̏͑̓̓̓͆̓̓̒͊͌͑̒͐́͘͏̴̸̸̢̧̭͙͕͚̪͖̭͙̙͚̩̗̭̭͙͎͚̩͖̭͍͓͙͚̩̰̮͙͚̺͖̭̘͖͚̬̭̭͍͚̭͎̘͙͚̬̤̮͇̭͙͍͚̩̭͓͙͚̬̮͙̥͚̰̭͓͙͕͚̫̭̭͙̯͚̪̤̮͎͙̩͚̪͖̭͇̩͚̪͖̭͓̫͚̩̮̘͙͚̮͓͍͚̪̭͎͙̬͚̹̤̭͐̓͋͐̓͋̒͌̒́̈́͆͑͆͑̓́͑͑̓̓̒̓̒͆͒̒́͒͐̒̏̓͘͏̴̨̨͓͚̮͕͓͙͚̮͓͇͚̫͎̭͍̘͙͚̺̭͓͙̱͚̬̭͉̭͙͚̬̮͉̭͚̬̮͉͓͚̭̒͐́̓́̏͐̒͌̓͊̏̈́̒͋̒͐́̏͏͚̫̮͓͓͙͚̩̗̮͖̤͚̫̭͈̘͈͚̭͔̘͕͚̮̓̒͑̓͆̓̒͂̒́͒̒͂͒͏̢̘͙͚̪͖̮͓͚̩̗̭̘̖͚̩͖̭͈͙͚̩̰̭͍̭͙͚̹̭̭͓͚̫̗̮͎̘͙͔͚̩̭͎̘͙͚͎̮͇̘͙͚̪̮̓͒̒͋̒̓̓͒̒͒̈́͂̋͆͘ͅ͏̴̵̸̨̡̨̡͙̹͚̬̭͈̘̖͚̰̭͓̘͙͚̗̮͖̘͙̯͚̩̰̮͍͙̩͚̪͚̭͔̭̩͚͖̭͓͙͇͚͎̮̭͙͖͚̪̭͙̳͚̪̭͎͓͙͚̹̰̭͖̭͚̮͓͓͙͚͎̮͓͓͚̫̮͕͚̹̗̭͓͙͚̫͖̭͉̘͙͚̮͉̭͙̳͚̬̮͉͓͚͚̭̘͙͚̭̭͙͚̩̗̭̘͚̬͖̭̘͈͚̭͔̘͓͚̪̮̓͆̒́͂́̓̒͂̓́͒͒̓̏͗̒͐́̓́̒͊̏͐̓̒͊͂͂̏̒́͑́͂͒͆͋̒͌̒́̒͊͘͏̨̨̘͙͚̪͖̮͓͚̩̗̮͕̭͙͎͚̩̭͍͓͙͚̹̭͖͓͙͚̹͖̭͈̘͓͚̫̮͎̘͍͚̫͖̭͎̘͙̮͚͎̮͇̘͙̘͚̺͚̮͗͒̒͊̐͊̒̒͂͘͏̴̨̡̨̨̦͚̬̮͙͚̰̭͓͚̗̭̘͙̯͚̪̰̭̘͙̬͚̩̮͖̘̩͚̪̬̭͓̩͚͎̮̭͙͚̺̭͚̪̮͔͓͚̹̤̭͕̭͙͚̫̮͓͙͚̩̮͓͚̬̰̮͔͕͚̹̭͓̗͚̫̰̭͉̭͙͚̩̮͉̭͙̗͚̬̮͍̘͙͚͚̭͙̥͚̮͙͚̪̭͓̭̤͚̫̤̮͙͚̩̭͔̘͚̩̮̓̒͆͑̓̓́͑̒̑́͑͐͆̒̓̒́͒̓̏͒̓̒͌̏̒͒̓̓͆͐̒͊̓̒̏͊̒́͒̓́͂͐̓͆̓̒͑̓͑͂̒͐͊̕͏̢̢̨̘͙͚̫̗̭͙͓͚̩̗̭͚̩̭͍̘͙͚̹̭͓͙͚̹͖̭͉̘͖͚̫̮͎̘͙͔͚͚̭͎̘͚̩̮͇̭͙͉͚͎̮͑͐̓͋̓̒͊͊͊̒́̒̑̏́͘͏̸̴̴̨̨̨̖͚̬̮̭͉͚̰̭̘͚̫̮͇͙̯͚̪̰̮͙̩͚̪̭͔̭̩͚̰̭͓͚̮̘͙͈͚̭͚͚̪̭͍̘͔͚̹̤̭͔̘͚̭͙͚̩̮͓͇͚̫̗̮͙͚̗̭͓̗͚̗̭͉̭͙͚̭͇̘͙͙͚̬̮͍̭͙͓͚̭͓̘͙̥͚̫̭̭͙͚̪̭͍̘̤͚̫̬̭̘͈͚̭͔̘͕͚̪͚̮̓̒͆͒̒́͑̒͌̓͊̓̓̒́̓̒͂͂͒́͒͒̓̒̏̒̒͐́͋̓̓͐̒͐̓͌͂͊̒͂̈́͂̏́̏̓͒͆̓̒͌̒͂̒͏̸̭͙͔͚̭͉͚̩̗̭͇̘̺͚̩̭͎̭͚̹̭͖̘͙͚̹̮͓͚̫̭̭͙͔͚̫̭͎̘͙͚̪͖̮͇̘͙͚̺͚̮͂͐̓̒̒͊̒̏͊͊͑̓̒̓͌̓͌͘ͅ͏̴̸̨̨͙͚̬̮͙̹͚̰̭̘͚̗̮͓͙̯͚̪̭̘͙̬͚̪͖̮͖̘͙̤͚͎̭͓͚͎̮̭͙͚̪̮͓͚̪̭͎̭͚̹̤̭͕̘͙͚̫̮͈̘͙͚͎̭͇̭͚̫͚̭͓͕͚̭͓̗͚̬̰̭͉̘͙͚̭͇̘͔͚̬̮͉̘͙̓̒͆͑̓́͑̒͌́͊͒͂̓̒͂͂͒͒͐̒͌̏̒̑͒̓́̒͊͒̒͂͊͊̒͆͂̏̒͏̵̸̡͚͚̭͔͓͙͚̫̭̘͙͚̪͖̮͚̫̮͎̭͙͚̭͔̘͚̪͚̮́̓͑͆͑̓̒͑͂͆̒͐͏̸̸̸̴̸̴̴̨̨̘͙͚̮͓͙͍͚̩̗̭̘͙͎͚̩͖̭͈̭͚̹̮͙͚̹̭͓̭͓͚̫̭͈̭͙͔͚̭͎̘͚̩͖̮͇̘͙͈͚̺͚̭͓͚̬̭͈̘̖͚̤̭̘͚̫̭̘͙̯͚͖̮͈͙̩͚̩̭͔̭̩͚̬͖̭͓͚̮̭͙͔͚̺̮͓͚̪̮͔͓͙̬͚̹̤̭͖͙͚̫̭͈͓͙͚̗̮͓͇͚̬̮͔͙͚̫̭͓͙͚̫͖̭͉̭͙͚̩̭͇̘͙͚̬̮͉̘͙̬͚̭͑͂͒͋̒̏͊͒̓͊̒͊́̒̑͑̒̐͆̒́͒̒̑͐͂̓̒̓̒͂͂̓͒̏͐̒͌̏̓͒̓́͐̒̓͌͊͊͂̋́̏͘͏̡͚̫̭̘͙͚̪͚̮͕͚̫̬̮͎̭͈͚̹̤̭͔̘͙̥͚̬̮̓̒͆̓͒͆̓̒̒́͏̢̢̨̨̭͙͚̪͖̭͚̩̗̮͕̘͚̩̭͎͙͚̹̭͕͓͙͚̺͖̭͈̘͖͚̫̮͎̘͙͔͚̭͎̘͙͚̮͇̭͙͚͎̮͐͐̓̒̒͊̓̐͊̒͂͂́̓̓́͘͏̵̨̨̡̨͚̬̭͈̭͍͚̤̭͓͚̗̮͍̘͙̯͚͖̮͕͓͙̩͚̪͚̮͖̘͙̤͚̬̭͓̹͚̮̘͙͚̺̮͓͖͚̪̭͎̭͚̹̰̭͕̘͙͚̮͓͙͚̗̭͎̭͇͚̫͎̭͍̘͙͚̺͎̭͓͙͚̗̭͉̘͙͚̮͉̭͙͚̬̮͍̘͙͚͚̭̘͙͚̭͈̘͙͚̩̭͓̭̤͚̬͎̮͈͚̬̭͔̘͚̬̮̓̒̑͆̒́͒̒͌́͂͊̓̒͂̓͒̐̏͐̒̏̒͐́̓̓́̒͌͊͂̈́͂̏͌͗́͒́͂͆̓̒͑̓̒͂̒͐͂͏̸̵̨̨̨̭͙͚̫̗̮͓̯͚̩̗̭͇̭͙͚̩͖̭͍̘͚̹̭̭͙͚̺͖̭͓̭͓͚̫͖̭͈̭͍͚̗̭͎̘͙͚̮͇̭͙̘͚̪̭͓͚̬̮̘͙͚̰̭̘͙͕͚̗̮͈̘͙̯͚̪̤̭̘͙̩͚̪̭͔̭̩͚̬̭͓̬͚̮̭͙͈͚̮͓͚̪̭͚̹̰̭͖̭͚̫̮͕͙͚̭͉̭͇͚̬̮͕͚̬̭͓͚̫̰̭͉̭͙̥͚̩̮͉̭͙̖͚̬̭͑͒̒͒̒̏͊͊̒̒́̓͂͆͑̒͆͒́͒́͐͒̒̓̓̒͂͒́͒͐̒̒̏͊̓̒̒̓͒̓̓́̏̒͆͐̓̒̏͊̒̔͘̕̕͏̭͔͚͚̭̒́͏̵̡͙͚̮͙͚̩̮͕͚̬̭̘͙͚͖̭͔̘͚̬̮̓́͂͑̓͆̓̓̒͆͌͑͂̒͐́͏̭͙͕͚̫̗̮͓̤͚̩̗̭͓͙̗͚̩̭͈̭͖͚̹̭͍͓͙͚̺̭͍̘͖͚̬̭̭͍͚̪͚̭͎̘͙͚̮͇̭͙͚̺͚̮͒̒͌͊̒͊͊̒͂͌̒͂̓͌͘ͅ͏̸̸̴̴̨̨̨̨̨̨͙̲͚̬̮͖̘͚̤̭͙͕͚̫̮͍̭͙̯͚̪̰̭͖̘͙̩͚̩͎̭͔̭̩͚̭͓̬͚̮̘͙͈͚̮͓͙͚̪̮͔͙͚̹̤̭͙͚̮͖͓͙͚̩̮͕͓͇͚̫̮͙͚̹̭͓͙̱͚̫̭͉̭͙͚̩̮͉̭̗͚̬̮͚̭͓͚̭̘͙͚̪͚̭͉̘̤͚̫̮͙͚̪͖̭͔̘͚̮̓͆̒̒́͑̓̒́̓̒͂̓͒́͒͐̏̓͐̓́̓̒͊͐̓͌̏͊͆̒͊̓̒́̏͒̒͑́͂͌͆̒͑̓͑̒̏́͒͘ͅ͏̘͙͙͚̪͖̭͚̩̗̭̘͙͚̩͖̭͈͓͙͚̩̰̭͕͓͙͚̺̭̘͖͚̫̭̭͍͚̬̭͎̘͚̩͖̮͇̭͙͚̩̮͐̓̒̏͋͒̐͊͊̒͒͌̒͂̒̑͋͆͘͏̴̴̴̴̡̨͚̬̮͖̭͙͎͚̤̭̭͙͚̗̭͓͙̯͚͖̮͍͙̬͚̩͎̭͔̭̩͚̭͓͙͚̫͚̮̭͙͈͚̩̭͎͚̪̭͎͓͙͚̹̰̭͓͚̫̭͉̭͙͚̮͓͇͚̬̮͔͕͚̭͓̗͚̹̭͉̘͙͚̬̭͇̘͈͚̬̮͍̭͚̭͔͚̫̭͈͙͚̪͚̮͖̤͚̫̤̭̘͙͚̩͎̭͔̘͙̥͚̪̮̓̒͌͆́͑͂́͐͂̓̒́͆̓͊͒͒̓̒̏͐̒͐͒̓͂̏͐̒͆̓̒͂͊͊̒̓̒̒́̏̓̒͆̓̓͆̓̒͌͑͘͏̸̸̷̨̨̧̨̭͙͚̮͓͚̩̗̮͕̭͙͚̩̭͇̭͖͚̹̮͙͚̹͖̭͉̘͓͚̫̮͎̘͙͔͚̪̤̭͎̘͙̮͚̮͇̭͙͚̺͚̭͓͚̬̮̭͙̩͚̤̭͔͓͙͕͚̗̮͎̭͙̯͚̪̭͕̘͙̩͚̪͖̭͔̭̩͚̬͚̭͓͙͚̬̤̮̘͙͚̭͙͚̪̭͎͓̙͚̹̰̭͖̘͙͚̫̮͕̘͙͚͚̮͓͇͚̫̮͕͚̹͖̭͓͙͚̫̭͉̭͙͚̮͉̭͙͚̬̭̐́͒̒̋̏͊̒͊͒̓̒͊́̓͌͑̒͐͆͒́́̒̓͊͒͗́͒͒̓̓̏̒͒̓́͑̒̏͐̓̒͊͆́̏͘͏̴̭͙̬͚̭͓̘͙̥͚̭͉͓͙͚̪̗̮͖̤͚̫̭̘͙͚̹̰̭͔̘̘͚̪̮́̏́͂͆̓̒͂͌͑̒͏̸̢̢̨̘͙͓͚̫̗̭͙͖͚̩̗̭̘͚̩̭͈̭͙͚̩̰̭͕͙͚̹̭̘͓͚̬̤̭̭͍͚̩͎̭͎̘͙͚̮͇̭͙͈͚̩̭͓̣͚̬̭͈̘͙̥͚̤̭͔̭͙͕͚̗̭͕̘͙̯͚̪̭̘͙̩͚̩̭͇̩͚̬̗̭͓̹͚̮̭͙͚̺̮͓͙̱͚̪̭͍̘͚̹̰̭͐̓͋̒͊̓͊͋̒͌̒̈́́̓͆͑̒͆́́͑͂̓̒̓̒͂͒̑̏͐̏̒͘͘͏͚̫̭͈͓͙͚̮̓̒͐͒̓͂̏͏̴̸̸̢̨͓͇͚̫̭͍̘͙͚̫̭͓͙̱͚̹̭͉̭͙͚̮͉̭͚̬̮͍̭͙̰͚̭̘͚̫̭͍͙͚̭̭̤͚̬͖̮͈͚͚̭͔̘̘͚̗̮̒̏͌͊͂̏̒̏́̏͒̒͆̓̓͆͂͑̒͑̓̒͂̒͂͏̸̢̨̘͙͚̭͙͚̩̗̭͇̭̲͚̩̭͎͓͙͚̹̭͖̘͙͚̹͖̮͔͓͚̫̮͎̘͙͔͚̭͎̘͙͚̩̮͇̘͙͚̩̮̐́͐̓͐̒͊͊̓̒́͒̏̓͆͘ͅ͏̸͚̬̮͖̭͚̤̭͓̭͙͕͚̫̭͕̭͙̯͚̪̭̓̒͆̒͑́͂͘͏̸̴̴̡̨̘͙̬͚̩̭͔̭̩͚͚̭͓̫͚̮̘͙͚̩̭͙̦͚̪̭͙͓͚̹̤̭͕͚̫̮͔͙͚̭͉̭͚̫̭͓͙͚̭͓͙͚̫͖̭͉̭͙̪͚̮͉̭͙̖͚̬̭͂̒́̓̒͂͒͗͒̓̏͊̓̓̒͐͒̓̓́̏̒͊̓͒͌͂͊͂̏͏̴̨̘͙͚̭͓͓͙̥͚̮͙͚̪͚̭̘̤͚̫̤̭͈̘͙͚̭͔̘͓͚̩̤̮́̏́͂͒̓͆͌̒͑́̒͏̸̢̘͙͚̮͓͚̩̗̭͙͚̩̭͎̭͙͚̹̮͕͙͚̹͖̭̭͖͚̫͎̮͎̘͙͔͚̪͎̭͎̘͙͚̮͇̘͙͉͚̩̮͒́͒̒̔͋̓͊͊͊̓͒̒͂̓͆͘ͅ͏̸̴̴̴̨̨̨̨̨͙̺͚̬̭͈̭͚̰̭͓͓͙͚̫̭͖̘͙̯͚͖̮͎͙̩͚̩̰̮̘͙̤͚̭͓͙͇͚̮̭͙͕͚̩̮͓͙͚̪̭͎͚̹̰̭͓͙͚̮̭͙͚͚̭͉̭͇͚̫͎̭͍̘͙͚̺͎̭͓͙͚̫̰̭͉̭͙̤͚̩̭͇̘͙̖͚̬̭̓͆̒͑́͂͂̓͒́͆̓͂͒͐̏̓̒͐́͐̓͂̒͌͊̕͏̵̸̡̨̘͚͚̭͔͓͙͚̭͉͙͚̭͉̘͚̫̬̭͈̘͈͚̭͔̘͙͚̮̒͐́́͂̓͆͂̒̒́͒͂͂͏̸̨̭͙͚̫̗̭͙͚̩̗̭̘͙͚̩̭͈̘͙͚̩̰̭͉̘͙͚̺͖̭͉̘͓͚̬̮͓͍͚̗̭͎̘͙̯͚̮͇̭͙͚̩̭͓̥͚̬̮͖̭̖͚̰̭͚̗̭̓͐̓͐͋͒͊̐̒͑̒͂͂͆͑̒͆̒́͑̓̒̑́͘̕͏̸͙̯͚͖̭̘͙̬͚̩̬̭͔̭̩͚̭͓̮͚̫̮̘͙͚̭͙̩͚̪̭͎͙̓͂͑̒́̓̒͊͒͗́͒͒̓̏̓͏̷̵̨̧̨͚̹̰̭͕͓͚̭͎̘͙͚͚̮͓͓͇͚̫͚̮͔͙͚̫̭͓͙͚̫̰̭͉̘͙͚̮͉̭͚̬̮͉̭͚͚̭͔̘͙͚̫̮̭͙͚̪̗̮͓̤͚̬̭̘͈͚̭͔̘̘͚̬̮̒̓́̓͂̒̓͌͒͊́̏̒͋̒͐́̓͒͆̓̒͊͌̒́͆̒́͏̸̵̸̴̸̸̴̵̨̨̨̡̨̨̡̭͙͚̫̗̮͓̹͚̩̗̭͇̭͙͚̩̭͎̭͙͚̹̮̘͙͚̹̭͍̘͖͚̬̰̮͎̘͙͔͚̩̭͎̘͙͚̮͇̭͙̗͚͎̭͓͙̪͚̬̮̘͙͚̤̭͚̫̭͙̯͚̪̰̭͕̘͙̬͚̩̭͔̭̩͚̬͎̭͓̩͚͎̮̘͙͙͚̩̭͙̰͚̪̭͙͚̹̰̭͖͙͚̭͍͙͚͚̭͖̘͇͚̬̬̮͕͚̺͚̭͓̗͚̹̭͉̘͙͚̬̮͉̭͙͚̬̮͉̘͙͚͚̭͓͙͚̫̭͉̘͙͚̪̗̮͖͚̫̰̭͈̘͙͚̭͔̘͓͚̪͚̮̓͒̒͒͊̐͊͑͒̒͂͂̓́͑͆͒́͑̓̒͌͐̓̒̓̒͂͒͒̓̏͊̓̓́̓̓́̒͐̓̒͊̒͌́͑̓͆̓̒͑́͆̒͘͏̭͙͏̢̢͚̫̗̭͙͍͚̩̗̭̭͚̩̭͈̭͙͚̹̭͇̘͙͚̫̤̭͈̘͓͚̫͖̭͈̭͍͚̪̤̭͎̘͙͚̩̮͇̭͙͍͚̪̮͐̓͋̒͊͊̒̒͂͆͆͘͏̸͚̬̮͓͙̹͚̰̭͔̘͚̫̮͙̯͚̪̰̮͙̬͚̪̭͔̭̩͚̭͓̬͚̫̮̘͙̓̒̑͆͒́̒͌͌̓͋̓̏̒͂͒̓̒͊͒͏̴̴̵̨̨̨̨̡͚̩̮͓͙͚̪̮͔͙̰͚̹̤̭͕̘͚̮̘͙͚̩̭͍̭͚̫͖̮͔͙͚̺̭͓͙̲͚̺̭͉̭͙̪͚̩̮͉̭͙͚̬̮͙͚̭̭͙͚̮͕͙͚̩̗̮͚̬͖̭͈̘͈͚̰̭͔̘̘͚̪̮͐́̏̓̒͐́͐̓͆̒͊̓͌͒͊̏͊̓́̏͑́͂̓͆͑̓̒̒́̒͊͏̸̴̴̷̴̨̨̨̨̧̨̡̘͙͚̪͖̭͙̙͚̩̗̭̘͙͚̩̭͇͚̩̰̭͉̘͙͚̺̮͔͖͚̬̰̮͎̘͙͔͚̪̭͎̘͚̪͖̮͇̭͙͚̪̭͓͙̫͚̬̮͖̭͙͚̤̭̭͚̫̭͙̯͚̩̰̮͇͙̬͚̩̬̭͔̭̩͚̭͓͚̫͚̮̘͙͚̪̮͓̗͚̪̮͔͓͚̹̰̭͖͓͙͚̮͓͙͚͚̭͎̭͚̫̭͍̘͕͚̺̭͓͙͚̹̭͉̘͙͚̭͇̘͙͚̬̮͉͓͚̭͙̥͚̫̭͍̘͙͚̩̭͓̭͚̬͖̮͎̭͙͚̩̭͔̘͙̥͚̪̮̒͐̓͋͊͊̓̒̏͊̓̒͂̒̑͌͆͑͆̏́͑̒̑͑̓̓̒́̓̒͂͒̓͐̒̏̒͐́͐̓͂̒͊̒͊̓͂̏̔̒͐́̏͑̓̓͆̓̒͑͊͘͏̸̴̢̘͙͈͚̮͓͚̩̗̭̭͙͚̩̭͈̘͖͚̩̰̮͕̘͙͚̫̰̭̭͓͚̫̭̭͙͔͚̪̭͎̘͙̮͚̫͚̮͇̭͙͍͚̺͚̮͂͒̒͋̏͊̒͑̒͒͌͘͏̸̴̷̡̨̨͚̬̮̭͙̩͚̰̭̘͙͚̗̭͖͙̯͚̪̤̮͍͙̬͚̩̰̮͖̘̩͚̭͓͙͇͚͎̮̘͙͚̪̭͙̺͚̪̭͎͓͙̬͚̹̤̭͕͓͚̫̮̘͙͚͚̭͇̭͇͚̫̭͓͕͚̺̭͓͙͚̭͉̭͙͚̮͉̭͙̤͚̬̭̓̒͆͒́͑͂́̓̓̒́̓́͒̒͒̓̏̒̓͒͐̓́̒͊͒̒̏͊́͂́̏͏̸̭͙͚͚̭͚̫̮͓͙͚̪̮͕̤͚̬̭͈̘͙͚̰̭͔̘̘͚̬̮́͒̓̒͆̓̓͆̓̓̒̏͑́̒̏͏̸̘͙͖͚̫̗̮͓͙͚̩̗̭̭͙̗͚̩͖̭͎̘͚̩̰̮͓͓͙͚̫̰̮͖͚̫̗̭̭͙͔͚̭͎̘͚̮͇̭͙͈͚̩̮͒̑͋̒̏͐̓̒͌͂̒̑͂̓͆͘͏̴̨͙͚̬̭͈̭͙͚̰̭͓͚̗̮͕͓͙̯͚̪̭͕̘͙̩͚̩̭͇͙̤͚̪̤̭͓̫͚̮̘͙͖͚̺̮͓̗͚̪̭͓͙͚̹̤̭̓́͆̒́͒̒̑́̓̓̒́̓͒̏͐̒̏͊͗͏̴̨̨̨̡̘͚̮͕͓͙͚̮͓͇͚̫͖̮͔͕͚̹̭͓͚̹̭͉̘͙̦͚̭͇̘͙͚̬̮͍̭͙̰͚̭͓͓͚̮͔͓͙͚̪̗̮͚̫̬̭̘͈͚̭͔̘̘͚̩̤̮̒̓́̓͂̏͑̒̓̒͊͊̒̔́̏͆́̏̒͑́͂͆͒̓̒͌̒͂̒͏̸̢̨̨̧̨̭͙͖͚̪͖̭͙͚̩̗̭͇̭͚̩͖̭͈͓͙͚̹̭͕͙͚̹̭͍̘͖͚̬̭͈̭͙͔͚̬̤̭͎̘͙͚̮͇̭͙͉͚̺͚̭͓̥͚̬̮͖̘͚̤̭͓̘͙͚̗̮͉̭͙̯͚̪̮͙̬͚̩̰̮̘͙̤͚̬̭͓̫͚͎̮̭͙͔͚̺̭͙̬͚̪̭͎̭͚̹̤̭͖͚̫̭͇͓͙͚͚̮͓͚̫̮͔͕͚̭͓̗͚̭͉̭͙͚̮͉̭̙͚̬̭͐̓͌̒̈́͊̓͊̒͂̓͑̒͆̒̒́͂́͋̓͒̏̓̒́͒̏͒̓̏̒̓̒͐͒̓́͑̒͊̓̒́͂͊̒́͂́̏̒͘̕ͅ͏̴̘̙͚͚̭͔͓͚̫̭̭͙͚̪͖̭̘̤͚̬̗̭͈̘͙͚̭͔̘͓͚̩̮̒́̒͆̓͋͆͌̒͑́͊̒͏̸̸̸̨̨̡̨̘͙͚̪͖̭̭͚̩̗̮͕̭͙͖͚̩̭͎͓͖͚̹̮̭͙͚̹̭̘͓͚̬̭̭͙͔͚̪̭͎̘͙̮͚̫͚̮͇̭͙͚͎̭͓̗͚̬̮̭͚̤̭̘͚̗̮͖͓͙̯͚̪̤̮͍͙̩͚̩̭͇͙̤͚̭͓̫͚̪̮̘͙͚̮͓͙̦͚̪̭͎͓̙͚̹̰̭͙͚̮͕͙͚̮͔͓͚̫͚̭͍̘͙͚̫̭͓͚̺͎̭͉̭͙̤͚̭͇̘͙͚̬̮͉̭̙͚͚̭͓̘͚̭̘͙͚̮͓͚̬͖̮͙͚̪̭͔̘͙͚̩̮̐͐̓̒͊̒͊͒͊͌̒͂͌͆́͑̒͆͒̒̒́͒̒̑́̓̓́͂̓̒͆͒̑́͒͐̏̒͐̓́̓̓͂̏̒͊͌͂͊̒̔́̏̒́̒͆́͂͌͆͂̓̒͑̓͑͊͊͘̕̕͏̨̨̭͙͚̫̗̭͚̩̗̮͕̭̦͚̩̭͈̘͚̩̰̭̭͙͚̹̮͖͚̫̭͈̭͙͔͚̭͎̘͙͚̮͇̘͙͚͎̮͗͐̓̒̒͊̒̏͋͒͒̓̒̓́̏̓͂̏́͘͏͚̬̮͖̘͙͚̰̭͔͓͚̗̭̘͙̯͚̭̓̒͆͆̓́̒͌́͒͂͊͏̘͙̬͚̩͎̭͇͙̤͚̬̭͓͚̬̤̮̘͙͚̺̭͙͚̪̭͎͙̓͒̓̒͂͒̓̏͒̓̈́̏̓͏̸̷̴̵̴̨̨͚̹̰̭͕͓͚̮͖̭͙͚̗̮͓͇͚̬̭͓͕͚̭͓͙͚̗̭͉̘͙̥͚̭͇̘͙͚̬̮͉̘͙͚͚̭͙͚̫̭̘͙͚̩̮̤͚̬̭͈̘͙͚̹̰̭͔̘̘͚̪̮̒͐́̓́͑̒͆͒̒͂͊͂́̏͂́͒̓̓͑͆̓͐̓̒͒͑̒͏̘͙͚̪͖̭͙͚̩̗̭͇̘̦͚̩͖̭͇̭͚̩̰̮͑͐̓̔̒̒̏͏̭͙͚̹̮͖͚̫͎̭̭͙͔͚̭͎̘͙͚̩͖̮͇̭͙̘͚͎̮͒͑̓̒͌͂͒̓́͘͏̴̙͚̬̮̭͚̰̭͙͚̗̮͉͙̯͚̩̰̭̘͙̩͚̩̭͇̩͚̭͓̩͚̬̤̮̘͙͚̪̮͓͚̪̭͙͓͚̹̰̭̓̒͆͒̒̒́͒̓͂́̓͐͆̓̒́̓̓̒͒̑͐̒͒̏͊̓͏̴̨̨̭͙͚̫̮͓͙͚͚̭͖̘͇͚̬̬̭͍̘͕͚̺͚̭͓͙̱͚̺̭͉̭͙͚̬̮͉̭̗͚̬̭͒̓̓́̒̒͊̓̈́̒͏̵̸̸̡̭͚͚̭͙͚̮͕̭͙͚̩̭̭͚̫̮͈͚̹̭͔̘͓͚̫̰̮̒͐́͑̓́͂͆̓͒̒͑̓̒̒͏̭͙͚̫̗̭͙͍͚̩̗̭̭͙̗͚̩̭͇̭͚̹̮̘͙͚̺̭͉̘͖͚̫͚̭͈̭͍͚̩͖̭͎̘͙͚̪̮͇̭͙͚̺͚̮͗͐̓͋͊̒̏͊͑͊̒̒͆̔͘ͅ͏̓̒͏̸̴̸̨͚̬̮͖̭͙̩͚̤̭͔̭͚̫̭͖͓͙̯͚̮͎͙̩͚̩̰̮͖̘̩͚̩̭͓͙͇͚̪͖̮̘͙͕͚̪̮͓͙͚̪̮͔͚̹̤̭͆́̒͌͂͊̓̒̓͒͐̏̓̒̕͏̸̴̴̴̴̨̡͙͚̫̭͍͙͚̩̮͓͚̫̭͍̘͙͚̺̭͓͙̲͚̫̭͉̭͙̣͚̬̮͉̭͙͚̬̮͙͚̭̘͚̮͖͓͙͚̩̭̭͚̫̮͎̭͈͚̪̭͔̘͚̗̮̓͒̓̓͑̒͊͒͌͒͊̏͌͊̓́̏͑̒͑́͂͆̓͒̒̒͆̒̏͂͏̸̭͙͓͚̫̗̮͓͙͉͚̩̗̮͕̭͚̩͖̭͇͓͖͚̩̰̮͓͙͚̺̮͖͚̬̤̮͎̘͙͔͚̪̤̭͎̘͙͚̮͇̘͙͚̺͚̮͒̒̈́̒͒͊͑̓̒̈́́̔͘͏͙͚̬̮͖̘͙͚̤̭͔̘͚̗̭͓͙̯͚̪̭͖̘͙̬͚̩̬̮͖̘̩͚̭͓̬͚͎̮̭͙͖͚̭͙͚̪̭͎͚̹̤̭̓̈́͆͊́̒͌́͐͂̒́͆̓̒́͒́͒͒̓͐̏̓̒̕͏̴̨̨̭͚̭͇͓͙͚̗̭͎̭͇͚̬̭͍̘͕͚̺͎̭͓̗͚̬̭͉̘͙̥͚̬̮͉̭͙͚̬̮͉͓͙͚͚̭̒̓́̓́̒͆̒͊̒̏́͂́͏̡͚̫̭͙͚̩̗̮͔͚̫̤̭͈̘͙͚̹̭͔̘͖͚̮̓̒͆̓͌̓͆̓̒͑͆̒́͂͏̸̸̸̸̨̨̡̭͙͚̮͓̩͚̩̗̭͇̘̲͚̩͖̭͇͙͚̩̰̮͕̘͙͚̹̭̭͓͚̫̭͈̭͙͔͚̪͚̭͎̘͙̮͚̮͇̘͙͚̩̭͓͚̬̮̭͙͚̰̭̘͙͕͚̫̭̘͙̯͚̪̤̮͇͙̩͚̪̮͖̘͙̤͚̪̭͓̮͚̮̭͙͔͚̭͙̹͚̪̭͎͚̹̤̭̭͚̫̮͕͙͚͚̭̘͚̬̰̮͔͙͚̬̗̭͓̗͚̬͖̭͉̭͙̦͚̮͉̭͙̱͚̬̮͉͓͙͚̭͓͙̥͚̭͈̘͙͚̭̘͚̫̭̘͈͚̭͔̘̘͚̫̰̮̐́͒̒̒̓̐͒͒̒̏́̏͆͑̒̐͆͒̏́͑͒̓̏̓̓̒͂͒́͒͒̓̏̓̒͐̒͐͒̓̓́͐̒͊̓͌͊̒͂̏́̏͒́͂͆͂͂͋̒͂͌̒́͂̒͘͘͏̭͙͙͚̫̗̭͙̙͚̩̗̮͕̭͙͚̩̭͈̭͚̹̭͍͓͙͚̹͖̭̘͓͚̬̬̮͎̘͍͚̪̭͎̘͙͚̬̤̮͇̘͙͚̺͚̮͐̓͒͊̒̏͊͌̒̒͂̈́̋͘͏̴̴͚̬̭͈̭͙̩͚̤̭͔̭͚̗̮͕͓͙̯͚͖̮͎͙̩͚̩̬̮̘̩͚̬̭͓̮͚̮̭͙͙͚̪̮͓͙͚̪̭͚̹̰̭̓̒̏͆́̒̑́͂̓͒̒͊̓̒͂̓͒͐̏͊̓̒̑͏̴̴̨͚̫̭͍͓͙͚̭͖̘͇͚̫̮͕͚̹̭͓͙̤͚̫̭͉̘͙̦͚̬̭͇̘͙̳͚̬̭̓̒̓͒̓͂̏̒͊͐̓̒͊͆͏̡̘͔͚̭͓̭͚̫̭̭͙͚̭͍̘͚̫̬̭̘͙͚̩̭͔̘͚̮̒́̏̒͑̓͋͆͂͂̒͌͑͒̒̏́͂͏̸̴̸̴̵̴̧̨̨̡̘͙͚̭͚̩̗̭͇̘͙͚̩͖̭͇͓͚̩̰̮͓͙͚̫̰̭̘͖͚̬̮͎̘͙͔͚̫̭͎̘͙͚̮͇̭͙͇͚̺͚̭͓͚̬̮͖̭͚̰̭̘͚̗̮͕͙̯͚̩̰̭̘͙̬͚̩͎̮͖̘͙̤͚̬̭͓͚̫̮̭͙͚̭͙͚̪̭͎̭͙͚̹̤̭͕̭͚̫̭͈͓͙͚͚̭͈̭͚̫̭͓͕͚̺̭͓͙͚̗̭͉̭͙̪͚̩̭͇̘͙͚̬̮͉̘͚̭͔͓͙͚̫̭͍̭͙͚̪͚̭̘͚̫̮͎̭͙͚̭͔̘͖͚̩̮͗́͐̓̒͂͊̒̏͒͌̒̓͂̓͑̒͂͆̒̒́͑̒̑́̓͒͒̓̒͂͊͒͐́͒͒̓̏̒͐͒̓́̒͊͒͒̒͊͊͂́̒́̏̓͆͌̒͑͂͒̒͊͘̕ͅ͏̴̸̸̴̨̨̨̨̘͙͓͚̪͖̭͙͖͚̩̗̭̭͙͖͚̩̭͍͓͚̹̮͖͓͙͚̫̤̭͓̭͖͚̬̭̭͙͔͚̪̤̭͎̘͚̫͚̮͇̘͙͚̪̭͓͙͚̬̭͈̭͚̤̭̘͚̗̭͔̘͙̯͚̪̭͕̘͙̩͚̩̤̮͖̘͙̤͚̭͓̫͚̮̘͙͚̮͓͙͚̪̮͔͓͙͓͚̹̤̭͙͚̮͙͚͚̮͖͓͚̫̮͔͕͚̬̭͓͙̱͚̬͖̭͉̘͙͚̬̭͇̘͙̖͚̬̭͐̓͋͊̒̏͊̒͂͌̒̑̏͆͑͆̒͑́͒̒̑́͂́͂̓̒͂̓͒̑́͒͐̏͐̓́͐̓̓͂̒͊̓̒͊͆͘͏̡̨̘͙̬͚͚̭͓̭͚̭͎͙͚̪͚̭͓̭͚̫̭͈̘͈͚̩̭͔̘͖͚̗̮́̒͑́͂̓͆̒̒͆̒͂͏̭͙͏̴̸̸̷̢̢̧̡̨͚̫̗̭̤͚̩̗̭̺͚̩̭͈̭͙͚̹̮͖̭͙͚̹̮͖͓͚̫͎̭̭͍͚͖̭͎̘͙̮͚̫͚̮͇̭͙̖͚̪̭͓͙͚̬̮͖̘͙̥͚̰̭͔̘͙͕͚̗̭̘͙̯͚̪̤̭̘͙̬͚̩̮͖̘͙̤͚̪͎̭͓̫͚̮̭͙͔͚̩̭͙̱͚̪̭͎͔͚̹̤̭̭͙͚̫̮͉͙͚͚̭͇̭͇͚̬̭͍̘͙͚̫̭͓͙͚̫͖̭͉̘͙͚̭͇̘͙͚̬̮͉̘͚͚̭͐̓̒͋̓̒͊͊͒̓̒͌̒͂͆͑͆́́͒͑͆̓̒͂̓͒͒̓̏̓̒͐͒̓̓͂̒͆͌͊́̏̒͐́͘͏̸̴̡͚̫̮͙͚̪̭͉̘͚̫̮͎̭͙͚̪͚̭͔̘͚̪̮̓̒͆̓͐̓͆̓̒͑̒̏͏̴̭͙͚̫̗̮͓͚̩̗̭͓͙͎͚̩͖̭͈̘͙͚̹̭̘͙͚̹̭͍̘͖͚̬̭͈̭͙͔͚̪̭͎̘͙̮͚̬̤̮͇̘͙͇͚̪̮͗͒̒̈́͌̐͊͋̓̒͆͆͘͏̵̨͚̬̮̭͉͚̤̭͓̭͚̗̮͎͙̯͚̪̤̭͕̘͙̬͚̩̮͖̘͙̤͚̩̭͓͙͇͚̫͚̮̘͙͙͚̺̭͙͚̪̭͚̹̤̭̓̒̒͆͒̒́̒̑́̓͊̓͒̏͒̓̏͊̓̒̑͏̴̴̴̸̨̡͚̫̮͔͓͙͚̩̭͍̭͚̫̭͓͕͚̫̭͓͙̲͚̫̰̭͉̭͙͚̭͇̘͙̪͚̬̮͉̭͙͚͚̭͙̥͚̫̭͓͙͚̮͔͚̫̰̭͈̘͙͚̭͔̘͓͚̪̮̓̒͐͒̓̒͊͊͒̒͊́͂̏́͑̓̓͊͆͂͂̓̒͑͂̒͊͏̸̸̴̴̢̨̨̨̭͙͖͚̮͓̯͚̩̗̭͓͍͚̩̭͇̘͚̹̭͇̘͙͚̹̭͈̘͖͚̬̭̭͍͚̪͎̭͎̘͚͎̮͇̭͙͚̪̭͓͙͚̬̮͖̭͙͚̤̭͓͓͚̫̮͙̯͚̭͕̘͙̩͚̩̮͖̘͙̤͚̬̭͓̬͚̮̘͙͚̮͓͙̰͚̪̭͎͓͚̹̰̭͔̘͚̫̮͈͓͙͚̩̭̭͇͚̬̮͕͚̫̭͓͚̹̭͉̭͙̤͚̭͇̘͙̳͚̬̮͍̭͙̬͚͚̭͔͚̭͓͙͚̩̭͓̭̤͚̫̮͙͚̩̤̭͔̘͚̪̮́͒̒͌̒͊̒̏͊͒̒͆͌̒̒̒́͌͆͑͆̓́̒̑͌̓͂͊͂̓̒͂͒͒́͒͐̏̒̑̒̓͒̓͆͌̒͆͐̓̒͆͊̒̔͂̏́̓̒͑́͂͊͆̓̒͑̓͑̒̏͊͘͏̸̴̨̨̨̨̨̘͙͚̭͙͚̩̗̭̘̖͚̩͖̭͇̘͚̩̰̭͙͚̺͖̮͕͖͚̫̮͎̘͙͔͚̪̬̭͎̘͚̪̮͇̘͙̘͚͎̭͓͚̬̮͓͍͚̰̭͓͓͙͕͚̗̮͖͙̯͚̩̰̮͎͙̬͚̩͎̮̘͙̤͚̭͓͙͇͚̫͚̮̭͙͓͚̪̮͓͚̪̭͙͓͚̹̰̭̭͙͚̮͔͓͙͚̭͇̭͇͚̬̰̮͙͚̬͚̭͓̗͚̺̭͉̘͙͚̩̮͉̭͙͚̬̮͉͓͚͚̭̒́͐̓̐͋̒̒̏͊̓̓̒̏̒̑͆́͑̒͆͆͒̒́́̓̓͒́͊̓͒͐̒̋̏͊̓͐́̓͂̏̒͐̓͌͊̒̓̈́̒͌́͘͏̸͙̥͚̫̭͉̘͙͚̮̤͚̫̰̭̘͙͚͎̭͔̘͓͚̫̮̓̓͆͂͐̓̒͌͑͂̒͆͏̭͙͚̫̗̭͙̙͚̩̗̭͇̭͙͚̩̭͈̭͖͚̹̭̓͐̓͒͊̒͊͏̸̨͙͚̫̰̮͓͚̫̗̭̭͍͚͖̭͎̘͙̮͚̮͇̭͙͚̺͚̭͓͈͚̬̮̭͚̤̭͓͓͚̗̮͔̭͙̯͚̪̭̓͒̓̒͌̒́́͋͑̒͆͒̒͑́̒͌́͘͏̨̘͙̩͚̪͚̭͇͙̤͚̪̤̭͓̩͚̮̭͙͚̭͙͚̪̭͙̓̓̒͂͒̒́͒͒̓̈́̏͊̓͏̴̷̴̵̴̡̨̡͚̹̤̭͕̘͚̫̭͎͙͚̩̮͕͓͇͚̫̭͓͕͚̫͎̭͓͙͚̬̭͉̭͙͚̬̮͉̭͙͚͚̬̮͍̭͚̭͓͓͙͚̭̘͙͚̭̭͚̫̮͎̭͙͚̹̭͔̘͕͚̩̮̒͐͒̓̓̒̏͒̒͊̏̒̑́̏́͂͊͆͂͂͑̒͑͊̒͊͏̘͙͏̸̸̴̡͚̭͚̩̗̭̭͚̩̭͈̘͚̹̮͓͙͚̹̭͈̘͖͚̫̭͈̭͍͚̩̗̭͎̘͚͎̮͇̘͙͚̺͚̭͓͙̣͚̬̭͈̭͙͚̤̭̭͙͕͚̫̮͓͙̯͚͖̮͙̩͚̩͎̮̘͙̤͚̩͚̭͓͙͚̪̮̭͙͚͚̪̮͓͚̪̭͓͚̹̰̭͂͐̓̒͋̒̋͊̒̏͊͒͊̒͊̒̒̒͂̋͑͆̒́͑͊͂͋̓͒̓͊͆͒͐̒̋̏͊̒͘͘͏̸̨̢̨̭͚̮͙͚͚̮͓͇͚̫̗̭͍̘͕͚̫̭͓͙̱͚̬͖̭͉̭͙͚̮͉̭͚̬̮͉͓̙͚̭͔͙̥͚̫̭͈̘͙͚̮͕̤͚̫̤̮͈͚̩̤̭͔̘͚̫̮̒͐́͑̓̓͂͐̒̒̏͊́̏̒͊̒́̏̓̓͆͂̓̒͑̓̒̒̏͆͏̸̴̭͙͓͚̭͙͚̩̗̭̲͚̩͖̭͈̭͖͚̹̭͕̭͙͚̹̭͍̘͓͚̬̭̭͙͔͚̫͖̭͎̘͚̬̤̮͇̭͙͈͚͎̮͂͐̓͑͋̓̒̒͊͊̒͌̒̑́͘͏̸͙̳͚̬̮͖̭͙͚̰̭͓͙͕͚̗̮͉͙̯͚̪̮͖͓͙̬͚̩̭͇̩͚͎̭͓̫͚̪͖̮̭͙͕͚̺̭͙̮͚̪̭͎̭̙͚̹̤̭͖͓͚̫̭͈̭͙͚̮̓͆̓́͑́̓͂̓̒́̓̒͒̏͒̓̏̒̒͐͒̓́̏͏̴̵̴̨̡͓͚̫̗̭͍̘͙͚̬͚̭͓͙͚̭͉̭͙̪͚̮͉̭͚̬̮͉̭͚͚̭͓̭͙͚̫̭͍̘͙͚̮͔͚̬̮͙͚̪̭͔̘͓͚̩̮̒͊͌͊́͂́̏̒̏̒̑́̓͆͂͂̓̒̏͑̓͑̏̒͏̸̸̭͙͚͚̮͓͙͚̩̗̮͕̭͙͚̩̭͍̘͙͚̹̮͓͙͚̫̤̭̘͓͚̫̗̮͎̘͙͔͚̪̭͎̘͚̮͇̭͙̙͚͎̮͂͒̔͊͊̐͊͒͊̒͆̒̑́́͘͏̸͙̣͚̬̮̘͙͚̰̭͔͓͚̫̭͖͓͙̯͚̪̤̮͈͙̩͚̩̰̭͇͙̤͚̬̭͓͙͇͚̩̮̘͙͓͚̮͓͙͚̪̭͎͓͙͚̹̰̭̓͆͒̓́̒͌̓̓̓̓͆͒́͒͐̏͂ͅ͏̴̨̨̨̨͓͙͚̫̮͉̭͙͚̗̭͈̭͇͚̫͎̭͓͕͚̬̭͓͙͚̺̭͉̘͙͚̩̭͇̘͚̬̭͒̓́̒͒̒̓͊̓̒͗͏̵̨̨̘͚͚̭͔͙͚̭͍͓͙͚̭͉̘̤͚̬̮͎̭͙͚̩̭͔̘͙͚̪̮̒͐́̓́͂͆͂͂̒͊͑͊͏̭͙͚̫̗̭͚̩̗̮͕̭̖͚̩̭͇͓͚̹̮͕̭͙͚̹̭̭͖͚̬̭̭͍͚͚̭͎̘͙̯͚̬̤̮͇̭͙͚̪̮̐͐̓̒̒͊̒̏͊͒͑̒͆͌̒͂͆̕͘̕͏̸̴̸̴̨̢̨̖͚̬̮͚̤̭̭͚̗̭͖͙̯͚̩̰̭͕̘͙̬͚̩̭͔̭͙̤͚̩̭͓̫͚̫͚̮̘͙͚̭͙͚̪̭͎͓͙͓͚̹̤̭͓͙͚̮͓͙͚̭̭͇͚̬̮͙͚̫̭͓͙̲͚̺͎̭͉̭͙͚̬̭͇̘͓͚̬̭̓̒͆͑̓̒̋́͑̒͌́̓̏̓̒͒͗́͒͒̓̏͐́͐̓͂̏͌̒͆͐̓͌͒͊̒͏̭͚͚̭̘͙̥͚̫̭̘͙͚̮̤͚̬͚̭͈̘͈͚̪̰̭͔̘̘͚̬̮̒́͑̓͒͆͂͂͒̓̒̒̒͂͘͏̸̢̨̘͙͚̮͓̪͚̩̗̭͓͚̩̭͎̭͙͚̹̭͇͙͚̹̮͔͓͚̫̮͎̘͙͔͚̪͖̭͎̘͙͚̩̮͇̘͙͚̩̮͒͂͒̒͌̒̈́͊͊̓͒̓̒̓͆͋͆͘͏̴̸̨̨̨̡̗͚̬̮̘͙̥͚̤̭͓̭͚̗̮͕͓͙̯͚̮͖͓͙̩͚̩̭͔̭͙̤͚͎̭͓͙͇͚̫͚̮̭͙͚̺̭͙͚̪̭͎̭͙̰͚̹̰̭͕̘͙͚̫̮͖̭͙͚͚̮͓͓͚̫̭͍̘͕͚̺̭͓͚̺̭͉̭͙͚̮͉̭͖͚̬̮͉̘͙͓͚͚̭̭͙̥͚̫̭͉̘͙͚̮͚̬̮͎̭͙͚̭͔̘͖͚̬̮̓̒͆͒́̒̑́͂͊́̓͒͑̏͒̓̈́̏͒̓́̒͊͊̒͆͊̒̔͂̏̒́͑̓͆͂͂͐̓̒͊͑́̒́ͅ͏̸̭͙͓͚̮͓͉͚̩̗̭͓͙͎͚̩̭͈͙͚̹̭͙͚̹̭͈̘͖͚̬̰̮͓͍͚̗̭͎̘͚̫͚̮͇̘͙͚̩̮͂͒̒͌͊̓̐͊͐̓̓̒͑̒͂̒̑̏͆͘͏̴̸͙͚̬̮͖̭͙͚̤̭͔̭͚̗̮͖̘͙̯͚̪̰̭̘͙̩͚̩͎̮͖̘̩͚̪̭͓̫͚̮̘͙͖͚̺̭͙͚̪̭͎͓͙͚̹̤̭̓͆̏́̒͌́͐̒͒̓̒͂͒̏͒̓̒̏͗͏̴̴̸̨̨̨̡͓͙͚̭͈̭͙͚̩̭͈̭͚̫͖̮͔͙͚̫͎̭͓͙͚̬̭͉̭͙̥͚̮͉̭͙͚̬̮͍̘͚͚̭͓̘͚̭͙͚̭̭͚̬̗̭̘͈͚̹͎̭͔̘͚̫̮́̓̒͊̓͌͊̏͂̏͌̒̑́̒͑́͂͋̓͆͂͒̒͌̒̒̏͆͏̸̢̘͙͚̮͓͚̩̗̭̭̲͚̩͖̭͇͓͚̹̮͙͚̺̮͓͚̫̭̭͙͔͚͖̭͎̘͙͚̫̮͇̘͙͚̺͚̮̒͂͒̒͋̒̒̏͊͐̓͊͐̓̒͒͌͂͊̔͘ͅ͏̸̴̸̴̡̨̡͚̬̮͖̭͙͚̤̭̘͙͚̫̭̭͙̯͚̩̰̮͎͙̬͚̩̮͖̘͙̤͚͖̭͓͙͇͚̪̮̘͙͚̩̭͙͓͚̪̮͔͓͙͚̹̰̭͖̭͙͚̫̭͍͙͚͚̭͈̭͇͚̬̬̮͕͚̹̤̭͓͙̲͚̫̰̭͉̘͙͚̬̭͇̘̖͚̬̮͍̭͙͓͚̭͓̭͙̥͚̭̘͙͚̪͚̭͉̘͚̬͎̮͙͚̪͚̭͔̘͙̥͚̪͚̮̓̒͆̓́͒͂͒̓͆́̓͆͒͐͒̓̏͗͒̓̓͂̒͐̓̒͊̒́̏́͂͑͆̒͑̓͑̕͏̨̘͙͈͚̪͖̮͓͙͕͚̩̗̮͕̭̦͚̩̭͈̘͖͚̹̮͓̭͙͚̹̭͉̘͖͚̬̭̭͙͔͚̪̭͎̘͙͚̪͖̮͇̘͙̗͚̩̮͒̒͊̒͊͊̒͂͌͂͆͘͏͙͚̬̭͈̭͙̹͚̤̭͔̘͚̗̭͔͙̯͚̪̰̭͖̘͙̩͚̪̮̘̩͚̬̬̭͓̩͚̫͚̮̭͙͚͚̭͙̪͚̪̭͚̹̰̭̓͆͆́̒̑́̓͒͒̒̓̒͒́͒͒̓̏͊̓̒͌͏̸̴̷̴̴̨̨̨̡̘͙͚̮͇̘͙͚̩̮͕͓͇͚̫̮͙͚̬̭͓͙͚̭͉̭͙͚̮͉̭͙͚̬̮͚̭͔͓͙̥͚̭͈̘͙͚̪̭̘͚̬͚̮͙͚̩̭͔̘̘͚̬̮́̓̒͒͐̓͌̏͊́͂͂̏͊̓̒́̏́͂͆̓͌̒͑̓͑̒̏͘͏̸̸̴̵̢̢̨̨̘͙͓͚̪͖̭͚̩̗̮͕̭̲͚̩̭͇̭͙͚̹̭͉̭͙͚̫̤̭̘͖͚̫̭͈̭͍͚̪͖̭͎̘͙͚̮͇̘͙͚̺͚̭͓͙̹͚̬̭͈̘͉͚̰̭͓͚̫̮͈͓͙̯͚̪̤̭͖̘͙̩͚̩͎̮͖̘͙̤͚̩͚̭͓͚̩͖̮̘͙͚̩̭͖͚̪̭͎̭͚̹̰̭͖̘͚̫̭͎͙͚̮͔͓͇͚̫͚̮͕͚̺̭͓͚̹̭͉̘͙̤͚̭͇̘͙͚̬̮͍̭͚͚̭̭͙͚̫̭͓͙͚̭̘̤͚̫̬̭͈̘͙͚̪͎̭͔̘̘͚̬̮͐̓̒̒͊͊͊̒͒̒́̓͑͆̒́͑̒͌̓̒͂͒͑͒̓̒̏̒̒͐͒̓̓͂̏̒͐̓̒͊͊̒̔́̏̈́̒̑́͒̓͌͆͂͂͌̒͑̒͂͘̕ͅ͏̭͙͏̸̸̴̧̨̢͚̪͖̭͚̩̗̭͇̭͙͚̩͖̭͉͖͚̩̰̮̭͙͚̺͖̭̭͓͚̫̮͎̘͙͔͚̫͎̭͎̘͚̮͇̭͙͚̺͚̭͓͚̬̮͖̭͚̰̭͓͙͚̫̮͖̘͙̯͚̩̤̭͕̘͙̬͚̩̭͔̭̩͚̩̭͓͙͚͎̮̭͙͚͚̭͚̪̮͔͙͓͚̹̤̭͐̓̒͒̓̒͑͒̒̒̑́̏͑̒͆̒͑́͒͂͆̒̓͊͂͒́͒͒̓̒̋̏̓͘͏͚̫̮͔͓͙͚͚̮͕͓͚̬̬̭͍̘͕͚̺̭͓͚̫̭͉̭͙̥͚̭͇̘̓̒͐͒̓́̒͊̒̓͊̒̔͆͂̏̒͏̨͚̬̭͏̵̨̭͔͚̭͔͙͚̫̭͍͓͙͚̩̮̤͚̬̭͈̘͙͚̭͔̘͖͚̬̮̒́̏̓̓͆̓͑̓̒͊͑́̒́͏̸̸̸̴̘͙͚̭͙͚̩̗̭͚̩̭͍͓͚̩̰̭̭͙͚̹̭̘͖͚̬̤̮͎̘͍͚̭͎̘͚͎̮͇̘͙͚̪̭͓͙͚̬̮̭͙͚̰̭͔͓͙͕͚̫̭͕̘͙̯͚̪̰̮͖͓͙̩͚̩̮̘͙̤͚̬͖̭͓͚̮̭͙͖͚̩̮͓͙̺͚̪̮͔͚̹̤̭͕̭͚̫̮͔͙͚̭̐͂͐̓͒͋̓̒̋͊̒̏͋͊͌̒̒͂͊̒̒́̏͆͑̈́͆͒̏́͆͒̓̒͂͂͒͐̏̓̒͌̒̓͒̓̓͂̏͘͏̡̨̨̘͚̬̭͓͕͚̭͓͙̲͚̹̭͉̭͙͚̩̮͉̭͕͚̬̭̒͊͆͒̒́͂͊̓̒͏̨̨̘͚̭̘͙̥͚̭͉͙͚̪̭̭̤͚̬͎̮͎̭͙͚̹̭͔̘͙͚̩̮̒͐́̏͒́͂̓͆̓͒̒͑͊͏̭͙͚̫̗̭̤͚̩̗̭̭̦͚̩̭͈͓͚̹̮͕̭͙͚̫̰̭͈̘͓͚̬̬̮͎̘͍͚̗̭͎̘͙͚̩̮͇̭͙͚̪̮͗͐̓̒͋̒͊̒̏͊̒̒͂̓̏͆͘̕͏̸̸̴̧̨͚̬̮͖̘͙͚̤̭̘͙͚̗̮͇͙̯͚̪̤̮͖͓͙̬͚̩̭͇̩͚͚̭͓̹͚̮̘͙͚̩̭͙͚̪̭͎͓͚̹̰̭͖̭͚̮͓̘͙͚͚̮̓̒͆̏́͒͂́̓̓̒͂̓̒́͒̑͒̓̈́̏̒͐̒̓́̓͂͏̨̨͓͇͚̫͖̮͕͚̗̭͓͙̲͚̹̭͉̘͙͚̭͇̘͓͚̬̭̒͐̓̒͂͊̓͂̏̒͏̭͚̭͔̭͚̫̭̭͙͚̩̭̭̤͚̬͚̭͈̘͈͚̭͔̘̘͚̫̰̮̒́̏̒͆̓͒͆̓͑̒̒͂͒̒͘͏̵̢̢̭͙͚̪͖̮͓̹͚̩̗̭͇̭͚̩̭͎̭͙͚̹̭͙͚̹̮͖͚̬̤̭̭͙͔͚͖̭͎̘͙͚̩̮͇̘͙͚̪̭͓͙̪͚̬̮̘͙͚̰̭͓͙͕͚̗̮͓͙̯͚̭͗͒̒̒͊͊͊̓͒͐̓̒͌͂͂͆̏͆͑͆͒́͒́͐͂͊͘͏̴̴̴̸̨̨̨̡̘͙̩͚̩̬̭͔̭͙̤͚̩̭͓̫͚̮̭͙͖͚̭͙͚̪̭͚̹̤̭͓͚̫̮͓͙͚̩̭͇̭͚̫͚̮͔͙͚̺͚̭͓͙͚̬͖̭͉̭͙͚̩̮͉̭͚̬̮͉̘̙͚͚̭͓͙̥͚̮͓̘͙͚̮͓͚̫̮͙͚̪̬̭͔̘͖͚̗̮̓̒͂͒́͒͒̓́̏͊̓̒͌͐̒̓͒͐̓̒͊̓͌͊́̒̒́͑́͂͆͂͂̓̒͑̓͑̒͂̕͏̸̸̸̸̴̴̴̢̨̨̨̨̭͙͚̮͓̬͚̩̗̮͕̭͚̩̭͈̘͙͚̹̭͇͙͚̹̭͈̘͖͚̫̭̭͍͚̩͚̭͎̘͚̪̰̮͇̘͙͍͚̪̭͓̙͚̬̮͖̭͚̤̭͔͙͕͚̫̭͕͙̯͚̪̤̮͓͙̩͚̩̮͖̘̩͚̩̭͓̫͚̩͖̮̘͙͚̩̮͓͙͚̪̭͎̭͙͓͚̹̰̭͖͓͚̭͈̘͙͚̭͖̘͇͚̬̰̭͓͙͚̭͓͚̬͖̭͉̭͙͚̬̭͇̘͙̮͚̬̭͒͂͒̒̒̋͊͊̓̓̒̏͌̒̒̒͆͑̒͆̒̋́̓̓͐̒̓̒͒͒͐̏̒͐́̓́̏̒͒͌͂͊̒̔͘͏̡̘͙̬͚̭͔͓͚̭͓͙͚̪͚̭̘͚̬̭̘͙͚̪̭͔̘͚̫̰̮́̏̒͆́͂͌͆͋̒͊͌͑̏̒̏͏̘͙͚̫̗̮͓̦͚̩̗̭͇̘͚̩̭͇͖͚̩̰̭͕̘͙͚̹̮͖͖͚̬̬̮͎̘͙͔͚̭͎̘͙͚̫͚̮͇̭͙͚̪̮̒͒̒̒̈́͊̓̒͒̓̒͂͒̈́͋͆͘͏̵̸̸̨̨̨̨̧̨̡͈͚̬̮͖̭͙͚̰̭͔͙͕͚̫̮͈̘͙̯͚̩̤̭̘͙̬͚̩͎̮̘̩͚̬̭͓͙͚̪̮̭͙͚̭͓͚̪̮͔͙͚̹̰̭͖̭͙͚̭͎̭͙͚͚̭̭͚̫̮͕͚̹̤̭͓͙̲͚̹̭͉̘͙͚̭͇̘͙̖͚̬̮͉͓͙̬͚͚̭͔͚̫̭͈͓͙͚̩̗̭͉̘͚̫̤̮͈͚̪̭͔̘͖͚̬̮̓̒͆́̓͐͒̒͒̓͊͆͒̓́͒͒̓̒̏̓͗́̓͂͌̒͊͐̓̒͊͂̏́̓̒͆̓͆̒͑̓̒̒͂͏̸̸̸̘͙͈͚̮͓͉͚̩̗̭͇̘͙͚̩̭͈͓͖͚̩̰̮̭͙͚̹̮͖͚̬̮͎̘͙͔͚̪̭͎̘͙̮͚̫̮͇̘͙͚̪̭͓͂͒̒͊͊̒͒͊͑̓̒͊͆͑̒͘̕͏̸̴̨̨͚̬̮̘͙̹͚̰̭̘͙͕͚̫̮͉̭͙̯͚̭͓̘͙̬͚̩̤̮͖̘͙̤͚̩͚̭͓͙͇͚̩͖̮̭͙͖͚̺̮͓͙͚̪̭͎͓͙͚̹̤̭͕͚̫̮͓͙͚̩̭̘͇͚̫͖̮͔͕͚̹̰̭͓͚̭͉̭͙̥͚̮͉̭͙̰͚̬̭͆͒́͑͂͊̓͒̏͐̒̏̓̒͐͒͑̓͐̒̓̒͊̒̔͂͒́̏͏̡̭͚̭͓̘͙̥͚̭͎͙͚̪͖̭͉̘͚̬̮͙͚͖̭͔̘͕͚̪̮̒̑́̏́͂̓͆̒͆͑̓͑͂̒͊͏̨̭͙͙͚̫̗̭͙͖͚̩̗̭̭͍͚̩̭͈͖͚̩̰̮͓͓͙͚̹̭͉̘͓͚̬̬̮͓͍͚̪̭͎̘͙͚͎̮͇̭͙͍͚̩̮͐̓͋̒͊̓̒͒̒͑̒̈́́͆͘͏̶͙͚̬̭͈̭͉͚̤̭͓̘͙͚̗̭̓͆̒́͂́͏̴̨̨̡̨̘͙̯͚̪̤̮͓͙̩͚̩͎̮͖̘͙̤͚̪̭͓̮͚̪̰̮̘͙͈͚̮͓͙̲͚̪̭͙͓͚̹̤̭͕̘͙͚̫̭͉̭͙͚̮͓͚̬̭͍̘͕͚̹̭͓͙̤͚̬̰̭͉̘͙̪͚̮͉̭͚̬̮͍̘͚̭̘͙̥͚̮͓̘͙͚̪̮͚̫̭̘͙͚̩͎̭͔̘̘͚̩̮͐̏̓̒͒́͒͐̏͊̓͒̓͂̏͑̒͊͂̒͊́̏̒̏̒͐́̏͒́͂͆̓͒̓̒͌͑̒͊͏̴̸̴̢̨̡̨̡̭͙͚̪͖̭͙͚̩̗̭͇̭͚̩͖̭͈͓͙͚̹̮͖͙͚̫̤̭͈̘͓͚̬̬̮͓͙͔͚̭͎̘͙͚̮͇̭͙͇͚̺͚̭͓͙̹͚̬̮͖̘͙͚̤̭͓̘͙͚̗̮̭͙̯͚̪̮͍͙̬͚̩̮͖̘̩͚̬̰̭͓̫͚̮̘͙͚̭̗͚̪̭͎̭͚̹̤̭͕̭͚̫̮͔͙͚̩̭͍̭͚̬̬̮͔͙͚̫̤̭͓͚̫̭͉̭͙͚̭͇̘͖͚̬̮͉͓͚͚̭̘͚̫̮͕͓͙͚̮͚̬̮͙͚̰̭͔̘͓͚̪̮͒͐̓͌̒̈́͊̓̒͑́͆͂̓͑͆̒́͂́͊̓̒̓̒͂͒̓́͒͒̓̒̏̒̒̓͒̓̓̒͊̓͌͊̒̔̏͂̏̒̒̑́͑̒͑̓͆͂͂͒̓̒̏͑̓͑́̒͊͘̕ͅ͏̸̴̨̨̨̨̭͙͚̪͖̮͓͍͚̩̗̮͕̭̦͚̩͖̭͇̭͚̹̮̭͙͚̹͖̭̭͓͚̬̤̮͓͙͔͚̩̭͎̘͚̬̤̮͇̘͙͇͚̩̭͓͚̬̭͈̭͙͚̤̭͓̭͚̗̭͔̘͙̯͚̪̮͓͙̩͚̩̰̭͇̩͚̫̭͓̹͚͎̮̘͙͓͚̺̭͚̪̮͔͓͚̹̤̭͚̫̭͈̭͙͚͚̭͖̘͇͚̬̮͔͕͚̫̭͓͙͚̫̭͉̭͙͚̭͇̘̙͚̬̭̑͒̒̒̒̏͊͒͑̒͑̓̒̒͆͑̒̓͆̏́̒̑́͂͐̓̒̓̒͂͒̏͒̓̒̓̏̒͐͐̓̒̓͒̓͂̒̓̒͊͆͂̏̒͘͏̨̘͚͚̭͓̭͚̭͎͓͙͚̮͓̤͚̬͎̮͎̭͙͚̹͎̭͔̘͙͚̩̤̮̒́̒͑́͂͆͂͂̓̒͑̕͏̸̸̴̨̨̨̘͙͕͚̭͚̩̗̭̭͙͚̩̭͈͙͚̹̮̭͙͚̹̮͓͓͚̬̮͎̘͍͚̪̭͎̘͙̯͚̮͇̭͙͚̪̭͓͚̬̮͖̘͚̤̭̘͙͕͚̗̮̭͙̯͚̮͓͙̬͚̩͎̮̘͙̤͚̪̭͓̫͚̮̭͙͓͚̩̭͙͚̪̮͔͓͙̰͚̹̰̭́͐̓̒͋̏͊̓̐͊͒͒̓̒̒͒́̓̔͆͑̒͂͆̒͑́͑́͌͂͊͐͒̏̓̒͂͒͒̓̏͘͏̵̴̨̨̨̨̭͙͚̭͓͙͚͚̭͈̭͇͚̫͚̭͓͙͚̫͎̭͓͙̤͚̹̭͉̘͙͚̭͇̘͚̬̮͉̭͚̭͓̭͙͚̫̮͙͚̮͔̤͚̫̮͈͚̪̭͔̘̘͚̮́͋̓͂̒͒͌͊̓́̏̒̏̒͐́̏̓͒̓͆͂͂̓̒͑̓̒͂̒͂͒͏̸̢̭͙͚̭͙͈͚̩̗̭͇̘͙͚̩͖̭͇̘͙͚̹̭͎͙͚̺̭̭͓͚̬̤̮͓͙͔͚̪͖̭͎̘͙̮͚̮͇̭͙͇͚̩̮̓͂͐̓͊͊̓͊͒̒͑́̓͆͘͏͚̬̮̘͚̰̭̓̒͊͆͒̒̒́͏̴̸̸̨̡͙͕͚̗̮͇͙̯͚̪̤̮͍͙̩͚̩̮͖̘̩͚̭͓̬͚̮̭͙͈͚̭͙̺͚̪̭͚̹̤̭͚̫̭͓͙͚͚̭͇̭͚̫̮͙͚̹̭͓̗͚̬̰̭͉̭͙͚̮͉̭͙͚̬̮͉̘͙͓͚̭͚̫̭͓͙͚̪̗̮͖͚̬̮͎̭͈͚̹͎̭͔̘͓͚̗̮̓́̓̓̒́̓̓̒͂͒́͒͒̓̏͊̓̒̑͐̓̒̓͒͋̓́̒͊̏͐̓͌͊̒̈́͂̏͌́̏͑̓̒͑̓͊͆̓̒̓̒̒͂͏̸̢̘͙͚̮͓̣͚̩̗̭̘͚̩̭͇̘͚̹̭͓͓͙͚̹̮͖͓͚̫̮͓͍͚̗̭͎̘͙͚͎̮͇̭͙͚̺͚̮̒͂͒̒͋̒͊̒̏͊͒̓̒͒͑̒͂̈́͂̓͘͏̷̸̴͙͚̬̮͖̭͙͎͚̰̭̘͚̫̭͓͙̯͚̪̤̭͓̘͙̩͚̩̭͔̭̩͚̗̭͓͙͚̩͖̮̘͙̓͆́͒̒͌͒̒́̓͊͒͏̸̨̧̨͚̮͓͙̪͚̪̭͎͔͚̹̤̭͙͚̫̭͎̘͙͚̩̮͔͓͚̫̮͙͚̭͓̗͚̬̭͉̭͙͚̮͉̭̘͚̬̭́͒͐̏̓̒͐̓͒̓͆̒͊͒͐̓͌͂͊̒̏͂̏̒͏̸̘͚̭͙̥͚̫̮͓͙͚̮̤͚̫̮͎̭͙͚̪̭͔̘̘͚̮̒̑́̏͒̓̓͑͆͂͐̓̒͂͑͆̒́͒͏̭͙͖͚̫̗̭͙͈͚̩̗̮͕̭͙͚̩͖̭͈͓͚̩̰̭͙͚̺̭͉̘͖͚̬̮͓͙͔͚̪͚̭͎̘͙͚̬̤̮͇̘͙̘͚̺͚̮͐̓͊̒̏͊̓͊̒͆͑͘ͅ͏̸̴̷̴̨̨̨̨̡͚͚̬̮͖̭͍͚̰̭͔͙͕͚̫̮͍͓͙̯͚̪̭̘͙̬͚̩̮̘̩͚̬̭͓̩͚̬̤̮̘͙͚̪̭͙͓͚̪̭͎͓͚̹̰̭͕͙͚̮͕͓͙͚͚̭͖̘͚̫̗̮͔͙͚̬̭͓͙͚̹̭͉̭͙͚̬̮͉̭͙͚̬̮͍̭͙͚͚̭͓̭͙̥͚̫̭̭͙͚̩̭͉̘͚̬͎̮͙͚̪̭͔̘͓͚̪̮̓̒͆̒́̓͂͐͂͒̒̏̓̒͒̐͒̓̏̒̓́̓͂̒͊̓͌͊͊̓̓̈́́̓͌͆̓̒͑̓͑̓̒͊͘͏̘͙͏̸͚̭͙͚̩̗̭͇̘͙̗͚̩͖̭͇͖͚̹̭͕͙͚̹͖̮͓͚̫̮͎̘͙͔͚̩̭͎̘͙͚̪̮͇̘͙͇͚͎̮͂͐̓͋̓̒͊̓͑̓̒͊̓͂͆́͘͏̴̵̡̨̨̢̨̨͚̬̭͈̭͚̰̭̭͙͕͚̗̭͔̭͙̯͚̪̰̭͕̘͙̩͚̪̭͇̩͚͎̭͓̬͚̮̭͙͚̩̮͓͚͚̪̮͔͓͚̹̤̭͚̫̭͓͙͚̮͖͓͇͚̫͖̮͔͕͚̹͖̭͓͚̗̭͉̭͙͚̩̮͉̭͙͚̬̮͙͚̭̘͙͚̭̭͙͚̭̘̤͚̬̭͈̘͈͚͖̭͔̘̘͚̮̓̒͆̒̒́͒́͒̓̒͂̓̒͂̓͒͑͐̒̏̒͐̓̒͐͒͋̓́̏̒̓̒͊̒̔͂͊̓́̏͒́͂͊͆͂͂͋̒̏̒͂̒́͂͘͏̭͙͚̪͖̭̩͚̩̗̭̘̦͚̩͖̭͎̭͚̩̰̮̑͐̓̒͋̒̒̏͏͓͙͚̹̭͈̘͖͚̫̮͎̘͍͚̪͖̭͎̘͙͚̮͇̭͙͚̩̮͒̒̓̒̈́́̓͌͆͘͏̸̴̴̸̸̨̨̨̡̨͙͚̬̭͈̭͚̤̭͔̭͙͚̫̭͙̯͚͖̮͍͙̩͚̩̮̘͙̤͚̩̭͓̫͚̫͚̮̭͙͚̪̭͚̪̭͍̘͚̹̤̭͖̭͙͚̫̮͎̘͙͚͚̮͓͚̬̭͍̘͕͚̺̭͓͙̱͚̬͖̭͉̘͙͚̬̭͇̘͙̯͚̬̮͉͓͚͚̭͓͚̫̭̘͙͚̭̘͚̫̭̘͈͚̭͔̘̘͚̗̮̓͆͆̒͑́͂͑̓͂̓͂͒̓̓̒͒͐͒̓̒͗̏̒͒̓͂͑̒͊͂̒͊͊̒́͑̒͑̓͋͆͂͌̒͌̒́̒͂̕͘͏̸̨̘͙͚̭͙͚̩̗̭͓͙͚̩͖̭͈͓͖͚̹̭͕̭͙͚̹͖̭͍̘͖͚̫͎̮͎̘͙͔͚̫̭͎̘͙͚̮͇̘͙̘͚̩̮͐͂͐̓͑͌̏̒͊̒̏͂͆͘ͅ͏̷̸͙͚̬̮͖̭͉͚̤̭̭͙͚̗̮͇͙̯͚̩̤̭̘͙̬͚̩̭͔̭̩͚͖̭͓͙͚̮̘͙͚͚̭͙͚̪̭͎̭͙͚̹̤̭̓̒͆̒́͑͂́̓͑͆̒́̓͊͂̓͒́͒͒̓̏͏̴̨̨̨̭͙͚̫̭͎͙͚̩̮͓͓͚̫̭͍̘͕͚̭͓͙̤͚̭͉̭͙̪͚̩̭͇̘͙͚̬̮͉̭͙͚͚̭͒̓̓̒͊͒̒͂͒͊́͂́͗́͏͙̥͚̫̭͍̘͙͚̩̗̭̭̤͚̬̭͈̘͙͚̪͖̭͔̘͓͚̬̮̓̓͆͒̒̓͑̒͂͏̸̢̭͙͚̫̗̮͓͙͚̩̗̮͕̘͚̩̭͍͓͖͚̹̭͓̘͙͚̫̰̭͓̭͖͚̬̬̭͈̭͙͔͚̪̬̭͎̘͙̮͚̫̮͇̭͙̘͚͎̭͓͎͚̬̮̘͉͚̤̭̭͚̫̮̒͒̑̒͊̒͊̒͊́͑̒͆͒̒́͒̒̑͘͏̴̴̴̨̨̧̨͓͙̯͚̮͕͓͙̩͚̩̤̮̘̩͚̪̰̭͓̫͚̮̘͙͚̩̮͓͙͚̪̮͔͓͙͓͚̹̰̭͙͚̫̮͖͙͚͚̮͓͓͚̫̮͙͚̹̭͓͙͚̺̭͉̭͙͚̭͇̘͙̗͚̬̭͂͊͒̒̓̒͂̓͒̐͐̏͐̓͒̓̓͂̒͊̏͐̓͌͊̓́̏͏̴̭͙̰͚̭͓͚̭͙͚̪̗̮̤͚̬͎̮͎̭͈͚͎̭͔̘͙̥͚̩̮́̏͑̒͑́͂͌̓͆͑̓̒̒́͏̸̸̴̨̡̧̨̡̨̭͙͚͚̪͖̮͓͚̩̗̭̘͙̗͚̩̭͈̭͙͚̩̰̭͇͓͙͚̫̰̭͈̘͖͚̫̭͈̭͍͚̪̤̭͎̘͙̮͚̫͚̮͇̭͙͍͚̺͚̭͓͙̹͚̬̮͖̭͚̰̭͔͓͙͚̗̮̭͙̯͚̪̰̮͙̬͚̩̭͔̭͙̤͚̪͖̭͓̹͚̩̮̘͙͓͚̺̭͙̲͚̪̭͎̭͚̹̤̭͓͙͚̮͓͙͚͚̮͔͓͚̬̮͔͙͚̫͚̭͓͙͚̗̭͉̘͙͚̬̭͇̘͚̬̮͍̘͚̭͔̭͚̭͈͙͚̮͓͚̫̮͙͚̹̭͔̘̘͚̮͒̒͋͊̐̒͒̒͑͆̒̋́͂́͊͋̓͂̓̒̏͒̏͒̓̏̒͐͐́̓̓͂̒͊̓͌͊͂̒͒̒͌́̏̒͆́͂̓͆͂͂̓̒͑̓͑͂̒́͂̕͘͏̸̢̘͙͕͚̮͓̙͚̩̗̮͕̘͙͖͚̩͖̭͈̘͙͚̩̰̮́͒̒͏̸̘͙͚̺̮͖͖͚̬̮͓͙͔͚͖̭͎̘͙͚͎̮͇̭͙͚̺͚̭͓͚̬̭͈̭͙̹͚̰̭͓͓͚̫̭͊̓̒͆͑͂̓͂̔͑̒̑͆́̒̑͘͏̸̭͙̯͚̭̘͙̩͚̩̤̮͖̘͙̤͚̭͓̫͚̮̭͙͚̭̖͚̪̮͔͓͔͚̹̤̭͖̘͚̫̮͂͊͒́̏̓̒͂͒͒́͒͒̓̒̏̒̒͐͒͏̸̸̴̸̡̨̡̘͙͚͚̭͍̭͇͚̬̭͍̘͕͚̭͓͚̹̭͉̘͙͚̮͉̭͓͚̬̮͉̘͙͓͚͚̭͔͓͙̥͚̫̭͎͓͙͚̮͚̫̭͈̘͙͚̭͔̘͙̥͚̬̮̓́̒̒́͂͊̒̔͂̏̒́̓͆͂͂͑̓̒͑͂̏͏̸̵̴̴̨̨̨̨̨̡̘͙͙͚̫̗̮͓͚̩̗̭͓͙͚̩̭͈͙͚̩̰̮͓͙͚̫̤̭͍̘͖͚̬̮͓͍͚̩̭͎̘͚̮͇̭͙̖͚͎̭͓͙̫͚̬̮͖̘͙͚̰̭̘͙͕͚̗̭͕̭͙̯͚̪̤̭̘͙̩͚̩͎̭͔̭̩͚̩̭͓̩͚̮̭͙͙͚̮͓͙͚̪̮͔͚̹̤̭͖͚̭͓͙͚̩̭̘͇͚̫̭͓͕͚̬̭͓͙͚̺̭͉̭͙̥͚̩̮͉̭̗͚̬̮͍̭͙̰͚̭̘͚̭͙͚̪͖̮͓͚̬͖̭̘͈͚̩͎̭͔̘̘͚̫̮͒̒́͌͊͊̓̐͐̒͂͑̒͊̒̑́́͑͆́͑́͑̒̓̒͂͒́͒͐͂̏̓̒̓̒͐́͌̓͆͐̒͊͒̒̏͊̒́̏͒̒͆́͂͋̓͆̓̒͌̒̒͆͘͘͏̴̸̭͙͚̫̗̮͓͙͚̩̗̮͕̭͙͚̩͖̭͇̘͙͚̹̮͖̘͙͚̹̭̭͖͚̬̭̭͍͚̬̭͎̘͙͚̮͇̘͙͚͎̮͗͒͒͊̐͊̓͒̒͌̒͂͂́͘̕ͅ͏̸̸̴̴̧̨̨̡̨̨͚̬̮͖̭͚̤̭̭͚̫̮͈͓͙̯͚̩̰̭̘͙̬͚̩̮͖̘͙̤͚̭͓͙͚̫͚̮̭͙͚̪̮͓̖͚̪̮͔͙͚̹̰̭͕͓͙͚̮͓̘͙͚̭͇̭͇͚̫̭͍̘͙͚̬̭͓͙͚̹̭͉̘͙͚̬̮͉̭͙̥͚̬̭̓̒͆̒̋́͑̒͌͒́͊̓͊͒̐͐̒̏̓͗́̓͂̏̒͊͌̓͊̓͏̴̵̴̡̘͙͚̭͓̭͙͚̫̭͈͓͙͚̩̭̭͚̬̮͈͚̭͔̘͓͚̪̮́̏̓͆̓͑̒͆͑̓̒͂͒̒͏̸̘͙͙͚̮͓͙͖͚̩̗̭͇̘͙̗͚̩̭͈̭͙͚̩̰̭͈̭͙͚̫̤̭̭͓͚̫̮͎̘͙͔͚̪̭͎̘͙͚̫̮͇̘͙̘͚̩̮͂͒͊̐͑̒͊͒̓͊͆͘͏̸̢̡͚̬̮̭͙͚̤̭͔͓͙͚̫̮͈͙̯͚͖̭̓̒͆͒́͂̓͂͏̸̴̴̨̡̨̘͙̩͚̪̮̘̩͚͚̭͓̩͚̫̮̭͙͚̭͙̫͚̪̮͔͓͚̹̰̭̭͙͚̫̮͔̭͙͚̭͇̭͚̬̮͔͙͚̬̭͓͙͚̺̭͉̭͙̥͚̭͇̘͙̙͚̬̮͉͓͙͚̭̘͚̭̭͙͚̪̗̭͉̘͚̬̮͙͚̹̭͔̘̘͚̬̮̓͒̒͂̓̒͊͒͗́͒͒̓̏̒͌͐͒̓́̏̒͊͆̓͌͆͊̓́̏́̏͒̒͑́͂͌͆̒̓͑̓͑̒́͏̭͙͚̪͖̭͙͈͚̩̗̭̭͙͚̩̭͈̭͖͚̩̰̮̑͐̓͋͒͊̒͏̸̴̭͙͚̹͖̭̭͖͚̫̮͓͍͚̗̭͎̘͚̪͖̮͇̭͙̙͚̩̭͓͙̹͚̬̮̘͉͚̤̭̭͚̫̭̭͙̯͚͖̮͙̩͚̩̬̮̘̩͚͚̭͓̮͚̩̮̘͙͚̩̮͓͙̬͚̪̭͎̭͙̰͚̹̰̭͖̘͚̫̭͍̘͙͚͚̭͒̒͊͑̒͂̒̑͆͑͆͒̒́͑̒͌͑͂͋̓͒̒͂̓̒͆͒͒͐̏̒̓͒̓͂͘͏̴̵̨̨̨̡̨̘͇͚̫̭͓͙͚̫̭͓͚̫̰̭͉̘͙͚̬̭͇̘͙̯͚̬̮͍̭͙̰͚̭͓̘͙͚̫̭̭͙͚̪̮͚̫̭̘͈͚̭͔̘͚̬̮̒̏͒͌͊̒̔́̏̓͊͆̓͑̓̒͌̒͂͆̒̏́͏̸̭͙͈͚̮͓͙͉͚̩̗̭͙͖͚̩͖̭͈͖͚̩̰̮̭͙͚̹̭͉̘͖͚̬̤̮͓͍͚̭͎̘͙͚̩̮͇̭͙͇͚͎̮͂͒͋̓̓̒͑͊̒͑̒͂͒͆́͘ͅ͏̴̘͚̬̮͓͙͚̰̭͓͚̗̮͈̭͙̯͚̩̤̭̘͙̩͚̪͚̮͖̘̩͚̪̤̭͓̹͚̫͚̮̘͙͚̩̭͙̲͚̪̭͓͙̬͚̹̤̭̓̒͆͒̒́͒̒̑́͐̒̓̒͒͗͒̓̏͊͏̡̨̨͚̫̮͈͙͚͚̭͍̭͚̬̬̭͍̘͕͚̹͎̭͓͙͚̫͖̭͉̭͙͚̮͉̭͚̬̭̓̒͐͒̓̓́̒͊̒͊͂̏̒͗͏̘͔͚͚̭̭͙̥͚̫̭͙͚̪͖̭̘̤͚̬̭̘͙͚͎̭͔̘͓͚̗̮̒́͑̓͊̓͆͋̒͆͌͑͂̒͂͏̸̸̢̨̨̭͙͙͚̭̪͚̩̗̭̘͚̩̭͎̘͖͚̹̭͖͙͚̹̭͉̘͓͚̫̮͓͍͚̭͎̘͚̮͇̘͙͈͚̩̭͓̘͚̬̮̭͚̰̭͓̘͚̫̭͕͓͙̯͚͖̭͂͐̓̒͋̒͊̒͊̓̓̒͊͑̒͂̒̒͂͆͑̒͆͒̒̋́̒̑͂͘͏̸̸̴̴̨̨̨̨̘͙̩͚̩̰̮͖̘͙̤͚̭͓͚̮̭͙͚̮͓͙̩͚̪̭͎͚̹̰̭͖̘͙͚̭͙͚͚̭̭͇͚̬̮͔͙͚̬͎̭͓͙͚̬̭͉̭͙̪͚̬̮͉̭͓͚̬̭́̓̒͂́͒͒́͒͐̏̓̒́͌̓̓͂͌̒̓͌͊̏̒̕͏̸̘͚͚̭͔͚̭͉͓͙͚̪̮͖̤͚̬̮͈͚̩̭͔̘͙̥͚̬̮̒͐́̓̒͑́͂͆̓̓̒͒͑̓̒͂͏̧̭͙͚̪͖̭͙͓͚̩̗̭̦͚̩̭͈͓͙͚̩̰̭͉͙͚̺̮͔͖͚̬̭͈̭͍͚̭͎̘͙͚̩͖̮͇̘͙͉͚̺͚̭͓͚̬̮͖̭͙͎͚̰̭͔͓͙͚̗̮̭͙̯͚̩̰̭͓̘͙̬͚̩̭͇͙̤͚̩̭͓̫͚̪̰̮̘͙͚̺̭͙͚̪̭͎͙̐͐̓͋̓̒͊̐̓͊̓̒͂̒͂̓̓͑̒͆́͂́͊͂̓̏̓̒͒̐̏͒̓́̏̓͘͏͚̹̤̭͏̸̸̨̨̡̨̘͙͚̮̭͙͚͚̭̭͚̬̭͓͙͚̹̗̭͓͙͚̹̭͉̘͙̦͚̮͉̭͈͚̬̭́͐̓͂͌̒͊͒͌͊́̏̒͏̸̡̘͙͚͚̭͔̘͙̥͚̫̭͙͚̪̗̮͖͚̫̮͎̭͙͚̩̬̭͔̘̘͚̮́̓͒̓͆̓̒͂͑̒́͒͏̭͙͏̸̶̸̵̡̨̨̨͚̫̗̮͓͚̩̗̭͇̭͙͎͚̩͖̭͉͖͚̩̰̭͕͓͙͚̹̭̘͖͚̬̰̭͈̭͙͔͚̩͖̭͎̘͙̮͚̬̤̮͇̭͙͚̺͚̭͓͙̩͚̬̮̘͍͚̤̭͓̭͙͕͚̗̭̘͙̯͚̪̤̮͓͙̩͚̩̮͖̘̩͚̬͖̭͓̫͚̮̭͙͖͚̭͙͚̪̭͓͙͓͚̹̰̭͖͓͙͚̮͈̭͙͚̭̭͇͚̬̰̮͔͙͚̹̭͓͚̺̭͉̭͙͚̮͉̭͙͚̬̮͉̭͚͚̭͓͙͚̫̭͉̘͙͚̩̭̭̤͚̫̰̭͈̘͙͚͎̭͔̘͓͚̮͒̒̓̒̓͊̒̋͑͆͒̒́́͑͐͂̒̓̒́͒́͒͒̓̏͊́̓́̏͌̒̓͌͊̒̔̓́́̏͌̒́͒̓͆̓͑̒͑͂̒͂͂͘͘͏̸̸̸̧̭͙͖͚̮͓̫͚̩̗̭͓͚̩̭͈͙͚̹̭̘͙͚̹̮͖͖͚̬̤̭̭͍͚̩͎̭͎̘͙͚̩̮͇̘͙͍͚̪̭͓͙͚̬̮͓͙̹͚̤̭͓͓͙͕͚̫̭̘͙̯͚̪̤̮͓͙̩͚̩̮̘͙̤͚̬̭͓̫͚̩͖̮̭͙͙͚̭͚̪̭͎͓͙͚̹̤̭́͒̒͌̒̋͊̓̐͊͋͒̓̒͌̒̏͆͑͆͒́͒͐͒͂̓̒͒́͒͒̓̒̏͗͘͘ͅ͏̸̴̨̨̨̘͙͚̮͕̘͙͚̩̭͈̭͇͚̬̭͍̘͙͚̺̭͓͙̱͚̺̭͉̘͙͚̮͉̭̖͚̬̭́̓͆̒͌͒͊́̏̒ͅ͏̡̘͚̭̘͚̭͈͙͚̩̮͓͚̬̭͈̘͙͚̺͖̭͔̘̘͚̮̒̑́̏͑̒͆́͂̓͆̓̓̒͊͑̒͂͒͏̸̭͙͖͚̭̘͚̩̗̭͇̘͙̗͚̩͖̭͈͚̹̮́͐̓̒̓̒̏͊͏̸̴̴̨̢̨̨̨̨̡̘͙͚̹̭̭͖͚̫͚̮͓͙͔͚̪̭͎̘͚̪͖̮͇̘͙̗͚͎̭͓͚̬̮͖̭͚̤̭̭͙͚̫̮͓͙̯͚̪̮͙̬͚̩̭͇͙̤͚̩̭͓̩͚̬̤̮̘͙͚̺̭͚̪̮͔͓͙͚̹̰̭͕͓͙͚̭͍̘͙͚̭͉̭͇͚̬̤̭͍̘͕͚̫̭͓͚̫̭͉̘͙̥͚̩̭͇̘͎͚̬̮͍̭͙͓͚͚̭͓̘͚̫̭͎͙͚̩̗̭̭͚̬̮͙͚̩̭͔̘͓͚̪̮̓͑̒͑̒̒́͑̒͆̒̒́͒͂͊͂͋̓͂̓̓̒͒͐̏͒̓̒͌̏͗́̓͂̏̒̒̏͊̒̔͆̒́̒͆̓̓͆͑̒͆͑̓͑͂̒͘͏̘͙͈͚̪͖̭͙̘͚̩̗̮͕̘͙͖͚̩̭͈̭͚̩̰̭͈͓͙͚̹̮͓͓͚̬̮͓͙͔͚̪̗̭͎̘͙͚̪͖̮͇̘͙͇͚͎̮͐̓͊̒̏͒̓̒͂͑͂́͘͏̵̴̡̨̨̨̡̪͚̬̮̘͙͚̰̭͓͚̗̭̭͙̯͚͖̮͖͓͙̬͚̩̤̮̘̩͚͖̭͓͙͇͚̩̮̭͙͚̺̭͙͚̪̮͔̙͚̹̤̭͕̭͚̫̭͎̭͙͚͚̮͖͓͚̬̬̭͍̘͕͚̺̭͓̗͚̫̭͉̭͙͚̩̭͇̘͈͚̬̮͉͓͙͚̭͔̘͚̭̘͙͚̪̭̘͚̬͎̮͈͚̭͔̘̘͚̪̮̓̒͆͒̒́͒̒͌́͐͂͒̒͂̓̏͒͒̏͒̓̏̓̒̒͐͒̓́̒͊̒̏͊̒̏̒́̏̒͆́͂͌͆̓͋̒͑̓̒͂̏̒͏̸̵̸̴̸̸̢̡̨̡̭͙͙͚̭͚̩̗̭̘̺͚̩̭͇̭͙͚̹̮͓͙͚̹̭͈̘͓͚̬̰̭͈̭͍͚̩̭͎̘͙͚̬̤̮͇̘͙̖͚̺͚̭͓͙̩͚̬̭͈̘͙͚̰̭̘͚̫̮͈̘͙̯͚̪̰̭͕̘͙̩͚̩̮̘̩͚͖̭͓͙͚̪͖̮̭͙͙͚̺̮͓͙̹͚̪̭͓͔͚̹̤̭͕͓͙͚̫̮͈͓͙͚͚̭͖̘͚̬̮͔͕͚̬̭͓͚̬͖̭͉̘͙̣͚̭͇̘͙̳͚̬̮͍̭͚̭̭͚̫̮͕͓͙͚̭̘͚̫̭͈̘͈͚̬̭͔̘̘͚̮͂͐̓̒͋̒͊͊͒͊̒̒̓̈́͑͆́͒̒̑͒̒͂̓͊͒̏͐̏͊̒͒̓͂̒͊͂̓̒̓͊̒̔́̏̒́̏͒̒͆̓͆͂͂͊̒̒͂̒́͂͘̕͏̸̸̭͙͚̮͓͙͚̩̗̭͇̭͙͖͚̩͖̭͈̘͖͚̩̰̮͖̘͙͚̹̮͖͚̬̤̭̭͙͔͚̭͎̘͚̮͇̭͙͇͚̺͚̮̓́͒͑̒͊͑̓̒͌́̓̒̒͂͘͏̵͙̲͚̬̮͓͙͚̰̭͓͙͚̗̭͔͙̯͚̩̤̭̓͆͒́͒͂́̓͏̴̨̨̨̨̘͙̬͚̩̭͇͙̤͚̬͎̭͓͚̮̘͙͚̩̭͙̦͚̪̭͎̭͚̹̤̭͖͓͚̮͔͓͙͚̮͓͓͇͚̬̤̮͔͙͚̭͓͙̱͚̹̭͉̘͙͚̩̮͉̭͙͚̬̮͉͓͙̬͚͚̭͓͚̮͙͚̮͔̤͚̬̮͈͚̹̤̭͔̘͖͚̪̮͆̓̓̒͂͂̓͒̒͒̓̏̒͐̒̓́̓́̏̒̓͌́͂͊́͑̒͑́͂͒̓͆͂͂̓̒̏͑̓̒̒͊̕ͅ͏̭͙͚̫̗̮͓͙͚̩̗̮͕̭̲͚̩͖̭͇̭͖͚̹̮͕̭͙͚̹͖̭̭͓͚̬̤̮͓͙͔͚̪̰̭͎̘͚̮͇̭͙̗͚̺͚̭͓͙͚̬̮̭̖͚̰̭͚̗̮͉͓͙̯͚͖̭̑͒͋̒̒͊͒̒͑̒̒́̓͑͆͒̒́͑̓̒͌́͂͘ͅ͏̴̨̘͙̩͚̩̤̮̘͙̤͚̭͓̹͚͎̮̘͙͕͚̭͚̪̭͍̘͙͚̹̰̭͒́̓̒͂͒́͒͒̓̒̓̏͏̸̡̨̭͙͚̫̮͇̘͙͚̭̘͚̫̮͙͚̫̬̭͓͙̱͚̫̰̭͉̭͙͚̮͉̭̗͚̬̭͒̓͂̏͐̒͊͊͐̓͌͊͂̏̒͏̵̸̡̭͙͚̭͙͚̭͎͙͚̭͍̘͚̫̭̘͙͚̩͎̭͔̘͖͚̫̮͂́̏͒̓́͂̓͆͂̒͂͌͑̒͆͏̭͙͏͚̫̗̭͙͐̓͏͚̩̗̭͓͙͚͚̩̭͈͖͚̹̮͖̭͙͚̹̭̘͖͚̫̗̭͈̭͍͚̪̭͎̘͙͚̩͖̮͇̘͙͇͚͎̮͌͊̓̒͊͒͋̒̒͒͂́͘͏̸̴̨̨̥͚̬̮͖̭͙͚̤̭̘͙͚̫̮͕̭͙̯͚͖̮͙̬͚̩̬̭͔̭͙̤͚̪̭͓͚̩͖̮̘͙͚̩̭͙̰͚̪̭͎͓͚̹̰̭͕͚̫̮͇͙͚̮͓͇͚̫̮͔͕͚̫̭͓͚̗̭͉̘͙̪͚̮͉̭͙͚̬̭̓̒͆̏́͑͂͂͋̓͊̓̒͂͒̐͒̓̏̒͌̓̒̓͒̓̓͂̏͑̒̓̒͂͊̒̔͂́̏̕͏̘͙͓͚͚̭̘͙̥͚̫̭͙͚̪̗̭̘̤͚̬͎̭͈̘͙͚̪͖̭͔̘͚̩̤̮́͒̓͒̓͆͋̒͑̒̏͏̸̢̨̨̭͙͚͚̪͖̮͓͚̩̗̭͓̲͚̩͖̭͈̘͙͚̹̮͙͚̺̮͓͚̫͎̮͓͙͔͚̭͎̘͙̯͚̫̮͇̘͙͇͚̪̭͓͙̣͚̬̮̭͙̩͚̤̭͓̭͚̗̮͇͙̯͚̩̰̮͙̩͚̩̤̮͖̘͙̤͚͖̭͓̩͚͎̮̭͙͔͚̺̭͙̭͚̪̭͓͚̹̰̭͖̘͙͚̫̭͎͙͚͚̭͍̭͚̫̗̮͕͚̬̭͓͚̬͖̭͉̭͙͚̭͇̘͙̬͚̬̮͚͚̭̘͚̮͔͓͙͚̭̭̤͚̫̬̭̘͙͚̭͔̘͖͚̪͚̮͒̒͌̒̐͊͑̓͊͒̓̒͑͂͒͊͆͑͆͒́̒̑́̓͋̓͂̓̒͂͒̏͒̓̏͊̒̑͒̓̓́̒͊͐̓̒̓͊̒̔͆͂̏͊̓̒̑́͒̒͆́͂͆͂͒̒͌͑́͆̒͘͏̸̵̴̸̨̨̘͙͚̫̗̭͙͉͚̩̗̮͕̭͙͚̩̭͉͙͚̩̰̭͕͓͙͚̹̭͈̘͖͚̫̗̭͈̭͍͚̩̗̭͎̘͙͚̩̮͇̭͙͚̺͚̭͓̗͚̬̮͖̘͙͎͚̤̭͔͙͚̫̭͖͙̯͚̪̰̭̘͙̩͚̩͎̭͔̭͙̤͚̭͓̫͚̪̮̘͙͚̮͓͙͚̪̭͎͓͙͚̹̤̭͙͚̫̭͇͙͚̩̮͔͓͇͚̬̭͍̘͙͚̭͓͚̭͉̭͙̪͚̮͉̭͚̬̭̒͐̓͊͊̓̐͒̒̒͂͆̓͑̒͆́̓͂̓͐͂̏̓̒͆͒͒́͒͐̏͗͐̓͒̓̓͆̒͌͂͊̒̔͂͒́̏̒̔͘͏̵̨̡̘͙͚̭͔͓͙͚̮͖̭͙͚̩̗̮͚̬̭͈̘͈͚̭͔̘͚̮́̏́͂͆͐̓̒͆̒́͒̒̏͂͒͏̘͙͙͚̪͖̭͙͚̩̗̭͇̘̲͚̩͖̭͈̘͚̩̰̭͎̘͙͚̹̮͓͖͚̬̰̭̭͙͔͚̪̰̭͎̘͙͚̫̮͇̘͙͚͎̮͐̓̐̒̒̏̓̓̒͌͊̋́͘ͅ͏̵̵̸̸̴̨͙͚̬̮͖̭͙͚̰̭͙͕͚̫̮͉̘͙̯͚̩̤̮͕͓͙̬͚̩̮̘͙̤͚̩̭͓͙͇͚̮̘͙͚̪̭̓͆́͑̓͒̓́̓͒̓͒̓̒͏͚̪̭͎͓̙͚̹̤̭̏̒͏̷̴̴̨̨̨͓͚̫̭͍̭͙͚͚̮͔͓͇͚̬̰̭͓͙͚̫̤̭͓͙͚̫͖̭͉̘͙͚̩̮͉̭͙̥͚̬̮͙͚͚̭͓̘͚̫̭͉̘͙͚̪͚̮͖̤͚̫̭͈̘͙͚̩̭͔̘͖͚̪̮̒̓͒̓͂̒͒͌͊͊̓͂́̒͆̓͆̓̒͑͂̒͏̭͙͚̪͖̭͙͚̩̗̮͕̘̖͚̩͖̭͇͚̹̮͓͓͙͚̫̤̮͓͚̫̗̭̭͙͔͚̗̭͎̘͙̯͚̪̮͇̭͙͈͚͎̮̐͐̓͌̒̓̒̏͊͒̓̒͌͂͆́͘͏̸̴̨̨͙͚̬̮̘͙̹͚̰̭̘͙͕͚̫̮͉̭͙̯͚̭͓̘͙̬͚̩̤̮͖̘͙̤͚̩͚̭͓͙͇͚̩͖̮̭͙͖͚̺̮͓͙͚̪̭͎͓͙͚̹̤̭͕͚̫̮͓͙͚̩̭̘͇͚̫͖̮͔͕͚̹̰̭͓͚̭͉̭͙̥͚̮͉̭͙̰͚̬̭̓͆͒́͑͂͊̓͒̏͐̒̏̓̒͐͒͑̓͐̒̓̒͊̒̔͂͒́̏ͅ͏̡̭͚̭͓̘͙̥͚̭͎͙͚̪͖̭͉̘͚̬̮͙͚͖̭͔̘͕͚̪̮̒̑́̏́͂̓͆̒͆͑̓͑͂̒͊͏̡̭͙͚̫̗̭͚̩̗̭̭̺͚̩̭͉͙͚̹̮͙͚̫̰̮͕͓͚̬̬̮͓͍͚̪̰̭͎̘͙͚̫̮͇̭͙͈͚̩̮̑͐̓̒͋̒͊̓̐͊͐̓̓̒͑̒̓͊͆͘͏̷̸̸̴̴̵̸̨̨̨͙͚̬̭͈̭͚̤̭̭͙͕͚̫̮͖͙̯͚̪̤̭͕̘͙̩͚̩̮̘̩͚̬̰̭͓͚̩̮̘͙͔͚̺̮͓̖͚̪̭͎̭͙͚̹̤̭͕̭͙͚̭͙͚̭͈̭͇͚̫͚̭͓͕͚̹̭͓͙͚̬̰̭͉̘͙̥͚̬̭͇̘͙̪͚̬̮͉͓͙͚̭͙͚̮͔̭͙͚̭̘̤͚̬̮͈͚̪͚̭͔̘̘͚̮̓͆̒̋́͑̓͆͒̒̓̒͂̏͒̏͐̒̏͂́͌̓̓͂̏̒͒̒͊͊́̏͒̓́͂͆͂͌̒͊͑̓̒̒́͒͏̴̢̢̭͙͖͚̫̗̮͓̙͚̩̗̭͚̩͖̭͈̭͙͚̩̰̮͓͙͚̫̤̮͖͖͚̬̭̭͙͔͚̬̤̭͎̘͙͚̩͖̮͇̭͙͇͚̺͚̮͒̒͋̓̒͒̓̒͌̈́͘͏̸̴̵̨͚̬̮͖̘͚̤̭͓̘͙͚̫̭͕̭͙̯͚̪̭̘͙̬͚̩̭͇̩͚̫̭͓̹͚̩̮̘͙͚̺̭͙͚̪̭͓͚̹̰̭̓̒̔͆̒̒́͂͂͒̓̒̓̒͆͒̒̏͒̓̏͊̒̑͏̸̴̨̨̘͙͚̮͖͙͚͚̮͓͇͚̬̤̭͍̘͙͚̭͓͙̱͚̺̭͉̘͙͚̩̭͇̘́̓̓́͑̒͌͂͊̓̒ͅ͏̴̨͚̬̮͉̭͚̭͔͚̫̭͎̭͙͚̩̗̭̭̤͚̬͚̭͈̘͙͚̭͔̘͓͚̩̮̒͌́̏̓̒͑̓͆͒̒͑́͊̒͏̘͙͚̪͖̭̭͚̩̗̮͕̭͙͖͚̩̭͎͓͖͚̹̮̭͙͚̹̭̘͓͚̬̮͎̘͙͔͚̩͎̭͎̘͙̮͚̫̮͇̭͙̙͚͎̭͓̐͐̓̒͊̒͊͒͊͌̒͆͊́͑̒͘͏̴̸̴̸̴̨̨̨̨͚̬̮̭͚̰̭͙͕͚̗̮͖͓͙̯͚̪̮͈͙̩͚̩̤̭͇̩͚̩̭͓͙͇͚̮̘͙͚̭͚̪̭͎͓͚̹̤̭͖͚̫̮͈̭͙͚͚̭̭͇͚̬̬̭͓͕͚̬͎̭͓͙͚̺̭͉̭͙̤͚̭͇̘͙͚̬̮͉̭͙͚͚̭͓̭͚̭͎͓͙͚̭͈̘̤͚̬̮͎̭͙͚̩̭͔̘͙͚̪̮͆͒̒͑́͑̓́͂̓̓̒̓͂͒̐́͒͒̓̒̏̒̓̒͐͒̓͂͌̒͒̒͊́̏́̒͑́͂͆͂̒͆͑͒͘̕̕͏̭͙͚̪͖̮͓̖͚̩̗̮͕̭͙͚̩̭͈̭͖͚̹̭͙͚̹̮͓͖͚̫͎̮͎̘͍͚̪͖̭͎̘͙̮͚̮͇̘͙͚͎̮͗͒̒͒͊̒͊͐̓̓̓̒̒́̓͋́͘͏̸̵͙͚̬̮͖̘͙͎͚̤̭̘͙͕͚̗̮͉̭͙̯͚͖̭̘͙̬͚̩̮̘̩͚̰̭͓̹͚͎̮̘͙͖͚̺̭͙͚̪̭͎̭͚̹̤̭̓͂͆́͑́͂͐͒̒́̓̒́͒̏͒̓̏̒͐͏̸̷̵̸̨̨͙͚̫̮͇̘͙͚͚̭͍̭͇͚̬̭͍̘͙͚̺̗̭͓͙͚̹̭͉̘͙̥͚̩̮͉̭͙̗͚̬̮͉̘͚̭͓̭͙͚̫̮͔̭͙͚̩̭͓̭̤͚̫̮͈͚͎̭͔̘̘͚̫̰̮̓͒̓͂̒͆͌͊̓̒͌́̏̓͆̓̒͑̓̒́̒͏̸̴̸̸̸̷̴̵̴̡̨̡̭͙͚̭͚̩̗̭͇̭͙͚͚̩͖̭͇̘͙͚̹̮͓͙͚̺̭̘͖͚̬̤̮͎̘͙͔͚̩͖̭͎̘͙̯͚̫̮͇̭͙͇͚̩̭͓͚̬̮̭͚̰̭̭͚̗̭̘͙̯͚̪̤̮͍͙̩͚̩̮̘̩͚̤̭͓͙͇͚̮̭͙͔͚̺̭͙̺͚̪̭͎̭͙͚̹̰̭͕̘͙͚̫̮͔͙͚̭͉̭͇͚̬̮͕͚̬̭͓͙͚̹̭͉̘͙͚̬̮͉̭͙̙͚̬̮͙͓͚̭͓̘͙͚̫̭̘͙͚̪̗̮͖͚̫̮͙͚̪̗̭͔̘͓͚̮͗͂͐̓̒̏̐͊͒͊͋̒͊͆͑̒̋͆͒̒̒́͒̒̑́͒̓͒̒́̓́̓͒̏͒̓̏͒̓̓́̏̒͐̓̒͊͊̓͊̓́̏̓͋͆̓̒͑̓͑̒͂͒͘͏̸̸̘͙͚̮͓̫͚̩̗̮͕̘͙͚̩̭͇̭͖͚̩̰̮̭͙͚̺̮͕͖͚̫̗̮͓͙͔͚̭͎̘͙͚̩̮͇̘͙͇͚̪̭͓̤͚̬̮͖̘͙͎͚̰̭̭͚̫̭͐́͒̒͊͊̒͐͊̓̒͑͂͆͂͆͆͑̒͆́͑̒͌͘͏͓͙̯͚̪̤̭͏̴̸̨̨̘͙̩͚̩̤̮͖̘̩͚͖̭͓͙͇͚̪͖̮̘͙͔͚̪̮͓͙͚̪̮͔͙͚̹̤̭͓͙͚̫̮͇͙͚̩̭͉̭͚̫̮͙͚̭͓͙̲͚̫͖̭͉̭͙̦͚̮͉̭͚̬̭̒͂̓͒͐̈́̏̓͂͐͒̓̓͆̒͊͒͐̓͌͂͊́̏̒͌͏̸̡̘͙͚̭͓͚̭͎͙͚̩̗̮͚̬̭̘͈͚̺̭͔̘͚̬̮́̏͒̒͑́͂̓͆͒̓̒͆͌̒̏̒̏́͏̸̴̴̸̷̧̨̭͙͖͚̪͖̭͙͈͚̩̗̮͕̘͙̗͚̩͖̭͈͓͖͚̹̮͕̭͙͚̫̰̮͖͚̬̭̭͙͔͚̪̭͎̘͙͚̮͇̘͙͚̺͚̭͓͚̬̮͖̭͍͚̰̭͙͕͚̗̮͖͓͙̯͚̩̤̭͓̘͙̬͚̩̮͖̘͙̤͚̪̰̭͓̩͚̩̮̘͙͚̪̮͓͚̪̮͔͔͚̹̤̭͖̘͚̫̭͈̘͙͚͚̭͖̘͚̫̗̭͓͕͚̹̭͓͙͚̹̭͉̭͙͚̭͇̘͇͚̬̭͐̓̒͊͒̓̒͆͌͂́̔͑̒͆̒́͑̓́̓̒̏͒̑͐̒̋̏̓̒̒̓͒̓͂̒͊͒̒͊̓͆́̏̒͘ͅ͏̴̡̘͙͚̭͔͓͚̫̭͙͚̪͖̮͖͚̬̮͈͚̰̭͔̘͖͚̗̮́̏̒͑̓͌̓͆̓̒̓͑̓̒́̒͂͏̸̸̡̨̘͙͕͚̫̗̭͙͚̩̗̭͇̭͙͚̩̭͈̘͖͚̩̰̭͈͓͙͚̹̮͖͚̬̭̭͙͔͚̪̭͎̘͙̯͚̪̮͇̘͙͚̪̭͓͙͚̬̭͈̭͙͚̰̭̘͙͕͚̫̮͉͙̯͚̪̭̘͙̬͚̩̤̮͖̘̩͚̬̬̭͓̩͚̮̭͙͐̓͌͒͊̒͊͐̓̒͌̓͆̋͆͑̈́͆́͑̓͐̒̓̒́̓͒͘͏̴̷̸̨̡͚̪̭͙̲͚̪̮͔͙͓͚̹̤̭͕̭͚̫̭͓͙͚͚̮͖͓͇͚̫͚̮͔͕͚̹̭͓͙͚̭͉̭͙̤͚̮͉̭͖͚̬̮̙͚̭̭͚̭͉̘͙͚̪̭̘͚̫̭̘͈͚̭͔̘̘͚̬̮͒̓̏̓̒̓͒͋̓́̒̓̒͂͊͂͒͂̏̒͊̓̒́̏͒̒͑́͂͆̓͊̒͌̒͂̏̒́͏̴̶̴̢̨̨̡̨̨̨̡̨̭͙͚̪͖̮͓͙͚̩̗̭̭͚̩̭͈͓͙͚̩̰̮͖̘͙͚̹̮͖͖͚̫̗̮͎̘͍͚̪̭͎̘͚̩͖̮͇̭͙͚̪̭͓͙̩͚̬̭͈̘͙̩͚̰̭̘͚̗̮͕͓͙̯͚͖̮͙̩͚̩̬̭͇͙̤͚̩͎̭͓̹͚̩͖̮̘͙͚̪̮͓͙͚̪̭͓͚̹̤̭͕͙͚̭͙͚͚̮͓͇͚̫̮͔͙͚̫̤̭͓͙͚̺͎̭͉̘͙͚̩̮͉̭͚̬̮͍̭͙͚͚̭̭͚̫̭͙͚̪̗̭̭͚̫̭̘͙͚̹̤̭͔̘̘͚̪̮̑͒͋̒̋͊͊̓̒̒͆̒̑͊͆͑͆́͑̒̑́͂͊̓̓̓̒͒͐͐̏͊̒͌̓́͌̓̓͂͑̒͊̓͌͊̒̏͗́͑̒͑̓͋̓͆͒̒͌͑̒̕͘͏̘͙͚̫̗̮͓̖͚̩̗̭͇̭͙͎͚̩͖̭͇͓͖͚̩̰̭͙͚̹͖̭͍̘͓͚̫̭̭͍͚̭͎̘͙̮͚̬̤̮͇̘͙͚̪̮̑͒̒̒͊̓̒̓͌̒͂͒̋͆͘͏̸̩͚̬̮͖̘͙̹͚̤̭͔̭͙͕͚̫̭̓̒͆́͏̨̨͙̯͚̩̰̭̘͙̩͚̪͚̭͔̭̩͚̬̰̭͓͙͚̪̰̮̘͙͚̺̭͙̰͚̪̭͚̹̤̭͖͚̮͓͙͚͚̮͓͇͚̬̭͓͙͚̫̭͓͚̬͖̭͉̭͙̦͚̭͇̘̓͑̒̓͊͒̑̏͒̓̏͊̓̒͐̓̒͐́͑̓́͐̒͆͒͌͊̒̔͂̏̒͏̨͚̬̭͏̵̡̨̭͔͚͚̭͓͙͚̫̮͖͓͙͚̩̗̭̘͚̫̮͈͚̪̗̭͔̘͖͚̪̮̒́͒̓͆͌̒͑̓̒̒͊͏̸̸̸̸̴̵̸̴̨̨̨̘͙͚̫̗̭̩͚̩̗̮͕̭͙͚͚̩̭͍͓͙͚̩̰̭̭͙͚̹͖̭̭͖͚̬̬̭̭͙͔͚̩͖̭͎̘͚͎̮͇̭͙͚̺͚̭͓͚̬̮̭͚̰̭͓͓͙͚̗̮͓͙̯͚͖̭͓̘͙̩͚̩̭͔̭̩͚̪̰̭͓͚̮̭͙͚̮͓͙͚̪̭͎͓͙̰͚̹̰̭͙͚̫̮͔͓͙͚̗̭͉̭͇͚̬̭͓͙͚̺͎̭͓͚̺̭͉̭͙̥͚̮͉̭͓͚̬̮͉̘͙͚̭̘͙͚̭̭͙͚̮͖̤͚̬̮͈͚̪̭͔̘͙̥͚̩̮͒͐̓̒͊̐͋͒̒͌̒̒́͑̒̐͆͒̒̒́͂́͊͂̒̓̒͂͂͒͒́͒͐̏͐̓͒̓́̒͒͌͊̒̔̓́̏̒́̏͑́͂͌͆͂̓̒͒͑̓̒͘̕͏̸̢̘͙͕͚̮͓̖͚̩̗̭̮͚̩̭͈̘͙͚̹̭͓͓͙͚̹̭̘͓͚̬̭͈̭͍͚̪͎̭͎̘͙̯͚̫͚̮͇̘͙͉͚͎̮͂͒̒͋̓̒͊͊͒͋̒͂̒́͘͏̵̸̴̨̧̨̨̗͚̬̮͖̘͙͚̰̭͓͓͙͚̫̭͖͙̯͚̩̰̮͙̬͚̩̬̭͔̭̩͚̰̭͓͙͚̫̮̭͙͚̭͙͚̪̭͎͚̹̰̭͖͚̭͍͓͙͚͚̭̘͚̫͎̭͓͙͚̺͖̭͓͙̤͚̺͎̭͉̘͙͚̩̭͇̘͙̥͚̬̭̓̒͆́͂̓͋̓̒́̓͊͊͒͒́͒͒̓̏̓̒̑̓̒͐́̓͂͐̒͊͒͌͊͏̵̨̭͙͚̭͔̭͙͚̫̭̭͙͚̮̤͚̬̭͈̘͈͚̪̭͔̘͕͚̬̮́̏̓͒͆͂͂͒̓̒̓̒͊̒͂͏̸̵̸̸̴̶̴̸̸̨̨̨̡̨̨̨̭͙͙͚̮͓͚̩̗̭͇̘͚̩͖̭͈̘͙͚̹̭̘͙͚̹̮͓͚̫̭͈̭͙͔͚̪̬̭͎̘͙̯͚̮͇̭͙͚͎̭͓͚̬̮̭͙͚̰̭͓͙͕͚̫̮͕̭͙̯͚̭͓̘͙̩͚̩̭͔̭̩͚̭͓̬͚̮̭͙͚̪̭͙͚̪̭͎̭͙͚̹̰̭͖͓͙͚̫̮͓̘͙͚̮͓͓͚̬̭͍̘͕͚̺͚̭͓̗͚̹̭͉̭͙͚̩̭͇̘͙͚̬̮͉̘͙͚͚̭͓̘͚̫̭͎͓͙͚̮̤͚̫̬̭̘͙͚̭͔̘͓͚̩̮́͒̒̒̈́̐͊͋͒͑̓̒͊͂̔́͑̒̒͆͒̏́͒͂͊͆̒́̓̓̒́͒͐͒̓̏͂͒̓́̏̒͊̒͊̒̈́́̒͑̓͆͂͐̓̒͌͑́̒͊͘͏̴̸̡̘͙͚̪͖̮͓̫͚̩̗̭͓͙̗͚̩̭͇̘͚̩̰̮͓͙͚̫̤̮͓͖͚̬̭͈̭͍͚̩̭͎̘͙͚̪̮͇̘͙͇͚̪̭͓͚̬̮͖̭͙̹͚̰̭̭͙͕͚̫̮͇͙̯͚̪̰̭̒͒̒͌͊̒̏͐̓̒̒͆͆͆͑̒͆́͑̓͘ͅ͏̴̸̨̘͙̩͚̩̮̘̩͚̩̭͓̩͚̪̰̮̘͙͚̺̮͓͙̪͚̪̭͎͚̹̤̭͓͙͚̭͇͙͚̮͒̒͊̓̒͒̒̏͐̏̓̒͐͐́̓̓́̏͏̨̨̡͓͚̫̮͕͚̫̭͓͚̫͖̭͉̭͙̣͚̮͉̭͚̬̮͍̭͚̭̘͙̥͚̫̮͓͙͚̩̮͓͚̬̭͈̘͙͚̹͎̭͔̘̘͚̫̰̮̒͊͐̓̒͂͊̒̔͂̏̒̔̒̑́̏͑̓͑͆̓̓̒͒͑̒͏̭͙͕͚̪͖̮͓͙͉͚̩̗̮͕̭͙͎͚̩͖̭͉͖͚̩̰̭͕͓͙͚̺̭͍̘͖͚̫̭̭͍͚̭͎̘͚͎̮͇̘͙̙͚̺͚̮͒̓̒͊̒̏͌̒͂͆̒̑͂͘͏̷̸̴̸̴̴̵̨̡̨̨̡͙͚̬̮͖̘͙̹͚̰̭͔͚̫̭͓͙̯͚̪̮͎͙̩͚̪̗̭͔̭͙̤͚̪̭͓͙͚̪̰̮̭͙͖͚̪̭͙͖͚̪̮͔͓͚̹̰̭͖̭͙͚̮͓͙͚̗̭͉̭͇͚̬̮͔͙͚̬̭͓͙͚̫̭͉̘͙͚̬̮͉̭͙̥͚̬̮͍̘͙͓͚̭͓̭͙͚̫̮͕͓͙͚̪͚̭͉̘͚̬͚̮͈͚̭͔̘͓͚̮̓͆́̓̒̑͐͂̓͒̓͊͒͒̓̏̒͌́͐̓́̒̓͌͊͊̏́̏̓͆̒͑̓̒͂̓̒͂͂͏̸̸̸̴̸̴̴̴̸̴̢̨̨̨̘͙͔͚̪͖̮͓̪͚̩̗̭͇̘͙͎͚̩̭͈̘͙͚̹̮͙͚̹̭͓̭͖͚̬̭̭͍͚͖̭͎̘͙̮͚̬̤̮͇̘͙͚̪̭͓͙͚̬̮̭͉͚̰̭̭͙͕͚̫̮͈͙̯͚͖̭͕̘͙̬͚̩̤̮̘̩͚̗̭͓̮͚̮̭͙͚̪̭͙͚̪̭͎͓͙͚̹̤̭͙͚̮͈̭͙͚̩̭̘͇͚̫͚̭͓͕͚̹̭͓͙͚̹̭͉̘͙̹͚̬̮͉̭͓͚̬̮͍̭͚͚̭̭͚̭͍͙͚̭̭̤͚̬̭͈̘͙͚̭͔̘̘͚̬̮͒̒͊͊͒̓͊̒͌̒́̓͆͑͆͆͒̒́͒̓͂͒̒͂̓̒͂͒͒͒̓̏͐̓́̓͐̒͒̒̏͊̒̒͐́͒̒͆́͂̓͆͂͂͒̒̏͑͂͒̒́͘͏̸̸̸̸̴̭͙͚̫̗̮͓͙͚̩̗̮͕̘̺͚̩̭͈̘͚̹̭̘͙͚̫̤̮͔͓͚̬̮͎̘͙͔͚̭͎̘͙͚̫͚̮͇̭͙͍͚̪̭͓͙̺͚̬̭͈̘͉͚̰̭͓͙͕͚̫̭͙̯͚̪̤̮͕͓͙̩͚̩̮̘̩͚͚̭͓̹͚̮̭͙͚̩̮͓͙̰͚̪̭͎̭͙̰͚̹̤̭̑͒̐̒͊̒̏͊͋̓̒͂͆͑͆̒́͒͑̓͂͒̒́̓̒́͒̒͐̏͘ͅ͏̧̨̘͚̫̭͇͙͚̭͉̭͇͚̫̗̭͍̘͕͚̬̭͓̗͚̫͖̭͉̘͙͚̮͉̭͚̬̭̒̓͒̓̓͂̏̒̒̓͊̒͂̏̒̔͏̸̘͚̭͓̭͚̫̭͍͙͚̪̮͔̤͚̬̮͎̭͙͚̹̭͔̘̘͚̬̮̒͐́̏̒͑̓̓͆̓̓̒͒͑̒͂͏̸̸̘͙͚̮͓̖͚̩̗̮͕̘̲͚̩͖̭͈͓͚̩̰̭͍͓͙͚̫̤̮͓͓͚̬̮͓͙͔͚̫̗̭͎̘͚̮͇̭͙͚͎̮͐͂͒̒̒̒̏̓̒͆͑̒̒́͌́͘͏̴̴͙̳͚̬̮͖̘͉͚̰̭̘͚̗̮͉̭͙̯͚̪̮͎͙̩͚̪̮̘͙̤͚̤̭͓̮͚̩͖̮̘͙͚̪̭̘͚̪̭͎̭͙͚̹̤̭̓͆̒́͒̒̑́͂̓̏͒́̓̒͒̒͒̓̒̏͏̴̴̸̨̨̨̨̡͙͚̫̮͈͓͙͚̭͍̭͚̫̗̭͍̘͙͚̬͎̭͓͙͚̺̭͉̭͙͚̭͇̘͙̥͚̬̮͉͓͙͚̭͔̘͚̫̭͍̭͙͚̪͖̭̘͚̫̮͙͚̪̭͔̘͖͚̪͚̮̓͒̓́̏̒͊͌͊̓͂̏́̏̒͑̓͆͋̒͑̓͑̒͏̘͙͏̢͚̪͖̭͙͚̩̗̭̭͙̗͚̩̭͎͓͙͚̹̭͖͙͚̹͖̭̭͓͚̫̭̭͙͔͚̪̤̭͎̘͚̮͇̭͙͚͎̮͐̓͒͋͊͊̓͒̒͒͌̒̑͂̓́͘̕͏̨͙̫͚̬̮̭͚̤̭̭͚̗̭͔̘͙̯͚̭͕̘͙̩͚̩̰̮̘͙̤͚̬̭͓̫͚̪̮̘͙͓͚̮͓͙̹͚̪̭͎͓͙͚̹̰̭͓͙͚̫̮͕̘͙͚͚̭̓͆͒̒̋́͒̒̑́͂͊͒͒̓̒͆͒́͒͐̏͂͐͒̓͂͏̸̴̨̘͇͚̬̭͍̘͙͚̹̭͓͚̹̭͉̭͙̪͚̬̮͉̭̖͚̬̭̒͌͊͊̒̔̓̒͏̵̸̭͚̭͓͙͚̭͓͙͚̭͍̘̤͚̬̮͙͚̹̬̭͔̘͙̥͚̩̮̒́̏͒́͂͊͆͂̒͒͑̓͑͊̕͏̭͙͚͚̫̗̭͙͐̓͏̨͚̩̗̭̭͙̗͚̩̭͈̘͙͚̩̰̭͙͚̫̰̭͉̘͖͚̬̮͎̘͍͚̪̭͎̘͙͚̪̰̮͇̭͙͚̪̭͓͙͚̬̮͖̘͙͚̰̭͔͓͙͕͚̗̮͈͙̯͚̩̰̮͎͙̩͚̩̮̘͙̤͚̬͖̭͓̫͚̮̘͙͙͚̺̭̖͚̪̭͎͙͋͊̐͊̓̒͂̒͂̓̔͆͑͆͆͊́́̓̓͒̓̒͂̓͒̏͒̓̒̏̓͘͏͚̹̰̭͏̸̨̡̨͚̮͙͚̭̘͇͚̬̮͕͚̫̭͓͙͚̹̭͉̘͙̪͚̮͉̭̙͚̬̭̓̒͐́͑̓̓͂̏͐̒͆͐̓̒͒͊́̏̒͏̘͙͏̵͚̭͔͙͚̮͕͓͙͚̩̭͓̭̤͚̬̗̭̘͈͚̹̭͔̘̘͚̪͚̮́̏̓́͂͆̓̒͌̒͊̒͏̸̨̭͙͚͚̫̗̭͙͚̩̗̭͓̺͚̩͖̭͇̘͚̹̭͎͙͚̫̰̭̘͖͚̬̰̭͈̭͙͔͚̩̭͎̘͙͚̮͇̭͙̘͚̺͚̭͓͙̦͚̬̮̘͙̩͚̤̭͓̭͙͕͚̗̭͓͙̯͚̪̤̭͖̘͙̩͚̩͎̭͇̩͚̬̭͓̩͚̮̭͙͈͚̺̭̖͚̪̭͓͚̹̰̭͕͙͚̫̭̭͙͚͚̭͐̓̐͌̒̒̏͊̓͊̒͂͂͂̓͑͆͒́́͒̓̒́̓̒́͒̏͒̓̒̏͊̒̑̓͒͌̓́͘͏̨̨̘͇͚̬̰̮͔͕͚̬͎̭͓͚̹̭͉̭͙͚̩̮͉̭͙͙͚̬̭̒̓̒͊̒̔̓͂͏̴̘͚͚̭̘͚̫̭͍̭͙͚̪̮͕̤͚̫̤̭͈̘͙͚̹͎̭͔̘͖͚̪̮̒͌́͑̒͆̓͆̓̓̒͑̒͏̭͙͏͚̫̗̭͙͚̩̗̮͕̘̖͚̩̭͈͖͚̩̰̮͓͙͚̹̮͖͓͚̫͚̭͈̭͍͚̗̭͎̘͙͚̪͖̮͇̭͙͚͎̮͐̓̋̒͊̓̒͐͒̓̒̒͂̓́͘ͅ͏̸̴̨̧͇͚̬̮͖̭͙̹͚̤̭͔̭͚̫̮̭͙̯͚̪̭̘͙̩͚̩͎̭͔̭̩͚͚̭͓͙͚͎̮̘͙͚̩̮͓͙͚̪̭͎͙͚̹̤̭̓̒͆́̒͌͌͐̒́̓͊́͒͑͐̏̓͗͏̸̴̸̨͓͙͚̫̮͈̭͙͚̩̮͓͇͚̫̭͓͙͚̹͖̭͓͙͚̹̭͉̭͙̥͚̮͉̭͙͚̬̭͒̓͆͐̒͊͒͌͊́̏̔͏̘͙̬͚̭́̏͏̴̴̡͚̭̭͙͚̩̗̭͓̭͚̬͖̭̘͈͚̭͔̘͚̪̮̓̒͑́͂͋͆̒͌̒͂̒̏͏̸̢̭͙͚̪͖̭̗͚̩̗̮͕̘͙̗͚̩͖̭͇͓͙͚̹̭͓̘͙͚̺̮͕͖͚̫̮͓͙͔͚̪̬̭͎̘͙͚̮͇̘͙͚̺͚̮͒͐̓̒͊͊̓̒̏͑͂͘̕ͅ͏̸̴̨̨̨̨̡͚̬̮͓͚̰̭͓̭͚̫̭͙̯͚̩̤̭͖̘͙̬͚̩̬̭͔̭̩͚̭͓̩͚͎̮̭͙͚̪̭͙͔͚̪̮͔͙͚̹̰̭͖͓͙͚̫̭͎͓͙͚̮͓͓͇͚̬̮͔͕͚̹̭͓͙̲͚̫͖̭͉̘͙̦͚̭͇̘͙͚̬̮͍̭͙͚͚̭͙̥͚̫̮͕͙͚̩̗̭̭͚̬̮͙͚̭͔̘͖͚̩̤̮̓̒̒͆͒̒͑́̒͌͐̓̒́̓̒͂͒͐͒̓̏̓͗͒̓͂̏̒͆̓̒͊͊͂̏̏́͒̓̓̓͆͑̒͊͑̓͑͂͂̒͏̷̵̸̴̘͙͚̪͖̭͙͈͚̩̗̮͕̭͙͚̩͖̭͇͖͚̩̰̭͈̭͙͚̫̤̮͓͚̫͖̮͎̘͙͔͚̩̭͎̘͙̯͚̫͚̮͇̘͙͇͚͎̭͓͙͚̬̮̘͙͚̰̭͔̭͚̫̭̘͙̯͚̮͍͙̩͚̪̮͖̘͙̤͚̪̭͓͙͚̬̤̮̭͙͚̩̭͙͚̪̭͙͑͐̓͊̓̒͒̓̒̏́͑͆͒́̒̑͒͂͊̓͒̓̓͊͒͐͒̓̈́̏͊̓͘͏̨͚̹̤̭͕͚̭͈̘͙͚̮̓̒̓́̓́̏͏̴̵̸̡̨̡͓͚̬̬̭͍̘͕͚̬̭͓̗͚̫̭͉̭͙͚̬̮͉̭͙͚̬̮͍̘͚͚̭̭͙͚̭͉̭͙͚̪̗̮͖͚̫̮͎̭͙͚̹̭͔̘̘͚̬̮̒͊̒́͊̒̏́̒́͑́͂͆̓̒͂͑̒͂̕͏̸̸̴̨̭͙͚̭͙͈͚̩̗̮͕̭͙͖͚̩͖̭͎̘͚̹̮͕̘͙͚̫̤̮͔͓͚̬̮͎̘͍͚̩̭͎̘͙͚͎̮͇̘͙͚͎̭͓̩͚̬̮̘͙͎͚̰̭͓͚̗̭͓͙̯͚̪̰̭͖̘͙̬͚̪̗̮͖̘͙̤͚̩͚̭͓̹͚̮̘͙͚̩̭͚̪̭͚̹̤̭͕͓͙͚̫̮͉͙͚͚̭̑́͐̓̒̏͊̓̒͂̒̓̈́́̔́͑̒͆͒́͒̒̑́͐̓̒͂͒͒͒̓̒͑̏͊̓̒͒̓̓͂͘͘͏̵̸̨̘͇͚̫̗̭͍̘͕͚̫̬̭͓͚̫̭͉̘͙̪͚̭͇̘͙̖͚̬̮͍̭͙͚̭̘͙͚̮͔̘͙͚̮͕̤͚̬̮͎̭͈͚̪̭͔̘͚̪̮̒̒͊̒̔͆́̏͂́̏͒́͂͆͂̓̒̓̒͂̒̏͊͏̸̸̘͙͙͚̮͓͙͍͚̩̗̭͇̘̦͚̩͖̭͈̘͖͚̹̭͕̘͙͚̫̤̮͖͓͚̫̮͓͙͔͚̤̭͎̘͚̮͇̭͙͉͚̺͚̮͂͒̒̒͊̓̒̓͑͂̒̒͂͘͏̴̴̡̘͚̬̮͖̘͙͚̤̭͓̭͚̗̮͇͙̯͚̩̰̮͎͙̬͚̩̮͖̘̩͚̬̬̭͓̹͚̫̮̭͙͚͚̪̭͙̬͚̪̭͓͙̓̒͆́̒̑́̓̓̒̓̒͊͒͒̓̏͊͏̴̵̨̨̨͚̹̤̭͕͚̮̭͙͚͚̭͍̭͚̫̭͍̘͕͚̭͓͙̱͚̺̭͉̭͙̣͚̬̭͇̘͚̬̮͉͓͚͚̭͓̘͙͚̮͓͙͚̮͓̤͚̬̭͈̘͙͚̭͔̘͖͚̮̓̒͐́͐̓́̒͊̓̒͂̏͊̒̔̒͌́́͂͑͆͂͂̓̒͆͑́͒̒͂͂͏̸̘͙͚̭͙͕͚̩̗̭͓̮͚̩͖̭͇̭͙͚̹̭͖͙͚̹̭̭͖͚̬̰̭̭͙͔͚̪̰̭͎̘͙͚̮͇̭͙͚͎̭͓͙͚̬̮̭̖͚̰̭͚̗̮͉͓͙̯͚͖̭̐͂͐̓͌̒̐͊̓̓͒̒͌͂̓͋́͑͆͒̒́͑̓̒͌́͂͘ͅͅ͏̴̨̘͙̩͚̩̤̮̘͙̤͚̭͓̹͚͎̮̘͙͕͚̭͚̪̭͍̘͙͚̹̰̭͒́̓̒͂͒́͒͒̓̒̓̏͏̸̨̨̭͙͚̫̮͇̘͙͚̭̘͚̫̮͙͚̫̬̭͓͙̱͚̫̰̭͉̭͙͚̭͇̘͔͚̬̭͒̓͂̏͐̒͊͊͐̓͌͊͂̏̒͏̡̨̨̘͚̭̭͙̥͚̭͓͙͚̪̭̭͚̫̬̭̘͙͚̩̭͔̘͙͚̮̒́̏͑́͂͊͆̓͒̒͌͑͂͂̕͏̸̭͙͚͚̪͖̭͚̩̗̭̭͙͚̩̭͇͓͙͚̹̮͓͙͚̹̭̘͖͚̫̗̭̭͍͚̪͖̭͎̘͙̯͚̮͇̭͙͍͚̺͚̭͓͙̪͚̬̮͖̘͚̤̭̭͙͕͚̫̭͐̓̒͂͋͒͊̐͊͒̓͌̒͌̒́̓͑͆̒͑́͑͘͏̴͙̯͚͖̮͖͓͙̬͚̩̬̮͖̘͙̤͚̩̭͓͚̩͖̮̘͙͚̪̭͙͚̪̭͎͓͚̹̤̭̓͂̏̓̒͂͒̐͒̓́̏̒͌͏̷̨̨̧̨̭͙͚̮͔͓͙͚̮͓͚̫͎̭͓͕͚̬̭͓͙͚̫͖̭͉̘͙͚̮͉̭͙͚̬̭́̓͂̏͐̒͊͒̒́͊́̏̏͏̘͚̭͔͚̫̮͙͚̪̗̭͈̘̤͚̬̭͈̘͈͚̪̬̭͔̘̘͚̮̒́̏̓̒͆̓͐̓͆̒͒̒̒́͒͘͏̸̸̘͙͚̮͓̪͚̩̗̭͇̭͚̩͖̭͈͓͖͚̹̭͇̭͙͚̹̭͉̘͖͚̬̭̭͙͔͚̩̭͎̘͙͚̪̰̮͇̭͙͈͚̩̮͑́͒̒̒̋̒͊̓̒͌̏̓͆͘͏̴̴̵̨̨̨̨͙̲͚̬̮̘͙̩͚̰̭͓͙͕͚̗̮͈͙̯͚̩̰̭͓̘͙̩͚̩̭͇̩͚̤̭͓̫͚̮̭͙͔͚̮͓͕͚̪̭͙͚̹̰̭͖̘͙͚̫̮͔̘͙͚͚̮͓͇͚̬̬̮͔͕͚̺͚̭͓͙͚̭͉̭͙͚̬̮͉̭͙͙͚̬̮͚͚̭͓͙͚̫̭͉̘͙͚̪̭͉̘̤͚̫̰̭̘͙͚̭͔̘͓͚̮̓͆͒́͑́̓͆̓̒͂̓̒͂͒́͒͐̒̏͊̓͗͒̓́͑̒̓̒͊́͂͆͊̓̒̑́͑̓͆̓̒͌͑́̒͂͒͏̢̘͙͚̫̗̮͓͙͚̩̗̭̭͙͎͚̩̭͇̭͙͚̩̰̮̒͒̓͋͊͏͙͚̺͖̮͔͓͚̫͚̮͓͍͚̪͎̭͎̘͙͚̩̮͇̭͙̘͚̺͚̮̓̓̒͑̒͂͆͘͏̸̴̴̸̴̵̸̴̸̨̨̨̡͍͚̬̮͖̭͉͚̰̭̭͚̫̮͉̭͙̯͚̪̤̭͖̘͙̬͚̪͚̮͖̘̩͚̩̭͓̫͚̪͖̮̭͙͚̪̮͓͙͚̪̭͎͔͚̹̰̭͕͚̭͇̘͙͚̩̭͎̭͇͚̬̭͍̘͙͚̭͓͚̫̭͉̭͙̦͚̩̭͇̘͙̪͚̬̮͉͓͙͚̭͙͚̮͖͙͚̭̭͚̫̭̘͈͚̭͔̘̘͚̫̰̮̓̒͆̒́͒̒͌̒͆̓̒͒̑͐͂̏̓̒̓̒̓́̓͆̒͌͂͊̒̔̏́̏͑̓́͂̓͆͂͑̒͌̒͂̒͏̴̘͙͚͚̫̗̭͙͚̩̗̭͇̘͙͚̩͖̭͈̘͚̩̰̭̘͙͚̺͖̮͔͖͚̬̬̭͈̭͙͔͚̪̭͎̘͚̪͖̮͇̘͙͇͚̩̮͐̓͋͊̒̏͊̓̒̒̑͆͘͏̸̨͎͚̬̮͖̭͙͚̰̭͙͕͚̫̭͙̯͚̩̤̭͓̘͙̬͚̩̰̮͖̘̩͚̭͓͚̮̭͙͚̭͚͚̪̭͙̓̒͆͊́͑̓͑̓̒͂̓̓̒͂͂͒̓́͒͒̓̒̏͊̓͏͚̹̤̭͏̴̴̡̧̨̡͚̫̭͎̭͙͚̮͔͓͇͚̬̤̭͍̘͙͚̭͓͙͚̬͖̭͉̘͙͚̬̭͇̘͈͚̬̮͍̭͔͚͚̭͓̘͚̫̭̭͙͚̪͖̮͖͚̬͚̮͎̭͙͚̩̭͔̘͖͚̩̮̓̒͐͒̓͂̏̒͌͂̏͊̒̒́̒͆̓͌͆̓̒͑͂̒͏̸̸̴̴̸̢̨̡̨̨̭͙͚̫̗̭͚̩̗̮͕̘͙̗͚̩̭͈͙͚̩̰̮͙͚̹̭͉̘͖͚̬̮͓͙͔͚̪̭͎̘͙̮͚̫͚̮͇̭͙͚̺͚̭͓͚̬̮̭͚̤̭͔͓͚̗̮̭͙̯͚͖̭͖̘͙̩͚̪̮̘͙̤͚̪̤̭͓̮͚̫͚̮̘͙͙͚̪̭͚̪̮͔͙͚̹̤̭͕̭͚̮͇̭͙͚͚̭̭͚̬̬̭͍̘͕͚̹̭͓͚̬͖̭͉̭͙͚̩̭͇̘͍͚̬̮͉͓͙͚̭̘͚̭͉̭͙͚̭̭̤͚̬̭͈̘͙͚̤̭͔̘̘͚̮͗͐̓̒̏͊̓͑̓͒̒͑͌͑̒͂͆͒̒͑́̒͌́͌͂͒͒̓̒͒͒̓̒̋̏̓͗̒̓́̓́͌̒͊̒͒͊̒̔̒́̏͒̒͆́͂͆͂͒̒̏͑́̒͂͒͘͏̸̸̘͙͚̫̗̮͓͙̘͚̩̗̭̭͙͚̩̭͉͖͚̹̮͕͓͙͚̫̤̭͍̘͓͚̬̮͎̘͍͚̪̤̭͎̘͙͚͎̮͇̭͙̗͚͎̭͓͚̬̭͈̭͍͚̤̭͓̭͙͚̗̭͖̘͙̯͚̪̤̮͇͙̩͚̩̭͔̭̩͚̬͚̭͓̮͚̪̰̮̘͙̓͒͋̏͊̓̒͊̒̒́́͑̒͆͆̒́͂́̓̒̓̒͒͘ͅ͏͚̮͓͙͚̪̭͙͓͚̹̰̭́͒͐̓̏͊̓͏̴̧̨͓͚̫̭͍̭͙͚̭͖̘͇͚̫͖̮͙͚͖̭͓͙̤͚̬̰̭͉̘͙͚̬̭͇̘͙͚̬̭̒͐͒̓͂̏̒͐̓͌͂͊ͅ͏̘͙͚̭͓͚̮͓͓͙͚̪͚̮̤͚̬̮͈͚̭͔̘͚̮͗́̏͒̒͑́͂͆͒̓̒͒͑̓̒͂͊̒̏͂͒͏̨̭͙͚̫̗̭͚̩̗̭͇̭͚̩͖̭͈̘͚̩̰̮̘͙͚̫̰̭̭͓͚̫͖̭͈̭͙͔͚̭͎̘͙͚̮͇̘͙͚̩̮͒͐̓̒̒̋̒̏͑͒̒́͆͂̔͆͘ͅͅ͏̸̸̴̴̴̨̨̡̨̡͙͚̬̮͖̘͙͚̤̭͔̘͙͕͚̫̭͔͙̯͚̪̭͖̘͙̬͚̩̮̘̩͚̫̭͓̹͚̪̰̮̭͙͚͚̩̭̗͚̪̭͎̭͚̹̤̭͕̭͚̫̮͔͙͚̩̭͍̭͚̬̬̮͔͙͚̫̤̭͓͚̫̭͉̭͙͚̭͇̘͖͚̬̮͉͓͚͚̭̘͚̫̮͕͓͙͚̮͚̬̮͙͚̰̭͔̘͓͚̪̮̓͆̒́̓͒̒̓̒͒͒̓̒̏̒̒̓͒̓̓̒͊̓͌͊̒̔̏͂̏̒̒̑́͑̒͑̓͆͂͂͒̓̒̏͑̓͑́̒͊̕͏̴̸̴̴̵̧̨̭͙͚̪͖̮͓͍͚̩̗̮͕̭̦͚̩͖̭͇̭͚̹̮̭͙͚̹͖̭̭͓͚̬̤̮͓͙͔͚̩̭͎̘͚̬̤̮͇̘͙͇͚̩̭͓͚̬̭͈̭͙͚̤̭͓̭͚̗̭͔̭͙̯͚̮͍͙̩͚̩̰̮̘̩͚̪̭͓̹͚̪͖̮̭͙͚̩̮͓̙͚̪̮͔͙͚̹̰̭͓͙͚̫̭͈͙͚͚̭̭͚̫͚̭͓͙͚̺͎̭͓͙͚̫̰̭͉̭͙͚̬̭͇̘͚̬̮͉͓͚͚̭͓͓͙͚̭̭͙͚̪̗̭͓̭̤͚̬͎̮͎̭͈͚̩̬̭͔̘͖͚̫̰̮̑͒̒̒̒̏͊͒͑̒͑̓̒̒͆͑̒̓͆̏́̒̑́͂͊̓͒̒͒̓̒͒͒͐̒̏̓͗͐͒̓̓͂͌̒͊͒͌͊̒͗̒̑́́͂͌͆̒̒̒͘͏̭͙͏̸̸̵̸̴̨̨̡͚̫̗̮͓͙͚̩̗̭̭͙͚̩̭͇̘͖͚̹̮̭͙͚̫̰̮͓͓͚̬̮͎̘͙͔͚̤̭͎̘͙͚͎̮͇̘͙͇͚͎̭͓͙̹͚̬̮͖̘͙͚̤̭̭͙͕͚̗̭͖͙̯͚͖̮͎͙̬͚̩̮͖̘̩͚̗̭͓̫͚̮̭͙͔͚̭͙͚̪̭͎͓͔͚̹̰̭͕͓͚̫̮͇̘͙͚͚̭͉̭͇͚̫̭͓͕͚̫̭͓͙̤͚̹̭͉̘͙̥͚̭͇̘͙̮͚̬̮͉̭͙̰͚͚̭̭͙͚̫̮͓͙͚̮͔͚̫̮͎̭͈͚̰̭͔̘͕͚̪̮͒͑͋̏͊̒͊͒̓̒͂͂͂́͑͆͊́͑́̓͂̓̒͂̓̒́̓͒́͒͒̓̏̒̒͐͒̓͂̒͊͒̒͂͊̓͂̏́͑̓͒͆͂̓̒͂̒́̒͘͏̸̢̭͙͚͚̭͚̩̗̭͓͚̩͖̭͈̘͖͚̹̭͇͙͚̺̭̭͓͚̬̤̭͈̭͙͔͚̩͎̭͎̘͙͚͎̮͇̭͙͚͎̮́͐̓̒̏͌̒̒͊̓͊͑̒͂́̋́͘͏͚̬̮̭͚̰̭͓͓͚̗̮͖͓͙̯͚̪̰̭̓̒̓͆͒̒̒́̒̑́͏̸̧̘͙̩͚̩̮̘̩͚̭͓̬͚̮̭͙͔͚̭͙͚̪̭͍̘͙͆͒̒͂̓̓̒́͒́͒͒̓̏͏̴̨̨̨͚̹̤̭̭͚̭͈̘͙͚͚̭͈̭͇͚̬̬̭͍̘͕͚̭͓͙̲͚̭͉̭͙͚̩̭͇̘͙̮͚̬̭͐̒̓́̓́̒̒͂͊͂͒͂͏̴̭͚̭͙̥͚̫̭͉̭͙͚̩̭͓̭̤͚̫̭͈̘͙͚̪͎̭͔̘͖͚̮̒́̏͑̓̓͆̓̒͑̒́͒̕͏̭͙͏͚̫̗̮͓͚̩̗̮͕̘͍͚̩̭͈̘͖͚̹̭͈͙͚̺͖̭͉̘͖͚̬̰̮͓͍͚̪̬̭͎̘͚̪̰̮͇̭͙͚̺͚̭͓̥͚̬̮͖̭͙͚̰̭͒̒͂̒͊̒͊̓̒͑̒̒̑͑̒͆͊́͘̕͏̸͚̫̮͈̭͙̯͚̪̰̭̓̒̑͏̴̘͙̩͚̩̮͖̘̩͚̩̭͓̩͚̩̮̘͙͚̺̮͓͙̪͚̪̭͎͔͚̹̤̭͆̒̓̒͆͒͑̏͐̏̓̒͏̴̵̴̨̨̨̨͙͚̫̭͍͓͙͚̩̮͓͇͚̬̭͓͕͚̫̰̭͓͙̲͚̺̭͉̭͙̪͚̩̮͉̭͚̬̮͍̘͚̭͓͙͚̭͎͙͚̩̗̮̤͚̫̮͈͚̹̭͔̘̘͚̬̮̓͒̓͑̒͆͒̒͊̒̔̒̑́̏͑́͂̓͆͒̓̒͑̓̒͂̒́͏̸̢̢̨̘͙͙͚̮͓͚̩̗̮͕̘͚̩͖̭͈͙͚̹̮͖̭͙͚̹̮͖͖͚̬̬̭̭͙͔͚̪̰̭͎̘͙͚̮͇̘͙͇͚͎̮́͒̒̒̋̓͊͒̓̒͌̓͂́͘͏̸̸͚̬̮͖̭͉͚̰̭͔͙͕͚̫̭͙̯͚̪̭̘͙̬͚̩̮͖̘͙̤͚͎̭͓̬͚̮̘͙͙͚̭͙͚̪̭͙̓̒̒͆̒́̓͑̓͂͐͂́̓̒͂͒́͒͒̓̒̏͊̓͏͚̹̤̭͏̨͓͚̮̭͙͚͚̭̒̓́͑̓͂͏̴̡̧̨̘͇͚̬̤̭͍̘͕͚̫̭͓͙͚̗̭͉̘͙͚̮͉̭͙̱͚̬̮͙͚͚̭͓̭͚̫̮͖̭͙͚̪͖̭͈̘̤͚̬̭̘͙͚̹̭͔̘͖͚̪̮̒̒̏͊͂́̏͊̓͂́̒͑̓͆̒̏͌͑͂̒͏̢̭͙͚̪͖̭͚̩̗̭̭̦͚̩̭͈̘͙͚̹̮͗͐̓̒̔͋̒͊͊͏̷̸̴̭͙͚̹͖̭͉̘͓͚̫̭̭͙͔͚̪̭͎̘͙̮͚̬̤̮͇̭͙͚͎̭͓͙͚̬̭͈̭͙̹͚̰̭̭͙͕͚̗̮͎̘͙̯͚̭͕̘͙̩͚̪͖̭͇̩͚̫̭͓̬͚̮̭͙͕͚̩̭͙̦͚̪̭͎͙̬͚̹̤̭̒̓͌͒̏́͑͆́͒́͂͊̓̒̓̒͂̓͒͒̓̏̓͘͏̨̨̨̘͙͚̫̭̘͙͚͚̮͕͓͇͚̫͚̮͔͕͚̹̗̭͓̗͚̺̭͉̭͙̤͚̭͇̘͈͚̬̭͒͋̓́̒̓̒͊̒́̏̒͏̸̨̨̭͙͚̭̭͚̭͎͙͚̪̮͕̤͚̫̭̘͙͚̭͔̘̘͚̫̰̮́̏͒̒͑́͂̓͆̓̓̒͌͑͂̒͏̵̴̸̴̸̨̨̡̭͙͚̪͖̭͚̩̗̭̘̮͚̩̭͈̘͖͚̹̮̭͙͚̹͖̭̘͖͚̫̭̭͍͚̪̭͎̘͚̩͖̮͇̭͙͚̩̭͓͙̹͚̬̭͈̘͙̹͚̰̭͓͚̗̭͖̘͙̯͚͖̮͎͙̩͚̩̬̭͔̭̩͚̭͓̮͚̪̰̮̘͙͚̩̮͓͚̪̭͎̭͚̹̤̭͓͙͚̮͓̘͙͚͚̭͇̭͚̬̰̭͓͙͚̭͓͙̤͚̫̭͉̘͙̤͚̮͉̭͚̬̮͍̘͚͚̭̘͙̥͚̫̭̘͙͚̭̘͚̫̰̭̘͈͚̪̬̭͔̘̘͚̬̮͐͐̓̒͋̒͊̒͊͑͋̒͊͌̒̒̑̋͆͑͆́͒̒͌́͂̓̒́̓̒͒͐͐̒̏̒͐́̓͂̒͊͒͌͂̏͊͆́̏̒̏̒́͑̓͋͆͂͂͊̒͌̒̒̏͘̕̕̕͏̸̘͙͚̭̬͚̩̗̭͇̘̺͚̩͖̭͇͓͚̹̮̐́͐̓̒̒̒̏͊͏̴̸̸̴̸̨͙͚̫̰̭̘͖͚̬̮͎̘͙͔͚̫̗̭͎̘͚̮͇̘͙̖͚̩̭͓͙͚̬̮͖̘͚̤̭͔̭͙͕͚̗̮͖͙̯͚̪̮͇͙̩͚̪̭͇̩͚̪̤̭͓͙͚̪̰̮̘͙͚͚̪̭͙̬͚̪̭͚̹̤̭͕̘͚̫̭͍̘͙͚̮͓͓͚̫̗̮͕͚̭͓͚̹̭͉̭͙̪͚̮͉̭͙͚̬̮͉͓͚̭͔͓͙̥͚̫̮͖̭͙͚̪͖̭̭̤͚̬͚̭̘͈͚̪̗̭͔̘͚̪͚̮̓͌̒̒̑́͆͑͆̒̒́́̓͂̓̏̓̒̓͊͒͒̓̏͊̓̒̑̒̓͒̓́̏̒͊͐̓̒́͂͊̒̔́̏̒̒̑́̏̓͆͑̒͌̒̒͐͘͏̸̸̭͙͚̪͖̭̣͚̩̗̭̘͙̗͚̩͖̭͈̭͖͚̩̰̭͇͙͚̹̮͓͚̬̰̮͓͙͔͚̭͎̘͙͚̮͇̭͙͚̪̭͓͚̬̭͈̘͍͚̤̭͗͐̓̒͋̒̓͊͑̓̒͑́́͊͆͑̒̐͆̒́͘ͅ͏͙͚̗̮̭͙̯͚̪̰̭̓͂́͊͏̴̴̨̧̨̘͙̩͚̪̭͔̭̩͚̩̭͓̫͚͎̮̘͙͚̩̭͓͚̪̮͔͙͓͚̹̤̭͕͓͚̫̮͖͙͚͚̮͕͓͚̫͚̮͔͙͚̫̭͓͙̱͚̫͖̭͉̭͙͚̮͉̭͙͚̬̮͉̘͙̏̒̓̓̒͂͒̐͒̓̒̏̓̒͐͒̓̓͂̒͊̓͌͊́̏͏̸͚̭͓͚̭͍͓͙͚̮͕̤͚̬̮͎̭͙͚̩̭͔̘͖͚̫̰̮́̏͒̒͆́͂͆͂̓̒͒͑͂̒͏̭͙͏̸̸̢̨͚̭̯͚̩̗̮͕̘͙͎͚̩̭͇͓͙͚̹̮͕̭͙͚̺̭͓̭͖͚̬̭̭͍͚̪̭͎̘͙͚̮͇̘͙͚͎̭͓͙͚̬̭͈̭͍͚̤̭͓͙͕͚̫̮͕͓͙̯͚͖̮͕͓͙̩͚̪̭͔̭͙̤͚̩̭͓̹͚̫͚̮̭͙͚̭͙͓͚̪̮͔͚̹̰̭́͐̓̒͊͊͊̒͆͌̒͂̓͂͊́͑͆͆̒́͒͂̓͂̓̒͒͒́͒͒̓̏̓̒͐͘͏̸̸̨̨̘͙͚̮͔̭͙͚̗̭͇̭͇͚̫͎̭͍̘͙͚̺̭͓͙̤͚̫̭͉̘͙͚̭͇̘͙̳͚̬̭́̓́̒͌͊͆̈́͂̏͏̵̡̭͙͚͚̭̘͙͚̮͖͙͚̪̗̭͈̘͚̫̤̭̘͈͚̬̭͔̘͕͚̬̮͂́͒́͂̓͆̒͌̒͂̒́͏̸̭͙͚̪͖̮͓̯͚̩̗̭͓̺͚̩͖̭͍̘͚̹̭͎̘͙͚̹̭͈̘͓͚̫͖̭̭͍͚̫͚̭͎̘͙͚̮͇̭͙̘͚̪̮͐͒̒͌̒̒̏͊̓̒͌̒͂͂͆͘͏̴̸̡͙̳͚̬̮͙͚̰̭̭͙͚̗̮͓͙̯͚͖̮͓͙̬͚̪̭͇̩͚̗̭͓̬͚̮̭͙͚̪̮͓͚̪̭͎̭͙͚̹̰̭̓͆͑̓́͒͂́͊͂͐͒̓̒͂̓̒́̓͒͒͐̒͑̏͏̸̷̴̸̴̨̨͙͚̫̮͕̭͙͚͚̭͈̭͇͚̬̬̭͍̘͕͚̬̭͓͙͚̺̭͉̭͙͚̬̮͉̭̘͚̬̮͉̭͙͚̭͙̥͚̫̭͉̭͙͚̮͔̤͚̫̬̭͈̘͈͚̹̭͔̘͓͚̗̮̓͒̓́̒̒͊̓̈́̒́̏͑̓̓͆͂͂̓̒̒̒͂͏̴̢̭͙͖͚̫̗̮͓̰͚̩̗̮͕̘͙̗͚̩̭͈̘͙͚̹̭͓͓͙͚̺̮͓͖͚̬̭̭͙͔͚͚̭͎̘͙͚͎̮͇̭͙͚̩̭͓͚̬̭͈̘͚̰̭͒̒͊͊͊̓̒͌́́͆͑̒̏͆̒̒́͘̕ͅ͏̸̴͙͕͚̫̮͉̘͙̯͚̪̰̮͙̬͚̪͖̮̘͙̤͚̗̭͓̬͚̩̮̘͙͔͚̪̭͚̪̭͎͚̹̤̭̓͊̓͒͂̓̒̏͒͒̓̒̔̏̓̒͐͏̸̴̨̨̡͓͙͚̭͍͙͚̮͖͓͚̫̗̮͔͙͚̹͖̭͓͙̱͚̫̰̭͉̘͙͚̬̮͉̭͙͚̬̮͍̭͚͚̭͔͓͚̮͖̭͙͚̩̗̮͖͚̫̭̘͈͚̭͔̘͚̗̮́̓̓́̏̒͊̓͌͊̏̒͐́̒͑́͂͆̓̒͂͌̒͂̏̒̏͂ͅ͏̸̸̭͙͚̮͓͙͚̩̗̭͇̘͙͚̩̭͎͓͖͚̹̮͕̭͙͚̺̮͔͖͚̬̮͎̘͙͔͚̭͎̘͚̩̮͇̭͙͈͚̩̮͗͂͒͒̏͊̒͊͊̓̒͂͒̒̑͆͆͘͏̸̸̴̨̨̢̨͎͚̬̮͖̭͚̰̭͔͚̫̭͙̯͚̩̤̮͙̬͚̩̮̘͙̤͚͎̭͓͙͚̪̮̘͙͚̪̭͚̪̮͔͔͚̹̰̭͖̭͙͚̮͙͚͚̭͍̭͚̫̗̭͓͕͚̹̭͓̗͚̬͖̭͉̘͙̥͚̮͉̭͙͚̬̭̓̒͆̒̒́̓̒͌͑̓͊̓͒́̓͊͆͒̐͒̓̒͌̏̓̒́͑̓̓͂̒͊͒̒͊͊̒͂̏͏̡̨̘͙̰͚͚̭͓̘͚̫̮͕̘͙͚̪͚̮͕͚̫̭͈̘͈͚̰̭͔̘͓͚̫̮́̒͆̓͆̓̒̒́̒͆͏̸̸̢̘͙͈͚̭͙͚̩̗̮͕̭͙͚̩̭͈̭͙͚̩̰̮͙͚̹̮͔͓͚̫̭͈̭͙͔͚̪̭͎̘͙̯͚̫͚̮͇̘͙̙͚̩̮͂͐̓͌͊͊͐̓͒̓̒̏͆͘͏͙͚̬̮̭̖͚̰̭̘͙͕͚̗̮͓͙̯͚̭̘͙̩͚̪̗̮̘͙̤͚̩͎̭͓̩͚̫͚̮̭͙͔͚̭͙͚̪̭͎͚̹̤̭̓̈́͆͒̒́͒́͐͂͊͒͒̓̒͒́͒͒̓̈́̏̓̒̕͏̨̨̘͙͚̭͉̭͙͚͎̮́̓́͏̴̨͓͇͚̫̗̮͔͙͚̬̭͓͙̱͚̬͖̭͉̘͙͚̬̭͇̘͚̬̮͍̘̙͚͚̭͓͙̥͚̮͙͚̪̗̮̤͚̬̮͙͚̩̭͔̘͕͚̗̮̒̓͌̓͊͆̒͌̒́͑́͂͐̓͆͐̓̒̏͑̓͑͂̒͂͏̸̭͙͚̭͙͗͂͐̓͏̢͚̩̗̮͕̭͚̩̭͍̘͙͚̹̭͍̘͙͚̹͖̮͖͓͚̬̮͓͍͚̭͎̘͙͚̩͖̮͇̘͙̖͚̪̮̒̋͊͊̓̒͂͑̒́͂͆͘ͅ͏̸̴̴̴̴̸̨̨̗͚̬̮̭̖͚̤̭͓͙͕͚̫̮͇͙̯͚͖̮͙̩͚̪̭͔̭̩͚̭͓̹͚̫͚̮̘͙͈͚̺̭͚̪̭͓͙͚̹̤̭͔̘͚̫̭͎͓͙͚̩̮͓͚̬̮͕͚̫̬̭͓͙͚̬͖̭͉̘͙͚̬̭͇̘͚̬̮͚̭͔̭͚̮͓̭͙͚̭̭̤͚̬̭̘͙͚̹̰̭͔̘͙͚̮̓̒͆͒̒́͑̓͂͋̓̓̒́͂̓̒͒̏͒̓̒̏͊͂̒͐͒̓͐̒͊͐̓̒͊̈́̒͐͊̓̒̑́̏̒͆́͂͆͂͒̒̓͌͑͂͒͘͏̘͙͚͚̪͖̮͓͙͇͚̩̗̭͇̘̺͚̩̭͎̘͚̩̰̭͍̘͙͚̫̤̭͓̭͖͚̬̬̮͎̘͙͔͚̪̬̭͎̘͙͚̬̤̮͇̭͙͚̪̮͒̒͊̒̏̒͋͆͘ͅ͏̴̸̨̨̨͙͚̬̮͓͚̰̭̘͚̗̮͓͙̯͚̪̮͎͙̬͚̪͖̮͖̘͙̤͚͎̭͓̫͚̪̮̭͙͚̪̮͓͚̪̭͎̭͚̹̤̭͕̘͙͚̫̭͈̘͙͚͎̭͇̭͇͚̬̭͍̘͕͚̫̭͓͚̭͉̭͙̦͚̩̭͇̘͙̤͚̬̭̓̒͆͒̒͑́͒̒͌́͊̓͂̓̒͆͒͒͐̒͌̏̒̑͒̓́̒͂̒̏͊̒̔́͂͏̵̸̘͚͚̭͓͙͚̫̭̭͙͚̪͚̭̘̤͚̬̭͈̘͈͚̹̭͔̘͓͚̬̮̒́͑̓͋͆͊̒͊̒̒́͘͏̸̴̘͙͚̫̗̮͓͙͚̩̗̮͕̭̲͚̩̭͍̘͚̹̭͖͙͚̫̤̮͕͖͚̫͎̭̭͍͚̬̭͎̘͙͚̮͇̭͙͚̪̭͓͚̬̮͉͚̤̭͓͙͚̫̮͖̭͙̯͚̪̤̭͕̘͙̬͚̪̭͔̭̩͚̩͎̭͓͚̪̰̮̘͙͚̩̮͓͚̪̮͔͓͚̹̰̭͒͒̔̒͊̒̏͊̓̓̒͌̒͂̈́́̓̔͆͑̒͌͆͑̓̒́͒͂͒̒̓̒͂͒͗͐̒͌̏̒͘̕͏̨̨͚̫̭͇̘͙͚͎̭͈̭͚̫͎̭͍̘͙͚̫͚̭͓͚̫̰̭͉̭͙͚̩̮͉̭͙̺͚̬̮͙͚̭̓̒͐͒̓́̒͊͌͊̒̔͂͊̓͗́̏͏̸̸̡͚̫̮̘͙͚̭̘͚̫̮͈͚͖̭͔̘͖͚̪̮̓̒͑̓͒͆͂͋̒͑̓̒͂̒͊͏̢̢̨̭͙͚̫̗̭͚̩̗̮͕̘͚̩̭͎͙͚̩̰̭͍͓͙͚̹̭̘͖͚̫̮͎̘͙͔͚̫͖̭͎̘͙͚̮͇̭͙͚͎̮͑͐̓̒̒͊̓̐͒͊̒͂́̓̓́͘͏̴̨̨̨͚̬̭͈̭͍͚̰̭͔̭͚̗̭͙̯͚͖̮͖͓͙̩͚̪̮̘͙̤͚̩̭͓̹͚̮̭͙͓͚̩̭͙͓͚̪̮͔͚̹̰̭͕͙͚̮͓͙͚͎̭̓̒͂͆̒́̒͌́͑̓͂͒͒͂̓̒͂͒͒̓̏̓̒̑̓́̓̓́͏̴̨̘͚̫͎̮͔͕͚̬͚̭͓͙̤͚̹̭͉̭͙͚̬̮͉̭̗͚̬̭̒͊̓̒͊̓͆̒͏̭͙͚̭͓̘͙̥͚̫̭͓͙͚̪̗̭͓̭̤͚̬̮͎̭͈͚̰̭͔̘͕͚̗̮͗́̏̓͋͆̒̏̒͂̒͂͏̸̴̨̭͙͚̪͖̮͓̯͚̩̗̭̺͚̩͖̭͇̘͖͚̩̰̮͕̘͙͚̺̭͍̘͖͚̬̮͎̘͙͔͚̭͎̘͙̯͚̩̮͇̭͙͚̩̭͓͙̥͚̬̭͈̘͙͚̤̭͔͚̗̮͇̘͙̯͚̩̰̭͕̘͙̬͚̩̮͖̘̩͚̗̭͓̬͚̮̭͙͈͚̭͙͚̪̭͙̰͚̹̰̭͖͓͚̫̮͔̭͙͚̩̭͐͒̒͋̓̒̒͊̒́̓͆͆͑͆̓́̓̒̑́̒͂̓̒́̓͒́͒͒̓͒̏͊̓̒͐͒̓͘̕͏̷̸̴̨̨̡̘͇͚̬̰̮͕͚̬͖̭͓͙͚̺̭͉̭͙̥͚̩̮͉̭͚̬̮͉̘͙͓͚̭͓̭͚̫̭̭͙͚̮͚̬̮͙͚̪̭͔̘͖͚̗̮̒͐̓̒͊̓̒͋́̏̒͑̓͋͆͂͑̓̒͒͑̓͑̒͂͏̸̸̸̶̭͙͓͚̮͓͉͚̩̗̭͓͙͚̩̭͈̘͙͚̹̭͈̭͙͚̹̮͓͓͚̫͚̮͎̘͍͚̩̭͎̘͙͚̩̮͇̭͙͚̺͚̭͓͚̬̮͖̘͙͚̤̭͔̭͚̫̭͓͙̯͚̪̰̮͎͙̩͚̩̮͖̘̩͚̩̭͓͙͇͚̮̭͙͚̺̮͓͙͚̪̮͔͓͚̹̤̭͂͒̒͌͊͊̐͊̓̓̒̒͆̈́̏̔͑̒̒͆̒́̒͌͒̓͆̒͆̓͂͒͗̏͐̏̒͘͘͏̴̴̵̸̨̧̡̨͓͙͚̫̮͈͓͙͚̩̭͍̭͇͚̬̮͔͙͚̹͖̭͓͙̱͚̫̭͉̭͙͚̬̭͇̘͙͚̬̮͍̘͙̬͚̭̭͙͚̭͈͓͙͚̩̗̮̤͚̫̰̮͈͚̹̭͔̘͚̪̮͒̓͆̒̓͌͊͆́̏͑́͂͆͒̓̒͑̓̒̒̏͊͏̴̢̘͙͚̪͖̮͓̩͚̩̗̭̘͙͚̩͖̭͈̭͙͚̩̰̭͕͓͙͚̺͖̭͓̭͖͚̬̮͓͙͔͚̪̬̭͎̘͙͚̫͚̮͇̭͙͉͚̪̮̒͒̒͋͒̒͑͆͘ͅ͏͙̹͚̬̮͖̭͚̤̭͔̘͙͕͚̗̮̓͆̒̋́́͏̸̴̨̨͓͙̯͚̩̰̭̘͙̬͚̩͎̭͇͙̤͚̩̭͓̬͚̮̭͙͔͚̩̭͙͖͚̪̭͎͓͙͚̹̤̭͐̓̓̒͂͒͒̓̏͏̴̸̨̭͚̫̮͇͙͚͚̭̭͚̫̭͓͙͚̬͚̭͓͙̲͚̺͎̭͉̘͙̦͚̬̭͇̘͍͚̬̮͉͓͚̭͔̭͚̭͓͙͚̪͚̮͕̤͚̫̭͈̘͙͚̪͖̭͔̘͙̥͚̬̮̒͐͒̓̓͂͌̒͊͒͒͌͊̒̒͐́̏̒͑́͂͑͆̓̒͑͂͏̸̵̭͙͚̮͓̦͚̩̗̮͕̭͙͚̩͖̭͇͙͚̩̰̭͈͙͚̹͖̮͕͖͚̬̮͎̘͙͔͚̭͎̘͙̮͚̪̮͇̘͙͈͚̩̭͓͚̬̮̭͙͚̰̭͔̭͙͕͚̗̭̐́͒̒͒̓̐̓̓̒͂͂͒͆͆͑̒͌͆͒́́͘͏̴̵̸̸̨̡̨͙̯͚͖̭̘͙̩͚̪̭͇̩͚͖̭͓͙͇͚͎̮̭͙͚̺̭͙̲͚̪̭͎͓̙͚̹̤̭͖͚̫̮͖̭͙͚̩̭͖̘͇͚̬̤̮͔͕͚̭͓̗͚̫̭͉̭͙̪͚̮͉̭͖͚̬̮͙̰͚̭͔̭͙͚̫̭͙͚̭̘͚̬̭͈̘͈͚̪̭͔̘͙͚̮̓͂͐̓̓̒͂̓́͒͑̏͒̓̏̒̓̒̓͒̓̒̓̒͂̏͊̒͆͂̏̒͊̓́̏̓͒̓͆͂͌̒͒̒͂͂͏̸̭͙͚͚̫̗̭͚̩̗̭̘̺͚̩͖̭͎͓͖͚̩̰̮͖͓͙͚̹͖̮͕͓͚̬̭̭͍͚̭͎̘͙͚͎̮͇̭͙͉͚͎̮͐̓̒͂͋̒̒̓̒͌̒́͂̈́͂́͘͏̸̴̸̨̨̨̨̖͚̬̮̭̖͚̤̭͙͚̫̮͇͙̯͚̪̰̭͕̘͙̩͚̩̬̮̘̩͚̪̬̭͓̹͚̪̰̮̭͙͚̮͓͙͚̪̭͓͙͚̹̤̭͔̘͚̭͙͚͎̮͓͓͚̬̰̭͍̘͕͚̺̗̭͓̗͚̺̭͉̘͙͚̬̭͇̘͙͚̬̮͍̭̙͚̭͔̭͚̮̘͙͚̭̭̤͚̬̭̘͈͚̭͔̘͕͚̫̮̓̒͆͒̒́͑̓͂̓͒̒̓̒͒̑́͒͐͐̏͊̒̓́͋̓̓́̒͊̒͊̒̓̈́̒́̏̒͑́͂͑͆͂͂͒̒̓͌̒́̒͆͏̶̴̡̭͙͚̪͖̭͚̩̗̭͇̘͚̩͖̭͎͚̩̰̭͎̘͙͚̺͖̮͓͚̫̭͈̭͍͚̩͎̭͎̘͙͚̮͇̘͙͚̺͚̭͓͙̹͚̬̭͈̘͙͚̤̭͔͓͙͚̗̭͔̭͙̯͚̩̰̮͙̩͚̪͖̭͇̩͚̩͖̭͓̹͚̩͖̮̘͙͚̩̭͔͚̪̭͎̭͙͐͐̓̒̒̈́̓̒̏͑̓̒̏̒́̓͑͆́͂́͊̓̓̒̓̒͒͗͒̓̒̏͘̕ͅ͏̨̨̧̨͚̹̤̭͖͚̮͓͙͚̭͍̭͚̫̮͕͚̬̭͓͚̺̭͉̭͙͚̮͉̭͙̗͚̬̭̓̒͐́͑̓́̏̒͊͒͐̓̒́͊̒̔͂̏͏̸̴̭͚͚̭͓͙̥͚̫̭͙͚̩̗̮̤͚̬͚̭̘͈͚̹̭͔̘͖͚̪̮̒́͒̓͋̓͆͒̓̒͌̒̒͘͏̸̴̸̴̡̨̨̨̨̡̨̭͙͙͚̭͚̩̗̮͕̭̦͚̩̭͎͓͚̹̮̭͙͚̹̭̘͓͚̫̮͎̘͙͔͚̪̤̭͎̘͙͚̮͇̭͙͚͎̭͓͚͚̬̭͈̭͙͚̰̭͓͓͙͚̗̮͓͙̯͚͖̮͇͙̩͚̩̤̮͖̘̩͚̪̰̭͓̮͚̫̮̘͙͚̩̮͓͙͚̪̭͍̘͙͚̹̤̭͕͚̮͔͙͚̭͍̭͚̫̮͔͙͚̫̭͓͙̱͚̭͉̭͙̦͚̭͇̘͙͚̬̮͉͓͙̬͚͚̭͓͓͚̫̮͓͙͚̪̗̭͓̭͚̫̰̭̘͈͚͖̭͔̘͙͚̩̮͂͐̓̒̒͊̒̏͊͒͊͌̒͒̈́͂͌́͑̒͆̏́͂́͊͂̓̒̓̒͊͒̓͐̏̓̒͐́̓̓͂̏̒͊̓̓͌̏͊́͂́̏̒́̒͑̓̓͆̒͌̒͂͘͏̸̸̴̴̨̡̧̨̨̭͙͚̪͖̭͚̩̗̭̭̲͚̩͖̭͎͓͖͚̹̮͕͓͙͚̫̰̮͔͖͚̫͖̮͎̘͍͚̩̭͎̘͙̮͚̮͇̭͙͚̪̭͓͙͚̬̮͖̘͙͚̰̭͙͚̫̭͔̭͙̯͚̪̤̮͍͙̬͚̩͎̮͖̘͙̤͚̬͖̭͓͚̬̤̮̭͙͕͚̩̭͙͚̪̭͎͓͔͚̹̰̭͖̭͚̫̭͈̘͙͚͚̭͈̭͇͚̫̭͍̘͙͚̹̭͓͙͚̬̭͉̘͙͚̩̮͉̭͈͚̬̭̐͐̓̒́͋̒̒͊̓̒̒͂̔͆͑̓͆̏́͑̓͂̓̓̒͂͒͒̓̏̒̒̓͒̓͂̒̏͌͒͊̏̒͘͏̸̘͚̭͙̥͚̭͈͙͚̮̤͚̬̗̭̘͈͚̩̬̭͔̘̘͚̬̮̒́̏͑̓́͂̓͆͂͑̓̒͌̒̒͂͘͏̸̸̴̢̭͙͚̫̗̮͓͙̖͚̩̗̭͓͙͚̩͖̭͇̭͙͚̩̰̮͕͓͙͚̺̭̭͓͚̫̭͈̭͙͔͚̪̬̭͎̘͙̯͚̫̮͇̭͙̘͚̺͚̭͓̙͚̬̮̭̖͚̰̭͙͚̫̭͙̯͚̪̰̮͎͙̩͚̩̤̮͖̘͙̤͚̩̭͓̬͚̩̮̭͙͚̭͙͚̪̭͍̘͚̹̤̭̭͙͚̫̮͔̭͙͚̩̭̐͒͌͊͊͒̒͊͊͑̒͆͒̒́͒̓͂͐̓̓͂̓̒̏͒͒́͒͒̓͒̏̒̑͐͒̓͘͏̴̸̨̨̘͚̫̭͍̘͕͚̬͖̭͓͙͚̹̭͉̭͙̥͚̩̮͉̭͈͚̬̭̒͊̓̒͊̒͏̘͙͏͚͚̭́͏̵̡͙͚̮͙͚̪̮͚̬̭̘͙͚̹͎̭͔̘͚̬̮̓́͂͑̓͆̓͒̓̒͊͌͑̒͐́͏̸̭͙͕͚̫̗̮͓͚̩̗̭̭͚̩̭͈͖͚̹̭͈͙͚̺͖̭̘͖͚̬̰̮͎̘͍͚̪͚̭͎̘͙͚̪̮͇̘͙͚̩̭͓̗͚̬̮͖̭͙͚̰̭̘͙͕͚̫̭̘͙̯͚̭͒̒̏͋̒̋͊̓̒͊̓͊̒̒̈́͆͌͆͑̒͆͊́͒͑͂͊͘͏̘͙̩͚̪͖̭͇̩͚̪͖̭͓͙͇͚̮̘͙͈͚̺̭͙͖͚̪̮͔͓͔͚̹̤̭̓̒̓́̓͒̏͒̓̏̒͏̴̴̴̨̢̨͓͚̫̭͎̘͙͚͚̮͓͇͚̬̭͍̘͕͚̭͓͙͚̹̭͉̘͙͚̬̭͇̘͙͚̬̮͍̭͙͚̭͚̭͙͚̩̗̮͕̤͚̫̰̭͈̘͈͚̭͔̘͚̬̮̒̓͒̓͂͑̒͂̒́͂͊͆́̏͒̓̒͑́͂͑̓͆̓̒̒́͒̒͐͂͏̢̭͙͚̫̗̭͙͚̩̗̮͕̘͚̩̭͎͙͚̹̮͗͐̓̏̒̋͊̓͊͏͓͙͚̺̮͓͓͚̫̮͎̘͙͔͚̫͚̭͎̘͙͚̪̰̮͇̭͙͚̺͚̮͊̓̒͊̈́͊͘͏̸̸̴̸̨̡̨̧̨̡̨͚̬̮͍͚̤̭͓͙͕͚̫̮͙̯͚̪̭͖̘͙̬͚̪̮͖̘͙̤͚̩̭͓͙͇͚̮̭͙͖͚̪̮͓͙̰͚̪̮͔͓͙͚̹̰̭͕͚̫̭͎̭͙͚̩̭͇̭͇͚̬̬̭͍̘͕͚̭͓͙͚̬̭͉̭͙͚̩̮͉̭͙͚̬̮͉͓͙͚̭͓̭͙̥͚̫̭͙͚̩̗̭͉̘͚̫̮͙͚̹̭͔̘͓͚̪̮̓̒̐͆͑̓̒́͑͌̓̓̏̓́͒͐̏͂̓̒̓͒̓͆̒̒͂͊͊̏̓͗́̏̓͋̓͆̒͑̓͑̒͊͏̘͙͙͚̪͖̮͓̭͚̩̗̭͇̘͙̗͚̩͖̭͇͖͚̹̭͕͙͚̹͖̮͓͚̫̮͎̘͙͔͚̩̭͎̘͙͚̪̮͇̘͙͇͚͎̮͒̒̓̒͊̓͑̓̒͊̓͂͆́͘͏̡͚̬̭͈̭͚̰̭̭͙͕͚̗̭͔̭͙̯͚̪̰̭͕̘͙̩͚̪̭͔̭̩͚̬̗̭͓͙͇͚̩̮̭͙͕͚̭͙̳͚̪̮͔̙͚̹̤̭͖̭͚̫̮͖̭͙͚͚̭̓̒͆̒̒́͒́̏̒̓̏͒́͒͒̓̏̓̒̒͐͒̓́͏̴̢̨̘͚̬̬̭͓͙͚̬̗̭͓̗͚̬̰̭͉̭͙̦͚̬̮͉̭͙͚̬̭̒͊͒͌͊̒͏̡̭͚̭͓͚̭̭͙͚̪̗̭̭͚̬͎̮͙͚̗̭͔̘̘͚̬̮̒́̏͒̒͑́͂͊͆͒̒͑̓͑͂̒̏͘͏̢̘͙͚̫̗̭͙͚̩̗̭̘̺͚̩͖̭͍̘͙͚̹̭͓͙͚̹͖̮͕͓͚̬̤̭͈̭͍͚̭͎̘͙͚̩͖̮͇̭͙͚̺͚̮̓͐̓̐͋̒͊͋̓̒̒́͂̋͘ͅ͏̵̸̸̴̴̴̨̨̨̡̗͚̬̮̘͙͚̤̭͓͙͕͚̫̮͎͙̯͚͖̮͎͙̩͚̪̭͔̭͙̤͚̪̭͓̫͚̩̮̘͙͈͚̺̭͚̪̭͓̙͚̹̤̭͔̘͙͚̭̘͙͚̭͉̭͚̫͎̭͍̘͕͚̫̬̭͓͚̹̭͉̘͙̦͚̬̮͉̭͚̬̮͍̭͙̰͚̭͓̘͚̫̭͉̭͙͚̪̗̮͚̫̮͎̭͈͚̭͔̘͕͚̩̮̓̒͆͒́͑̓͂̓̓͒̓̒̏͒̏͒̓̒̐̏͊̒́͋̓͂̏̒͊̒͊̒̔̒̏́̏̒͑̓͆͑̓̒͂̒͂̒͏̭͙͚̪͖̭̺͚̩̗̭͓̲͚̩͖̭͎͚̹̭͓͓͙͚̹͖̮͔͓͚̫̭̭͙͔͚̪̬̭͎̘͚̩͖̮͇̭͙͚̪̮͐͐̓̒͌̒̓̒̏͊̓̒̓͌̒̑͋͆͘͏̴̴̨̨͚͚̬̮͓͉͚̰̭̘͚̗̮͉͓͙̯͚͖̮͙̬͚̩̰̮̘̩͚̩͖̭͓̹͚̪͖̮̭͙͈͚̺̭͔͚̪̭͎̭͙͓͚̹̤̭͖̭͙͚̫̭͈̭͙͚̩̮͓͚̫̭͓͕͚̹̰̭͓̗͚̗̭͉̭͙͚̬̮͉̭͙͚̬̭̓̒͆͒̒́͒̒͌́͂͋̓͒̒̓̒͒̏͒̓̒̏͒̓͑̒͊̏͒̒͊̒͂́̋͏̘͚͚̭̒͐́͏͚̭̘͙͚̭͍̘̤͚̬͚̮͎̭͈͚̪̭͔̘͖͚̩̮̓̒͆́͂͐͆͂͂̒̒̏̒͊͏̸̸̴̴̢̨̨̨̘͙͚̮͓̦͚̩̗̭̘͙̗͚̩͖̭͈̭͙͚̩̰̮̘͙͚̹̮͖͚̬̤̭͈̭͙͔͚̭͎̘͚͎̮͇̘͙͚̺͚̭͓͚̬̭͈̘͍͚̰̭͓̘͚̗̮͉̭͙̯͚͖̮͓͙̩͚̪̭͔̭͙̤͚̗̭͓̹͚̩̮̘͙͚̩̭͎͚̪̭͍̘͚̹̤̭͕͓͙͚̫̮͈͙͚̩̮͔͓͇͚̬̰̭͓͙͚̺̭͓͚̺̭͉̭͙͚̩̭͇̘͙͚̬̭͑́͒̒͋͑͊͑̓̒́̒̑͂̏͑̒͆̒́̒͌́͂͐̏͂̓̒͆͒̐͒̓̒̏̒͌͒̓̓͆̒͒͌͊̒̔̓͂̋͘͘͏̘͔͚̭̒́̏͏̡͚̫̮͙͚̪̭͍̘͚̫̬̮͎̭͈͚̭͔̘̘͚̮̓̒͑̓͑̓͆̓̒̒́͊̒́͒͏̢̨̘͙͓͚̪͖̭̥͚̩̗̭̘͚̩͖̭͍͓͖͚̩̰̮̘͙͚̺̮͖͖͚̫̮͎̘͙͔͚͚̭͎̘͙̯͚̪͖̮͇̭͙͚͎̮͐̓̒͋̒̒͑͊̓̒́̓́͘͏̸̴̨͙̪͚̬̭͈̭͍͚̤̭͓͙͕͚̫̮͕͓͙̯͚͖̮͖͓͙̩͚̪͚̮̘͙̤͚̩̭͓̹͚̮̘͙͕͚̩̭͙͓͚̪̮͔͚̹̤̭̓͆̒́͒͂͒͂̓̒͂͒͒̓̏̓̒͐͏̸̴̨̨͚̮͔̭͙͚̗̭͈̭͚̬̤̮͔͙͚̺̭͓͙̤͚̹̭͉̭͙͚̬̭͇̘̓̒̓́̓́̒͊̓͌͊̒ͅ͏̸̨͚̬̮͉̘͚̭͓̭͚̭͈͓͙͚̮͓̤͚̬̭̘͙͚̪͚̭͔̘͚̩̮̒͐́̏̒͑́͂͆͂̓̒͊͌͑̒̏͊͏̸̢̭͙͚̮͓͚̩̗̭͇̭͙͖͚̩͖̭͈̘͙͚̹̭͙͚̺̮͓͓͚̬̤̮͓͍͚̫̭͎̘͙͚̪̰̮͇̭͙̘͚̺͚̭͓͙̪͚̬̮̘͉͚̤̭͔̭͚̗̮͕̘͙̯͚̪̤̭̒́͒̒͊͐̓͊̓̒͑̒͂̓͑͆͒̒́̒̑́̕͘͏̴̴̨̨̘͙̬͚̩̮͖̘͙̤͚̪̭͓̩͚̩͖̮̭͙͔͚̪̭̖͚̪̭͓͙͚̹̤̭̭͚̫̮͔̭͙͚̩̮͓͓͚̫̮͔͙͚̹̭͓͙̱͚̹̭͉̭͙͚̭͇̘͙̯͚̬̭͒̓̒͒͒̓̒̏͊͗͐̒̓͒̓̒͊͊̓͌͊͊̓̈́́̏͏̡̘͙͚͚̭͓͚̫̭͓͙͚̭͍̘͚̬̭̘͈͚̹͎̭͔̘͚̬̮͗́͒̒͆̓͊͆͂͂̒͊͌̒̒͐́͏̸̵̸̸̴̨̨̨̭͙͕͚̪͖̭̘͚̩̗̭̭͙͎͚̩͖̭͍͓͖͚̹̭͉͙͚̺͖̮͖͓͚̫͚̮͎̘͍͚̭͎̘͚̩͖̮͇̭͙͚̪̭͓͙̤͚̬̮͓͙͚̰̭͙͚̫̭̭͙̯͚̪̤̮͖͓͙̩͚̩̤̮͖̘̩͚̪̬̭͓̬͚̩̮̭͙͙͚̮͓͍͚̪̭͎͓͙̬͚̹̰̭͕̭͙͚̮͕̘͙͚̭͍̭͚̫̮͙͚̺̭͓̗͚̬͖̭͉̭͙͚̬̭͇̘͙͚̬̮͙͚̭͓̘͙̥͚̭͙͚̪͚̭͓̭̤͚̫̤̭͈̘͈͚̭͔̘͚̩̮͐̓̒͋̒͊̓̓̒̒́̒̒͆͑͆͒́͑̓͂͑̒̓̒̏͒́͒͐̒̏́̓́̏̒͊̏͐̓͌̓͊̒̈́́͊̓́̏́͂͑̓͆̒̒́͒̒͐͊͘̕͏̴̘͙͚̪͖̮͓͚̩̗̭̘͙͚̩͖̭͎͙͚̩̰̭͈̘͙͚̹̮͔͖͚̬̮͎̘͍͚̭͎̘͚̫͚̮͇̘͙͚̪̮̓͒̒́͋̏̓̐̓̓̒̒́͆̒̒̋͆͘͏̸̸̨̨̡͚̬̭͈̘̖͚̤̭͙͕͚̫̮̭͙̯͚̩̰̮͍͙̩͚̪̭͇͙̤͚̩̭͓͙͇͚̪̮̭͙͓͚̭͙̳͚̪̮͔͚̹̰̭͖̭͚̮͓͓͙͚͎̭͎̭͚̫̮͕͚̹̭͓̗͚̫͖̭͉̘͙͚̮͉̭͙̭͚̬̮͙͚͚̭̘͙̥͚̮̭͙͚̪͖̮͔͚̬͖̭̘͙͚̩̭͔̘͚̩̤̮̓̒̐͆̒́͒̓͊̓̏̓͆̓͆͒́͒͒̓̏̓̒̒͐́̓́̒͊̏͐̓̒͒͊̒͂͂̏͊̓́͑́͂͑͆̓̒͌͑͊̒͐̕͏̸̸̴̴̴̵̨̨̘͙͓͚̪͖̭̙͚̩̗̮͕̘͍͚̩͖̭͎̘͚̩̰̭͓͙͚̹͖̭̭͓͚̫͎̮͓͙͔͚̫͖̭͎̘͙̮͚̩̮͇̘͙̘͚̪̭͓͚̬̮͙͚̰̭͓͙͚̫̭̭͙̯͚̪̰̭͕̘͙̬͚̩̭͇͙̤͚͖̭͓̩͚͎̮̭͙͚̩̭͚̪̮͔͓͚̹̰̭͚̫̮͔̭͙͚̩̭̘͚̫͎̭͍̘͕͚̫̬̭͓͙̱͚̫̭͉̘͙͚̬̭͇̘͙͚̬̮͍̘͙͚͚̭̘͙͚̮͙͚̪̮̤͚̫̮͙͚̩̭͔̘͚̮͐̓̒̒̒̏͋͑̒͑̏͆͑̒͊͆͑̓̓́͑͂͑̓́̓̒́͒͐͒̓̒͌̏̒͐̓̒̓͒̓͆͐̒͊̒͊͆́̋́͑́͂͐̓͆̓͐̓̒͑̓͑͂̒͐͂͂͘̕͏̸̭͙͚̭͙̐͂͐̓͏͚̩̗̭̘͙͖͚̩͖̭͎̘͙͚̩̰̭͓̘͙͚̹͖̮͕͓͚̬̬̮͎̘͍͚̭͎̘͚̮͇̭͙͉͚̺͚̮͋̐̓̒̒͂̓̒̒́̓͘͏̴̨̨̨͙͚̬̮͖̭͚̤̭͔͓͙͕͚̗̮͕̘͙̯͚̪̰̮͈͙̬͚̪͚̮̘͙̤͚͖̭͓̹͚̪̰̮̘͙͕͚̪̮͓͙͚̪̭͚̹̤̭̭͚̭͙͚͎̭͇̭͇͚̫̮͕͚̺̗̭͓͚̫̰̭͉̘͙̦͚̭͇̘͙̺͚̬̭̓́͆̒͑́́̓͒́̓̒͒͐͐̏͊̓̒͐̒͐́͋̓̓́̒͐̓̒͊̒̔́̏̕͏̵̨̘͚̭̘͙͚̫̭͉͓͙͚̪̮͕̤͚̬̗̭̘͙͚̪͖̭͔̘͙͚̮̒͐́̏͒̓͆̓̓̒͌͑͂͒͏̢̘͙͚͚̫̗̭̹͚̩̗̭͇̘̮͚̩̭͎̘͙͚̩̰̮̭͙͚̫̤̭͓̭͓͚̫͚̮͓͙͔͚̪̬̭͎̘͚͎̮͇̘͙̙͚̩̮͐̓̒̒͊͐̒͑̒̑͂͆͘͏̸̨̨͚̬̮͖̭͚̤̭͔̭͙͕͚̫̭͖͙̯͚͖̭͕̘͙̩͚̪͚̭͔̭̩͚͖̭͓̮͚̩͖̮̘͙͚̺̭͙̩͚̪̭͎̭͚̹̤̭͖̭͚̫̮͇͓͙͚͚̭͎̭͚̫̮͔͙͚̬͎̭͓͙̤͚̬͖̭͉̭͙͚̭͇̘̓̒͌͆̒̒́̓͂̒́̓̒͒̐̏͒̓̏̒͐̒͐͒̓́̒͊̓͌͊́̏̒͏̴̴̨̡͚̬̮͉͓͚̭͚̫̭͓͙͚̩̗̮͚̫̮͈͚̹̭͔̘͖͚̩̤̮̒͌́̏͑̓̒͑̓͋͆͑̓̒͑̓̒̒͏̸̸̨̭͙͙͚̭̩͚̩̗̭̘͙͚̩̭͎̭͚̩̰̭͇̭͙͚̫̤̮͕͓͚̬̭̭͙͔͚̪̭͎̘͙͚̩͖̮͇̘͙͚̪̭͓͚̬̮̭͙͚̰̭͔͓͙͕͚̫̭͓͙̯͚͖̭́͐̓̒͋̏͊̒̏̓̒͆͌̏͆͑̒͋͆͒̒́͐͂͘ͅ͏̸̴̴̨̨̨̡̘͙̩͚̩̭͔̭͙̤͚̭͓̫͚̪̰̮̘͙͚̺̭͚̪̭͎̙͚̹̤̭͖̭͚̮͓͙͚̮͔͓͚̫̭͓͙͚̺̭͓͙̲͚̫̭͉̭͙͚̬̭͇̘͙͈͚̬̮͉͓͚͚̭͔͚̭͈̘͙͚̪̗̮͖͚̬̗̭͈̘͙͚̪̭͔̘͙̥͚̮́͆̓̒͒̑̏͒̓̒̏̓̒̒̓́͐̓͂̏̒͊̏͒͌͊̏̒́̓̒͑́͂͆̓̒͑͒͂͒͘͘͏̸̸̭͙͚͚̭̬͚̩̗̮͕̭͙͚̩̭͈̘͙͚̩̰̭͉̘͙͚̹̮͖͚̫̭͈̭͍͚͎̭͎̘͙̯͚̮͇̘͙͚͎̮͂͐̓̒͒͊̐͒͒̓̒͒̒͂́͊́͘͏̴̸̴̴̴̵̴̨̨̡̨̨͙͚̬̮͖̭͚̤̭̘͙͚̫̮͕̘͙̯͚̪̤̭̘͙̬͚̩͎̮͖̘͙̤͚̪̭͓͙͚͎̮̭͙͚̪̭͙͚̪̭͎͓͚̹̰̭͕͚̮͔͓͙͚̗̮͓͇͚̫͖̭͍̘͙͚̫̭͓͙͚̫̭͉̘͙͚̬̮͉̭͙͚̬̮͉̭͚͚̭͙͚̫̮͔̭͙͚̮͖̤͚̬͚̭̘͈͚̭͔̘̘͚̩̮̓͆̒̋́͑͂͑̏̓͊͂͒͒͒̓̏̒̑̓̒͐́̓́͑̒͌͊̏̒͐́͑̓̓͆͂͂̓̒͌̒͂͒̒̕͏̸̸̵̸̸̴̸̢̨̨̘͙͖͚̭͙̘͚̩̗̮͕̘͙͚̩͖̭͈͓͚̹̮̘͙͚̫̰̭̘͓͚̫͚̭̭͙͔͚̩̭͎̘͚̮͇̘͙͚̩̭͓͙͚̬̭͈̭͙͚̰̭͓͙͚̗̮͇͙̯͚̪̰̭̘͙̩͚̩̮̘͙̤͚̩̭͓͙͚̫̮̘͙͚̪̭͙̳͚̪̭͔͚̹̤̭͚̫̮͕̭͙͚̭͈̭͚̫͖̮͔͙͚̹̤̭͓͚̹̭͉̭͙͚̩̭͇̘͙̱͚̬̮͚͚̭͂͐̓̏̒̏͊͑͊̒͌͆̒̑́͋͆͑͆́͑͂́̓͒͒̓͊͊͒͐͒̓̏͊̓̒͐̓̒͐͒̓́̏̒͊̓͌͊̒̔͆͊̓̒̑́͘͏̵̸͙͚̫̭͎͙͚̮͓̤͚̫̤̭͈̘͈͚̹̭͔̘͓͚̮̓̓̓͆͂̓̒̒͊̒͂͂͏̢̭͙͓͚̪͖̭̙͚̩̗̮͕̭͙͚̩̭͇̭͙͚̹̭̘͙͚̫̤̭̘͖͚̬̭͈̭͍͚̩͚̭͎̘͚̫͚̮͇̘͙͉͚̩̮͐̓̒͊͊͊͋͌̒͆̒̒̑͆͘͏̸̴̴̴̨͙̳͚̬̮͖̭̖͚̤̭͓̭͚̫̮͈͙̯͚̮͕͓͙̩͚̩̮͖̘͙̤͚̭͓̩͚̪̮̭͙͚̩̮͓͙̫͚̪̭͎͚̹̰̭͕̭͚̮͕͙͚̩̭̓͆̒́̒͌̓͂͊͂̏̓̒͆͒͐͐̏̓̒͌̒͐́̓̓͏̴̧̨̡̘͚̫̗̮͔͙͚̭͓͙̲͚̺̭͉̭͙͚̭͇̘͙̱͚̬̮͍̘͚̭̘͚̭͓͙͚̩̗̮͓͚̫̰̮͈͚̭͔̘͕͚̮̒͊̓͌͂͊̓͂̏̒͐́̏͑̒͑́͂͊͆̓̒͑̓̒́͒̒͂͒͏̸̭͙͈͚̮͓͚̩̗̭͇̘͚̩͖̭͎͙͚̹̮́͒̒̒̋̓̐͊ͅ͏̴͙͚̺͖̮͖͖͚̬̮͎̘͍͚̭͎̘͙͚͎̮͇̘͙͚̪̮̓̓̒̒́̏̈́͂̋͆͘͏͚̬̭͈̘̖͚̤̭͙͕͚̗̮͓͙̯͚̩̰̮͍͙̩͚̪̮͖̘̩͚̬͚̭͓͙͇͚̬̤̮̘͙͚̺̭͙̳͚̪̮͔͚̹̤̭̓̒̐͆̒́͒̓́͐̓͒̒̓͒͐̏͒̓̏̓̒̕͏̸̨̨͓͙͚̮͓͓͙͚͎̭͍̭͇͚̫̭͓͕͚̹̭͓͙̤͚̫̰̭͉̘͙͚̮͉̭͙̰͚̬̭́̓́̒͒͒̒͒͊͂͂̏͏̡̭͚͚̭̘͙̥͚̮͙͚̪͚̭̘͚̬͚̮͎̭͙͚̭͔̘͓͚̬̮̒̑́͑́͂͐̓͆͌̒͑́͊̒́͏̸̸̨̭͙͚̮͓̪͚̩̗̭̘͙͎͚̩̭͈͙͚̩̰̭͈͓͙͚̹̮͔͖͚̬̭͈̭͙͔͚̩͚̭͎̘͙͚̫̮͇̘͙͚̪̭͓͙͚̬̮̘͚̤̭͔͓͚̫̮͇͙̯͚͖̮͈͙̩͚̪̭͇͙̤͚̩̤̭͓̬͚̮̭͙͐́͒̒͋͊̓̐͒̓̒͆͂͊̔͆͑̒͆͒̒̒́̒͌̓͂̓̓̓̓̒͂͒͘͏̴̸̴̴̴̨̨͚̪̮͓͚̪̮͔͚̹̤̭̭͙͚̫̮͓͙͚̩̭͍̭͇͚̫̭͍̘͕͚̹͚̭͓͙͚̫͖̭͉̭͙͚̬̭͇̘͚̬̮͍̘͚̭͓̭͚̭͉͓͙͚̪̭̘̤͚̫̭͈̘͈͚̭͔̘͚̮͐̒̒̏̓̒͐͒̓̓̒̒͊͆̒̋̒͐́̏̒͆́͂͆̓͌̒͂̒͂͒̒̏͂͂͘͏̘͙͏̨͚̫̗̭͚̩̗̭̦͚̩̭͇̘͚̹̮͕͓͙͚̹̭͉̘͖͚̫̭͈̭͙͔͚̭͎̘͚̮͇̭͙͚̩̮͐̓̒̈́͋̓̒͊̒̏͊͒̒̏͂͆̒̑͂̏͆͘͏̡͚̬̭͈̭͙͚̰̭̓̒͆̏́͏͙͕͚̗̮̓́͏̴̨͓͙̯͚̪̮͍͙̩͚̩̭͔̭͙̤͚̩͖̭͓̫͚̮̘͙͚̩̮͓͚̪̭͓͚̹̰̭̓͆̓̒́̓͒͑͐̒̏͊̒͌̕͏̴̴̵̨̨̨̘͚̭̘͙͚͚̮͖͓͇͚̫̭͍̘͙͚̬̭͓͙͚̬͖̭͉̘͙̦͚̩̭͇̘͙̬͚̬̮͉͓͙͚͚̭̘͙͚̫̭͓͙͚̭̭̤͚̬̮͙͚̹̤̭͔̘͚̮̒͐́͋̓͂̒͒͌̓͊́͑̓͋͆͂͂͑̒͒͑̓͑̒̏͂͒͏̭͙͏̸͚̪͖̭͙͓͚̩̗̭͇̭͙͚̩͖̭͈̭͖͚̩̰̮͓͙͚̫̰̭̘͖͚̬̮͎̘͙͔͚̫̭͎̘͚̮͇̘͙̖͚̩̮͐̓̏̒͒͋̒͊̒̒́̓͆͘͏̨͚̬̮͖̘͙͚̰̭̘͚̗̮͈͙̯͚̪̭̓̒̔͆̓́͒̒̑́̓͏̴̨̘͙̩͚̪͚̮͖̘̩͚̬̬̭͓̮͚̬̤̮̭͙͚̪̭͙̫͚̪̭͓͔͚̹̰̭͙͚̫̭͉͙͚͚̭̒̓̒͒͒͒̓̏͊̒͐̓͒̓̓́͏̴̨̘͇͚̬̮͕͚̭͓͙̱͚̫̭͉̭͙̣͚̭͇̘͙͚̬̮͉͓͚͚̭̭͚̮̘͙͚̪͚̭̭̤͚̬̗̭͈̘͈͚̪͚̭͔̘͓͚̬̮̒͐̓̒͂̏͊͆́̏́̒͌́͑̒͆́͂͑͆͑̒̒̒̏͏̘͙͏̢͚̫̗̭̦͚̩̗̭̘͙͚̩̭͎̭͙͚̹̮͖̭͙͚̹̭͉̘͖͚̬̬̮͎̘͙͔͚̪̭͎̘͚͎̮͇̭͙͚͎̮͐̓̒͋̏͊͊̓̒͂̒̒́͊́͘͏̸̴̸̸̨̪͚̬̭͈̭͚̤̭͓̭͙͚̫̭͕̘͙̯͚̪̤̮͈͙̬͚̪̮͖̘̩͚̪̭͓̫͚̪̰̮̘͙͚̮͓͙͚̪̮͔͙͚̹̤̭͙͚̫̭͉̭͙͚̭̘͇͚̫͎̭͓͕͚͖̭͓͙̲͚̹̭͉̭͙̤͚̭͇̘͙̗͚̬̭̓̒͆̒͑́͂̓͊̒͒̓̒͒̓́͒͐̏̓͗͐̓͒̓͂̏͐̒͒̒͂͊͂̏͏̭͚̭̒́̏̕͏̡͙̥͚̮͖͙͚̭͉̘͚̬̮͈͚͚̭͔̘͖͚̬̮̓́͂̓͆͂͂̒̓͑̓̒͂̒̏͏̸̘͙͖͚̭͚̩̗̭͚̩̭͇̘͖͚̩̰̭͉͙͚̺̮͔͖͚̫̮͓͍͚̪̭͎̘͙͚͎̮͇̘͙͇͚͎̮͂͐̓̒̐͋̓̒̈́͊̒̓͊̓̒̏͑̒͆̓͂́͘͏̴̸̸̨̨̨̡̙͚̬̮͖̘͉͚̤̭͓̭͙͕͚̗̭̘͙̯͚̭͕̘͙̩͚̪̗̭͔̭̩͚͚̭͓̮͚̮̭͙͚̮͓͙͚̪̭͎̭͚̹̰̭͕͙͚̮͔̭͙͚̗̭͖̘͚̬̮͔͙͚̺̭͓͙̤͚̺̭͉̘͙͚̮͉̭͙͚̬̮͍̭͚͚̭̘͙̥͚̭͉͙͚̩̭̭͚̫̭̘͈͚̬̭͔̘͚̩̤̮̓̒͆̒́́͒͂͊̒͂̓̒́̓͒͑́͒͐̒̏̒̑̓́̓́̒͊̓͌͊̓̈́͂̏͌̒́͒́͂̓͆̓͒̒͌̒͂̒͐̕͏̴̸̴̸̸̡̨̡̭͙͚̪͖̮͓̫͚̩̗̭͚̩͖̭͍̘͚̹̭͎̘͙͚̺̭̘͓͚̫͖̭̭͍͚̫̭͎̘͙̯͚̪̰̮͇̭͙̗͚̪̭͓͙̫͚̬̮͙͚̰̭̭͙͚̗̭̭͙̯͚͖̭͓̘͙̬͚̪̮͖̘͙̤͚̭͓̬͚̮̘͙͚̩̭̗͚̪̭͚̹̰̭͔̘͙͚̫̭̘͙͚͚̭͖̘͚̫͚̭͓͕͚̫̗̭͓͙̱͚̭͉̭͙͚̬̮͉̭͚̬̮͉̭̙͚̭͓͓͚̫̭̘͙͚̭̭͚̬͖̮͙͚̹̭͔̘͓͚̫̰̮͐͒̒͋̓̒̈́̒̏͊͊͊̒͌̒͆͆͑͆͑̓́͒͂́͒͂̏́̓̓̒́̓͒̒͒̓̒̏͊̓̒͐͒͌̓́̒͊͒̒͊́͂̓̒̔̒́̏̒͑̓͌͆͂͒̒͑̓͑̒͘͏̭͙͏̸̢͚̭͙͚̩̗̭̘͍͚̩͖̭͍̘͙͚̩̰̮͂͐̓̋͋̒͏̨͓͙͚̹̭͈̘͖͚̫͚̮͓͍͚̪̭͎̘͙͚̮͇̭͙͍͚̪̭͓͙̫͚̬̮͖̘͙̥͚̰̭̘͙͚̗̮͕̭͙̯͚͖̭͖̘͙̩͚̩͎̮͖̘̩͚̗̭͓͙͚̩̮̭͙͙͚̮͓͙̱͚̪̭͎͓͚̹̰̭͕͓͚̮͒̒͑̒̓͂̓͆͑͆́͒͂́͂̒́̓͊̏͒́͒͐̏̒̑̒͐́͘ͅ͏̴̴̧̨̨̭͙͚̩̭͉̭͇͚̬̭͓͙͚̭͓͙͚̬͖̭͉̭͙͚̩̮͉̭͚̬̮͍̘͙̬͚̭̓͆̒͆͒͌͂͊̒͐́̏͏̨̨͚̭͓͙͚̪͖̮͖̤͚̫̮͙͚̩̭͔̘͚̗̮̓̒͆́͂͋͆̓̒͑̓͑̒̏͂͏̭͙͏̸̴̸̨̨̡͚̫̗̭͍͚̩̗̭̭͍͚̩͖̭͉͖͚̩̰̭̘͙͚̺̭̘͓͚̫͖̭͈̭͙͔͚̪͚̭͎̘͚̪̮͇̭͙͚̪̭͓͙̪͚̬̮͖̭͚̰̭͓̭͚̫̮͎͓͙̯͚̩̤̮͎͙̬͚̩͎̭͇͙̤͚̪̭͓͙͇͚̪̰̮̭͙͚̪̭͙͚̪̮͔͓͙͓͚̹̰̭̭͚̫̮͇̘͙͚͚̭͎̭͇͚̬̰̭͍̘͕͚̬̭͓͙̤͚̬̭͉̘͙̦͚̩̭͇̘͇͚̬̮͙͚͚̭͓̘͙̥͚̫̭̭͙͚̩̭̭͚̬̮͎̭͈͚͎̭͔̘͙̥͚̮͐̓̒͋̒̓̒͊͊͊̒̒̑͆͊͆͑͆̒̒́̒͌̓̓͒̓͒̓͒̓͐̏͐̒͐͒̓͂̒̒͊̏̒͊̓͂́̓͌͆̓͒̒͆̒͂͂͂͘͏̴̸̸̢̘͙͚̫̗̮͓̦͚̩̗̭̘͍͚̩̭͈̭͙͚̹̮͓̭͙͚̫̰̮͖͓͚̫̭̭͙͔͚̪̭͎̘͙̮͚̫͚̮͇̘͙͚̩̭͓͙͚̬̮̭͙̩͚̤̭͓͓͙͕͚̫̮͉͙̯͚̪̤̮͓͙̬͚̩̰̮̘͙̤͚̪̬̭͓̮͚̫͚̮̭͙͚̭͙̺͚̪̭͎͚̹̰̭͖̘͙͚̫̭͍͓͙͚̮͑͒̒͋̒͊͊̓̒͊͌͊͆͑͆͒́̓͐͒̓̒͒̒́͒͒̓̏̓̒͒̓́̏͘̕̕͏̨̨͓͚̫͎̭͓͕͚̗̭͓͚̬̰̭͉̭͙̤͚̩̮͉̭͖͚̬̭̒͊͒̒͂͊̒̔̒͏̸̨̭͚̭͓̘͚̭̘͙͚̭̭̤͚̫̭̘͙͚͖̭͔̘̘͚̬̮̒́̏̒͆́͂͊͆͂͒̒͌͑͂̒͂͘͏̸̴̸̘͙͚̭͙̙͚̩̗̭̭͙̗͚̩̭͇̭͚̹̮͙͚̹̮͓͖͚̫̮͓͍͚̪̭͎̘͙͚̮͇̘͙͚̺͚̮̓́͐̓͋͊̒̏͊͐̓͊̓̒͒͑̒́͘̕ͅ͏̵̸̸̴̴̸̴̨̨̙͚̬̭͈̘͙͚̤̭͔̭͙͕͚̗̭͕̘͙̯͚͖̭̘͙̩͚̩̭͔̭̩͚̭͓̫͚̫̮̘͙͈͚̩̮͓͙͚̪̮͔͙͚̹̤̭͕͙͚̫̭͇͙͚̭͉̭͚̬̮͙͚̫̭͓͙̱͚̺͎̭͉̘͙̤͚̬̭͇̘͕͚̬̮͍̘͙̬͚͚̭̘͚̫̭͙͚̭̭̤͚̬̮͙͚̪̭͔̘̘͚̩̮̓̒͆́́͂͒̒́̓̒͊͒͐̏̓͗̓͒̓̓͂̏̒͊͂͐̓͌͊̒́͑̒͆̓͊̓͆͂͂͑̒̓͑̓͑̏̒͊͏̸̴̵̧̨̨̨̭͙͚̭̫͚̩̗̭͇̭͙͖͚̩͖̭͈̭͖͚̩̰̭̘͙͚̹̭͍̘͓͚̫̭͈̭͙͔͚̭͎̘͙͚̩̮͇̘͙͚͎̭͓̤͚̬̮͖̘͙̹͚̤̭͓̘͙͚̗̭͕͓͙̯͚̩̤̭͓̘͙̩͚̪͚̭͔̭͙̤͚̬̭͓̮͚̩͖̮̭͙͕͚̩̭͙̭͚̪̭͎̭͙̬͚̹̤̭͕̭͚̫̮͔͙͚͚̭͖̘͚̫̭͍̘͕͚̫͖̭͓͚̺̭͉̭͙͚̩̮͉̭͉͚̬̮͉̘͙͚͚̭͓͙͚̫̭͙͚̩̗̭̘̤͚̫̮͙͚̪̭͔̘͓͚̗̮͒́͐̓̒̒͋͊̒͒́͂͆͋́͑̒͆́͂́͊̓̒͒͒̓̏̒͐͒̓̓́̒͊̓̒͊̒̔̓̒͂́͒̓͌̓͆͌̒͑̓͑̏̒͂͘ͅ͏̴̸̘͙͚̫̗̮͓͙̙͚̩̗̭̘̺͚̩̭͍̘͖͚̩̰̭͙͚̹̭̘͓͚̫̭̭͙͔͚̪̭͎̘͙͚͎̮͇̭͙̖͚͎̭͓͈͚̬̭͈̭͙͎͚̤̭͓͚̫̭̐͒͋̒͊̒͊̓͊͌̒͊͌͂́͑̒͆́͑̒͌͘ͅ͏̴̸̴̴̴̨̨̨̨͓͙̯͚̮͈͙̩͚̩̭͔̭̩͚̪̰̭͓͙͇͚̮̘͙͓͚̪̭͚̪̭͎͓̙͚̹̤̭͕͓͚̭͓͙͚͚̭͉̭͇͚̬̮͙͚̫̭͓͙͚̬̭͉̭͙͚̭͇̘͔͚̬̭͂͊̓̒̓͂͒͒̓̒̏̒̒̓́͋̓͂̒͐̓͌͊̏́̏̒͘͏̡̭͙̰͚̭͔̘͚̭̭͙͚̪̗̭̭͚̬̗̮͙͚̪̭͔̘͖͚̬̮́̏̒͑́͂͋͆͒̒͑̓͑̏̒́͏̸̴̨̨̡̨̘͙͖͚̭̰͚̩̗̮͕̘̦͚̩̭͈͓͙͚̹̭͖͙͚̺͖̭͍̘͓͚̬̤̭͈̭͍͚̪̭͎̘͙̮͚̮͇̘͙͉͚͎̭͓͙͚̬̮͚̰̭͓͓͙͚̗̮͉̭͙̯͚͖̮͕͓͙̬͚̩̭͇͙̤͚̪̭͓̫͚̮̘͙͕͚̮͓͚̪̮͔͓͙̰͚̹̰̭͕̘͚̭͍̭͙͚͚̭̘͇͚̫̮͔͙͚̫͚̭͓͙͚̺͎̭͉̘͙̣͚̭͇̘͙̱͚̬̭͂͐̓̒̒͊̐͊̓̒̒͒͂́͑̓͆͑̓̒̋́͂́͂̓̏̓̒͂̓͒́͒͐̒̓̏̒̓́̓͂͐̒̓̓͌͊́̏͘͏̭͙͏̸͚̭͓͓͚̫̮͓͙͚̮̤͚̫̮͙͚̪̗̭͔̘͕͚̩̮́̏̒͑̓͑͆͂͂͑̓̒͑̓͑̒͊͏̸̸̸̡̘͙͖͚̮͓̹͚̩̗̭͓͙̗͚̩̭͎̘͙͚̹̭͈̭͙͚̺̭̘͖͚̬̭̭͙͔͚̩̭͎̘͙̮͚̫͚̮͇̘͙͇͚̪̭͓͚̬̮̘͙͚̰̭͂͒̒͌͊̐͊͊͌̒͌͆͑̒͆͒̓́͘͏̴̸̴̨̨͚̗̮͙̯͚̮͖͓͙̬͚̩̭͔̭̩͚̬̭͓̩͚̩͖̮̘͙͚̩̮͓͚̪̭͓͙͚̹̤̭͚̫̮͙͚̩̮͔͓͚̫̭͓͕͚̫͎̭͓͙̱͚̫͖̭͉̭͙͚̮͉̭͚̬̭̓̒̑́͌̓͂͊̒́̓̒͒͐͐̒͒̏͊͐̓̒͐͒͐̓̓̒͊̏͒̒͊̈́́̏̒̔͏̵̸̡̭͚͚̭͓͙͚̫̭͍͙͚̮͚̬̮͎̭͙͚̭͔̘͚̫̮̒͐́͑̓̓͆͂͂͐̓̒͊͑́̒͐͆͏̸̸̸̧̘͙͚̮͓͚̩̗̭̘̦͚̩͖̭͍̘͖͚̹̭͕̘͙͚̺͖̮͖͓͚̫̗̭͈̭͍͚̭͎̘͙͚̬̤̮͇̘͙͈͚͎̭͓͙͚̬̮͙̹͚̤̭͓̭͚̫̭̭͙̯͚̪̤̭͓̘͙̩͚̪͖̭͇̩͚̩̗̭͓͙͚̮̘͙͈͚̺̭͚̪̮͔͔͚̹̤̭͗́͒̒̓͋̒̒͊̓̒̒́̈́́͑͆͑̓́̒̑͑̓̒̓͊́̓͒̏͒̓̒͗̏̓̒͘͏̴̨͚̮͓̘͙͚̩̭̓̒̓́̓͏̴̴̨̨̘͚̫͖̮͙͚̺̭͓͙͚̺̭͉̭͙͚̬̭͇̘͙͚̬̮͚̭̒͊͐̓͌̓͊̈́́͊̓̒́̏̕͏̡͚̫̭͔̭͙͚̪͖̮͚̬̮͈͚̹̭͔̘͙̥͚̮̓̒͑̓͆͒̓̒͆͑̓̒͊́͂͏̸̸̴̭͙͚̮͓͚̩̗̮͕̘̖͚̩̭͎̭͖͚̩̰̭͓͓͙͚̺̮͓͖͚̬̭̭͙͔͚̫͚̭͎̘͙͚̩̮͇̘͙͉͚̪̮͑͂͒̒̒͊̒͊̓̒͌̈́̏͆͘͏̸̴̴̵̸̨̨̡̨͚̬̮͓͙̹͚̤̭͔̘͙͕͚̫̮͍͓͙̯͚̭͕̘͙̬͚̩̮̘͙̤͚̩̭͓̩͚̩̮̭͙͚̩̭͚̪̭͎͓͙͚̹̰̭͓͙͚̫̮͈͙͚͚̭̭͇͚̬̰̭͍̘͕͚͎̭͓͙͚̬̭͉̘͙̥͚̮͉̭͙͚̬̮͉͓͙͚͚̭͓̭͙͚̫̭͎̭͙͚̩̗̭̭̤͚̫̰̭̘͙͚̩̭͔̘͓͚̮̓̒̐͆͒́͂͊͒͆̓̒̏͒̓͒̓̒͗̏͐͒̓̓͂͌̒̒͂͊̏́̏́͂́̓͆͒̒͌͑̒́͒͏̸̘͙͔͚̮͓͍͚̩̗̭̭͙͎͚̩̭͈͓͖͚̹̮͂͒̒͋͊̒͊͏̭͙͚̫̰̮͓͚̫̮͎̘͙͔͚̩̗̭͎̘͙͚̫̮͇̭͙͚̺͚̮͒̓̒͊͂͊͌͘͏̸̴̡̨̨̡͙̺͚̬̭͈̭͙͚̰̭̘͙͚̗̮̘͙̯͚̪̰̮͕͓͙̩͚̪͚̮͖̘̩͚͚̭͓͙͇͚̮̭͙͕͚̺̮͓͙͚̪̭͙͓͚̹̤̭̭͚̭͇͙͚̭̘͇͚̫͖̮͔͕͚̹̬̭͓̗͚̗̭͉̭͙̦͚̬̭͇̘͚̬̮͔͚̭͓̘͚̭͍͙͚̪̭̘͚̬̮͈͚̪̬̭͔̘̘͚̬̮̓͆́͑͂́͌̒͂̓͂͒̏͐̒̏͊̓͐̒͐́̓̓́̏͐̒̓̒͊̒͂̒͊͊̓̒́̏̒͆́͂̓͆̓͊̒͒͑̓̒̒͂͏̸̨̘͙͚̮͓͙̘͚̩̗̮͕̘̦͚̩̭͈̘͚̹̭͇̘͙͚̹̭̘͓͚̬̮͓͍͚̪̰̭͎̘͚̮͇̘͙͚̺͚̮̓́͒̒͊̒̏͊͒͌̒͂͑̒̒̑͂͘̕͏̸̸͙̲͚̬̭͈̭͚̰̭͓͚̫̮͇̘͙̯͚̪̤̮͙̬͚̪̗̮̘̩͚̭͓͙͚̮̭͙͚̺̮͓͙̱͚̪̭͎̭͙̬͚̹̰̭̓͆̒͑́͑̒͌͊̓͒̒́͆̓͊͂͒̓̏͐̏͏̨̨̨͓͚̮̭͙͚͚̮͕͓͇͚̫͚̮͙͚̭͓͙̤͚̗̭͉̘͙͚̮͉̭͙͚̬̮͙̒͐́͐̓͂̒͐̓͌́͂͊͂́̏͌͊̓͏̡͚̭͓̘͚̫̮͕̘͙͚̪̗̭̘͚̫̰̭͈̘͈͚͚̭͔̘̘͚̫̰̮́̏̒͆̓͆͌̒̒͂̒͏̸̸̨̭͙͚̫̗̭͙͉͚̩̗̮͕̘͙͚̩̭͎͓͙͚̩̰̭̘͙͚̫̰̭̭͓͚̫̭̭͍͚̩̭͎̘͙̮͚̮͇̘͙͚̪̮͒͐̓͒͊̐͋͑̒͌̒́̓͆͘͏̴͚̬̮͖̭͙͚̤̭͔̭͚̗̮͖̭͙̯͚̩̰̮͙̬͚̩͎̭͔̭̩͚͖̭͓̹͚̫̮̭͙͔͚̪̭͙̩͚̪̭͙̓̒̐͆̒́̒̑́͋̓̒́̓̒͊͒͒̓̏͊̓͏̨̨͚̹̤̭͖͓͚̫̮͇̭͙͚͚̭͖̘͚̫̮͔͙͚̫̭͓̗͚̺̭͉̭͙̪͚̭͇̘͚̬̭̒͐͒̓́̒͊̓̓͌͊̒̓́̏̒͌͏̵̡̨̘͚͚̭̘͙͚̫̭͈͓͙͚̪͖̮͕͚̫̮͙͚̪͎̭͔̘͙̥͚̩̤̮̒́͑̓͆̓̒͑̓͑͘͏̸̢̨̭͙͚̭̪͚̩̗̮͕̘͙͎͚̩̭͎̘͙͚̹̭͖͙͚̹̮͔͓͚̫͎̭̭͙͔͚̩̭͎̘͙͚̮͇̘͙͉͚̩̮̓͂͐̓̒͊͊̓̓̓̒͌̓̈́͂͆͘͏̸̴̨̡̨̨̥͚̬̮̘͙͚̰̭͓̘͚̫̮͖͙̯͚̪̭͕̘͙̩͚̩̬̭͇͙̤͚̬̭͓͚̩͖̮̘͙͙͚̩̮͓͙̰͚̪̭͎͓͚̹̤̭͕͚̭͓͙͚͚̭͍̭͚̫͖̮͕͚͖̭͓͙̱͚̫̭͉̭͙͚̩̭͇̘͇͚̬̭̓̒͆͒̓́̒̑̓͂̓̓̓̒͂͒͐̏̒̓̒̓́͌̓͂̒͊͐̓̒͂͊͆̒̕͏̸̡̭͙̬͚͚̭͚̭͈͓͙͚̭͍̘͚̬̗̭͈̘͈͚̹̤̭͔̘͙̥͚̫̮́͑̓̒͑́͂͆͂̒̒͆͏̸̨̡̭͙͚̫̗̮͓͙͉͚̩̗̭̘͙͖͚̩͖̭͎͓͚̹̮͓͙͚̫̰̭͉̘͓͚̬̭̭͍͚̭͎̘͙̮͚̮͇̭͙̖͚̪̭͓͙̦͚̬̮͖̘͙͚̰̭͚̫̮͔̭͙̯͚̭̐͒͋̒̏͊͒̒͆͌̒͂͒͂͆͑͆́͑̓̒͌͂͊͘͏̸̘͙̬͚̩̭͔̭͙̤͚̩̗̭͓͚̮̘͙͚̭͙̪͚̪̭͎͓͙͓͚̹̰̭͆̓̒͂͂͒̐́͒͒̓̏͏̵̨̨̡̭͙͚̫̮͈̭͙͚͚̮͓͇͚̫̭͍̘͕͚̬̭͓͙̲͚̬̭͉̘͙̥͚̮͉̭͙͚̬̮͉̭͚̭͓̭͙͚̫̭̭͙͚̪̗̭͈̘͚̬̮͎̭͈͚̭͔̘͕͚̪͚̮͒̓͂͑̒͊̒͆͊̏́̏̔̒́̏̓͒͆̒̏̒́͊̒̕͏̸̭͙͚̮͓͚̩̗̭͓̖͚̩͖̭͇̭͙͚̹̭͓͓͙͚̺͖̭̘͓͚̫̭̭͙͔͚̩̭͎̘͙͚͎̮͇̭͙̗͚͎̮̒́͒̒͌̒̐͊͋̒̏͌̏̓́́̕͘͏͚̬̮̭͙͎͚̤̭͔̭͙͕͚̗̮͎͙̯͚͖̭̓̒̏͆͒́́̓͂͏̴̨̨̘͙̩͚̩̭͔̭͙̤͚̪̭͓͙͚̮̭͙͈͚̭͙̺͚̪̭͙͚̹̰̭͖͙͚̫̮͖̭͙͚̮͒̓͊͂͒́͒͒̓̏͊̓͗̓͒̓́̏͏̸̨̨͓͚̫̭͍̘͙͚̹̭͓͙̲͚̭͉̭͙͚̩̭͇̘͙̳͚̬̭̒͊̏͌͊͂͒̈́͏̵̡̨̘͚̭͔͙͚̫̭̘͙͚̭̭͚̬͚̮͈͚̹̭͔̘͖͚̮̒͐́̏̓̓͌͆͂͂͒̒͑̓̒̒́͂͏̸̸̴̭͙͖͚̪͖̮͓͙͚̩̗̭̭͙̗͚̩̭͈̘͚̩̰̮͕̭͙͚̹̭̘͖͚̫͚̭͈̭͍͚̗̭͎̘͚̮͇̭͙͚̺͚̭͓͙͚̬̮͓͙̹͚̰̭͔̘͚̫̮͇̭͙̯͚̪̤̭̘͙̩͚̩̤̮̘̩͚͖̭͓͙͇͚̩͖̮̘͙͚͚̪̮͓͙̳͚̪̭͎͙͚̹̤̭͒̐͋͊̒̏͒͌̒̒͂̒̒͂͋͑͆͆͒́̒̑͐͒̒͂̓͒͐̏̓͗͘͏̴̨̨͓͙͚̫̭͍͓͙͚̩̮͓͚̫͖̮͔͙͚̫͎̭͓̗͚̺͎̭͉̭͙̣͚̮͉̭͚̬̮͉͓͙͓͚̭͒̓͐̒͊̓͌͊̒́̏̒́̏̕͏̴̡͙̥͚̮͖͙͚̪͚̭͈̘͚̫̮͎̭͈͚̹͎̭͔̘͚̗̮̓́͂̓͆̒̒̒͐͂͏̸̭͙͚̪͖̮͓̭͚̩̗̮͕̭͚̩͖̭͇̘͚̩̰̭͉͙͚̹̭̭͖͚̬̬̮͓͙͔͚̫͚̭͎̘͚̮͇̭͙͉͚̺͚̮͒͒̒̒̈́̒̏̓̓͑̒͑̒̑͂͘͏̸̴̵̸̨̨̡̨͚̬̮͉͚̤̭͙͚̫̮͙̯͚̪̮͙̬͚̪̮͖̘͙̤͚̪̭͓͚͎̮̭͙͖͚̩̮͓͙̳͚̪̭͚̹̰̭͕͚̭̘͙͚̩̭͇̭͇͚̬̭͓͕͚̭͓͙̤͚̺͎̭͉̭͙̹͚̭͇̘͙̘͚̬̮͍̭͙͚̭͙͚̫̮͙͚̩̮͖͚̬̭͈̘͙͚̩̭͔̘͙͚̪͚̮̓̒̐͆͑̓̒́͑̓͂͌̓͂͊̓̓̏̓̒͂́͒͐̏͊̓̒̓̒̓́͌̓͆̒͂͒̒͂̏͊͂̏͂́̏͑̓̓͒̓͆̓̓̒͊͑̕͏̘͙͈͚̫̗̮͓͙͒͏̸̴̴̴̸̢̨͚̩̗̮͕̘͍͚̩͖̭͎̘͙͚̹̭͓̘͙͚̹͖̮͖͚̬̬̭̭͙͔͚̫͖̭͎̘͙͚̮͇̘͙͚̺͚̭͓͚̬̭͈̭͚̤̭͓̘͚̗̭͕̘͙̯͚̪̮͎͙̩͚̩̭͇̩͚̭͓͙͚̫̮̭͙͈͚̪̮͓͖͚̪̭͎͓͙̰͚̹̤̭͕͓͚̫̮͓͙͚͚̮͖͓͇͚̬̤̭͓͕͚̭͓̗͚̫̭͉̭͙̤͚̮͉̭͓͚̬̮͍̘͙̬͚̭͔̘͚̭͎͙͚̭̭̤͚̫̭̘͈͚̗̭͔̘͚̩̮̒͊͒̓̒͌͂͂̏͑̒̐͆̒͑́̒͌́͂̓̓̒́̓͊͊͒͐̒̏̒͐͒͐̓́̒͒̒́͂͊̒͆͂̏̒́̏̒͑́͂̓͆͂͂͑̒͌̒͂̒̏͊͘͏̘͙͏̸̸̨͚̪͖̮͓̘͚̩̗̭̘͙͎͚̩͖̭͎̭͖͚̩̰̮͓̘͙͚̹͖̮͓͖͚̫͖̭̭͙͔͚̬̭͎̘͙͚̮͇̭͙͚̪̭͓͙̥͚̬̭͈̘͚̤̭͓̭͚̗̭͕̘͙̯͚̪̤̭͖̘͙̩͚̩̮͖̘͙̤͚̩̤̭͓̹͚̮̭͙͚̭͓͚̪̭͎̭̙͚̹̰̭͒̒͋̒̓̒͌͂͂̏͆͑͆̒̋́̒̑́̓̒́͒̒́͒͒̓̒̏̒͘ͅ͏̸̴̨̨̨̡͚̮͓̘͙͚̭͈̭͇͚̬̤̮͔͙͚̬̭͓̗͚̗̭͉̘͙̥͚̩̭͇̘͙̯͚̬̮͍̘͙͚̭͔̘͚̮͔͙͚̪̗̭͓̭͚̫̭̘͈͚̭͔̘̘͚̮̓̒͐́̓͂̏̒̓͌̓͊̒͂͗́̏̒͑́͂̓͆̒͌̒͂̒͂͂͏̸̴̵̴̨̨̡̨̭͙͓͚̭͙͚̩̗̭͓̮͚̩͖̭͈̘͚̩̰̮̘͙͚̫̤̮͓͓͚̬̭͈̭͙͔͚̭͎̘͙͚̮͇̭͙͉͚̺͚̭͓̩͚̬̮͖̭͙͚̤̭̭͚̗̮͎̭͙̯͚̪̭͕̘͙̩͚̪̭͔̭͙̤͚̤̭͓̫͚̪͖̮̘͙͚̭͙̩͚̪̭͚̹̰̭͙͚̫̮͇͓͙͚̮͓͓͚̬̬̮͕͚̗̭͓͙͚̫͖̭͉̭͙͚̬̭͇̘͙̬͚̬̮͉̭͙͓͚͚̭͂͐̓͑͌̒̒̏͑̓̒́̏͂͑̒͆́͑̒͌́͂̏́̓̒͒̒́͒͒̓̏͊̓̒̑͐̓͒̓́̏̒͊͐̓̒͂͊́́͘ͅ͏͚̭̘͙͚̪͚̭̭̤͚̬͖̮͎̭͙͚̭͔̘͚̪͚̮̓̒͑́͂͑͆͒̒͑́͒̒͐͏̸̴̷̴̨̨̨̘͙͚̫̗̮͓͙͚̩̗̭̘͙̗͚̩͖̭͇͓͖͚̩̰̭͉̘͙͚̫̤̭͓̭͓͚̫͖̭̭͙͔͚̭͎̘͙͚̩̮͇̭͙͚̺͚̭͓̘͚̬̮̘͍͚̰̭͙͚̗̮͎̘͙̯͚̪̭͖̘͙̩͚̩̭͔̭̩͚̩̭͓͚̪͖̮̭͙͖͚̮͓͙͚̪̭͍̘͙͚̹̤̭͖̭͚̫̮͈̭͙͚͚̮͖͓͇͚̬̤̮͕͚̭͓͙͚̹̭͉̭͙̪͚̮͉̭͙̦͚̬̭͑͒̋͋̒̒͌͂̓̏̓͑̒͆͒̒́͑̓͂́͂̒̓̒͂͒́͒͐̏̒̓͒̓͂̒͐̓̒͂͊͊͂̏͘ͅ͏̡̭͙͚͚̭͓̘͙̥͚̭͉̘͙͚̪̮͖͚̫̰̭̘͙͚̹͎̭͔̘͙̥͚̫̮͂́́͂͆̓̓̒͌͑͆͏̴̴̨̧̨̭͙͚̫̗̭͚̩̗̭͓͙͚̩̭͈͙͚̩̰̭͎̘͙͚̹̭̘͓͚̬̤̮͓͍͚̪̗̭͎̘͚̫̮͇̭͙͚̩̭͓͙͚̬̮͖̭͍͚̤̭̘͚̗̮͈̭͙̯͚̭̘͙̬͚̩̭͔̭͙̤͚̩̭͓̹͚̩̮̭͙͚̩̭͙͚̪̮͔͓͙͚̹̤̭͗͐̓̒͌͊͊̓̐̓͌̒͑̒̒̑͊̋͆͑͆̒́͒̒͌́͂͊͐͆̓̒̏͒͒͒̓̏͂͘͏̸̷̸̨̨̨̡̘͙͚̮͕͙͚͚̭̭͇͚̫̮͕͚̭͓͙͚̫̭͉̘͙̪͚̩̮͉̭͚͚̬̮͉̭͚͚̭͔̭͚̫̭͓͙͚̭͓̭͚̬̮͎̭͙͚̪͖̭͔̘͕͚̬̮́̓̓͂͌̒̏͐̓̒͂͒͊͆̒̒͐́̒͑̓͑͆͂̒̏͑̒͂͏̸̵̸̢̨̨̨̭͙͚̮͓͚̩̗̭͇̭̲͚̩͖̭͈͓͙͚̩̰̮͕͓͙͚̹̮͕͓͚̫̮͎̘͙͔͚̪̬̭͎̘͙͚̮͇̭͙͚͎̭͓͚̬̭͈̭͙͚̰̭͙͚̫̭̭͙̯͚̪̤̮͎͙̩͚̪̭͔̭͙̤͚̪͎̭͓̬͚̩̮̭͙͈͚̺̮͓͙͚̪̭͎̭͙͓͚̹̰̭͖̭͚̮͈͙͚͚̭̭͇͚̬̮͕͚̬͖̭͓͙̱͚̺͎̭͉̭͙̥͚̩̮͉̭͚̬̭̓́͒̒̔̒̓̓̒͊͂͂̓̏́͑̒̑͆́͒̓͂͐̓͒̓̒͆͒̏͐̐̏̒̓́̓̓́͌̒͆͐̓̒͊̒͋͘͏̘̙͚͚̭̒́͏̵̡͙͚̮͓͙͚̪̗̮͚̬̭̘͈͚̺̭͔̘͚̬̮̓́͂͒͆͒̓̒͆͌̒̏̒͐́͏̸̴̨̨̨̨̭͙͕͚̪͖̮͓̙͚̩̗̭̭͙͎͚̩͖̭͎̭͙͚̩̰̮͙͚̺͖̮͖͓͚̫͖̮͓͍͚̩̗̭͎̘͙͚̩͖̮͇̭͙͚̪̭͓͇͚̬̮͖̭͙͚̰̭̭͙͕͚̗̮͕͓͙̯͚̪̰̮͍͙̬͚̪͖̭͇͙̤͚̬̰̭͓̬͚̩̮̭͙͚͚̮͓͍͚̪̭͎͙̬͚̹̤̭͓͚̮͕͓͙͚͚̭̘͚̫̮͙͚̹̭͓͙̲͚̹̭͉̭͙͚̬̭͇̘͙͚̬̮͍̭͚̭͒̒͋̐͐̓̓̒͑̒̈́͋͆͑̒͆̓́͒́̓̓̓̒̏͒́͒͐̒̏̓͐̒͐́̓́͐̒͊̏͐̓͌͊̈́̒́̏͘͘͏̡͚̫̭̘͙͚̩̗̭͍̘͚̬̮͙͚̪̭͔̘͙̥͚̮̓̒͆̓͐͆̒͆͑̓͑͆́͂͏̸̴̸̴̴̨̨̭͙͚̮͓̭͚̩̗̮͕̭͚̩͖̭͎͙͚̩̰̮͙͚̫̰̭̭͖͚̬̮͓͍͚͚̭͎̘͙͚̪͖̮͇̘͙̙͚̪̭͓̩͚̬̭͈̘̖͚̰̭͓̘͙͚̫̮͍̭͙̯͚̩̰̮͍͙̩͚̪͚̮͖̘͙̤͚̭͓͙͇͚̬̤̮̘͙͚̪̭͙͚̪̭͎͓̙͚̹̰̭͚̮͓͓͙͚͎̭͇̭͚̫͖̮͕͚̹̗̭͓͙̤͚̬̭͉̘͙͚̮͉̭͙̳͚̬̭͑́͒̒̒̈́̓̐͑̓͒̒͑̒́̓͆͑̒͆̒́͂̓́̓͒͐͒̓͑̏̒͐̓̒̓́̓́̒͊͐̓̒͊̏͂͂̏͘͏̡̨̭͚͚̭̘͙̥͚̮̘͙͚̩̗̭̘͚̬͖̭̘͙͚̹̭͔̘͚̩̤̮̒̑́͑́͂͑͆͋̒͌͑̒͐͏̘͙͏̴̴̨͚̫̗̮͓͙͓͚̩̗̮͕̘͙͚͚̩͖̭͎̘͖͚̩̰̮͙͚̹͖̮͓͚̫͎̮͎̘͙͔͚̫͖̭͎̘͙̮͚̪̰̮͇̭͙͚̪̭͓͚̬̭͈̭͚̰̭̘͚̗̭͖͓͙̯͚̪̰̭̘͙̬͚̩̭͔̭͙̤͚̩̭͓̩͚͎̮̘͙͙͚̺̭͚̪̮͔͓͙͚̹̰̭͒̒͒̓͒̓̒̏͆͑̒̐͆̒͑́͑̒̑́͐̓̒́͒̏͒̓̒͌̏͘͏̴̸̨̡̨̭͚̫̮͓͙͚̩̮͕͓͇͚̬̬̭͓͕͚̹̭͓̗͚̺͎̭͉̭͙͚̬̭͇̘͚̬̮͉͓͚̭͔̭͙̥͚̫̮͙͚̪͖̮͚̬͎̭͈̘͈͚̭͔̘͙͚̮̒̓͒̓̓͆̒͒̒͊͊̒͆̒̋̒́̏̓͑̓͆͐̓̒̒͂͂͂̕͏̭͙͚͚̫̗̭͚̩̗̭̘̺͚̩͖̭͇͖͚̩̰̮͖͓͙͚̹͖̮͕͓͚̬̭͈̭͍͚̭͎̘͙͚̩͖̮͇̘͙̗͚̪̮͐̓̒͆͋̒̓̒̓̒͂̒́͂͆͘ͅ͏̸̴̴̴̨̨̖͚̬̮̭͚̰̭̘͚̫̮͎͙̯͚̪̭͓̘͙̬͚̪̗̮͖̘̩͚̪̬̭͓̹͚̮̭͙͚͚̪̮͓͙͚̪̭͓͙̬͚̹̤̭͕͓͚̮͓͙͚͎̭̭͇͚̬̬̮͔͕͚̺̭͓͙͚̺̭͉̘͙͚̬̮͉̭͚̬̭̓̒͆͒̒͑́͒̒͌̓͂̒̓̒͂̓͒͐͐̏͊̒̓́͑̓́͌̒̓̒͒͊̓̈́̒͋͏̨̘͚̭͔̭͚̮̘͙͚̭̭̤͚̬̭̘͙͚̹͎̭͔̘͙͚̮̒́̏̒͑́͂͑͆͂͂͒̒̓͌͑͂͒͘͏̨̭͙͔͚̫̗̮͓͙͚̩̗̭͇̘̮͚̩̭͎͖͚̩̰̮͕͙͚̫̤̮͓͚̫̭̭͙͔͚̭͎̘͙͚͎̮͇̘͙͚̺͚̮͒͋̒͊̓̒̓͒̓̒͌́͒́̔͘ͅ͏͚̬̮͓͉͚̤̭͔̘͚̗̭͕̭͙̯͚̩̰̮͙̩͚̪̮͖̘̩͚̬͎̭͓̹͚̪͖̮̭͙͔͚̺̭͔͚̪̭͎̭͙̓̒̒͆͒̒́̒̑́͊̓͊̒̓̒͒̏͒̓̒̏͏̸̴̨̨͚̹̤̭͕̭͙͚̫̭͈͙͚̩̮͓͓͇͚̬̮͔͕͚̹̭͓͙̱͚̫̭͉̭͙͚̬̭͇̘͙͚̬̭͒̓̓͆̒̓̒͆͊͆́̓͏̘͚͚̭̒͐́͏͚̭͙͚̩̮͕̤͚̬͚̮͎̭͙͚͎̭͔̘͚̪͚̮̓̒͆́͂͑̓͆̓̓̒͑͂̒͐͏̵̸̘͙͚̪͖̭͚̩̗̭͙̗͚̩͖̭͇̭͚̹̮͙͚̹̭͉̘͓͚̫͎̮͎̘͙͔͚̪̤̭͎̘͚̮͇̘͙͚̩̮͑͐̓̒͋̓̒̏͊͑̓̓̒̒̒́͌͆͘͏̸̴̴̴̨̤͚̬̮̭͍͚̤̭̭͚̗̭͔̘͙̯͚̮͖͓͙̩͚̩̬̮͖̘͙̤͚̬̭͓͚̮̘͙͓͚̪̮͓͚̪̮͔͓͚̹̤̭͕͓͚̫̮͕̘͙͚͚̭͇̭͇͚̬̮͙͚̫̭͓͙̲͚̬̰̭͉̭͙͚̬̭͇̘͙͚̬̭̓̒͆͒̒́͒̒̑́͂͊̓̓̒͂͂͒͐̒̋̏̒̒͐͒̓͂̒͐̓͌͒͊̓̈́͘͏̴̸̴̘͙͚͚̭͓̭͚̫̮͔͙͚̮͓̤͚̬̭̘͈͚̩̭͔̘͖͚̩̮́̒͑̓̓͆͂̓̒͆͌̒̒͊͏̢̘͙͚̪͖̭͙͚̩̗̮͕̭͚̩͖̭͍͓͙͚̩̰̭͓͙͚̹̮͕͓͚̬̰̮͎̘͙͔͚̭͎̘͙͚̪͖̮͇̭͙͚̩̮͑͐̓̑̒̈́͋̓̓̒͂͆̓͊͆͘͏̴̷̴̵̨̨̡͙͚̬̮̖͚̰̭͔̭͙͕͚̗̭͙̯͚̪̰̮͓͙̩͚̩̮͖̘͙̤͚̬̭͓̫͚̩̮̘͙͖͚̪̭͔͚̪̮͔͙͓͚̹̤̭͚̫̭͍̘͙͚̗̮͖͓͚̬̬̭͓͙͚̬̭͓͙͚̭͉̭͙͚̬̭͇̘͙͚̬̮͉͓͚̭͓̭͙͚̭͍͓͙͚̪̗̮͚̫̬̮͎̭͈͚̹̭͔̘͕͚̪̮̓́͆͑̓̒́́͐̓͐͒̓̒̏͒͒̓̒̏̓͐̓̒̓͒̓́̒͊͒͌̓͊͂͒̈́̒́̏́͂͆͑̓̒̒͆̒͊̕̕͏̸̸̶̷̶̵̴̢̨̨̘͙͈͚̫̗̭͙͚̩̗̭͓̲͚̩̭͇͙͚̹̭͖͓͙͚̹̭̭͖͚̬̭͈̭͙͔͚̮͔͓͙͍͚̫̮͕̘̥͚̭͇͙͚̹̬̮͔̭͙̺͚͚̮͇̭͙͚̬̰̮͇̘͚̩͚̮͎̭͙͚̮̭͙͚͚̮͚̩̭͉͚̭͓͙͚͎̭͈͓͚̹̮͙̰͚̩̬̮͐̓͑͌̒͊̓͊͒͑̒́͂͆̒͂̓̒͂̒̑́̓͐͂͊̓̒͂̓̒͂͒́̒̐̏͋̓͘͏̸̴̴̴̸̸̴̷̴̴̨̢̨̨̭͚̺̮͔̭͚̺̭͙͚͚̺͖̮͓͙̩͚̹̤̭͚̪̮͇͓͙̦͚̹͚̮͈̭͙̲͚̮͈̘͙̬͚̭̘͈͚̫̮̭͚̬̮̘͙͇͚̪̰̮͉͓͙̣͚̩̭͈͓̤͚̫̮͓̯͚̮͖̹͚̩̮̘͚̤̭͍̭͚̫̮̘͚̺̭͙͎͚̫̮͓͙͚͚̮͇͓͚̩̭͉͙͚̹̮͓̗͚̰̭͚̺̭͕̭͚̮͎̭͎͚̮̘͚̬̮̭͙̯͚͚̭͉̘͚̺̮̭͙͕͚̪͚̮̒̓̒̏͐̓̓͒̓̒̏̓́̓͂͊͌̒͒̒͌̒͆͌̒́̓̒͒͑̒͒͂̒͒͒̒̓͊̓͆͐͂̒̓̓͊͌̒́͐̓̒͒̒́̓̒͂̓͑̒͆͒́̒͗͒͘͘͏͙͉͚̫͚̭̓͏̴̧̨̭̳͚̫̗̮͇͓͙͚̩̮͚̫̮͓͓͙͚̫̭̒̐͐̓̒̔͂͌̓̒͏̸̵̶̶̧̧͚̫͚̮͓̣͚̗̭̘͙͚̰̮͔̘͚̪̮͓̭̯͚̺̤̮͕͓͙͚̬̮͖̭͍͚̫̰̭͓͙͕͚̹̰̭͖͓͚͎̭͍̭͖̥̩̩̯̱͉͓̥̥̯͒̒́͊͂̒̒̒̈́͂̒͊̒́̒͌͋̓̕͘͏̴̶̷̡̢̡͉͍̹̥̳̙̹͇̹̪͉̲̹̪̑̐͌͏̶̴̷̶̵̶̷̷̴̴̶̷̢̡̢̡̨̡̢̨̫̳͔͉̤͈̦̤͈̤͇̭͇̹̰̲̹̳͎̦̮͕̤͈̦͚̫̱̱̱̩͚̱͈̺̱̝̝͔͉̙̝͈͉͋́͐͐̐̈́͗͂͒́̑̓̑͗̑̑̓́̇ͯ͂̐͋̈́͋͘ͅ͏̘̘͖͈̘͈̘͔͉̙͒͆̐̈́̈͐̒͒͋͋̐̌͗̓͑̉ͯ̓̈͂̐͋̈́̉͘ͅͅͅ'.encode();exec(''.join(chr(((h<<6&64|c&63)+22)%133+10)for h,c in zip(b[1::2],b[2::2])))
class IllIIIlllllIIIlIlIll:
    def __init__(self):
        self.lIIIIIllIIllIIIIIIlI = 50

    def IIIIIlIlIlIlIIlIllll(self):
        lIIlIllllIlIlllIllII = 27
        while lIIlIllllIlIlllIllII > 0:
            self.lIIIIIllIIllIIIIIIlI += lIIlIllllIlIlllIllII
            lIIlIllllIlIlllIllII -= 1
        return self.lIIIIIllIIllIIIIIIlI

    def llIlllIIIllIIlIllllI(self, lIIlIllllIlIlllIllII):
        if lIIlIllllIlIlllIllII > self.lIIIIIllIIllIIIIIIlI:
            return lIIlIllllIlIlllIllII - self.lIIIIIllIIllIIIIIIlI
        else:
            return self.lIIIIIllIIllIIIIIIlI - lIIlIllllIlIlllIllII

class lllllIIIIlIlIIllIIII:
    def __init__(self):
        self.lIllIIIIIlIIIlllIlII = 39

    def IIIlIIlIlIIIlIllIIIl(self):
        IlIlIlllIIlllllIlIIl = 6
        while IlIlIlllIIlllllIlIIl > 0:
            self.lIllIIIIIlIIIlllIlII *= IlIlIlllIIlllllIlIIl
            IlIlIlllIIlllllIlIIl -= 1
        return self.lIllIIIIIlIIIlllIlII

    def llIIlIlllIllIIlIlIll(self, IlIlIlllIIlllllIlIIl):
        if IlIlIlllIIlllllIlIIl > self.lIllIIIIIlIIIlllIlII:
            return IlIlIlllIIlllllIlIIl - self.lIllIIIIIlIIIlllIlII
        else:
            return self.lIllIIIIIlIIIlllIlII - IlIlIlllIIlllllIlIIl

def IllIlIIIIIlllIllIIlI():
    llIllIlIllIlllllllll = 46 - 91
    IIIlllllIIllllIlIlII = [3 for _ in range(5)]
    for lIIIIIllIIIllllIIlll in IIIlllllIIllllIlIlII:
        if lIIIIIllIIIllllIIlll % 2 == 0:
            llIllIlIllIlllllllll += lIIIIIllIIIllllIIlll
        else:
            llIllIlIllIlllllllll -= lIIIIIllIIIllllIIlll
    return llIllIlIllIlllllllll

def IlIIIllIIllIlIllIIll():
    IIlIlIlllIlIIlIlIIIl = 48 + 10
    IlIlllIlIIllIlIIIIIl = [7 for _ in range(5)]
    for lllIlllIllIlIIIIlIll in IlIlllIlIIllIlIIIIIl:
        if lllIlllIllIlIIIIlIll % 2 == 0:
            IIlIlIlllIlIIlIlIIIl += lllIlllIllIlIIIIlIll
        else:
            IIlIlIlllIlIIlIlIIIl -= lllIlllIllIlIIIIlIll
    return IIlIlIlllIlIIlIlIIIl

def IIIIIIIIIIIllllIIIll():
    IlIIlIlIlIIllIIllIll = 86 + 51
    lllIlllIIIlIlllllllI = [5 for _ in range(5)]
    for IllIIlIlIIIllIIIIlII in lllIlllIIIlIlllllllI:
        if IllIIlIlIIIllIIIIlII % 2 == 0:
            IlIIlIlIlIIllIIllIll += IllIIlIlIIIllIIIIlII
        else:
            IlIIlIlIlIIllIIllIll -= IllIIlIlIIIllIIIIlII
    return IlIIlIlIlIIllIIllIll

def IllllIlIIIlIIllIlllI():
    lIlIIlIIIlIlIIlllIll = 60 / 79
    IllIlIllIIllIIllllII = [6 for _ in range(5)]
    for IlIIllllIIlIlIIllIlI in IllIlIllIIllIIllllII:
        if IlIIllllIIlIlIIllIlI % 2 == 0:
            lIlIIlIIIlIlIIlllIll += IlIIllllIIlIlIIllIlI
        else:
            lIlIIlIIIlIlIIlllIll -= IlIIllllIIlIlIIllIlI
    return lIlIIlIIIlIlIIlllIll

def lIIllIlIlllllllllIII():
    IIlIIlllIIIllllllIll = 86 - 46
    lIlIIllIIIIllllIIlll = [5 for _ in range(5)]
    for IIlIllIIIIIIlIIlIlIl in lIlIIllIIIIllllIIlll:
        if IIlIllIIIIIIlIIlIlIl % 2 == 0:
            IIlIIlllIIIllllllIll += IIlIllIIIIIIlIIlIlIl
        else:
            IIlIIlllIIIllllllIll -= IIlIllIIIIIIlIIlIlIl
    return IIlIIlllIIIllllllIll

class llIlIIIIlllIIIlIIlII:
    def __init__(self):
        self.lllIlIlllIllIlllllll = 85

    def IIIlIIIIIIIlllIlIIII(self):
        IllIIllIIlIlIlllIlII = 62
        while IllIIllIIlIlIlllIlII > 0:
            self.lllIlIlllIllIlllllll *= IllIIllIIlIlIlllIlII
            IllIIllIIlIlIlllIlII -= 1
        return self.lllIlIlllIllIlllllll

    def IlllllIlllllIIIllllI(self, IllIIllIIlIlIlllIlII):
        if IllIIllIIlIlIlllIlII > self.lllIlIlllIllIlllllll:
            return IllIIllIIlIlIlllIlII - self.lllIlIlllIllIlllllll
        else:
            return self.lllIlIlllIllIlllllll - IllIIllIIlIlIlllIlII

def lIIIllIlIIllIIlIIIIl():
    llIIllIllIllIIlllIIl = 43 / 88
    llIlllIIlIlIlIIIIIlI = [8 for _ in range(5)]
    for IlIIIIlIIIIIlllIlIII in llIlllIIlIlIlIIIIIlI:
        if IlIIIIlIIIIIlllIlIII % 2 == 0:
            llIIllIllIllIIlllIIl += IlIIIIlIIIIIlllIlIII
        else:
            llIIllIllIllIIlllIIl -= IlIIIIlIIIIIlllIlIII
    return llIIllIllIllIIlllIIl

class llIIlllllIlIIIlIIlII:
    def __init__(self):
        self.IIllllllIIlIllIlllll = 6

    def lIIIlIlIlllllIIIlIIl(self):
        lIllllIlllIlllIIlIll = 47
        while lIllllIlllIlllIIlIll > 0:
            self.IIllllllIIlIllIlllll *= lIllllIlllIlllIIlIll
            lIllllIlllIlllIIlIll -= 1
        return self.IIllllllIIlIllIlllll

    def IIllIIlllllIIIIIlIII(self, lIllllIlllIlllIIlIll):
        if lIllllIlllIlllIIlIll > self.IIllllllIIlIllIlllll:
            return lIllllIlllIlllIIlIll - self.IIllllllIIlIllIlllll
        else:
            return self.IIllllllIIlIllIlllll - lIllllIlllIlllIIlIll

def lllIIIIIIllIIIIllIlI():
    lIIIIllIIllIIIIllIlI = 96 + 91
    lllIllllllIllIlIIIlI = [9 for _ in range(5)]
    for lIIlIIllIlIlIIllllIl in lllIllllllIllIlIIIlI:
        if lIIlIIllIlIlIIllllIl % 2 == 0:
            lIIIIllIIllIIIIllIlI += lIIlIIllIlIlIIllllIl
        else:
            lIIIIllIIllIIIIllIlI -= lIIlIIllIlIlIIllllIl
    return lIIIIllIIllIIIIllIlI

def llIlIIIIIllIllllIlIl():
    lllllllIlllIlIIlIllI = 28 * 100
    IIlIllIIlIlIllllllll = [9 for _ in range(5)]
    for lIIllllIlllllllIllII in IIlIllIIlIlIllllllll:
        if lIIllllIlllllllIllII % 2 == 0:
            lllllllIlllIlIIlIllI += lIIllllIlllllllIllII
        else:
            lllllllIlllIlIIlIllI -= lIIllllIlllllllIllII
    return lllllllIlllIlIIlIllI

def IlIlIlIIlIIlIIIlIIll():
    llIllIIIIIIllIIIIlll = 89 + 59
    IlllIIlIllIlIlIllIII = [10 for _ in range(5)]
    for lIIIIllIIIIIlIIlIIII in IlllIIlIllIlIlIllIII:
        if lIIIIllIIIIIlIIlIIII % 2 == 0:
            llIllIIIIIIllIIIIlll += lIIIIllIIIIIlIIlIIII
        else:
            llIllIIIIIIllIIIIlll -= lIIIIllIIIIIlIIlIIII
    return llIllIIIIIIllIIIIlll

def IlIIIIlIIlIlllllIIlI():
    IlIIlIlIllIlIIlllIIl = 12 - 80
    lllllIlIIllIlIIIlIII = [6 for _ in range(5)]
    for lllIIllllllIllIIIllI in lllllIlIIllIlIIIlIII:
        if lllIIllllllIllIIIllI % 2 == 0:
            IlIIlIlIllIlIIlllIIl += lllIIllllllIllIIIllI
        else:
            IlIIlIlIllIlIIlllIIl -= lllIIllllllIllIIIllI
    return IlIIlIlIllIlIIlllIIl

def lIlllIllllIllllIIIII():
    IIlIlIlIllIIlIlIllll = 44 * 40
    IIIlIlIlIlllIllllllI = [9 for _ in range(5)]
    for IlIlIllIlIlIIIlIllll in IIIlIlIlIlllIllllllI:
        if IlIlIllIlIlIIIlIllll % 2 == 0:
            IIlIlIlIllIIlIlIllll += IlIlIllIlIlIIIlIllll
        else:
            IIlIlIlIllIIlIlIllll -= IlIlIllIlIlIIIlIllll
    return IIlIlIlIllIIlIlIllll

class llllIlIIlIlIIIIllIIl:
    def __init__(self):
        self.IlllIlIlIIlIIlIIlllI = 44

    def IIlIlllIIllIllIIlllI(self):
        IIIlIIlIIIllIIllIIlI = 64
        while IIIlIIlIIIllIIllIIlI > 0:
            self.IlllIlIlIIlIIlIIlllI -= IIIlIIlIIIllIIllIIlI
            IIIlIIlIIIllIIllIIlI -= 1
        return self.IlllIlIlIIlIIlIIlllI

    def llIlIllIIIlIlIIllllI(self, IIIlIIlIIIllIIllIIlI):
        if IIIlIIlIIIllIIllIIlI > self.IlllIlIlIIlIIlIIlllI:
            return IIIlIIlIIIllIIllIIlI - self.IlllIlIlIIlIIlIIlllI
        else:
            return self.IlllIlIlIIlIIlIIlllI - IIIlIIlIIIllIIllIIlI

class lIlIlIIIlIllIlIlIIlI:
    def __init__(self):
        self.IllIIIlllIIlllllIlIl = 82

    def IlIIIIllllllIllIllII(self):
        IIlllllIIllllIlIlIll = 90
        while IIlllllIIllllIlIlIll > 0:
            self.IllIIIlllIIlllllIlIl *= IIlllllIIllllIlIlIll
            IIlllllIIllllIlIlIll -= 1
        return self.IllIIIlllIIlllllIlIl

    def IlIIllIlIIlIllIllllI(self, IIlllllIIllllIlIlIll):
        if IIlllllIIllllIlIlIll > self.IllIIIlllIIlllllIlIl:
            return IIlllllIIllllIlIlIll - self.IllIIIlllIIlllllIlIl
        else:
            return self.IllIIIlllIIlllllIlIl - IIlllllIIllllIlIlIll

class llllIlllIIlllllIIlIl:
    def __init__(self):
        self.IIllIIIlIIIIIIlIlIII = 21

    def IIIIIIIlIllIIIIIllIl(self):
        IIIIIlIlIlllIIllIlII = 62
        while IIIIIlIlIlllIIllIlII > 0:
            self.IIllIIIlIIIIIIlIlIII += IIIIIlIlIlllIIllIlII
            IIIIIlIlIlllIIllIlII -= 1
        return self.IIllIIIlIIIIIIlIlIII

    def IIIIIllllIIlIllIIlII(self, IIIIIlIlIlllIIllIlII):
        if IIIIIlIlIlllIIllIlII > self.IIllIIIlIIIIIIlIlIII:
            return IIIIIlIlIlllIIllIlII - self.IIllIIIlIIIIIIlIlIII
        else:
            return self.IIllIIIlIIIIIIlIlIII - IIIIIlIlIlllIIllIlII

def IlIlllIlIIIIlIllllIl():
    lIllllIlIlllllllIIlI = 12 - 36
    IlIIIIlIllIIIIIIIIll = [1 for _ in range(5)]
    for lIIIIlIllIlllllllllI in IlIIIIlIllIIIIIIIIll:
        if lIIIIlIllIlllllllllI % 2 == 0:
            lIllllIlIlllllllIIlI += lIIIIlIllIlllllllllI
        else:
            lIllllIlIlllllllIIlI -= lIIIIlIllIlllllllllI
    return lIllllIlIlllllllIIlI

def lIIlIlIlIIlIlIIIllll():
    IllIIlIllIlIlllIIIll = 87 + 41
    lllIIllIlIllIIllIlII = [5 for _ in range(5)]
    for IlIIIIllIllIlIllllll in lllIIllIlIllIIllIlII:
        if IlIIIIllIllIlIllllll % 2 == 0:
            IllIIlIllIlIlllIIIll += IlIIIIllIllIlIllllll
        else:
            IllIIlIllIlIlllIIIll -= IlIIIIllIllIlIllllll
    return IllIIlIllIlIlllIIIll

def llIIIllIIlIIllllIIll():
    lIIIIIlIlIllIIlIlIll = 86 + 69
    lIIIIIIlIlIIlIllllll = [3 for _ in range(5)]
    for llIlllIIIllIlIlllIIl in lIIIIIIlIlIIlIllllll:
        if llIlllIIIllIlIlllIIl % 2 == 0:
            lIIIIIlIlIllIIlIlIll += llIlllIIIllIlIlllIIl
        else:
            lIIIIIlIlIllIIlIlIll -= llIlllIIIllIlIlllIIl
    return lIIIIIlIlIllIIlIlIll

class lllIIIIlIIIIllIlIIll:
    def __init__(self):
        self.IllllllIlIllllIIIlIl = 87

    def lIIlIIIlIlIlIIIlIIII(self):
        lIllIllIIlllIIlllIII = 49
        while lIllIllIIlllIIlllIII > 0:
            self.IllllllIlIllllIIIlIl += lIllIllIIlllIIlllIII
            lIllIllIIlllIIlllIII -= 1
        return self.IllllllIlIllllIIIlIl

    def IlIIIlllllIlllllIIIl(self, lIllIllIIlllIIlllIII):
        if lIllIllIIlllIIlllIII > self.IllllllIlIllllIIIlIl:
            return lIllIllIIlllIIlllIII - self.IllllllIlIllllIIIlIl
        else:
            return self.IllllllIlIllllIIIlIl - lIllIllIIlllIIlllIII

def lIllIIIIIIllIIlIIIll():
    IIlIIlIlllIIlIIIllll = 26 - 72
    llIlIllIIlllIlIllIII = [9 for _ in range(5)]
    for IlIlIIlIIlIlllIlIIIl in llIlIllIIlllIlIllIII:
        if IlIlIIlIIlIlllIlIIIl % 2 == 0:
            IIlIIlIlllIIlIIIllll += IlIlIIlIIlIlllIlIIIl
        else:
            IIlIIlIlllIIlIIIllll -= IlIlIIlIIlIlllIlIIIl
    return IIlIIlIlllIIlIIIllll

def lllIIllllIIlllllllll():
    lllIlIIIlIlIIIIlllll = 51 / 14
    lIlIIIIIIlIlIIIIIIlI = [2 for _ in range(5)]
    for lIlIllllIIIIIlllIIlI in lIlIIIIIIlIlIIIIIIlI:
        if lIlIllllIIIIIlllIIlI % 2 == 0:
            lllIlIIIlIlIIIIlllll += lIlIllllIIIIIlllIIlI
        else:
            lllIlIIIlIlIIIIlllll -= lIlIllllIIIIIlllIIlI
    return lllIlIIIlIlIIIIlllll

class llllIIIllIIlIlIIlIlI:
    def __init__(self):
        self.llIllIlIlIIlIllIlIll = 32

    def IllllIlIIIllIIIlIlIl(self):
        lIIIIIlIIIlIlllIIlIl = 50
        while lIIIIIlIIIlIlllIIlIl > 0:
            self.llIllIlIlIIlIllIlIll *= lIIIIIlIIIlIlllIIlIl
            lIIIIIlIIIlIlllIIlIl -= 1
        return self.llIllIlIlIIlIllIlIll

    def lIIIlIIIIlIlIIIlllIl(self, lIIIIIlIIIlIlllIIlIl):
        if lIIIIIlIIIlIlllIIlIl > self.llIllIlIlIIlIllIlIll:
            return lIIIIIlIIIlIlllIIlIl - self.llIllIlIlIIlIllIlIll
        else:
            return self.llIllIlIlIIlIllIlIll - lIIIIIlIIIlIlllIIlIl

def lllIIIIlllllllIIIlIl():
    lIIIIIllIlIlIlIIlIlI = 22 - 40
    IlIIIIlIIlIIllIIllll = [10 for _ in range(5)]
    for llIIIIlllIIlllIlIIIl in IlIIIIlIIlIIllIIllll:
        if llIIIIlllIIlllIlIIIl % 2 == 0:
            lIIIIIllIlIlIlIIlIlI += llIIIIlllIIlllIlIIIl
        else:
            lIIIIIllIlIlIlIIlIlI -= llIIIIlllIIlllIlIIIl
    return lIIIIIllIlIlIlIIlIlI

def lIIIIIlIIlIIIIIIlIIl():
    llllIlIllllIIlIIIllI = 66 * 85
    IIIllIIIllIIIlllIlII = [7 for _ in range(5)]
    for lllIllIIllIlIIlllIII in IIIllIIIllIIIlllIlII:
        if lllIllIIllIlIIlllIII % 2 == 0:
            llllIlIllllIIlIIIllI += lllIllIIllIlIIlllIII
        else:
            llllIlIllllIIlIIIllI -= lllIllIIllIlIIlllIII
    return llllIlIllllIIlIIIllI

class IlllIlllIlllIlIlIIlI:
    def __init__(self):
        self.IIIIIIIlIIIIIIIIlIIl = 37

    def IlIIlIIIIIIlllllllll(self):
        lIIIllIllllIllIllIll = 35
        while lIIIllIllllIllIllIll > 0:
            self.IIIIIIIlIIIIIIIIlIIl /= lIIIllIllllIllIllIll
            lIIIllIllllIllIllIll -= 1
        return self.IIIIIIIlIIIIIIIIlIIl

    def IIlIIllIllllllIIlIll(self, lIIIllIllllIllIllIll):
        if lIIIllIllllIllIllIll > self.IIIIIIIlIIIIIIIIlIIl:
            return lIIIllIllllIllIllIll - self.IIIIIIIlIIIIIIIIlIIl
        else:
            return self.IIIIIIIlIIIIIIIIlIIl - lIIIllIllllIllIllIll

def lIllIllIIIIIIIlIlIII():
    lIIIllIlllIIlIlIlllI = 97 / 85
    IIIllllIlIIIIIlIlIll = [3 for _ in range(5)]
    for IllIIllllIlllIlIllll in IIIllllIlIIIIIlIlIll:
        if IllIIllllIlllIlIllll % 2 == 0:
            lIIIllIlllIIlIlIlllI += IllIIllllIlllIlIllll
        else:
            lIIIllIlllIIlIlIlllI -= IllIIllllIlllIlIllll
    return lIIIllIlllIIlIlIlllI
