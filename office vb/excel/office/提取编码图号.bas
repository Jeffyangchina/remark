Attribute VB_Name = "ģ��11"
Sub ��ȡ����ͼ��()
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
                    If Cells(h, 9) <> 0 And hstart = 0 Then
                        hstart = h
                    End If
                    If Cells(h + 1, 9) = 0 And Cells(h + 2, 9) = 0 And Cells(h + 3, 9) = 0 Then
                        hend = h
                        Exit For
                    End If
                Next
                For hi = hstart To hend
                    a = hi - hstart + 1 + heall
                    Workbooks("he.xls").Sheets("sheet1").Cells(a, 1) = Cells(hi, 8)
                    Workbooks("he.xls").Sheets("sheet1").Cells(a, 2) = Cells(hi, 9)
                    Workbooks("he.xls").Sheets("sheet1").Cells(a, 3) = Cells(hi, 10)
                Next
                heall = hend - hstart + 1 + heall
            Next i
            MsgBox "��" & heall & "����Ϣ" & "," & lend + 1 & "����Ϣ"
        End If
    End With
End Sub
