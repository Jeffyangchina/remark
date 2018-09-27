VERSION 5.00
Object = "{92096210-97DF-11CF-9F27-02608C4BF3B5}#1.0#0"; "oradc.ocx"
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   4965
   ClientLeft      =   60
   ClientTop       =   450
   ClientWidth     =   7500
   LinkTopic       =   "Form1"
   ScaleHeight     =   4965
   ScaleWidth      =   7500
   StartUpPosition =   3  '´°¿ÚÈ±Ê¡
   Begin ORADCLibCtl.ORADC ORADC1 
      Height          =   1455
      Left            =   2160
      Top             =   1800
      Width           =   3255
      _Version        =   65536
      _ExtentX        =   5741
      _ExtentY        =   2566
      _StockProps     =   207
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "ËÎÌå"
         Size            =   9
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      DatabaseName    =   "orcl"
      Connect         =   "system/sysman"
      RecordSource    =   ""
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub form_load()
With ORADC1
.Connect = "system/sysman"
.DatabaseName = "orcl"
.Recordset = "select * from MICRO3_RT_SYNOPTICS"
.Refresh
End With
End Sub

