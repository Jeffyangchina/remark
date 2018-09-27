Attribute VB_Name = "模块11"
Sub 复制多文件()
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
                hstart = 0
                lend = 1
                For h = 1 To 30000
                    If Cells(h, 4) <> 0 And hstart = 0 Then
                        hstart = h
                    End If
                    If Cells(h + 1, 4) = 0 And Cells(h + 2, 4) = 0 And Cells(h + 3, 4) = 0 Then
                        hend = h
                        Exit For
                    End If
                Next
                For l = 1 To 30
                    If Cells(hstart, l) <> 0 Then
                        lendmax = l
                        If lend <= lendmax Then
                            lend = lendmax
                        End If
                    End If
                Next
                For h = hstart To hend
                    Cells(h, lend + 1) = Workbooks("he.xls").Sheets("sheet2").Cells(i, 1)
                Next
                For hi = hstart To hend
                    For li = 1 To lend + 1
                        a = hi - hstart + 1 + heall
                        Workbooks("he.xls").Sheets("sheet1").Cells(a, li) = Cells(hi, li)
                    Next
                Next
                
                heall = hend - hstart + 1 + heall
            Next i
            MsgBox "共" & heall & "行信息" & "," & lend + 1 & "列信息"
        End If
    End With
    Windows("he.xls").Activate
    Sheets("Sheet1").Select
    Cells(1, lend + 1) = "所属文件"
    For i = 2 To heall
        If Cells(i, 1) = Cells(1, 1) Then
            For a = i To heall
                For b = 1 To lend + 1
                    Cells(a, b) = Cells(a + 1, b)
                Next
            Next
        End If
    Next
End Sub
