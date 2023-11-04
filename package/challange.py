def sisa(data):
    gross = (data//144)
    kodi = (data % 144)//20
    lusin = (data % 144 % 20)//12
    buah = (data % 144 %20 %12)
    return print(f"{data} = {gross} gross,{kodi} kodi,{lusin} lusin, {buah} buah")

