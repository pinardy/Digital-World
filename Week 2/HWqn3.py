def windChillTemp(ta, v):
    twc = (35.74 + 0.6215*ta - 35.75*(v**0.16) + 0.4275*ta*(v**0.16))
    return twc