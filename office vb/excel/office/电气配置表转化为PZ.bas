Attribute VB_Name = "模块1"
Sub 电气配置表转化为PZ()
    az = 89     '电气配置表行数
    ba = 9      '电气配置表用户起始列数
    bz = 11     '电气配置表用户终止列数
    i = 1
    For a = 2 To az
        For b = ba To bz
            i = (a - 2) * (bz - ba + 1) + (b - ba + 1)  '变量i为（a-2）*用户总数+（b-用户起始列数+1）
            Cells(i, 2) = Sheets("BOM1").Cells(a, 1)
            Cells(i, 4) = Sheets("BOM1").Cells(a, 2)
            Cells(i, 5) = Sheets("BOM1").Cells(a, b)
            Cells(i, 10) = Sheets("BOM1").Cells(1, b)
            Cells(i, 9) = Sheets("BOM1").Cells(a, 8) & Sheets("BOM1").Cells(1, b)
            Cells(i, 1) = 2
            Sheets("BOM1").Cells(a, b) = ""
        Next
    Next
End Sub


