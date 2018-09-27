Attribute VB_Name = "模块1"
Sub 数据匹配()
    For i = 2 To 17609     'BOM行数
        For j = 2 To 5830      '需配表格行数
            If Cells(i, 4) = Sheets("sheet1").Cells(j, 1) And Sheets("sheet1").Cells(j, 3) = "" Then
                Cells(i, 32) = Sheets("sheet1").Cells(j, 2)
                Sheets("sheet1").Cells(j, 3) = "Y"
            End If
        Next
    Next
End Sub
