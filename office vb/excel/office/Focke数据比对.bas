Attribute VB_Name = "ģ��1"
Sub ���ݱȶ�()
    a = 7591   '�±�������
    b = 6657   '�ɱ�������
    For i = 2 To a
        For j = 2 To b
            If Cells(i, 4) = Sheets("0115").Cells(j, 4) Then '�±����롱��ɱ�0115����ͬ
                If Cells(i, 7) = Sheets("0115").Cells(j, 7) Then '�±��������롱��ɱ�0115����ͬ
                    If Cells(i, 21) = Sheets("0115").Cells(j, 21) Then '�±���������ɱ�0115����ͬ
                        Cells(i, 34) = "��ͬ"
                        Sheets("0115").Cells(j, 34) = "��ͬ"
                        Cells(i, 35) = Sheets("0115").Cells(j, 1)
                        Sheets("0115").Cells(j, 35) = Cells(i, 1)
                    Else
                        Cells(i, 37) = "��������"
                        Cells(i, 38) = Sheets("0115").Cells(j, 21)
                        Cells(i, 35) = Sheets("0115").Cells(j, 1)
                        Sheets("0115").Cells(j, 37) = "��������"
                        Sheets("0115").Cells(j, 38) = Cells(i, 21)
                        Sheets("0115").Cells(j, 35) = Cells(i, 1)
                    End If
                    If Cells(i, 11) = Sheets("0115").Cells(j, 11) Then '�±��汾����ɱ�0115����ͬ
                        Cells(i, 34) = "��ͬ"
                        Sheets("0115").Cells(j, 34) = "��ͬ"
                        Cells(i, 35) = Sheets("0115").Cells(j, 1)
                        Sheets("0115").Cells(j, 35) = Cells(i, 1)
                    Else
                        Cells(i, 36) = "�汾����"
                        Sheets("0115").Cells(j, 36) = "�汾����"
                        Cells(i, 35) = Sheets("0115").Cells(j, 1)
                        Sheets("0115").Cells(j, 35) = Cells(i, 1)
                    End If
                Else
                    Cells(i, 39) = "����"
                    Sheets("0115").Cells(j, 39) = "ȥ��"
                End If
            Else
                Cells(i, 39) = "����"
                Sheets("0115").Cells(j, 39) = "ȥ��"
                
            End If
        Next
    Next
End Sub

