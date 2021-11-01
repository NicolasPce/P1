#Cleaning Variable Age:

def limpiezasexo(string):
    """
    #Esta función limpia la variable sexo para tener valores homógeneos que faciliten su comparación
    Argumentos:
    Los valores en la columna "Sex ".
    Devuelve:
    Su valor lógico (ie: "M " devuelve "M")
    """
df["Sex "] = df["Sex "].replace({"M ":"M", "lli":"M", "N":"Other", ".":"Other"})

def limpiezaedad(string):
    """
    #Esta función limpia la variable edad para tener valores homógeneos que faciliten su comparación
    Argumentos:
    Los valores en la columna "Age".
    Devuelve:
    Su valor lógico (ie: "20 or 22" devuelve "21")
    """
    df["Age"] = df["Age"].replace({"40s":"45", "20s":"25", "Teen": "16", "60's":"65",
                               "18 months":"2", "30s":"35", "50s":"55","teen":"16", "28 & 26":"27",
                               "18 or 20":"19", "12 or 13":"12", "46 & 34": "40", "28, 23 & 30":"27",
                               "Teens":"16", "36 & 26":"31","8 or 10":"9", "30 or 36":"33", "6½":"7",
                               "21 & ?":"21", "33 or 37":"35","mid-30s":"35", "23 & 20":"21", " 30": "30",
                               "7      &    31": "19", " 28":"28", "20?":"20", "60's":"65", "32 & 30": "31",
                               "16 to 18":"17", "Elderly":"70", "mid-20s":"25", "Ca. 33":"33", "74 ":"74",
                               "45 ":"45", "21 or 26": "24", "20 ":"20", ">50":"60", "18 to 22":"20",
                               "adult":"40","9 & 12":"11", "? & 19":"19", "9 months": "1","25 to 35": "30",
                               "23 & 26":"25","(adult)":"40","33 & 37":"35","25 or 28":"26", "60s":"65",
                               "37, 67, 35, 27,  ? & 27":"35","21, 34,24 & 35":"30","30 & 32":"31",
                               "50 & 30":"40","17 & 35":"26", "middle-age":"40", "13 or 18":"15",
                               "34 & 19":"27", "33 & 26":"30", "2 to 3 months":"1", " 43":"43",
                               '"young"':"20", "7 or 8":"8", "17 & 16":"17", "Both 11":"11", "9 or 10":"10",
                               "young":"20", "36 & 23":"30",'"middle-age"':"40",
                               "?    &   14":"14","10 or 12":"11","31 or 33":"32",
                               "2½":"3","13 or 14":"14"}) 