Attribute VB_Name = "模块11"
Sub 签名()
    y = 129         '总页码
    b = 26          '两页间相隔行数
    qs = 24         '第一页签名行数
    bz = 19         '编制列数
    sh = 23         '审核列数
    For i = 2 To y
        Cells(b * (i - 1) + qs, 19) = Cells(qs, 19)
        Cells(b * (i - 1) + qs, 23) = Cells(qs, 23)
    Next
End Sub
