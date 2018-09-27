Attribute VB_Name = "模块1"
Sub 修正设备无编码()
Attribute 修正设备无编码.VB_Description = "zch4537 记录的宏 2006-4-11"
Attribute 修正设备无编码.VB_ProcData.VB_Invoke_Func = " \n14"
    For j = 1 To 60
        If Cells(1, j) = "设备" Then
            a = j
        End If
    Next
    For i = 2 To 60000
        If Cells(i, a) <> "" Then
            Select Case Cells(i, a)
                Case "钣金"
                    Cells(i, a) = "钣金(EE30)"
                Case "锻工"
                    Cells(i, a) = "锻造(EB00)"
                Case "焊工"
                    Cells(i, a) = "焊工(EF00)"
                Case "金钳"
                    Cells(i, a) = "金钳(EX22)"
                Case "平板"
                    Cells(i, a) = "平板(EX10)"
                Case "钳工"
                    Cells(i, a) = "钳工(EX21)"
                Case "热工"
                    Cells(i, a) = "热工(ED00)"
                Case "委外"
                    Cells(i, a) = "委外(E000)"
                Case "立铣"
                    Cells(i, a) = "立铣(E261)"
                Case "万铣"
                    Cells(i, a) = "万铣(E211)"
                Case "无心磨"
                    Cells(i, a) = "M1020A(E481)"
            End Select
        End If
    Next
End Sub
