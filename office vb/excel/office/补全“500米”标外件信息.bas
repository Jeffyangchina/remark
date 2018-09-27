Attribute VB_Name = "模块1"
Sub 补全"500米"标外件信息()
    For i = 2 To 753
        For j = 2 To 20000
            If Sheets("sheet1").Cells(i, 4) = Sheets("cd_item").Cells(j, 1) Then
                Sheets("sheet1").Cells(i, 8) = Sheets("cd_item").Cells(j, 2)            '名称
                Sheets("sheet1").Cells(i, 10) = Sheets("cd_item").Cells(j, 3)           '型号
                Sheets("sheet1").Cells(i, 9) = Sheets("cd_item").Cells(j, 4)            '规格
                Sheets("sheet1").Cells(i, 17) = Sheets("cd_item").Cells(j, 6)           '制造商
                'Sheets("sheet1").Cells(i, 5) = Sheets("cd_item").Cells(j, 7)           '单位
                Sheets("sheet1").Cells(i, 11) = Sheets("cd_item").Cells(j, 8)           '标准号
                Sheets("sheet1").Cells(i, 20) = Sheets("cd_item").Cells(j, 9)           '外来代码1
                Sheets("sheet1").Cells(i, 21) = Sheets("cd_item").Cells(j, 10)          '外来代码1
                Sheets("sheet1").Cells(i, 18) = Sheets("cd_item").Cells(j, 11)          '订货号
                Sheets("sheet1").Cells(i, 22) = Sheets("cd_item").Cells(j, 12)          '供应商
                Sheets("sheet1").Cells(i, 12) = Sheets("cd_item").Cells(j, 14)          '描述
                Sheets("sheet1").Cells(i, 16) = Sheets("cd_item").Cells(j, 16)          '来源
                Sheets("sheet1").Cells(i, 15) = Sheets("cd_item").Cells(j, 21)          '材料
            End If
        Next
    Next
End Sub
