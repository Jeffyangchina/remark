Attribute VB_Name = "Module11"
Sub bplot()

Dim sstext As AcadSelectionSet
Dim filtert(0) As Integer
Dim b As Integer
Dim c As Integer
Dim filterd(0) As Variant

Dim objDoc As AutoCAD.AcadDocument
 
Dim pdfpth As String
Dim pos As Integer
Dim h As String
Dim nh As String
Dim x As AcadHyperlinks
Dim xh As AcadHyperlink
Dim hs As String
Dim a As Integer

Dim exl As Excel.Application
Dim wb As Excel.Workbook
Dim sht As Excel.Worksheet
Dim i As Integer
Dim pickobj As AcadEntity


Set exl = CreateObject("Excel.Application") '定义excel
Set wb = exl.Workbooks.Open("E:\BITMAP\" & "bit.xls")
Set sht = wb.Worksheets("sheet1")

MyPath = "E:\BITMAP\"
MyFile = Dir(MyPath & "*.dwg")


Do While MyFile <> ""

Set objDoc = Documents.Open(MyPath & MyFile)
Set sstext = objDoc.SelectionSets.Add("ss")
filtert(0) = 0
filterd(0) = "TEXT"
sstext.Select acSelectionSetAll, , , filtert, filterd
For Each pickobj In sstext
 If pickobj.ObjectName = "AcDbText" Then
  hs = pickobj.TextString
  If hs <> "" Then
  
  a = Asc(Mid(hs, 1, 1))
  End If
  If a < 55 And a > 47 Then
   For i = 1 To 443
    h = exl.Cells(i, 1)
    b = InStr(hs, h)
     If b = 1 And h <> "" Then
       pickobj.Color = acGreen
       c = c + 1
      nh = ".\" & h & ".dwg"
      Set xh = pickobj.Hyperlinks.Add("c")  '超级链接
      
      
      xh.URL = nh '"e:\BITMAP\" & h & ".dwg"
       'xh.URLNamedLocation = h
     
      
       
       Exit For
     End If
     Next i
 End If
 End If
 
  Next pickobj

On Error Resume Next
objDoc.Save

objDoc.Close
MyFile = Dir
Loop

wb.Close
End Sub


