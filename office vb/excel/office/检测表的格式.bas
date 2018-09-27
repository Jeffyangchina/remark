Attribute VB_Name = "模块11"
Sub 检测表的格式()
    Dim n As String, m As String, j As String, h As Integer
    heall = 0
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
                For li = 1 To 19
                    Workbooks("he.xls").Sheets("sheet1").Cells(i, li) = Cells(3, li)
                Next
                Workbooks("he.xls").Sheets("sheet1").Cells(i, 20) = Workbooks("he.xls").Sheets("sheet2").Cells(i, 1)
            Next i
        End If
    End With
End Sub
