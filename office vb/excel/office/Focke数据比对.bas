Attribute VB_Name = "模块1"
Sub 数据比对()
    a = 7591   '新表总行数
    b = 6657   '旧表总行数
    For i = 2 To a
        For j = 2 To b
            If Cells(i, 4) = Sheets("0115").Cells(j, 4) Then '新表“编码”与旧表0115的相同
                If Cells(i, 7) = Sheets("0115").Cells(j, 7) Then '新表“所属编码”与旧表0115的相同
                    If Cells(i, 21) = Sheets("0115").Cells(j, 21) Then '新表“数量”与旧表0115的相同
                        Cells(i, 34) = "相同"
                        Sheets("0115").Cells(j, 34) = "相同"
                        Cells(i, 35) = Sheets("0115").Cells(j, 1)
                        Sheets("0115").Cells(j, 35) = Cells(i, 1)
                    Else
                        Cells(i, 37) = "数量更改"
                        Cells(i, 38) = Sheets("0115").Cells(j, 21)
                        Cells(i, 35) = Sheets("0115").Cells(j, 1)
                        Sheets("0115").Cells(j, 37) = "数量更改"
                        Sheets("0115").Cells(j, 38) = Cells(i, 21)
                        Sheets("0115").Cells(j, 35) = Cells(i, 1)
                    End If
                    If Cells(i, 11) = Sheets("0115").Cells(j, 11) Then '新表“版本”与旧表0115的相同
                        Cells(i, 34) = "相同"
                        Sheets("0115").Cells(j, 34) = "相同"
                        Cells(i, 35) = Sheets("0115").Cells(j, 1)
                        Sheets("0115").Cells(j, 35) = Cells(i, 1)
                    Else
                        Cells(i, 36) = "版本更改"
                        Sheets("0115").Cells(j, 36) = "版本更改"
                        Cells(i, 35) = Sheets("0115").Cells(j, 1)
                        Sheets("0115").Cells(j, 35) = Cells(i, 1)
                    End If
                Else
                    Cells(i, 39) = "新增"
                    Sheets("0115").Cells(j, 39) = "去除"
                End If
            Else
                Cells(i, 39) = "新增"
                Sheets("0115").Cells(j, 39) = "去除"
                
            End If
        Next
    Next
End Sub

