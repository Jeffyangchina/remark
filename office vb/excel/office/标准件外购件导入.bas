Attribute VB_Name = "模块1"
Sub 标准件外购件导入()
Attribute 标准件外购件导入.VB_Description = "宏由 zch 录制，时间: 2008-12-12"
Attribute 标准件外购件导入.VB_ProcData.VB_Invoke_Func = " \n14"
    Columns("A:C").Select
    Selection.Insert Shift:=xlToRight
    Columns("E:K").Select
    Selection.Insert Shift:=xlToRight
    Columns("N:N").Select
    Selection.Cut
    Columns("M:M").Select
    Selection.Insert Shift:=xlToRight
    Columns("R:R").Select
    Selection.Cut
    Columns("O:O").Select
    Selection.Insert Shift:=xlToRight
    Columns("X:X").Select
    Selection.Cut
    Columns("P:P").Select
    Selection.Insert Shift:=xlToRight
    Columns("Q:R").Select
    Selection.Insert Shift:=xlToRight
    Columns("AG:AG").Select
    Selection.Cut
    Columns("S:S").Select
    Selection.Insert Shift:=xlToRight
    Columns("AC:AC").Select
    Selection.Cut
    Columns("T:T").Select
    Selection.Insert Shift:=xlToRight
    Columns("X:X").Select
    Selection.Cut
    Columns("U:U").Select
    Selection.Insert Shift:=xlToRight
    Columns("W:W").Select
    Selection.Cut
    Columns("V:V").Select
    Selection.Insert Shift:=xlToRight
    Columns("Z:Z").Select
    Selection.Cut
    Columns("W:W").Select
    Selection.Insert Shift:=xlToRight
    Columns("Z:Z").Select
    Selection.Cut
    Columns("X:X").Select
    Selection.Insert Shift:=xlToRight
    Columns("AA:AA").Select
    Selection.Cut
    Columns("Y:Y").Select
    Selection.Insert Shift:=xlToRight
    Columns("Z:AF").Select
    Selection.Insert Shift:=xlToRight
    Columns("BD:BD").Select
    Selection.Cut
    Columns("AD:AD").Select
    Selection.Insert Shift:=xlToRight
    Columns("AI:AI").Select
    Selection.Cut
    Columns("G:G").Select
    ActiveSheet.Paste
    Cells(2, 2) = 0
    Cells(3, 2) = 1
    Cells(2, 4) = "BZJWGJ"
    Cells(2, 12) = "标准件、外购件库"
End Sub
