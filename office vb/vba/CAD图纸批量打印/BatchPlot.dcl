
dcl_settings : default_dcl_settings { audit_level = 3; }

BatchPlotMain : dialog {
    label = "批量打印";
    : row {
        : column {
            : boxed_radio_column {
                label = "图框形式";
                : radio_button {
                    label = "理正图框(L): *_TITLE层";
                    key = "LzFrameRadio";
                    mnemonic = "L";
                }
                : radio_button {
                    label = "图块(B): 图框为特定图块";
                    key = "BlockRadio";
                    mnemonic = "B";
                }
                : radio_button {
                    label = "图层(N): 指定图层封闭矩形";
                    key = "LayerRadio";
                    mnemonic = "N";
                }
            }
            : boxed_column {
                label = "图块与图层";
                key = "BlockAndLayerSettings";
                : button {
                    label = "从图中指定图块或图层(P)<";
                    key = "PickBtn";
                    mnemonic = "P";
                }
                :row {
	                : text {
	                    label = "图块名";
	                    value = "图块名";
	                }
	                : popup_list {
	                    key = "BlockNameEdit";
	                    fixed_height = false;
	                    fixed_width = true;
	                    width = 20;
	                }
	        }
                :row {
	                : text {
	                    label = "图层名";
	                    value = "图层名";
	                }
	               : popup_list {
	                    key = "LayerNameEdit";
	                    fixed_height = false;
	                    fixed_width = true;
	                    width = 20;
	                }
                }

            }
            : boxed_radio_column {
                label = "输出选项";
                : radio_button {
                    label = "直接批量打印(1)";
                    key = "PlotRadio";
                    mnemonic = "1";
                }
                : radio_button {
                    label = "批量生成布局(2)";
                    key = "LayoutRadio";
                    mnemonic = "2";
                }
                : radio_button {
                    label = "生成PLT文件(3)";
                    key = "PlotFileRadio";
                    mnemonic = "3";
                }
                : radio_button {
                    label = "打印已有布局(4)";
                    key = "PlotLayoutRadio";
                    mnemonic = "4";
                }
            }
            : button {
                label = "选择批量打印图纸(S) <";
                key = "SelectFramesBtn";
                mnemonic = "S";
            }
            : boxed_row {
                : text {
                    label = "选中图纸：0";
                    key = "StatusLabel";
                }
                : button {
                    label = "亮显(L)..";
                    key = "ShowFramesBtn";
                    mnemonic = "L";
                    is_enabled = false;
                }
            }
        }
        : column {
            children_alignment = right;
            : boxed_column {
                label = "打印设置";
                key = "PageSetupSettings";
                : row {
                    : popup_list {
                        label = "预设配置:";
                        key = "PageSetupPopup";
                    }
                    : button {
                        label = "打印设置(A)..";
                        key = "PageSetupBtn";
                        mnemonic = "A";
                        width = 20;
                        fixed_width = true;

                    }
                }
                : text {
                    label = "打印设备名：";
                    value = "打印设备名：";
                    key = "PlotterLabel";
                }
                : text {
                    label = "纸张大小：";
                    value = "纸张大小：";
                    key = "PaperLabel";
                }
                : row {
                    : text {
                        label = "打印样式：";
                        value = "打印样式：";
                        key = "PlotStyleLabel";
                    }
                    : edit_box {
                        label = "打印份数:";
                        value = "1";
                        key = "CopiesEdit";
                        width = 8;
                        fixed_width = true;
                    }
                }
            }
            : boxed_row {
                label = "打印比例";
                key = "ScaleSettings";
                : radio_row {
                    width = 40;
                    fixed_width = true;
                    : radio_button {
                        label = "自动比例";
                        key = "AutoScaleRadio";
                    }
                    : radio_button {
                        label = "适合图纸";
                        key = "ScaleToFitRadio";
                    }
                    : radio_button {
                        label = "固定比例:";
                        key = "FixScaleRadio";
                    }
                }
                : edit_box {
                    label = "1:";
                    value = "100";
                    key = "FixScaleEdit";
                }
            }
            : boxed_row {
                label = "图纸定位";
                key = "LocationSettings";
                  : toggle {
                       label = "自动旋转";
                       key = "AutoRotateCheck";
                  }
                  : toggle {
                       label = "反向";
                       key = "UpsideDownCheck";
                  }
                  : radio_row {
                      : radio_button {
                          label = "自动居中";
                          key = "AutoCenterRadio";
                      }
                      : radio_button {
                          label = "偏移";
                          key = "OffsetRadio";
                      }
                  }
                 : edit_box {
                      label = "X=";
                      value = "0";
                      edit_width = 4;
                      key = "XOffsetEdit";
                  }
                  : edit_box {  
                      label = "Y=";  
                      value = "0";
                      edit_width = 4;
                      key = "YOffsetEdit";  
                  }  
            }
            : boxed_row {
                label = "打印顺序";
                key = "PlotOrderSettings";
              : radio_row {
                      : radio_button {
                          label = "选择顺序";
                          key = "SelectOrderRadio";
                      }
                      : radio_button {
                          label = "左右，上下";
                          key = "LeftToRightRadio";
                      }
                      : radio_button {
                          label = "上下，左右";
                          key = "TopToBottomRadio";
                      }
              }
              : toggle {
                label = "逆序";
                key = "ReverseOrderCheck";
              }
            }
            : boxed_column {
                label = "打印文件";
                key = "PlotFileSettings";
                : row {
                    : edit_box {
                        label = "文件名前缀:";
                        key = "PlotFilePrefixEdit";
                    }
                    : toggle {
                        label = "删除已有同前缀名的PLT文件";
                        key = "DeletePlotFileCheck";
                    }
                }
                : row {
                    : edit_box {
                        label = "保存位置:";
                        key = "PlotFileFolderEdit";
                    }
                    : button {
                        label = "浏览..";
                        key = "BrowsePLTFolderBtn";
                        width = 15;
                        fixed_width = true;
                    }
                }
            }
            : boxed_column {
                label = "布局设置";
                key = "LayoutSettings";
                : row {
                    : edit_box {
                        label = "布局名前缀:";
                        key = "LayoutPrefixEdit";
                    }
                    : toggle {
                        label = "删除图中已有同前缀名的布局";
                        key = "DeleteLayoutCheck";
                    }
                }
                : toggle {
                    label = "在布局中强制使用模型空间的线型比例";
                    key = "LtScaleCheck";
                }
            }
        }
    }
    : row {
        : button {
            label = "预览(R)";
            key = "PreviewBtn";
            mnemonic = "R";
            is_enabled = false;
        }
        spacer_1;
        spacer_1;
        spacer_1;
        spacer_1;
        spacer_1;
        spacer_1;
        : button {
            label = "确定(O)";
            key = "OKBtn";
            mnemonic = "O";
            is_default = true;
            is_enabled = false;
        }
        : button {
            label = "取消(C)";
            key = "CancelBtn";
            mnemonic = "C";
            is_cancel = true;
        }
        : button {
            label = "帮助(H)";
            key = "HelpBtn";
            mnemonic = "H";
        }
    }
}
