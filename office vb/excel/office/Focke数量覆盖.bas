Attribute VB_Name = "模块111"
Sub Focke数量覆盖()
    For i = 2 To 99  '原版BOM中的行数
        For j = 2 To 99 '发图清单中的行数
            If Cells(i, 4) = Sheets("1").Cells(j, 1) Then
            '原版BOM的“material number”单元格数据与发图清单（表“1”）的“子项代码”单元格数据相等

                Sheets("1").Cells(j, 14) = Cells(i, 5)
                '数量覆盖
                
                Cells(i, 6) = "Y"
                '数量覆盖完成
                
            End If
        Next
    Next
End Sub
