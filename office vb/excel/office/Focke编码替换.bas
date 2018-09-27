Attribute VB_Name = "模块11"
Sub Focke编码替换()
    For i = 2 To 17637  '原版BOM中的行数
        For j = 2 To 99 '发图清单中的行数
            If Cells(i, 4) = Sheets("1").Cells(j, 13) Then
            '原版BOM的“material number”单元格数据与发图清单（表“1”）的“外来代码”单元格数据相等
            
                Cells(i, 4) = Sheets("1").Cells(j, 1)
                '“material number”单元格数据“替换为”“子项代码”单元格数据
                
                Sheets("1").Cells(j, 14) = Cells(i, 1)
                '原版BOM的“sequence number”数据写入发图清单（表“1”），表示“子项代码”覆盖“material number”
            End If
        Next
    Next
End Sub
