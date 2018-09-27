Attribute VB_Name = "模块1"
Sub 虚拟层名称()
    Sheets("Sheet3").Select
    Dim i As Integer
    Dim ma As String
    For i = 1 To 9
        Sheet3.Cells(i + 10, 1) = Sheet3.Cells(i, 1)
        Sheet3.Cells(i + 10, 2) = Sheet3.Cells(i, 2)
        Sheet3.Cells(i + 10, 3) = Sheet3.Cells(i, 3)
        Sheet3.Cells(i, 4) = "（基础部件）"
        Sheet3.Cells(i + 10, 4) = "（变换部件）"
    Next
    Range("E1").Select
    ActiveCell.FormulaR1C1 = "=CONCATENATE(RC[-3],RC[-2],RC[-1])"
    Selection.Copy
    Range("E1:E19").Select
    ActiveSheet.Paste
    Columns("E:E").Select
    Application.CutCopyMode = False
    Selection.Copy
    Selection.PasteSpecial Paste:=xlValues, Operation:=xlNone, SkipBlanks:= _
        False, Transpose:=False
    Dim j As String
    j = 1
    Do While j <= 9
        For i = 1 To 140
            If Sheet1.Cells(i, 1) = 0 Then
                Sheet1.Cells(i, 3) = Sheet3.Cells(11, 2)
                dqma = "26" + Sheet1.Cells(i, 2) + "8000000"
                jcma = "21" + Sheet1.Cells(i, 2) + j + "000000"
                bhma = "23" + Sheet1.Cells(i, 2) + j + "000000"
                dq = i
            End If
            If Sheet1.Cells(i, 2) = dqma Then
                Sheet1.Cells(i, 3) = Sheet1.Cells(dq, 3) + "电气部件"
            End If
            If Sheet1.Cells(i, 2) = jcma Then
                Sheet1.Cells(i, 3) = Sheet3.Cells(j, 5)
            End If
            If Sheet1.Cells(i, 2) = bhma Then
                Sheet1.Cells(i, 3) = Sheet3.Cells(j, 5)
            End If
            If Sheet1.Cells(i, 1) = "" Then
                Sheet1.Cells(i, 3) = ""
            End If
        Next
    j = j + 1
    Loop
    Sheets("Sheet3").Select
    Cells.Select
    Selection.ClearContents
    Sheets("Sheet2").Select
    Cells.Select
    Selection.ClearContents
    Sheets("Sheet1").Select
End Sub

