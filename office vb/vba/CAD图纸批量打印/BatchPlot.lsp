;;;--------------------------------------------------------------------------
;;;   Batchplot.LSP
;;;    版权(C) 1999-2003  邱枫
;;;
;;; 模型空间的批量打印程序 第二版
;;; 秋枫, 2003年11月1日
;;; 最新更新：2005年4月8日10时2分
;;;
;;;   本程序免费可供进行任何用途需求的拷贝、修改及发行, 但请遵循下述原则:
;;;
;;;   1)  上列的版权通告必须出现在每一份拷贝里.
;;;   2)  相关的说明文档也必须载有版权通告及本项许可通告.
;;;
;;;   本程序仅提供作为应用上的参考, 而未声明或隐含任何保证; 对于任何特殊
;;;   用途之适应性, 以及商业销售所隐含作出的保证, 在此一概予以否认.
;;;
;;; ========================================================================
;;; 更新历史：
;;;
;;; 修正调试程序时的一个疏忽，把有用的代码注释掉了导致不能选取图块（7月22日）2.9.1
;;; 支持除理正图框层外的其它图层上的图框（封闭矩形PLINE）6月29日
;;; 支持反向打印（图纸旋转180度）6月29日
;;; 理正图框支持“*_TITLE”6月29日
;;; 添加支持“理正电气(ELE_TITLE)”图层的图框。4月8日
;;; 修正“在布局空间中强制使用模型空间线型比例”选项不起作用的问题(笔误)4月8日
;;; 因DCS与UCS不一致而产生的Bug，Target系统变量（2005.2.24）
;;; 在状态栏显示比例与进度信息(7月5日)
;;; BUGFIX: 图块列表(7月5日)
;;; 提供打印多个Layout的功能（7月1日） 
;;; 打印不出图框边线问题（6月30日）
;;; 在DWG文件中保存上次的批量打印设置（6月28日） 
;;; 增加打印顺序调整功能（6月25日） 
;;; 自动打印比例算法调整（6月25日） 
;;; 支持在UCS下的图块图框（6月25日） 
;;; 自动旋转设为可选。如选成不自动，可以在页面设置中调整方向（6月25日） 
;;; 支持在UCS下的理正图框（6月24日） 
;;; 2.2版。增加图纸偏移与居中选项（6月9日） 
;;; 增加了一个打印份数的选项。 
;;; 加入打印机驱动或打印机不存在时的出错处理。 
;;; 第二版全面改写，新增对话框。 
;;; 加入对理正图框的支持。 
;;; 第一版。 

(defun BATCHPLOT (/		    rcode	      dcl_id
		  clayout	    DCLValues	      BlockList LayerList
		  key		    plot	      acaddoc
		  ;; Local Functions
		  ax:ListLayouts    qf_getFolder      AddBS
		  BrowseplotfileClick		      default_dclvalues
		  SetValue	    GetValue	      GetBlockList GetLayerList
		  disableCtrls	    EnableCtrls	      SetCtrlStatus
		  ShowMainDlg	    SSMAP	      ss->elist
		  ax:GetBoundingBox ax:2DPoint	      getwidth
		  islandscape	    CopyLayout	      GetNewAutoNumName
		  doBatchLayout	    doBatchPlot	      SelectBlock SelectLayer
		  GetFrames	    HighLightShow
		  allPageSetupsOfModelType	      getPageSetupName
		  RefreshPlotSettings		      catch
		  InViewP	    fixscale	      expandbounding
		  doPlotLayoutsInTabOrder
		  PlotLayoutsInTabOrder
		 )
  (defun allPageSetupsOfModelType (doc / aps pc)
    (vlax-for pc (vla-get-plotconfigurations doc)
      (if (= (vla-get-ModelType pc) :vlax-true)
	(setq aps (cons (vla-get-name pc) aps))
      )
    )
    (vl-sort aps '<)
  )
  ;; the following 3 functions from internet
  (defun getPageSetupName (layout / laydict psn dn)
    (setq dn (cdr (assoc -1 (dictsearch (namedobjdict) "ACAD_LAYOUT"))))
    (setq laydict (dictsearch dn layout))
    (setq psn (member '(100 . "AcDbPlotSettings") laydict))
    (if	(= (caadr psn) 1)		; Page Setup Name exist
      (setq psn (cdadr psn))
    )
  )
  (defun setPageSetupName
	 (doc layout newpsn / pc layoutitem exist1 exist2)
    (vlax-for layoutitem (vla-get-Layouts doc)
      (if (= (strcase (vla-get-name layoutitem)) (strcase layout))
	(setq exist1 T)
      )
    )
    (if	exist1				; layout exist
      (vlax-for	pc (vla-get-plotconfigurations doc)
	(if (and (= (strcase (vla-get-name pc)) (strcase newpsn))
		 (if (= (strcase layout) "MODEL")
		   (= (vla-get-ModelType pc) :vlax-true)
		   (= (vla-get-ModelType pc) :vlax-false)
		 )
	    )
	  (setq exist2 T)
	)
      )
    )
    (if	exist2				; page setup name exist for selected model type
      (vla-copyfrom
	(vla-item (vla-get-layouts doc) layout)
	(vla-item (vla-get-plotconfigurations doc) newpsn)
      )
    )
  )
  (defun ax:ListLayouts	(/ layouts c lst lay)
    (vl-load-com)
    (setq layouts (vla-get-layouts
		    (vla-get-activedocument (vlax-get-acad-object))
		  )
	  c	  -1
    )
    (repeat (vla-get-count layouts)
      (setq lst (cons (setq c (1+ c)) lst))
    )
    (vlax-for lay layouts
      (setq lst (subst (vla-get-name lay) (vla-get-taborder lay) lst))
    )
    (reverse lst)
  )
  (defun qf_getFolder (msg / WinShell shFolder path catchit)
    (vl-load-com)
    (setq winshell (vlax-create-object "Shell.Application"))
    (setq
      shFolder (vlax-invoke-method WinShell 'BrowseForFolder 0 msg 1)
    )
    (setq
      catchit (vl-catch-all-apply
		'(lambda ()
		   (setq shFolder (vlax-get-property shFolder 'self))
		   (setq path (vlax-get-property shFolder 'path))
		 )
	      )
    )
    (if	(vl-catch-all-error-p catchit)
      nil
      path
    )
  )
  (defun AddBS (cPath)
    (if	(not (= (substr cPath (strlen cPath)) "\\"))
      (strcat cPath "\\")
      cPath
    )
  )
  (defun BrowseplotfileClick (/ folder)
    (setq folder (qf_GetFolder "选择PLT文件保存位置"))
    (setq folder (AddBS folder))
    (if	folder
      (progn (set_tile "PlotFileFolderEdit" folder)
	     (setvalue 'PlotFileFolder folder)
      )
    )
  )
  ;;有名图块列表
  (defun GetBlockList (/ blist b)
    (setq blist nil)
    (if	(tblnext "BLOCK" T)
      (progn (setq blist (cons (cdr (assoc 2 (tblnext "BLOCK" T))) blist))
	     (while (setq b (tblNext "BLOCK"))
	       (setq blist (cons (cdr (assoc 2 b)) blist))
	     )
      )
    )
    (vl-remove-if '(lambda (s) (= "*" (substr s 1 1))) blist)
  )
  (defun GetLayerList (/ llist l)
    (setq llist nil)
    (if	(tblnext "LAYER" T)
      (progn (setq llist (cons (cdr (assoc 2 (tblnext "LAYER" T))) llist))
	     (while (setq l (tblNext "LAYER"))
	       (setq llist (cons (cdr (assoc 2 l)) llist))
	     )
      )
    )
    (vl-sort llist '<)
  )
  ;;设置保存值
  (defun SetValue (key value)
    (if	(assoc key DCLValues)
      (setq DCLValues (subst (cons key value)
			     (assoc key DCLValues)
			     DCLValues
		      )
      )
      (setq DCLValues (cons (cons key value) DCLValues))
    )
  )
  ;;读取保存值
  (defun GetValue (key / r)
    (if	(assoc key DCLValues)
      (cdr (assoc key DCLValues))
      (cdr (assoc key default_dclvalues))
    )
  )
  ;;灰显控件
  (defun disableCtrls (keylist / key)
    (foreach key keylist (mode_tile key 1))
  )
  ;;激活控件
  (defun EnableCtrls (keylist / key)
    (foreach key keylist (mode_tile key 0))
  )
  ;;设置控件状态
  (defun SetCtrlStatus ()
    (EnableCtrls
      '("LzFrameRadio"		"BlockRadio" "LayerRadio"
	"BlockAndLayerSettings"	"PickBtn"
	"BlockNameEdit"	"LayerNameEdit"	"PlotRadio"
	"LayoutRadio"		"PlotFileRadio"
	"PlotLayoutRadio"	"SelectFramesBtn"
	"ShowFramesBtn"		"PageSetupSettings"
	"PageSetupBtn"		"PlotterLabel"
	"PaperLabel"		"PlotStyleLabel"
	"ScaleSettings"		"AutoScaleRadio"
	"ScaleToFitRadio"	"FixScaleRadio"
	"FixScaleEdit"		"PlotFileSettings"
	"PlotFilePrefixEdit"	"DeletePlotFileCheck"
	"PlotFileFolderEdit"	"BrowsePLTFolderBtn"
	"LayoutSettings"	"LayoutPrefixEdit"
	"DeleteLayoutCheck"	"LtScaleCheck"
	"PreviewBtn"		"OKBtn"
	"CancelBtn"		"HelpBtn"
	"PageSetupPopup"	"CopiesEdit"
	"LocationSettings"	"AutoCenterRadio"
	"OffsetRadio"		"XOffsetEdit"
	"YOffsetEdit"		"AutoRotateCheck" "UpsideDownCheck"
	"PlotOrderSettings"	"SelectOrderRadio"
	"LeftToRightRadio"	"TopToBottomRadio"
	"ReverseOrderCheck"
       )
    )
    (if	(= "0" (get_tile "BlockRadio"))
      (disableCtrls
	'("BlockNameEdit")
      )
    )
    (if	(= "0" (get_tile "LayerRadio"))
      (disableCtrls
	'("LayerNameEdit")
      )
    )
    (if (= "1" (get_tile "LzFrameRadio"))
      (disableCtrls '("PickBtn"))
    )    
    (if	(= "0" (get_tile "FixScaleRadio"))
      (disableCtrls '("FixScaleEdit"))
    )
    (if	(= "0" (get_tile "OffsetRadio"))
      (disableCtrls '("XOffsetEdit" "YOffsetEdit"))
    )
    (if	(= "0" (get_tile "LayoutRadio"))
      (disableCtrls
	'("LayoutSettings"	  "LayoutPrefixEdit"
	  "DeleteLayoutCheck"	  "LtScaleCheck"
	  "CopiesEdit"
	 )
      )
    )
    (if	(= "1" (get_tile "LayoutRadio"))
      (disableCtrls
	'("AutoCenterRadio"
	  "OffsetRadio"
	  "XOffsetEdit"
	  "YOffsetEdit"
	 )
      )
    )
    (if	(= "0" (get_tile "PlotFileRadio"))
      (disableCtrls
	'("PlotFileSettings"	      "PlotFilePrefixEdit"
	  "DeletePlotFileCheck"	      "PlotFileFolderEdit"
	  "BrowsePLTFolderBtn"	      "CopiesEdit"
	 )
      )
    )
    (if	(= "1" (get_tile "PlotRadio"))
      (enableCtrls '("CopiesEdit"))
    )
    (if	(null (getvalue 'SelectedFrames))
      (disableCtrls '("PreviewBtn" "OKBtn" "ShowFramesBtn"))
    )
    (if	(= "1" (get_tile "PlotLayoutRadio"))
      (progn
	(disableCtrls
	  '("LzFrameRadio"	     "BlockRadio" "LayerRadio"
	    "BlockAndLayerSettings"    "PickBtn"
	    "BlockNameEdit"  "LayerRadio"	     "SelectFramesBtn"
	    "ShowFramesBtn"	     "PageSetupSettings"
	    "PageSetupBtn"	     "PlotterLabel"
	    "PaperLabel"	     "PlotStyleLabel"
	    "ScaleSettings"	     "AutoScaleRadio"
	    "ScaleToFitRadio"	     "FixScaleRadio"
	    "FixScaleEdit"	     "PlotFileSettings"
	    "PlotFilePrefixEdit"     "DeletePlotFileCheck"
	    "PlotFileFolderEdit"     "BrowsePLTFolderBtn"
	    "LayoutSettings"	     "LayoutPrefixEdit"
	    "DeleteLayoutCheck"	     "LtScaleCheck"
	    "PreviewBtn"	     "PageSetupPopup"
	    "CopiesEdit"	     "LocationSettings"
	    "AutoCenterRadio"	     "OffsetRadio"
	    "XOffsetEdit"	     "YOffsetEdit"
	    "AutoRotateCheck"	     "UpsideDownCheck" "PlotOrderSettings"
	    "SelectOrderRadio"	     "LeftToRightRadio"
	    "TopToBottomRadio"	     "ReverseOrderCheck"
	   )
	)
	(enableCtrls '("OKBtn"))
      )
    )
  )
  (defun RefreshPlotSettings ()
    ;; refresh
    (vla-RefreshPlotDeviceInfo clayout)
    (set_tile "PlotterLabel"
	      (strcat "打印设备：" (vla-get-configname clayout))
    )
    (set_tile "PaperLabel"
	      (strcat "纸张设定："
		      (vla-GetLocaleMediaName
			clayout
			(vla-get-CanonicalMediaName clayout)
		      )
	      )
    )
    (set_tile "PlotStyleLabel"
	      (strcat "打印样式：" (vla-get-stylesheet clayout))
    )
  )
  ;;显示主对话框
  (defun ShowMainDlg
	 (/ blockname Layername pagesetups pagesetupname SetDlgValues)
    (defun SetCurrentPageSetup (Index / Name)
      (if (setq Name (nth Index PageSetups))
	(SetPageSetupName acaddoc "Model" Name)
      )
    )
    (defun SetDlgValues	()
      (if blocklist
	(progn (start_list "BlockNameEdit")
	       (foreach blockname blocklist (Add_list blockname))
	       (end_list)
	)
      )
      (if (and (getvalue 'Blockname)
	       (vl-position (getvalue 'Blockname) Blocklist)
	  )
	(set_tile "BlockNameEdit"
		  (itoa (vl-position (getvalue 'Blockname) Blocklist))
	)
      )
      (if Layerlist
	(progn (start_list "LayerNameEdit")
	       (foreach Layername Layerlist (Add_list Layername))
	       (end_list)
	)
      )
      (if (and (getvalue 'Layername)
	       (vl-position (getvalue 'Layername) Layerlist)
	  )
	(set_tile "LayerNameEdit"
		  (itoa (vl-position (getvalue 'Layername) Layerlist))
	)
      )
      ;; add page setups
      (setq pagesetups (allPageSetupsOfModelType acaddoc))
      (start_list "PageSetupPopup")
      (mapcar 'Add_list pagesetups)
      (Add_list "")
      (end_list)
      (if (and (setq PageSetupName (getPageSetupName (getvar "ctab")))
	       (member pagesetupName pagesetups)
	  )
	(set_tile "PageSetupPopup"
		  (itoa (vl-position PageSetupName pagesetups))
	)
	(set_tile "PageSetupPopup" (itoa (length pagesetups)))
      )
      ;;
      (RefreshPlotSettings)
      (set_tile "CopiesEdit" (getvalue 'Copies))
      (set_tile (getvalue 'Frame) "1")
      (set_tile (getvalue 'Output) "1")
      (if (= (getvalue 'PlotScale) "Auto")
	(set_tile "AutoScaleRadio" "1")
	(if (= (getvalue 'PlotScale) "ScaleToFit")
	  (set_tile "ScaleToFitRadio" "1")
	  (progn (set_tile "FixScaleRadio" "1")
		 (set_tile "FixScaleEdit" (rtos (getvalue 'PlotScale)))
	  )
	)
      )
      (if (= (getvalue 'Offset) "Center")
	(set_tile "AutoCenterRadio" "1")
	(progn (set_tile "OffsetRadio" "1")
	       (set_tile "XOffsetEdit" (rtos (car (getvalue 'Offset))))
	       (set_tile "YOffsetEdit" (rtos (cadr (getvalue 'Offset))))
	)
      )
      (set_tile "AutoRotateCheck" (getvalue 'AutoRotate))
      (set_tile "UpsideDownCheck" (getvalue 'UpsideDown))
      (set_tile (getvalue 'PlotOrder) "1")
      (set_tile "ReverseOrderCheck" (getvalue 'ReverseOrder))
      (set_tile	"StatusLabel"
		(strcat	"选中图纸:"
			(itoa (length (getvalue 'SelectedFrames)))
		)
      )
      (set_tile "PlotFilePrefixEdit" (getvalue 'PlotFilePrefix))
      (set_tile "PlotFileFolderEdit" (getvalue 'PlotFileFolder))
      (set_tile "LayoutPrefixEdit" (getvalue 'LayoutPrefix))
      (set_tile "DeletePlotFileCheck" (getvalue 'DeletePlotFile))
      (set_tile "DeleteLayoutCheck" (getvalue 'DeleteLayout))
      (set_tile "LtScaleCheck" (getvalue 'MSLineScale))
      ;; callbacks:
      ;; buttons
      (action_tile "PageSetupBtn" "(done_dialog 10)")
      (action_tile "PickBtn" "(done_dialog 11)")
      (action_tile "SelectFramesBtn" "(done_dialog 12)")
      (action_tile "PreviewBtn" "(done_dialog 13)")
      (action_tile "BrowsePLTFolderBtn" "(BrowseplotfileClick)")
      (action_tile "ShowFramesBtn" "(done_dialog 14)")
      (action_tile "HelpBtn" "(batchplot_help)")
      ;; radio
      (foreach key '("BlockRadio" "LzFrameRadio" "LayerRadio")
	(action_tile key "(SetCtrlStatus) (setvalue 'Frame $key)")
      )
      (foreach key '("PlotRadio"
		     "LayoutRadio"
		     "PlotFileRadio"
		     "PlotLayoutRadio"
		    )
	(action_tile key "(SetCtrlStatus) (setvalue 'Output $key)")
      )
      (action_tile "CopiesEdit" "(setvalue 'Copies $value)")
      (action_tile
	"AutoScaleRadio"
	"(SetCtrlStatus)(setvalue 'PlotScale \"Auto\")"
      )
      (action_tile
	"ScaleToFitRadio"
	"(SetCtrlStatus)(setvalue 'PlotScale \"ScaleToFit\")"
      )
      (action_tile
	"FixScaleRadio"
	"(SetCtrlStatus)(setvalue 'PlotScale (read (get_tile \"FixScaleEdit\")))(mode_tile \"FixScaleEdit\" 2)"
      )
      (action_tile
	"FixScaleEdit"
	"(set_tile \"FixScaleRadio\" \"1\")(setvalue 'PlotScale (read $value))"
      )
      (action_tile
	"AutoCenterRadio"
	"(SetCtrlStatus)(setvalue 'Offset \"Center\")"
      )
      (action_tile
	"OffsetRadio"
	"(SetCtrlStatus)(setvalue 'Offset (list (read (get_tile \"XOffsetEdit\"))(read (get_tile \"YOffsetEdit\"))))(mode_tile \"XOffsetEdit\" 2)"
      )
      (action_tile
	"XOffsetEdit"
	"(set_tile \"OffsetRadio\" \"1\")(setvalue 'Offset (list (read $value)(read (get_tile \"YOffsetEdit\"))))"
      )
      (action_tile
	"YOffsetEdit"
	"(set_tile \"OffsetRadio\" \"1\")(setvalue 'Offset (list (read (get_tile \"XOffsetEdit\"))(read $value)))"
      )
      ;;order
      (foreach key '("SelectOrderRadio"
		     "LeftToRightRadio"
		     "TopToBottomRadio"
		    )
	(action_tile key "(setvalue 'PlotOrder $key)")
      )
      (action_tile
	"ReverseOrderCheck"
	"(setvalue 'ReverseOrder $value)"
      )
      (action_tile
	"AutoRotateCheck"
	"(setvalue 'AutoRotate $value)"
      )
      (action_tile
	"UpsideDownCheck"
	"(setvalue 'UpsideDown $value)"
      )
      ;;checkbox
      (action_tile
	"DeletePlotFileCheck"
	"(setvalue 'DeletePlotFile $value)"
      )
      (action_tile
	"DeleteLayoutCheck"
	"(setvalue 'DeleteLayout $value)"
      )
      (action_tile
	"LtScaleCheck"
	"(setvalue 'MSLineScale $value)"
      )
      ;;editbox
      (action_tile
	"BlockNameEdit"
	"(setvalue 'BlockName (nth (read $value) blocklist))"
      )
      (action_tile
	"LayerNameEdit"
	"(setvalue 'LayerName (nth (read $value) Layerlist))"
      )
      (action_tile
	"PageSetupPopup"
	"(SetCurrentPageSetup (atoi $value))(RefreshPlotSettings)"
      )
      (action_tile
	"PlotFilePrefixEdit"
	"(setvalue 'PlotFilePrefix $value)"
      )
      (action_tile
	"PlotFileFolderEdit"
	"(setvalue 'PlotFileFolder $value)"
      )
      (action_tile
	"LayoutPrefixEdit"
	"(setvalue 'LayoutPrefix $value)"
      )
    )
    ;; main for show dialog
    (if	(null dcl_id)
      (setq dcl_id (load_dialog "BatchPlot"))
    )
    (if	(< dcl_id 0)
      (progn (alert "错误：无法加载对话框文件。") (exit))
    )
    (new_dialog "BatchPlotMain" dcl_id)
    ;; for debug
    ;;(setdlgvalues)
    ;;(setctrlstatus)
    (vl-catch-all-apply 'SetDlgValues nil)
    (vl-catch-all-apply 'SetCtrlStatus nil)
    (start_dialog)
  )
  ;;选择集遍历例程
  (defun SSMAP (func ss / n)
    (if	(eq 'PICKSET (type ss))
      (repeat (setq n (fix (sslength ss))) ; fixed
	(apply func (list (ssname ss (setq n (1- n)))))
      )
    )
  )
  ;;选择集→表
  (defun ss->elist (ss / elist)
    (ssmap '(lambda (e) (setq elist (cons e elist))) ss)
    elist
  )
  ;;物体包围盒
  (defun ax:GetBoundingBox (ent / ll ur)
    (vla-getboundingbox (vlax-ename->vla-object ent) 'll 'ur)
    (mapcar 'vlax-safearray->list (list ll ur))
  )
  ;;2维点列程
  (defun ax:2DPoint (pt)
    (vlax-make-variant
      (vlax-safearray-fill
	(vlax-make-safearray vlax-vbdouble '(0 . 1))
	(list (car pt) (cadr pt))
      )
    )
  )
  ;;
  ;; 取得图框的长边长度
  (defun getwidth (bounding / x1 y1 x2 y2)
    (setq x1 (caar bounding)
	  y1 (cadar bounding)
	  x2 (caadr bounding)
	  y2 (cadadr bounding)
    )
    (if	(< (abs (- x1 x2)) (abs (- y1 y2)))
      (abs (- y1 y2))
      (abs (- x1 x2))
    )
  )
  ;; 判断图框是否横向
  (defun islandscape (bounding / x1 y1 x2 y2)
    (setq x1 (caar bounding)
	  y1 (cadar bounding)
	  x2 (caadr bounding)
	  y2 (cadadr bounding)
    )
    (if	(< (abs (- x1 x2)) (abs (- y1 y2)))
      nil
      'T
    )
  )
  ;;自动比例
  (defun fixscale (n / i large small)
    (setq i 0)
    (setq large (> n 100))
    (setq small (< n 10))
    (while (or (> n 100) (< n 10))
      (if large
	(setq n (/ n 10.0))
	(setq n (* n 10.0))
      )
      (setq i (1+ i))
    )
    (setq n (fix (+ 0.5 n)))
    (repeat i
      (if large
	(setq n (* n 10.0))
	(setq n (/ n 10.0))
      )
    )
    n
  )
  ;;复制布局
  (defun CopyLayout (nLayoutName / clayoutName tmpName namelist)
    (setq clayoutName (getvar "ctab"))
    (setq tmpName (strcat "$_QF_TMP_LAYOUT_NAME_OF_" clayoutName))
    (setq namelist (ax:ListLayouts))
    (vl-cmdf "_.layout" "_copy" clayoutName tmpName)
    (vl-cmdf "_.layout" "_rename" clayoutName NLayoutName)
    (vl-cmdf "_.layout" "_rename" tmpName clayoutName)
    (princ)
  )
  ;; 得到自动编号名
  (defun GetNewAutoNumName (prefix FixNum NameList / i istr Name)
    (setq i 1)
    (setq istr (itoa i))
    (while (< (strlen istr) FixNum)
      (setq istr (strcat "0" istr))
    )
    (setq Name (strcat prefix istr))
    (while (member Name Namelist)
      (setq i (1+ i))
      (setq istr (itoa i))
      (while (< (strlen istr) FixNum)
	(setq istr (strcat "0" istr))
      )
      (setq Name (strcat prefix istr))
    )
    Name
  )
  ;; 批量生成布局
  (defun doBatchLayout (bdlist	     plotscale	  layoutprefix
			deletelayout ltscale	  autoRotate UpsideDown
			/	     landscapeList
			portraitList NoRotationList
			RotationList bd		  layouts
			layout	     ll		  ur
			MarginLL     MarginUR	  prdisplay
			crtvp	     showpg	  pwidth
			pHeight	     paperwidth	  item
		       )
    (setq prdisplay (vla-get-display
		      (vla-get-preferences (vlax-get-acad-object))
		    )
    )
    (setq layouts (vla-get-layouts acaddoc))
    (setq portraitList (vl-remove-if 'islandscape bdlist))
    (setq landscapelist (vl-remove-if-not 'islandscape bdlist))
    (vla-getpapersize clayout 'pWidth 'pHeight)
    ;; 取得当前纸张的长边长度
    (if	(< pwidth pheight)
      (setq paperWidth pHeight)
      (setq paperwidth pWidth)
    )
    ;; decide what to rotated
    (setq NoRotationList
	   (if (> pwidth pHeight)
	     landscapeList
	     portraitList
	   )
    )
    (setq RotationList
	   (if (> pwidth pHeight)
	     portraitList
	     landscapeList
	   )
    )

    (if	(null AutoRotate)
      (progn
	(setq NoRotationList bdlist)
	(setq RotationList nil)
      )
    )

    (setq crtvp	 (vla-get-LayoutCreateViewport prdisplay)
	  showpg (vla-get-LayoutShowPlotSetup prdisplay)
    )
    (vla-put-layoutcreateviewport prdisplay :vlax-false)
    (vla-put-layoutshowplotsetup prdisplay :vlax-false)
    ;; delete existing layout with same prefix
    (if	(= "1" deletelayout)
      (foreach item (ax:ListLayouts)
	(if (wcmatch item (strcat layoutprefix "*"))
	  ;;(vla-delete (vla-item layouts item))
	  (vl-cmdf "_.layout" "_delete" item)
	)
      )
    )
    ;; create 0 degree template
    (if	NoRotationList
      (progn
	(vla-put-layoutcreateviewport prdisplay :vlax-false)
	(vla-put-layoutshowplotsetup prdisplay :vlax-false)
	(vl-cmdf "_.Layout" "_New" "$temp_No_Rotation")
	(vl-cmdf "_.Layout" "_Set" "$temp_No_Rotation")
	(vla-put-layoutcreateviewport prdisplay crtvp)
	(vla-put-layoutshowplotsetup prdisplay showpg)
        ;(alert ltscale)
	(if (= "1" ltscale)
	  (setvar "psltscale" 0)
	)
	(setq layout (vla-item layouts "$temp_No_Rotation"))
	(vla-put-ConfigName
	  layout
	  (vla-get-ConfigName (vla-item layouts "Model"))
	)
	(vla-put-CanonicalMediaName
	  layout
	  (vla-get-CanonicalMediaName (vla-item layouts "Model"))
	)
	(vla-put-stylesheet
	  layout
	  (vla-get-stylesheet (vla-item layouts "Model"))
	)
	(vla-put-showplotstyles layout :vlax-true)
	(vla-getpapermargins layout 'MarginLL 'MarginUR)
	(setq marginll (vlax-safearray->list marginll))
	(setq marginur (vlax-safearray->list marginur))
	(setq ll (mapcar '- MarginLL))
	(setq ur (mapcar '+ ll (list pwidth pHeight)))
	(cond ((= plotscale "ScaleToFit")
	       (vl-cmdf	"_.MView"
			'(0 0)
			(mapcar	'-
				(list pwidth pHeight)
				(list (car marginll) (cadr marginll))
				(list (car marginur) (cadr marginur))
			)
	       )
	      )
	      ((= plotscale "Auto") (vl-cmdf "_.Mview" ll ur))
	      ('T (vl-cmdf "_.Mview" ll ur))
	)
	(vla-put-paperunits layout acMilliMeters)
	(vla-put-standardscale layout acVpCustomScale)
	(vla-setcustomscale layout 1 1)
	(vla-put-plotrotation layout (if upsidedown ac180degrees ac0degrees))
					;(vla-regen acaddoc acAllViewports)
	(vl-cmdf "_.zoom" "_all")
	(foreach bd NoRotationList
	  (copylayout
	    (GetNewAutoNumName layoutprefix 2 (ax:ListLayouts))
	  )
	  (vl-cmdf "_.MSPACE")
	  (vl-cmdf "_.Zoom" "_Window" "_non" (car bd) (cadr bd))
	  (if (numberp plotscale)
	    (vl-cmdf "_.zoom"
		     "_Scale"
		     (strcat (rtos (/ 1.0 plotscale) 2 100) "xp")
	    )
	  )
	  ;; restore to paperspace
	  (vl-cmdf "_.pspace")
	)				; end loop
	(vl-cmdf "_.layout" "_delete" "$temp_No_Rotation")
      )
    )
    ;; create 90 degree template
    (if	RotationList
      (progn
	(vla-put-layoutcreateviewport prdisplay :vlax-false)
	(vla-put-layoutshowplotsetup prdisplay :vlax-false)
	(vl-cmdf "_.Layout" "_New" "$temp_90_Rotation")
	(vl-cmdf "_.Layout" "_Set" "$temp_90_Rotation")
	(vla-put-layoutcreateviewport prdisplay crtvp)
	(vla-put-layoutshowplotsetup prdisplay showpg)
	(if (= "1" ltscale)
	  (setvar "psltscale" 0)
	)
	(setq layout (vla-item layouts "$temp_90_Rotation"))
	(vla-put-ConfigName
	  layout
	  (vla-get-ConfigName (vla-item layouts "Model"))
	)
	(vla-put-CanonicalMediaName
	  layout
	  (vla-get-CanonicalMediaName (vla-item layouts "Model"))
	)
	(vla-put-stylesheet
	  layout
	  (vla-get-stylesheet (vla-item layouts "Model"))
	)
	(vla-put-showplotstyles layout :vlax-true)
	(vla-put-paperunits layout acMilliMeters)
	(vla-put-standardscale layout acVp1_1)
	(vla-getpapermargins layout 'MarginLL 'MarginUR)
	(setq marginll (vlax-safearray->list marginll))
	(setq marginur (vlax-safearray->list marginur))
	(setq ll (mapcar '- (list (cadr marginUR) (car marginLL))))
	(setq ur (mapcar '+ ll (list pHeight pwidth)))
	(cond ((= plotscale "ScaleToFit")
	       (vl-cmdf	"_.MView"
			'(0 0)
			(mapcar	'-
				(list pHeight pwidth)
				(list (cadr marginur) (car marginur))
				(list (cadr marginll) (car marginll))
			)
	       )
	      )
	      ((= plotscale "Auto") (vl-cmdf "_.Mview" ll ur))
	      ('T (vl-cmdf "_.Mview" ll ur))
	)
	(vla-put-paperunits layout acMilliMeters)
	(vla-put-standardscale layout acVpCustomScale)
	(vla-setcustomscale layout 1 1)
	(vla-put-plotrotation layout (if upsidedown ac270degrees ac90degrees))
					;(vla-regen acaddoc acAllViewports)
	(vl-cmdf "_.zoom" "_all")
	(foreach bd RotationList
	  (copylayout
	    (GetNewAutoNumName layoutprefix 2 (ax:ListLayouts))
	  )
	  (vl-cmdf "_.MSPACE")
	  (vl-cmdf "_.Zoom" "_Window" "_non" (car bd) (cadr bd))
	  (if (numberp plotscale)
	    (vl-cmdf "_.zoom"
		     "_Scale"
		     (strcat (rtos (/ 1.0 plotscale) 2 100) "xp")
	    )
	  )
	  ;; restore to paperspace
	  (vl-cmdf "_.pspace")
	)
	(vl-cmdf "_.layout" "_delete" "$temp_90_Rotation")
      )
    )
    ;; back to model
    (setvar "ctab" "Model")
    (princ "\n布局生成完毕。")
  )
  ;; 主要功能在这里实现:
  (defun doBatchPlot (bdlist	   mode		plotscale
		      AutoRotate  upsidedown /		bounding
		      scale	   plotfile	pWidth
		      pHeight	   key		GetPlotFileList
		      pltfile	   pltfilebaselist
		      count	   i            target
		     )
    (defun GetPlotFileList ()
      (vl-directory-files
	(getvalue 'PlotFileFolder)
	(strcat (getvalue 'PlotFilePrefix) "*.plt")
	1
      )
    )
    (vla-getpapersize clayout 'pWidth 'pHeight)
    ;; 取得当前纸张的长边长度
    (if	(< pwidth pheight)
      (setq paperWidth pHeight)
      (setq paperwidth pWidth)
    )
    (if	(and (= mode "FILE") (= "1" (getvalue 'DeletePlotFile)))
      (foreach pltfile (GetPlotFileList)
	(princ "\n删除已有打印文件:")
	(princ (strcat (getvalue 'PlotFileFolder) pltfile))
	(vl-file-delete (strcat (getvalue 'PlotFileFolder) pltfile))
      )
    )
    ;; 对每个图框循环
    (setq count	(length bdlist)
	  i	0
    )
    (foreach bounding bdlist
      (setq i (1+ i))
      (vla-put-paperunits clayout acMilliMeters)
      ;;(vla-put-plotorigin clayout (ax:2dpoint '(0 0)))
      ;; 设置打印方向
      (if AutoRotate
	(if (= (islandscape bounding) (> pWidth pHeight))
	  (vla-put-plotrotation clayout (if upsidedown ac180degrees ac0degrees))
	  (vla-put-plotrotation clayout (if upsidedown ac270degrees ac90degrees))
	)
      )
      ;; 设置打印范围
      (setq target (getvar "target"))
      (vla-SetWindowToPlot
	clayout
	(ax:2dpoint (mapcar '- (car bounding) target))
	(ax:2dpoint (mapcar '- (cadr bounding) target))
      )
      ;; (apply 'vl-cmdf (cons "rectang" bounding))
      ;; 设置打印方式为window
      (vla-put-plottype clayout acWindow)
      ;; 设置打印比例
      (cond
	((= plotscale "ScaleToFit")
	 (progn	(vla-put-standardscale clayout acScaleToFit)
		(princ "\n当前打印比例: 适合可打印区域\n")
		(grtext	-2
			(strcat	"正在打印: 第"
				(itoa i)
				"/"
				(itoa count)
				"页, 比例: 适合可打印区域"
			)
		)
	 )
	)
	((= plotscale "Auto")
	 (progn
	   (setq scale (fixscale (/ (getwidth bounding) paperwidth)))
	   (vla-put-standardscale clayout acVpCustomScale)
	   (vla-setcustomscale clayout 1 scale)
	   (princ (strcat "\n第"
			  (itoa i)
			  "/"
			  (itoa count)
			  "页, 比例 1:"
			  (rtos scale)
		  )
	   )
	   (grtext -2
		   (strcat "正在打印: 第"
			   (itoa i)
			   "/"
			   (itoa count)
			   "页, 比例 1:"
			   (rtos scale)
		   )
	   )

	 )
	)
	('T
	 (progn	(vla-put-standardscale clayout acVpCustomScale)
		(vla-setcustomscale clayout 1 plotscale)
		(princ (strcat "\n第"
			       (itoa i)
			       "/"
			       (itoa count)
			       "页, 比例 1:"
			       (rtos plotscale)
		       )
		)
		(grtext	-2
			(strcat	"正在打印: 第"
				(itoa i)
				"/"
				(itoa count)
				"页, 比例 1:"
				(rtos plotscale)
			)
		)
	 )
	)
      )
      ;; 让AutoCAD更新状态栏信息。（即允许AutoCAD处理其它消息） AutoCAD2000／2002不能及时更新状态栏显示。
      ;; 测试显示AutoCAD 2004／2005无需执行此句。
      (if (< (atof (getvar "acadver")) 16.0)
	(vla-eval (vlax-get-acad-object) "doEvents")
      )
      ;; 设置自动居中打印
      (if (= "Center" (getvalue 'Offset))
	(vla-put-centerplot clayout :vlax-true)
	;; else
	(vla-put-plotorigin clayout (ax:2dpoint (getvalue 'Offset)))
      )
      ;; 打印或预览
      (cond
	((= mode "PLOT")
	 (progn
	   (princ "\n打印份数: ")
	   (princ (getvalue 'Copies))
	   (princ "\n")
	   (vla-put-NumberofCopies plot (read (getvalue 'Copies)))
	   (if (= :vlax-false (vla-plotToDevice plot))
	     (exit)
	   )
	 )
	)
	((= mode "PREVIEW")
	 (if
	   (= :vlax-false (vla-displayplotpreview plot acfullpreview))
	    (exit)
	 )
	)
	((= mode "FILE")
	 (progn	(setq pltfilebaselist
		       (mapcar 'vl-filename-base
			       (GetPlotFileList)
		       )
		)
		(setq plotfile (GetNewAutoNumName
				 (getvalue 'PlotFilePrefix)
				 2
				 pltfilebaselist
			       )
		)
		(setq plotfile (strcat (GetValue 'PlotFileFolder)
				       plotfile
				       ".plt"
			       )
		)
		(princ "\n生成打印文件: ")
		(princ plotfile)
		(princ "\n")
		(vla-plottofile plot plotfile)
	 )
	)
      )
      (if (and (= mode "PREVIEW") (/= bounding (last bdlist)))
	(progn (initget "Yes No")
	       (setq key (getkword "是否继续预览下一张? [Yes/No]<Yes>"))
	       (if (= key "No")
		 (exit)
	       )
	)
      )
    )
  )
  ;; 批量打印布局
  (defun PlotLayoutsInTabOrder
	 (LayoutNameList Plot-To-File-P / LayoutName ctab)
    (setq ctab (getvar "ctab"))
    (foreach LayoutName	LayoutNameList
      (vl-cmdf "_.layout" "_set" layoutname)
      (vl-cmdf "_.pspace")
      (vl-cmdf "_.zoom" "_e")
      (if plot-to-file-p
	(vl-cmdf ".-plot" "No"		; Detailed plot configuration? [Yes/No] <No>:
		 LayoutName		; Enter a layout name or [?] <幼儿园一层平面>:
		 ""			; Enter a page setup name <>:
		 ""			; Enter an output device name or [?] <FinePrint pdfFactory Pro>:
		 "Yes"			; Write the plot to a file [Yes/No] <N>:
		 ""			; Enter file name <D:\五中花园\幼儿园0-幼儿园屋顶平面.>:
		 "No"			; Save changes to layout [Yes/No]? <N>
		 "Yes"			; Proceed with plot [Yes/No] <Y>:
)
	(vl-cmdf ".-plot" "No"		; Detailed plot configuration? [Yes/No] <No>:
		 LayoutName		; Enter a layout name or [?] <幼儿园一层平面>:
		 ""			; Enter a page setup name <>:
		 ""			; Enter an output device name or [?] <FinePrint pdfFactory Pro>:
		 "No"			; Write the plot to a file [Yes/No] <N>:
		 "No"			; Save changes to layout [Yes/No]? <N>
		 "Yes"			; Proceed with plot [Yes/No] <Y>:
)
      )
    )
    (vl-cmdf "_.layout" "_set" ctab)
  ) ;_end of PlotLayoutsInTabOrder
  (defun doPlotLayoutsInTabOrder
	 (/ LayoutNameList plot-to-file-p key indexlist)
    (setq LayoutNameList
	   (vl-remove-if
	     (function (lambda (name)
			 (= (strcase name) "MODEL")
		       )
	     )
	     (layout-tab-list acaddoc)
	   )
    )
    (setq layoutNameList
	   (vl-sort
	     layoutNameList
	     '(lambda (a b)
		(< (vla-get-taborder (vla-item (vla-get-layouts acaddoc) a))
		   (vla-get-taborder (vla-item (vla-get-layouts acaddoc) b))
		)
	      )
	   )
    )
    (initget "All Select _All Select")
    (setq key
	   (getkword
	     "\n打印布局[全部(A)/选择(S)]/<全部>:"
	   )
    )
    (if	(eq key "Select")
      (progn
	(setq indexlist	(crtListBox2
			  "选择要打印的布局:"
			  "布局:"
			  LayoutNameList
			)
	)
	(if (null indexlist)
	  (exit)
	)
	(setq LayoutNameList
	       (mapcar '(lambda (i) (nth i LayoutNameList)) indexlist)
	)
      )
    )
    (initget "Yes No _Yes No")
    (setq plot-to-file-p
	   (getkword "打印成PLT文件? [是(Y)/否(N)] <否>: ")
    )
    (setq Plot-to-file-p (= plot-to-file-p "Yes"))
    (PlotLayoutsInTabOrder LayoutNameList plot-to-file-p)
    (princ)
  ) ;_end of doPlotLayoutsInTabOrder
  (defun SelectBlock (/ objName)
    (vl-catch-all-apply
      '(lambda ( / bname)
	 (while	(/= objName "AcDbBlockReference")
	   (setq bname (car (entsel "\n指定图框图块:")))
	   (if (null bname)
	     (exit)
	   )
	   (setq bname (vlax-ename->vla-object bname))
	   (setq objName (vla-get-objectname bname))
	   (if (/= objName "AcDbBlockReference")
	     (princ "\n你必须选择图块物体.")
	   )
	 )
	 (setvalue 'BlockName (vla-get-name bname))
       )
      nil
    )
  )
  (defun SelectLayer ( / objName)
    (vl-catch-all-apply
      '(lambda (/ lname)
	 (setq lname (car (entsel "\n指定图框所在的图层的样板物体:")))
	 (if (null lname)
	   (exit)
	 )
	 (setq lname (vlax-ename->vla-object lname))
	 (setvalue 'LayerName (vla-get-Layer lname))
       )
      nil
    )
  )
  (defun inViewP (pt / sc w h vpmin vpmax vpctr) ; pt expressed in ucs
    (setq h (/ (getvar "viewsize") 2.0)); viewport height in drawing units
    (setq sc (getvar "screensize"))	; viewport size in pixels
    (setq w (* h (/ (car sc) (cadr sc))))
					; viewport width in drawing units
    (setq vpctr (getvar "viewctr"))	; viewport center in ucs
    (setq vpmin (mapcar '- vpctr (list w h)))
    (setq vpmax (mapcar '+ vpctr (list w h)))
    (and
      (> (car pt) (car vpmin))
      (> (cadr pt) (cadr vpmin))
      (< (car pt) (car vpmax))
      (< (cadr pt) (cadr vpmax))
    )
  )
  (defun expandbounding	(bd / rt pt1 pt2 offset w h)
    (setq w (- (caadr bd) (caar bd)))
    (setq h (- (cadadr bd) (cadar bd)))
    (setq offset (/ w 1e6))		; 增量，用于防止打印时打不出边线
    (setq pt1 (mapcar '- (car bd) (list offset offset)))
    (setq pt2 (mapcar '+ (cadr bd) (list offset offset)))
    (list pt1 pt2)
  )
  (defun GetFrames (/	    doGetFrames	    ss	    filterlist
		    elist   bdlist  e	    vlist   vlist2  ll
		    ur	    bd	    x1	    x2	    y1	    y2
		    ss2	    w	    h	    w2	    h2	    ent
		    flist   cen	    needzoom
		   )
    (defun doGetFrames ()
      ;; 图块图框
      (if (= "BlockRadio" (getvalue 'Frame))
	(setq filterlist
	       (list '(0 . "INSERT")
		     (cons 2 (getvalue 'BlockName))
	       )
	)
      )
      ;; 理正图框(PLINE)
      (if (= "LzFrameRadio" (getvalue 'Frame))
	(setq filterlist
	       '((0 . "LWPOLYLINE")
		 (8 . "*_TITLE")
		 (90 . 4)
		 (70 . 1)
		 (43 . 0.0)
		)
	)
      )
      ;; 指定图层矩形PLINE
      (if (= "LayerRadio" (getvalue 'Frame))
	(setq filterlist
	       (list '(0 . "LWPOLYLINE")
		     (cons 8 (getvalue 'LayerName))
		     '(90 . 4)
		     '(70 . 1)
		     '(43 . 0.0)
	       )
	)
      )      
      (setvar "highlight" 1)
      (setq ss (ssget filterlist))
      (if ss
	(progn
	  (setq elist (ss->elist ss))
	  (if (= "BlockRadio" (getvalue 'Frame))
	    (progn
	      (setq bdlist nil)
	      (foreach e elist
		(setq bd (ax:getboundingbox e))
					; e entity wcs frame: ur and ll
		(setq x1 (caar bd)
		      x2 (caadr bd)
		      y1 (cadar bd)
		      y2 (cadadr bd)
		)
		(setq vlist (list (list x1 y1)
				  (list x1 y2)
				  (list x2 y2)
				  (list x2 y1)
			    )
		)			; four vertexes wcs bounding
		(setq vlist (mapcar '(lambda (v) (trans v 0 1)) vlist))
					; convert to ucs
		(setq ll
		       (list (apply 'min (mapcar 'car vlist))
			     (apply 'min (mapcar 'cadr vlist))
		       )
		)
		(setq ur
		       (list (apply 'max (mapcar 'car vlist))
			     (apply 'max (mapcar 'cadr vlist))
		       )
		)
		(setq bd (list ll ur))	; ucs bounding box
		(setq w (- (car ur) (car ll)))
		(setq h (- (cadr ur) (cadr ll)))
		;; zoom
		(setq needzoom (not (and (inviewp ll) (inviewp ur))))
		(if needzoom
		  (vl-cmdf "_.zoom" "_window" "_non" ll "_non" ur)
		)
		;; eval actural width
		(setvar "highlight" 0)
		(setq
		  ss2 (ssget "_f"
			     (list (mapcar '+ ll (list 0 (/ h 2.0)))
				   (mapcar '- ur (list 0 (/ h 2.0)))
			     )		; fence list in ucs
			     filterlist
		      )
		)
		(setq ent (ssnamex ss2))
		(setq ent (vl-remove-if-not
			    '(lambda (x) (eq e (cadr x)))
			    ent
			  )
		)
		(setq ent (car ent))
		(setq flist (cdddr ent)) ; in wcs
		(setq
		  w2 (distance (cadar flist) (cadar (reverse flist)))
		)
		;; eval actural height 
		(setq
		  ss2 (ssget "_f"
			     (list (mapcar '+ ll (list (/ w 2.0) 0))
				   (mapcar '- ur (list (/ w 2.0) 0))
			     )		; fence list in ucs
			     filterlist
		      )
		)
		(setq ent (ssnamex ss2))
		(setq ent (vl-remove-if-not
			    '(lambda (x) (eq e (cadr x)))
			    ent
			  )
		)
		(setq ent (car ent))
		(setq flist (cdddr ent)) ; in wcs
		(setq
		  h2 (distance (cadar flist) (cadar (reverse flist)))
		)
		;; eval actural bounding
		(setq cen
		       (mapcar '(lambda (x1 x2) (/ (+ x1 x2) 2.0)) ll ur)
		)			; in ucs
		(setq ll (mapcar '- cen (list (/ w2 2.0) (/ h2 2.0))))
		(setq ur (mapcar '+ cen (list (/ w2 2.0) (/ h2 2.0))))
		;; zoom
		(if needzoom
		  (vl-cmdf "_.zoom" "_p")
		)

		;; append list
		(setq bdlist (cons (list ll ur) bdlist))
	      ) ;_end foreach
	      (setq bdlist (reverse bdlist))
	      (setq bdlist (mapcar 'expandbounding bdlist))
					; 增量，用于防止打印时打不出边线
	    )
					;else polyline frame
	    (progn
	      (foreach e elist
		(setq vlist (vlax-safearray->list
			      (vlax-variant-value
				(vla-get-coordinates
				  (vlax-ename->vla-object e)
				)
			      )
			    )
		)
		(setq vlist2 nil)
		(repeat	4
		  (setq	vlist2
			 (cons (list (car vlist) (cadr vlist))
			       vlist2
			 )
		  )
		  (setq vlist (cddr vlist))
		)
		(setq
		  vlist2 (mapcar '(lambda (v) (trans v e 1))
				 vlist2
			 )
		)
		(setq
		  ll (list (apply 'min (mapcar 'car vlist2))
			   (apply 'min (mapcar 'cadr vlist2))
		     )
		)
		(setq
		  ur (list (apply 'max (mapcar 'car vlist2))
			   (apply 'max (mapcar 'cadr vlist2))
		     )
		)
		(setq bdlist (cons (list ll ur) bdlist)) ; frame in ucs
	      ) ;_end loop
	      (setq bdlist (reverse bdlist))
	      (setq bdlist (mapcar 'expandbounding bdlist))
					; 增量，用于防止打印时打不出边线

	    )
	  )
	  (setvalue 'SelectedFrames bdlist)
	  (HighLightShow bdlist)
	)
      )
    )					;getframes main
    (vl-catch-all-apply 'dogetframes nil)
  )
  (defun HighLightShow (bdlist / bd)
    (vl-cmdf "_.redraw")
    (foreach bd	bdlist
      (grdraw (car bd) (list (caar bd) (cadadr bd)) acRed 1)
      (grdraw (car bd) (list (caadr bd) (cadar bd)) acRed 1)
      (grdraw (cadr bd) (list (caar bd) (cadadr bd)) acRed 1)
      (grdraw (cadr bd) (list (caadr bd) (cadar bd)) acRed 1)
      (grdraw (cadr bd) (car bd) acRed 1)
      (grdraw (list (caar bd) (cadadr bd))
	      (list (caadr bd) (cadar bd))
	      acRed
	      1
      )
    )
  )
  ;;对图框排序
  (defun OrderFrames (bdlist / vscoor)
    (defun vscoor (n)			; 屏幕视觉坐标，允许误差啦～大致相同就相同了。
      (fix (/ n (/ (getvar "viewsize") 100.0)))
    )
    ;; main orderframes
    (if	(= (getvalue 'PlotOrder) "LeftToRightRadio")
      (setq bdlist (vl-sort bdlist
			    '(lambda (f1 f2 / rt x1 y1 x2 y2 vs)
					; x1, y1对应于第一组的图框中心点的坐标
			       (setq y1 (vscoor (cadar f1)))
			       (setq y2 (vscoor (cadar f2)))
			       (setq x1 (vscoor (caar f1)))
			       (setq x2 (vscoor (caar f2)))
			       (setq rt (> y1 y2))
					;优先Y坐标比较，大的话在前
			       (if (and (null rt) (= y1 y2))
					;Y坐标相同时，比较X坐标，小的话在前
				 (setq rt (< x1 x2))
			       )
			       rt
			     )
		   )
      )
    )
    (if	(= (getvalue 'PlotOrder) "TopToBottomRadio")
      (setq bdlist (vl-sort bdlist
			    '(lambda (f1 f2 / rt)
			       (setq y1 (vscoor (cadar f1)))
			       (setq y2 (vscoor (cadar f2)))
			       (setq x1 (vscoor (caar f1)))
			       (setq x2 (vscoor (caar f2)))
			       (setq rt (< x1 x2))
					;优先X坐标比较，小的话在前
			       (if (and (null rt) (= x1 x2))
					;当X坐标相同时，比较Y坐标，大的话在前
				 (setq rt (> y1 y2))
			       )
			       rt
			     )
		   )
      )
    )
    (if	(= (getvalue 'ReverseOrder) "1")
      (setq bdlist (reverse bdlist))
    )
    bdlist
  )
  ;; ============================================
  ;; MAIN
  ;; ============================================
  (setvar "ctab" "Model")
  (setq acaddoc (vla-get-activedocument (vlax-get-acad-object)))
  (setq plot (vla-get-plot acaddoc))
  (setq clayout (vla-get-activelayout acaddoc))
  ;;(vla-put-paperunits clayout acMillimeters)
  (setq	catch (vl-catch-all-apply
		'vla-put-paperunits
		(list clayout acMillimeters)
	      )
  )
  (if (vl-catch-all-error-p catch)
    (progn
      (alert
	"设置打印机与单位时发生错误。无法使用当前的打机印配置，可能打印驱动程序不存在，或者打印机没有连接，或者打印驱动程序存在问题。\n\n请重新设置正确的页面设置。"
      )
      (vl-cmdf "_.pagesetup")
      (while (/= "" (getvar "cmdnames")) (vl-cmdf pause))
      (vla-put-paperunits clayout acMillimeters)
    )
  )
  (setq blocklist (getblocklist))
  (setq Layerlist (getLayerlist))
  (setq	default_dclvalues
	 (list
	   (cons 'Frame "LzFrameRadio")
	   (cons 'BlockName (car (getblocklist)))
	   (cons 'LayerName (car (getLayerlist)))
	   (cons 'Output "PlotRadio")
	   (cons 'PlotScale "Auto")
	   (cons 'Copies "1")
	   (cons 'Offset "Center")
	   (cons 'LayoutPrefix "BP_")
	   (cons 'PlotFilePrefix
		 (strcat (vl-filename-base (getvar "dwgname")) "_")
	   )
	   (cons 'PlotFileFolder (getvar "dwgprefix"))
	   (cons 'DeletePlotFile "0")
	   (cons 'DeleteLayout "0")
	   (cons 'MSLineScale "1")
	   (cons 'SelectedFrames nil)
	   (cons 'AutoRotate "1")
	   (cons 'UpsideDown "0")
	   (cons 'PlotOrder "SelectOrderRadio")
	   (cons 'ReverseOrder "0")
	 )
  )
  (setq	dclvalues (vlax-ldata-get
		    "_BATCHPLOT"
		    "Previous_Plot"
		    default_dclvalues
		  )
  )
  (setq rcode nil)
  (while (Not (or (= 0 Rcode) (= 1 Rcode)))
    (setq RCode (showMainDlg))
    (if	(= Rcode 10)
      (progn
	(vl-cmdf "_.PageSetup")
	(while (/= "" (getvar "cmdnames")) (vl-cmdf pause))
      )
    )
    (if	(= Rcode 11)
      (if (= "BlockRadio" (getvalue 'Frame))
          (selectblock)
	  (selectLayer)
      )
    )
    (if	(= Rcode 12)
      (GetFrames)
    )
    (if	(= Rcode 13)
      (vl-catch-all-apply
	'(lambda ()
	   (doBatchPlot
	     (orderFrames (getvalue 'SelectedFrames))
	     "PREVIEW"
	     (getvalue 'plotscale)
	     (= "1" (getvalue 'AutoRotate))
	     (= "1" (getvalue 'UpsideDown))
	   )
	 )
	nil
      )
    )
    (if	(= Rcode 14)
      (vl-catch-all-apply
	'(lambda ()
	   (HighLightShow (getvalue 'SelectedFrames))
	   (getstring "\n图中红色交叉框区即为选中的图框<返回>")
	 )
	nil
      )
    )
    ;; OK
    (if	(= Rcode 1)
      (progn (if (= "PlotRadio" (getvalue 'Output))
	       (doBatchPlot
		 (orderFrames (getvalue 'SelectedFrames))
		 "PLOT"
		 (getvalue 'plotscale)
		 (= "1" (getvalue 'AutoRotate))
		 (= "1" (getvalue 'UpsideDown))
	       )
	     )
	     (if (= "LayoutRadio" (getvalue 'Output))
	       (doBatchLayout
		 (orderFrames (getvalue 'SelectedFrames))
		 (getvalue 'plotscale)
		 (getvalue 'layoutprefix)
		 (getvalue 'deletelayout)
		 (getvalue 'mslinescale)
		 (= "1" (getvalue 'AutoRotate))
		 (= "1" (getvalue 'UpsideDown))
	       )
	     )
	     (if (= "PlotFileRadio" (getvalue 'Output))
	       (doBatchPlot
		 (orderFrames (getvalue 'SelectedFrames))
		 "FILE"
		 (getvalue 'plotscale)
		 (= "1" (getvalue 'AutoRotate))
		 (= "1" (getvalue 'UpsideDown))
	       )
	     )
	     (if (= "PlotLayoutRadio" (getvalue 'Output))
	       (doPlotLayoutsInTabOrder)
	     )
	     (vlax-ldata-put "_BATCHPLOT" "Previous_Plot" dclvalues)
      )
    )
  )
  (unload_dialog dcl_id)
  (vl-cmdf "_.redraw")
  (princ)
)

(defun batchplot_dcl_help (/ dcl_id helpcontext parse mc_getfile)
  (defun parse (str delim / lst pos)
    (setq pos (vl-string-search delim str))
    (while pos
      (setq lst	(cons (substr str 1 pos) lst)
	    str	(substr str (+ pos 2))
	    pos	(vl-string-search delim str)
      )
    )
    (if	(> (strlen str) 0)
      (setq lst (cons str lst))
    )
    (reverse lst)
  )
  (defun mc_getfile (files / tmplst x fn)
    (setq files (findfile files))
    (if	files
      (progn
	(setq fn (open files "r"))
	(while (setq x (read-line fn))
	  (setq tmplst (append tmplst (list x)))
	)
	(close fn)
	tmplst
      )
      nil
    )
  )
  ;; main
  (setq helpcontext (vl-get-resource "BP_help"))
  (if helpcontext
    (progn (setq helpcontext (parse helpcontext "\n"))
	   (foreach str	helpcontext
	     (setq nlist (cons (vl-string-subst "" "\r" str) nlist))
	   )
	   (setq helpcontext (reverse nlist))
    )
    ;; else no resource found
    (setq helpcontext (mc_getfile "BP_help.txt"))
  )
  ;; init dcl
  (setq dcl_id (load_dialog "BP_help"))
  (if (< dcl_id 0)
    (progn (alert "错误：无法加载对话框文件。") (exit))
  )
  (new_dialog "BP_Help" dcl_id)
  (start_list "HelpList")
  (mapcar 'add_list helpcontext)
  (end_list)
  (start_dialog)
  (unload_dialog dcl_id)
)


;;; new help function
(defun batchplot_help (/ filename fd str oIE)
  (setq oIE (vlax-create-object "InternetExplorer.Application"))
  (if oIE
    (progn
      (if (setq str (vl-get-resource "BP_HELP_HTM"))
	(progn (setq filename (vl-filename-mktemp "BatchPlot.htm"))
	       (setq fd (open filename "w"))
	       (princ str fd)
	       (close fd)
	)
	(setq filename (findfile "BP_HELP.htm"))
      )
      (vlax-invoke-method oIE "navigate" filename)
      (vlax-put-property oIE "visible" :vlax-true)
      (if str
	(vl-file-delete filename)	; delete temp file
      )
    )
    ;; else ie launch failed, show dcl style help
    (batchplot_dcl_help)
  )
  (princ)
)

;;;=========================
;;;|    命令：BatchPlot    |
;;;=========================
(defun c:BatchPlot (/ cmdecho backgroundplot sysvar)
  (if (< (atof (getvar "acadver")) 15.0)
    (progn
      (alert
	"此程序为AutoCAD2000以上的版本设计。不支持AutoCAD R14及以下版本。"
      )
      (exit)
    )
  )
  (vl-load-com)
  (setq cmdecho (getvar "cmdecho"))
  (setvar "cmdecho" 0)
  (vl-cmdf "_.undo" "_begin")
  ;; save and set system variables
  (setq	sysvar (ChangeVars
		 '(("backgroundplot" . 0)
		   ("LayoutRegenCtl" . 0)
		   ("osmode" . 0)
		   ("dimzin" . 8)
		   ("highlight" . 1)
		   ("ucsicon" . 0)
		  )
	       )
  )
  (vl-cmdf "_.ucs" "_world")
  (vl-cmdf "_.ucs" "_view")
  ;; for debug version:
  ;;(batchplot)
  (vl-catch-all-apply 'batchplot nil)
  (vl-cmdf "_.ucs" "_p")
  (vl-cmdf "_.ucs" "_p")
  (ChangeVars sysvar)			; restore system variables
  (grtext)
  (vl-cmdf "_.undo" "_end")
  (setvar "cmdecho" cmdecho)
  (princ)
)

(defun c:BPlot () (c:batchplot))

(defun CD_VL_GetTempfile ()
  (cond	((getenv "tmp") (strcat (getenv "tmp") "\\TEMP.DCL"))
	((getenv "temp") (strcat (getenv "temp") "\\TEMP.DCL"))
	(t "C:\\TEMP.DCL")
  )
)

(setq TEMPDCLfile (CD_VL_GetTempfile))

(defun crtListBox2 (title      label	  OptionList /
		    OptionVal  dcl_id	  tempdcl    ListItem
		    tempdcl
		   )
  (setq tempdcl (open TempDCLfile "w"))
  (write-line "ListBox : dialog {" tempdcl)
  (write-line (strcat " label = \"" title "\";") tempdcl)
  (write-line "" tempdcl)
  (write-line ":list_box {" tempdcl)
  (write-line " key = \"listbox1\";" tempdcl)
  (write-line (strcat " label = \"" label "\";") tempdcl)
  (write-line " width = 6;" tempdcl)
  (write-line " multiple_select = true;" tempdcl)
  (write-line "  }" tempdcl)
  (write-line " ok_cancel ;" tempdcl)
  (write-line "}" tempdcl)
  (close tempdcl)


  (if (findfile TempDCLfile)
    (progn
      (setq dcl_id (load_dialog TempDCLfile)) ; loads dialog ascii  
      (if (not (new_dialog "ListBox" dcl_id))
	(done_dialog)
      )

      (start_list "listbox1")
      (foreach ListItem OptionList (add_list ListItem))
      (end_list)

      (action_tile "listbox1" "(setq OptionVal $value)")
      (action_tile "accept" "(done_dialog 1)")
      (action_tile "cancel" "(Setq OptionVal nil)")
      (start_dialog)
      (unload_dialog dcl_id)
    )					;end progn (find temp.dcl)
    (progn
      (princ "\nDialog Definition temp.dcl not found!\n")
      (quit)
      (princ)
    )					;end progn (find temp.dcl)
  )					;end if (find temp.dcl)

  (if (findfile TempDCLfile)
    (vl-file-delete TempDCLfile)
  )
  (if OptionVal
    (read (strcat "(" OptionVal ")"))
    nil
  )
)

(defun layout-tab-list (doc / layouts)
  (mapcar 'vla-get-name
	  (vl-sort
	    (vlax-for layout (vla-get-layouts doc)
	      (setq layouts (cons layout layouts))
	    )
	    '(lambda (a b)
	       (< (vla-get-taborder a)
		  (vla-get-taborder b)
	       )
	     )
	  )
  )
)


;;; ================================================================
;;; ChangeVars
;;; 修改指定系统变量并返回其先值
;;; 这个函数来自“明经通道”
;;; 参数
;;; 一个包含要更改的系统变量和他们的新值的点对列表
;;; 示例
;;; (setq ret (changevars '(("filedia" . 0) ("cmdecho" . 0) ("osmode" . 512))))
;;; 注意
;;;  CHANGEVARS
;;; 返回一个包含所有指定的系统变量和他们先前值的列表。要恢复他们，
;;; 可简单地将该返回的列表提供给CHANGEVARS函数。
;;; ================================================================
(defun changevars (lst)
  (mapcar '(lambda (x / tmp var)
	     (setq
	       tmp (cons (car x)
			 (if (= (type (setq var (getvar (car x)))) 'list)
			   (list var)
			   var
			 )
		   ) ;_ end of cons
	     )
	     (if (getvar (car x))	; 保证存在这个系统变量. 有时有兼容问题，如backgroundplot只存在于2005以上的版本
	       (setvar (car x)
		       (if (= (type (cdr x)) 'list)
			 (cadr x)
			 (cdr x)
		       ) ;_ end of if
	       ) ;_ end of setvar
	     )
	     tmp
	   ) ;_ end of lambda
	  lst
  ) ;_ end of mapcar
) ;_ end of defun
;;; ================================================================

(princ "\n模型空间的批量打印程序")
(princ "\n命令: BatchPlot 或 BPlot ")
(princ)