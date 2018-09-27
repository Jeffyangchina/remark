Attribute VB_Name = "模块11"
Sub FBG转为新产品格式()
Attribute FBG转为新产品格式.VB_Description = "zch4537 记录的宏 2005-2-28"
Attribute FBG转为新产品格式.VB_ProcData.VB_Invoke_Func = " \n14"
    If Cells(1, 1) <> "序号" Then
        Columns("A:A").Select
        Selection.Insert Shift:=xlToRight
    End If
    Columns("I:I").Select
    Selection.Insert Shift:=xlToRight
    Selection.Insert Shift:=xlToRight
    Range("I1:J1").Select
    Range("J1").Activate
    Selection.Delete Shift:=xlToLeft
    Range("O1").Select
    ActiveWindow.SmallScroll Down:=-9
    Range("L1:N1").Select
    Selection.Insert Shift:=xlToRight
    Columns("L:N").Select
    Selection.Delete Shift:=xlToLeft
    Range("M1").Select
    Selection.Insert Shift:=xlToRight
    Columns("M:M").Select
    Selection.Delete Shift:=xlToLeft
    Range("Q1").Select
    Selection.Insert Shift:=xlToRight
    Columns("Q:Q").Select
    ActiveWindow.SmallScroll Down:=48
    Selection.Delete Shift:=xlToLeft
    Range("S1").Select
    Selection.Insert Shift:=xlToRight
    Columns("S:S").Select
    Selection.Delete Shift:=xlToLeft
    Range("U1").Select
    Selection.Insert Shift:=xlToRight
    Columns("U:U").Select
    Selection.Delete Shift:=xlToLeft
    ActiveWindow.SmallScroll Down:=-3
    Rows("1:1").Select
    Range("M1").Activate
    Selection.Insert Shift:=xlDown
    Selection.Insert Shift:=xlDown
End Sub
