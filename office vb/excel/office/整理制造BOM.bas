Attribute VB_Name = "模块1"
Sub 整理制造BOM()
    For j = 1 To 65000
        If Cells(j, 1) = "" And Cells(j + 1, 1) = "" And Cells(j + 2, 1) = "" Then
            ro = j - 1
            Exit For
        End If
    Next
    For i = 1 To 60
        If Cells(1, i) = "" And Cells(1, i + 1) = "" Then
            co = i - 1
            Exit For
        End If
    Next
    For i = 1 To co
        If Cells(1, i) = "操作说明" Then
            Cells(1, i) = "工艺内容"
        Else
            If Cells(1, i) = "FORGING_PIECE" Then
                Cells(1, i) = "毛坯可制锻件数"
            Else
                If Cells(1, i) = "ROUGH_LONG" Then
                    Cells(1, i) = "毛坯长度"
                Else
                    If Cells(1, i) = "特征码" Then
                        Cells(1, i) = "特征描述"
                    Else
                        If Cells(1, i) = "国外编码" Then
                            Cells(1, i) = "外来编码"
                        Else
                            If Cells(1, i) = "产品型号" Then
                                Cells(1, i) = "毛坯编码"
                            Else
                                If Cells(1, i) = "产品名称" Then
                                    Cells(1, i) = "毛坯名称"
                                End If
                            End If
                        End If
                    End If
                End If
            End If
        End If
    Next
    For j = 2 To ro
        For i = 2 To co
            If Cells(1, i) = Cells(1, i - 1) And Cells(j, i) = "" And Cells(j, i - 1) <> "" Then
                Cells(j, i) = Cells(j, i - 1)
                Cells(j, i - 1) = ""
            End If
        Next
    Next
    Columns("T:T").Select
    Selection.Delete Shift:=xlToLeft
    Columns("U:U").Select
    Selection.Delete Shift:=xlToLeft
    Columns("V:AA").Select
    Selection.Delete Shift:=xlToLeft
    Columns("W:AB").Select
    Selection.Delete Shift:=xlToLeft
    Columns("X:Y").Select
    Selection.Delete Shift:=xlToLeft
    Columns("AE:AH").Select
    Selection.Delete Shift:=xlToLeft
End Sub

