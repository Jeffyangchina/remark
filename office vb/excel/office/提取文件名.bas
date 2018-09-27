Attribute VB_Name = "模块11"
Sub 提取文件名()
    Dim n As String, m As String, j As String, h As Integer
    heall = 0
    Set fs = Application.FileSearch
    With fs
        .LookIn = "D:\d"
        .Filename = "*.*"
        If .Execute > 0 Then
            For i = 1 To .FoundFiles.Count
                Workbooks("he.xls").Sheets("sheet2").Cells(i, 1) = .FoundFiles(i)
            Next i
        End If
    End With
End Sub
