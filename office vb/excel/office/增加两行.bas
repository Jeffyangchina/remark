Attribute VB_Name = "模块2"
Sub 增加两行()
    Dim n As String, m As String, j As String, h As Integer
    Set fs = Application.FileSearch
    With fs
        .LookIn = "D:\d"
        .Filename = "*.*"
        If .Execute > 0 Then
            For i = 1 To .FoundFiles.Count
                Workbooks("he.xls").Sheets("sheet2").Cells(i, 1) = .FoundFiles(i)
                j = i
                Windows("he.xls").Activate
                Worksheets("sheet2").Select
                m = "A" + j
                n = Range(m)
                Workbooks.Open Filename:=n
                If Cells(1, 2) <> "" Then
                    Rows("1:1").Select
                    Selection.Insert Shift:=xlDown
                    Selection.Insert Shift:=xlDown
                End If
                Cells.Select
                Selection.EntireRow.Hidden = False
                Selection.EntireColumn.Hidden = False
            Next i
        End If
    End With
End Sub

