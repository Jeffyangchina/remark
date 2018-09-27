Attribute VB_Name = "模块1"
Sub 电气部件配置汇总()
    For i = 2 To 1666   'BOM行数
        For j = 2 To 41  '配置行数
            If Cells(i, 21) = Sheets("PZ").Cells(j, 1) Then
                For a = 23 To 28   '汇总表中用户列
                    For b = 9 To 16 '配置表中用户列
                        If Cells(1, a) = Sheets("PZ").Cells(1, b) Then
                            Cells(i, a) = Sheets("PZ").Cells(j, b)
                            Sheets("PZ").Cells(j, 4) = ""
                        End If
                    Next
                Next
            End If
        Next
    Next
End Sub
