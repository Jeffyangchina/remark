Attribute VB_Name = "模块1"
Sub newBOM转550包BOM()
Attribute newBOM转550包BOM.VB_Description = "ZCH4537 记录的宏 2007-2-15"
Attribute newBOM转550包BOM.VB_ProcData.VB_Invoke_Func = " \n14"
    Columns("E:E").Select
    Selection.Cut
    Columns("M:M").Select
    Selection.Insert Shift:=xlToRight
    Columns("M:P").Select
    Selection.Cut
    Columns("AE:AE").Select
    Selection.Insert Shift:=xlToRight
    Columns("R:R").Select
    Selection.Cut
    Columns("Q:Q").Select
    Selection.Insert Shift:=xlToRight
    Columns("T:T").Select
    Selection.Cut
    Columns("R:R").Select
    Selection.Insert Shift:=xlToRight
    Columns("T:T").Select
    Selection.Cut
    Columns("AE:AE").Select
    Selection.Insert Shift:=xlToRight
    Columns("V:W").Select
    Selection.Cut
    Columns("AE:AE").Select
    Selection.Insert Shift:=xlToRight
    Columns("V:AD").Select
    Selection.Insert Shift:=xlToRight
    Columns("N:N").Select
    Selection.Cut
    Columns("AK:AK").Select
    Selection.Insert Shift:=xlToRight
    Range("U1").Select
    ActiveCell.FormulaR1C1 = "父项代码"
    Columns("AN:AN").Select
    Selection.Cut
    Columns("U:U").Select
    Selection.Insert Shift:=xlToRight
    Columns("V:V").Select
    Selection.ClearContents
    Columns("AG:AJ").Select
    Selection.Cut
    Columns("K:K").Select
    Selection.Insert Shift:=xlToRight
    Columns("G:J").Select
    Range("J1").Activate
    Selection.Cut
    Columns("AK:AK").Select
    Selection.Insert Shift:=xlToRight
    Columns("AL:AL").Select
    Selection.Cut
    Columns("A:A").Select
    Selection.Insert Shift:=xlToRight
    Columns("B:B").Select
    Selection.Cut
    Columns("AM:AM").Select
    Selection.Insert Shift:=xlToRight
End Sub

