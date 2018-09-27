Attribute VB_Name = "模块1"
Sub FockeBOM转550包BOM()
Attribute FockeBOM转550包BOM.VB_Description = "宏由 张晨辉 录制，时间: 2011-3-3"
Attribute FockeBOM转550包BOM.VB_ProcData.VB_Invoke_Func = " \n14"

    Columns("L:L").Select
    Selection.Cut
    Columns("O:O").Select
    Selection.Insert Shift:=xlToRight
    Columns("L:L").Select
    Selection.Cut
    Columns("AG:AG").Select
    Selection.Insert Shift:=xlToRight
    Columns("N:O").Select
    Selection.Cut
    Columns("AG:AG").Select
    Selection.Insert Shift:=xlToRight
    Columns("Q:Q").Select
    Selection.Cut
    Columns("T:T").Select
    Selection.Insert Shift:=xlToRight
    Columns("AA:AA").Select
    Selection.Cut
    Columns("U:U").Select
    Selection.Insert Shift:=xlToRight
    Columns("V:AA").Select
    Selection.Insert Shift:=xlToRight
End Sub
