Attribute VB_Name = "模块1"
Sub 补全信息BOM()
    istart = 686
    
    iend = 1870
    a = 2
    For i = istart To iend
        For j = a To 32281
            If Cells(i, 4) = Sheets("cd_item").Cells(j, 1) Then
                a = j
                Cells(i, 9) = "Y"
                If Cells(i, 7) = "" Then
                    Cells(i, 7) = Sheets("cd_item").Cells(j, 7) '单位
                End If
                Cells(i, 12) = Sheets("cd_item").Cells(j, 2) '名称
                Cells(i, 13) = Sheets("cd_item").Cells(j, 4) '规格
                Cells(i, 14) = Sheets("cd_item").Cells(j, 3) '型号
                Cells(i, 15) = Sheets("cd_item").Cells(j, 8) '标准号
                Cells(i, 16) = Sheets("cd_item").Cells(j, 14) '描述
                Cells(i, 19) = Sheets("cd_item").Cells(j, 21) '材料
                If Cells(i, 20) = "" Then
                    Cells(i, 20) = Sheets("cd_item").Cells(j, 16) '来源
                End If
                If Cells(i, 21) = "" Then
                    Cells(i, 21) = Sheets("cd_item").Cells(j, 9) '外来代码1
                End If
                'Cells(i, 21) = Sheets("cd_item").Cells(j, 10) '外来代码2
                Cells(i, 22) = Sheets("cd_item").Cells(j, 6) '制造商
                Cells(i, 23) = Sheets("cd_item").Cells(j, 11) '订货号
                Cells(i, 25) = Sheets("cd_item").Cells(j, 12) '供应商
                Exit For
            End If
        Next
    Next
End Sub
