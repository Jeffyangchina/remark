Attribute VB_Name = "模块1"
Sub Focke数据比对后整理()
Attribute Focke数据比对后整理.VB_Description = "宏由 zch4537 录制，时间: 2010-7-16"
Attribute Focke数据比对后整理.VB_ProcData.VB_Invoke_Func = " \n14"

    a = 1474        '总行数
    
    Columns("AI:AI").Select
    Selection.Cut
    Columns("AH:AH").Select
    Selection.Insert Shift:=xlToRight
    Columns("AL:AL").Select
    Selection.Cut
    Columns("AI:AI").Select
    Selection.Insert Shift:=xlToRight
    For i = 2 To a
        If Cells(i, 36) <> "" Then
            Cells(i, 39) = Cells(i, 36)
            Cells(i, 36) = ""
        End If
        If Cells(i, 37) <> "" Then
            Cells(i, 39) = Cells(i, 37)
            Cells(i, 37) = ""
        End If
        If Cells(i, 38) <> "" And Cells(i, 39) <> "版本更改" Then
            Cells(i, 39) = Cells(i, 38)
            Cells(i, 38) = ""
        End If
    Next
End Sub
