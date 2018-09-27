Attribute VB_Name = "模块1"
Sub 部件配置汇总()
    For i = 2 To 24846    'BOM行数
        For j = 2 To 1610  '配置行数
            If Cells(i, 31) = Sheets("PZ").Cells(j, 2) Then
                For a = 32 To 39   '汇总表中用户列
                    If Cells(1, a) = Sheets("PZ").Cells(j, 10) Then
                        Cells(i, a) = Sheets("PZ").Cells(j, 5)
                        Sheets("PZ").Cells(j, 6) = "GP"
                    End If
                Next
            End If
        Next
    Next
End Sub
