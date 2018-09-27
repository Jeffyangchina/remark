Attribute VB_Name = "模块1"
Sub BOM转换—550包转newBOM()
Attribute BOM转换—550包转newBOM.VB_Description = "宏由 zch4537 录制，时间: 2010-7-14"
Attribute BOM转换—550包转newBOM.VB_ProcData.VB_Invoke_Func = " \n14"
    Columns("E:E").Select
    Selection.Insert Shift:=xlToRight
    Columns("M:O").Select
    Selection.Insert Shift:=xlToRight
    Columns("R:R").Select
    Selection.Insert Shift:=xlToRight
    Columns("W:W").Select
    Selection.Cut
    Columns("U:U").Select
    Selection.Insert Shift:=xlToRight
    Columns("W:W").Select
    Selection.Insert Shift:=xlToRight
    Columns("AA:AD").Select
    Selection.Insert Shift:=xlToRight
    Cells(1, 5) = "图号"
    Cells(1, 13) = "规    格"
    Cells(1, 14) = "型    号"
    Cells(1, 15) = "标准号"
    Cells(1, 18) = "重量单位"
    Cells(1, 23) = "订货号"
    Cells(1, 27) = "项目代号"
    Cells(1, 28) = "分类"
    Cells(1, 29) = "所属编码"
    Cells(1, 30) = "备注"
End Sub
