from TestScripts.ReadFromExcel import readWriteExcel

r=readWriteExcel("OrangeHRM_TestData.xlsx")
print(r.readByColIndex("SignIn",4,2))
print(r.readByColName("SignIn",2,"upass"))